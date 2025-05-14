.. _accelerating_filtered_statements:

*************************
Accelerating Filtered Statements
*************************

This page outlines a feature designed to significantly improve the performance of statements that include filters on large tables. By using **Metadata Partitions**, SQDB minimize the overhead associated with metadata scanning, leading to faster statement execution times, especially as tables grow.

.. contents::
   :local:
   :depth: 1    

The Challenge: Metadata Scan Overhead
=====================================

When you execute a statement with a filter (e.g., ``SELECT x, y FROM table1 WHERE X=7;``), the system needs to scan the metadata of each data chunk within the table to identify the relevant chunks containing the data that satisfies your filter condition. As tables scale to trillions of rows, this metadata scanning process can become a significant bottleneck, adding substantial latency to your statements. In some cases, this overhead can reach tens of seconds for very large tables.

The Solution: Metadata Partitions
=================================

To address this challenge, SQDB introduced **Metadata Partitions**. This feature creates an internal metadata metadata partitoning structure for each table, grouping data chunks based on the minimum and maximum values of sorted columns within those chunks. This allows the system to efficiently identify and target only the relevant partitions during a filtered statement, drastically reducing the amount of metadata that needs to be scanned.


Managing Metadata Partitions
============================

A new SQL function, `recalculate_metadata_partition`, is introduced to manage and update the Metadata Partitions for your tables.

Syntax
======

.. code-block:: postgres

	SELECT recalculate_metadata_partition('<schema_name>', '<table_name>', '<column_name>', ['true'/'false']);

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema
   * - ``table_name``
     - The name of the table
   * - ``column_name``
     - The name of the column
   * - ``case_sensitive_flag``
     - optional input - ``'false'`` (default) ignore case sensitivity. ``'true'`` for case sensitivity.


Important Considerations
========================

  * ```recalculate_metadata_partition`` function requires ``SUPERUSER`` privileges.
  * **Impact of Data Modifications:**
      * ``INSERT`` New chunks will be added, and a full scan of these new chunks will be performed until the Metadata Partition is updated.
      * ``DELETE`` The existing metadata partition might still be used, potentially leading to false positives (pointing to non-existent chunks) - which will later get filtered out from the statement results.
      * ``UPDATE`` The existing metadata partition will become irrelevant and will not be used.
      * ``CLEANUP_CHUNKS``, ``CLEANUP_EXTENNTS``, ``RECHUNK`` These operations will require dropping and recreating the Metadata Partition.
  * The ``recalculate_metadata_partition`` utility is designed to be CPU-based, ensuring that it does not impact GPU-intensive workloads.


Monitoring Metadata Partitions
==============================

A new catalog statement is available to list the existing Metadata Partitions and their status:

.. code-block:: postgres

	SELECT db_name, schema_name, table_name, column_name, last_update, total_chunks_per_column, total_metadata partitoned_chunks_per_column
	FROM sqream_catalog.metadata_partitions;
