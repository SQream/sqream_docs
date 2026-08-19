:orphan:

.. _validate_chunks_indexes:

***********************
VALIDATE CHUNKS INDEXES
***********************

``VALIDATE_CHUNKS_INDEXES`` cross-checks the :ref:`chunk index<accelerating_filtered_statements>` of a single column against the table's real chunks, and reports what does not line up.

Use it when a filtered statement returns unexpected results or scans more chunks than expected, to establish whether the column's index is complete and still matches the data. On a healthy index, ``chunks_not_indexed``, ``minmax_mismatches``, and ``positions_misaligned`` are all ``0``.

See also :ref:`accelerating_filtered_statements`, :ref:`get_chunk_info`.

Permissions
=============

The role must have the ``SUPERUSER`` permissions.

Syntax
==========

.. code-block:: postgres

   validate_chunks_indexes_statement ::=
       SELECT VALIDATE_CHUNKS_INDEXES('<schema_name>.<table_name>', '<column_name>' [, '<case_sensitive_names>'])
       ;

Parameters
============

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``schema_name.table_name``
     - The schema and table, given as a single dotted argument
   * - ``column_name``
     - The name of the column whose index is checked
   * - ``case_sensitive_names``
     - Optional. ``'false'`` converts the names to lower case, ``'true'`` uses them as written, and any other value raises an error. When the argument is omitted, the names are used as written

Returns
=========

One row per internal column id. A ``TEXT`` column is stored as more than one internal column, so checking one text column returns more than one row.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1

   * - Column name
     - Description
   * - ``column_id``
     - The internal column id
   * - ``column_name``
     - The internal column name
   * - ``index_pages``
     - Number of index pages written for this column
   * - ``indexed_chunks``
     - Number of chunks that appear in the index
   * - ``table_chunks_total``
     - Number of chunks the table actually has
   * - ``chunks_not_indexed``
     - Chunks in the table with no entry in the index
   * - ``chunks_indexed_but_missing``
     - Index entries pointing at chunks that no longer exist
   * - ``chunks_indexed_but_deleted``
     - Index entries pointing at chunks marked as deleted
   * - ``duplicate_chunk_entries``
     - Chunks appearing in the index more than once
   * - ``minmax_mismatches``
     - Entries whose minimum and maximum values disagree with the chunk itself
   * - ``first_indexed_chunk_id``
     - The lowest chunk id in the index, or ``-1`` when the index is empty
   * - ``last_indexed_chunk_id``
     - The highest chunk id in the index, or ``-1`` when the index is empty
   * - ``positions_misaligned``
     - Entry positions that do not line up across the columns of the index

Notes
===========

* ``VALIDATE_CHUNKS_INDEXES`` checks one column per call rather than reporting on a whole table.

* The statement reads the index directly for the column given, rather than scanning the whole table index.

Examples
===========

Checking a column whose index is healthy
------------------------------------------

.. code-block:: postgres

   SELECT VALIDATE_CHUNKS_INDEXES('public.transactions', 'customer_id');

Rebuilding an index and checking the result
---------------------------------------------

.. code-block:: postgres

   SELECT RECALCULATE_CHUNKS_INDEXES('public.transactions', 'customer_id');
   SELECT VALIDATE_CHUNKS_INDEXES('public.transactions', 'customer_id');
