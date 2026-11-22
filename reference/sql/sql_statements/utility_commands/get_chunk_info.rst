:orphan:

.. _get_chunk_info:

**************
GET CHUNK INFO
**************

The ``GET CHUNK INFO`` utility command allows you to retrieve information of specific chunks.

Syntax
======

.. code-block:: sql

	SELECT get_chunk_info(<database_name>, <table_id>, [ chunck_id ])

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``database_name``
     - The database within to search for chunk
   * - ``table_id``
     - The id of the table related to the chunk 
   * - ``chunck_id``
     - The id of a specific chunk to search for

Returns
=======

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``database_name``
     - The database within the chunk exists
   * - ``table_id``
     - The id of the table related to the chunk 
   * - ``column_id``
     - The id of the column related to the chunk
   * - ``chunk_id``
     - The id of the chunk
   * - ``extent_id``
     - The id of the extent
   * - ``uncompressed_size``
     - The size of the chunk's compressed data (see the note below)
   * - ``uncompressed_size``
     - The size of the chunk's uncompressed data
   * - ``compressed_Type``
     - The compression type of the chunk
   * - ``long_min``
     - The chunk's minimum value, as an integer
   * - ``long_max``
     - The chunk's maximum value, as an integer
   * - ``string_min``
     - The chunk's minimum value, as a string
   * - ``string_max``
     - The chunk's maximum value, as a string
   * - ``numeric_min``
     - The chunk's minimum value, as a numeric
   * - ``numeric_max``
     - The chunk's maximum value, as a numeric
   * - ``offset_in_file``
     - The offset of the chunk within its file

.. note:: The result set contains two columns named ``uncompressed_size``. The first one (the sixth column) holds the chunk's compressed size; the second one holds the uncompressed size.

Examples
========

.. code-block:: sql

	SELECT get_chunk_info('mfg_ldc_lake', 17271948, 143);
	
Output:

.. code-block:: console

	database_name |table_id |column_id |chunk_id |extent_id |compressed_size |uncompressed_size
	--------------+---------+----------+---------+----------+----------------+-----------------
	mfg_ldc       |17271948 |16        |143      |142       |9892            |9892 
	mfg_ldc       |17271948 |17        |143      |142       |8               |39568 


Permissions
===========

This utility function requires no special permissions.