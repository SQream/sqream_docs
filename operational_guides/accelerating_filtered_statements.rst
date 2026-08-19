.. _accelerating_filtered_statements:

********************************
Accelerating Filtered Statements
********************************

This page outlines a feature designed to significantly improve the performance of statements that include filters on large tables. By using **chunk indexes**, SQDB minimize the overhead associated with metadata scanning, leading to faster statement execution times, especially as tables grow.

.. contents::
   :local:
   :depth: 1

The Challenge: Metadata Scan Overhead
=====================================

When you execute a statement with a filter (e.g., ``SELECT x, y FROM table1 WHERE X=7;``), the system needs to scan the metadata of each data chunk within the table to identify the relevant chunks containing the data that satisfies your filter condition. As tables scale to trillions of rows, this metadata scanning process can become a significant bottleneck, adding substantial latency to your statements. In some cases, this overhead can reach tens of seconds for very large tables.

The Solution: Chunk Indexes
===========================

To address this challenge, SQDB introduced **chunk indexes**. This feature creates an internal indexing structure for each table, grouping data chunks based on the minimum and maximum values of sorted columns within those chunks. This allows the system to efficiently identify and target only the relevant chunks during a filtered statement, drastically reducing the amount of metadata that needs to be scanned.

Managing Chunk Indexes
======================

Three utility functions manage chunk indexes. ``RECALCULATE_CHUNKS_INDEXES`` builds or rebuilds the index of a column, ``REMOVE_CHUNKS_INDEXES`` removes the indexes of a whole table, and :ref:`VALIDATE CHUNKS INDEXES<validate_chunks_indexes>` checks an existing index against the table's real chunks.

Building a chunk index
----------------------

``RECALCULATE_CHUNKS_INDEXES`` builds or rebuilds the chunk index of a single column. A rebuild removes the column's existing index before writing the new one, so running it twice in a row does not grow the index.

.. code-block:: postgres

   SELECT RECALCULATE_CHUNKS_INDEXES('<schema_name>.<table_name>', '<column_name>', ['<case_sensitive_names>']);

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``schema_name.table_name``
     - The schema and table, given as a single dotted argument
   * - ``column_name``
     - The name of the column to index
   * - ``case_sensitive_names``
     - Optional. ``'false'`` converts the names to lower case, ``'true'`` uses them as written, and any other value raises an error. When the argument is omitted, the names are used as written

Removing chunk indexes
----------------------

``REMOVE_CHUNKS_INDEXES`` removes the chunk indexes of every column in a table. Statements that filter on the table continue to work afterwards, falling back to a sequential scan of the chunk metadata.

.. code-block:: postgres

   SELECT REMOVE_CHUNKS_INDEXES('<schema_name>.<table_name>');

Validating a chunk index
------------------------

``VALIDATE_CHUNKS_INDEXES`` cross-checks a column's chunk index against the table's real chunks, reporting chunks missing from the index, entries whose minimum and maximum values no longer match the data, and other inconsistencies. See :ref:`VALIDATE CHUNKS INDEXES<validate_chunks_indexes>`.

Important Considerations
========================

  * All three utility functions require ``SUPERUSER`` permissions.
  * **Impact of Data Modifications:**
      * ``INSERT`` New chunks will be added, and a full scan of these new chunks will be performed until the chunk index is updated.
      * ``DELETE`` The existing chunk index might still be used, potentially leading to false positives (pointing to non-existent chunks) - which will later get filtered out from the statement results.
      * ``UPDATE`` The existing chunk index will become irrelevant and will not be used.
      * ``CLEANUP_CHUNKS``, ``CLEANUP_EXTENTS``, ``RECHUNK`` These operations remove the chunk index, which then has to be recreated.
  * The ``RECALCULATE_CHUNKS_INDEXES`` utility is designed to be CPU-based, ensuring that it does not impact GPU-intensive workloads.

Monitoring Chunk Indexes
========================

A catalog table lists the existing chunk indexes and their status:

.. code-block:: postgres

   SELECT database_name, schema_name, table_name, column_name, last_update, total_indexed_chunks_per_column
   FROM sqream_catalog.metadata_partitions;
