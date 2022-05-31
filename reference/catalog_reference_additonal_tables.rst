.. _catalog_reference_additonal_tables:

*************************************
Additional Tables
*************************************
There are additional tables in the catalog that can be used for performance monitoring and inspection.

The definition for these tables is provided below could change across SQream DB versions.

extents
----------

``extents`` identifies storage extents.

Each storage extents can contain several chunks.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the extent
   * - ``table_id``
     - ID of the table containing the extent
   * - ``column_id``
     - ID of the column containing the extent
   * - ``extent_id``
     - ID for the extent
   * - ``size``
     - Extent size in megabytes
   * - ``path``
     - Full path to the extent on the file system

chunk_columns
-------------------

``chunk_columns`` lists chunk information by column.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the extent
   * - ``table_id``
     - ID of the table containing the extent
   * - ``column_id``
     - ID of the column containing the extent
   * - ``chunk_id``
     - ID for the chunk
   * - ``extent_id``
     - ID for the extent
   * - ``compressed_size``
     - Actual chunk size in bytes
   * - ``uncompressed_size``
     - Uncompressed chunk size in bytes
   * - ``compression_type``
     - Actual compression scheme for this chunk
   * - ``long_min``
     - Minimum numeric value in this chunk (if exists)
   * - ``long_max``
     - Maximum numeric value in this chunk (if exists)
   * - ``string_min``
     - Minimum text value in this chunk (if exists)
   * - ``string_max``
     - Maximum text value in this chunk (if exists)
   * - ``offset_in_file``
     - Internal use

.. note:: This is an internal table designed for low-level performance troubleshooting.

chunks
-------

``chunks`` identifies storage chunks.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the chunk
   * - ``table_id``
     - ID of the table containing the chunk
   * - ``column_id``
     - ID of the column containing the chunk
   * - ``rows_num``
     - Amount of rows contained in the chunk
   * - ``deletion_status``
     - When data is deleted from the table, it is first deleted logically. This value identifies how much data is deleted from the chunk. ``0`` for no data, ``1`` for some data, ``2`` to specify the entire chunk is deleted.

delete_predicates
-------------------

``delete_predicates`` identifies the existing delete predicates that have not been cleaned up.

Each :ref:`DELETE <delete>` command may result in several entries in this table.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the predicate
   * - ``table_id``
     - ID of the table containing the predicate
   * - ``max_chunk_id``
     - Internal use. Placeholder marker for the highest ``chunk_id`` logged during the DELETE operation.
   * - ``delete_predicate``
     - Identifies the DELETE predicate