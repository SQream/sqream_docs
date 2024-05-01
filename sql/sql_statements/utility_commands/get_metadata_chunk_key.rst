.. _get_metadata_chunk_key:

**********************
GET_METADATA_CHUNK_KEY
**********************

The ``GET_METADATA_CHUNK_KEY`` |icon-new_2022.1| command returns specific metadata key values for user-specified chunks.

.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   :width: 110

This reference page includes the following information:

.. contents:: 
   :local:
   :depth: 1

Syntax
======

The following is the syntax for the ``GET_METADATA_CHUNK_KEY`` command:

.. code-block:: postgres

   get_metadata_chunk_key(database_name, table_id, chunk_id);

Parameters
==========

The following table shows the ``GET_METADATA_CHUNK_KEY`` parameters:

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
=======

The following is an example of the ``GET_METADATA_CHUNK_KEY`` command:

.. code-block:: postgres

   master=> select get_metadata_chunk_key('master', 0, 1);

Output
======

The following table describes the output generated from the ``GET_METADATA_CHUNK_KEY`` command:

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
	 
   * - ``table_id``
     - The ID of the table where the chunk is located.
     - Numeric
     - ``0``
	 
   * - ``column_id``
     - The ID of the column.
     - Numeric
     - ``0``
	 
   * - ``chunk_status``
     - The status of the chunk.
     - Numeric
     - ``1``
	 
   * - ``chunk_aligned``
     - Describes the state of the chunk.
     - Text
     - ``chunk_state::``
	 
   * - ``offset_in_file``
     - Shows the file's offset setting.
     - Numeric
     - ``-1``
	 
   * - ``compressed_size``
     - Shows the file's compressed size.
     - Numeric
     - ``0``
	 
   * - ``uncompressed_size``
     - Shows the file's uncompressed size.
     - Numeric
     - ``2``
	 
   * - ``compression_type``
     - Shows the file's compression type.
     - Numeric
     - ``2``
	 
   * - ``min_long``
     - Shows the minimum value of the type.
     - Long
     - ``25``	
	 
   * - ``max_long``
     - Shows the maximum value in the chunk of a number.
     - Long
     - ``12345``
	 
   * - ``min_string_max_string``
     - Shows the minimum value of the string type.
     - String
     - ``"abc"``
	 
   * - ``min_numeric``
     - Shows the minimum value of the numeric type in the chunk.
     - Numeric
     - ``12.22``
	 
   * - ``max_numeric``
     - Shows the maximum value of the numeric type in the chunk.
     - Numeric
     - ``555.22``
	 
   * - ``column_aligned``
     - Relevant to text columns, aligment in memory.
     - Boolean
     - ``Yes`` / ``No``

The following is an example of the output generated from the ``GET_METADATA_CHUNK_KEY`` command:

.. code-block:: postgres

   master,0,0,1,chunk_state::clean,1,0,2,2,flat,0,0,,,0x7f722ffb7c60,0x7f722ffb7c70,1
   master,0,1,1,chunk_state::clean,1,0,8,8,flat,1,2,,,0x7f722ffb7c60,0x7f722ffb7c70,1
   master,0,2,1,chunk_state::clean,1,0,2,2,flat,0,0,,,0x7f722ffb7c60,0x7f722ffb7c70,1
   master,0,3,1,chunk_state::clean,1,0,8,8,flat,3,3,,,0x7f722ffb7c60,0x7f722ffb7c70,1
   master,0,4,1,chunk_state::clean,1,0,16,16,flat,0,0,abc,dfg,0x7f722ffb7c60,0x7f722ffb7c70,1
   
Permissions
===========

The ``GET_METADATA_CHUNK_KEY`` requires no special permissions.