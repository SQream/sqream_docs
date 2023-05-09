.. _get_extents_file_list_for_chunk:

********************
GET_EXTENTS_FILE_FOR_CHUNK
********************
The ``GET_EXTENTS_FILE_FOR_CHUNK`` |icon-new_2022.1| command points to all files that contain data related to a specific chunk. This command is used for debugging purposes.

.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   :width: 110

This reference page includes the following information:

.. contents:: 
   :local:
   :depth: 1

Syntax
==========
The following is the syntax for the ``GET_EXTENTS_FILE_FOR_CHUNK`` command:

.. code-block:: postgres

   select get_extents_file_list_for_chunk(database_name, "
        "table_id, chunk_id);"
		
Parameters
============
The following table shows the ``GET_EXTENTS_FILE_FOR_CHUNK`` parameters:

.. list-table:: 
   :widths: 10 100
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``database_name``
     - The name of the database where the chunk is located.
   * - ``table_id``
     - The ID of the table where the chunk is located.
   * - ``chunk_id``
     - The ID of the chunk.	 

Example
===========
The following is an example of the ``GET_EXTENTS_FILE_FOR_CHUNK`` command:

.. code-block:: postgres

   master=> select get_extents_file_list_for_chunk('master', 0, 3);
	 
Output
==========
The following table describes the output generated from the ``GET_EXTENTS_FILE_FOR_CHUNK`` command:

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
	 
   * - ``database_name``
     - The name of the database where the chunk is located.
     - Text
     - ``master``
	 
   * - ``table_name``
     - The ID of the table where the chunk is located.
     - Numeric
     - ``0``
	 
   * - ``table_id``
     - The ID of the column.
     - Numeric
     - ``0``
	 
   * - ``column_id``
     - The status of the chunk.
     - Numeric
     - ``1``
	 
   * - ``chunk_id``
     - Describes the state of the chunk.
     - Numeric
     - ``chunk_state::``
	 
   * - ``file_path``
     - Shows the path of the file.
     - Text
     - /home/sqream_testing_temp/sqreamdb/databases/master/tables
	 
The following is an example of the output generated from the ``GET_EXTENTS_FILE_FOR_CHUNK`` command:

.. code-block:: postgres

   master,public.t_1,0,0,3,/home/sqream_testing_temp/sqreamdb/databases/master/tables
   master,public.t_1,0,1,3,/home/sqream_testing_temp/sqreamdb/databases/master/tables
   master,public.t_1,0,2,3,/home/sqream_testing_temp/sqreamdb/databases/master/tables 
   master,public.t_1,0,3,3,/home/sqream_testing_temp/sqreamdb/databases/master/tables
   master,public.t_1,0,4,3,/home/sqream_testing_temp/sqreamdb/databases/master/tables
   
Permissions
=============
The ``GET_EXTENTS_FILE_FOR_CHUNK`` requires no special permissions.