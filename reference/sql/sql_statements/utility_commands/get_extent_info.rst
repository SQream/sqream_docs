:orphan:

.. _get_extent_info:

***************
GET EXTENT INFO
***************

The ``GET EXTENT INFO`` utility command allows you to retrieve information of specific extents.

Syntax
======

.. code-block:: sql

	SELECT get_extent_info(<database_name>, <table_id>, [ column_id ])

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``database_name``
     - The database within to search for extent
   * - ``table_id``
     - The id of the table related to the extent 
   * - ``column_id``
     - The id of a specific extent to search for

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
     - 
   * - ``compressed_size``
     - 
   * - ``uncompressed_size``
     - 

Examples
========

.. code-block:: sql

	SELECT get_extent_info(mfg_ldc_lake, 17271948, 143);
	
Output:

.. code-block:: console

	database_name |table_id |column_id |chunk_id |extent_id |compressed_size |uncompressed_size
	--------------+---------+----------+---------+----------+----------------+-----------------
	mfg_ldc       |17271948 |16        |143      |142       |9892            |9892 
	mfg_ldc       |17271948 |17        |143      |142       |8               |39568 


Permissions
===========

This utility function requires a ``SUPERUSER`` permission.