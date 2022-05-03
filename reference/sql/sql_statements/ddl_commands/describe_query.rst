.. _describe_query:

*****************
DESCRIBE QUERY
*****************
The ``DESCRIBE SESSIONS`` command replaces the `SHOW_NODE_INFO <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_node_info.html>`_ command. You can use it to display information about query execution for monitoring and troubleshooting purposes.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE QUERY [SESSION ID <session-id>] QUERY ID <query-id>;
   
Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE CLUSTER STATUS** command:

**Comment** - *Parameter table must be based on the example when provided. The following table is just a space holder.*

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
     - Status
   * - ``session-id``
     - Displays the session ID of the user.
     - (Optional) If blank, use the current session.
   * - ``query-id``
     - Displays the query ID of the user.
     - Required	 
	 
Example
==============
The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE QUERY SESSION ID '3d5b9e46-4ef8-46d7-bfc3-5c19505494b5' QUERY ID '5';
	 
Output
=============
**Comment** - *On the other pages I used the example above in the table below. Do we want to do the same with this page?*

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

Permissions
=============
**Comment** - *What are the permissions?*