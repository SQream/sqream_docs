.. _describe_query:

*****************
DESCRIBE QUERY
*****************
The ``DESCRIBE QUERY`` command replaces the `SHOW_NODE_INFO <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_node_info.html>`_ command. You can use it to display information about query execution for monitoring and troubleshooting purposes.

Syntax
==========
The following is the syntax for the ``DESCRIBE QUERY`` command:

.. code-block:: postgres

   DESCRIBE QUERY [SESSION ID <session-id>] QUERY ID <query-id>;
   
Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE QUERY** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``SESSION ID``
     - ``session_id``
     - (Optional) The session ID of the query.
     - Type
   * - ``QUERY ID``
     - ``query-id``
     - The query ID of the user.
     - Required	 
	 
Example
==============
The following is an example of the ``DESCRIBE QUERY`` command:

.. code-block:: postgres

   DESCRIBE QUERY SESSION ID '3d5b9e46-4ef8-46d7-bfc3-5c19505494b5' QUERY ID '5';
	 
Output
=============
Using the ``DESCRIBE QUERY`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``query_id``
     - Displays the ID of the query.
     - Text
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097:3
   * - ``node_id``
     - Displays the ID of the node.
     - Integer
     - 1
   * - ``parent_id``
     - Displays the ID of the parent.
     - Integer
     - -1
   * - ``node_type``
     - Displays the node type.
     - Text
     - ParallelReadMetadata	 
   * - ``elapsed_time``
     - Displays the elapsed query time.
     - Integer
     - 0	 	 
   * - ``total_compute_time``
     - Displays the query's total compute time.
     - Integer
     - 0
   * - ``total_waiting_time``
     - Displays the query's total waiting time.
     - Integer
     - 0	 
   * - ``rows_produced``
     - Displays the amount of rows produced by the query.
     - Integer
     - 0
   * - ``chunks_produced``
     - Displays the amount of chunks produced by the query.
     - Integer
     - 0		 
   * - ``data_read``
     - Displays the amount of data read by the query.
     - Integer
     - 0
   * - ``data_written``
     - Displays the amount of data written by the query.
     - Integer
     - 0
   * - ``output``
     - Displays the query output.
     - Integer
     - 0
   * - ``additional_info``
     - Displays additional information.
     - Text
     - public.t1
	 
The following is an example of the generated output in Studio:

.. code-block:: postgres

   query_id,node_id,parent_id,node_type,elapsed_time,total_compute_time,total_waiting_time,rows_produced,chunks_produced,data_read,data_written,output,additional_info

**Comment** - *I wasn't able to generate an external table. Please assist.*

Permissions
=============
No permissions are required for the ``DESCRIBE QUERY`` command.