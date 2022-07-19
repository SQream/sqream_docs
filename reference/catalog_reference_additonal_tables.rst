.. _catalog_reference_additonal_tables:

*************************************
Additional Tables
*************************************
The Reference Catalog includes additional tables that can be used for performance monitoring and inspection. The definition for these tables described on this page may change across SQream versions.

.. contents:: 
   :local:
   :depth: 1

Extents
----------
The ``extents`` storage object identifies storage extents, and each storage extents can contain several chunks.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the databse containing the extent.
   * - ``table_id``
     - Shows the ID of the table containing the extent.
   * - ``column_id``
     - Shows the ID of the column containing the extent.
   * - ``extent_id``
     - Shows the ID for the extent.
   * - ``size``
     - Shows the extent size in megabytes.
   * - ``path``
     - Shows the full path to the extent on the file system.

Chunk Columns
-------------------
The ``chunk_columns`` storage object lists chunk information by column.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the databse containing the extent.
   * - ``table_id``
     - Shows the ID of the table containing the extent.
   * - ``column_id``
     - Shows the ID of the column containing the extent.
   * - ``chunk_id``
     - Shows the chunk ID.
   * - ``extent_id``
     - Shows the extent ID.
   * - ``compressed_size``
     - Shows the compressed chunk size in bytes.
   * - ``uncompressed_size``
     - Shows the uncompressed chunk size in bytes.
   * - ``compression_type``
     - Shows the chunk's actual compression scheme.
   * - ``long_min``
     - Shows the minimum numeric value in the chunk (if one exists).
   * - ``long_max``
     - Shows the maximum numeric value in the chunk (if one exists).
   * - ``string_min``
     - Shows the minimum text value in the chunk (if one exists).
   * - ``string_max``
     - Shows the maximum text value in the chunk (if one exists).
   * - ``offset_in_file``
     - Reserved for internal use.

.. note:: This is an internal table designed for low-level performance troubleshooting.

Chunks
-------
The ``chunks`` storage object identifies storage chunks.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the databse containing the chunk.
   * - ``table_id``
     - Shows the ID of the table containing the chunk.
   * - ``column_id``
     - Shows the ID of the column containing the chunk.
   * - ``rows_num``
     - Shows the amount of rows in the chunk.
   * - ``deletion_status``
     - Determines what data to logically delete from the table first, and identifies how much data to delete from the chunk. The value ``0`` is ued for no data, ``1`` for some data, and ``2`` to delete the entire chunk.
	 
.. note:: This is an internal table designed for low-level performance troubleshooting.

Delete Predicates
-------------------
The ``delete_predicates`` storage object identifies the existing delete predicates that have not been cleaned up.

Each :ref:`DELETE <delete>` command may result in several entries in this table.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the databse containing the predicate.
   * - ``table_id``
     - Shows the ID of the table containing the predicate.
   * - ``max_chunk_id``
     - Reserved for internal use, this is a placeholder marker for the highest ``chunk_id`` logged during the ``DELETE`` operation.
   * - ``delete_predicate``
     - Identifies the DELETE predicate.
	 
.. note:: This is an internal table designed for low-level performance troubleshooting.