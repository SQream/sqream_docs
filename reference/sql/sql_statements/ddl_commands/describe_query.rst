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
   * - ``HISTORY``
     - Returns closed sessions.
     - Optional
	 
**Comment** - *If HISTORY is out of scope for MVP, perhaps we should not include it in the example...*
	 
Examples
==============
The following is an example of the **DESCRIBE SESSIONS** command:

.. code-block:: postgres

   DESCRIBE QUERY [SESSION ID <session-id>] QUERY ID <query-id>;
   
**Comment** - *Can you fill in the session-id and query-id above?*
	 
Output
=============
Using the **DESCRIBE CLUSTER STATUS** command generates the following output:

+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                        | Type               | Comments                                                                                                                                                                   |
+==============================+====================+============================================================================================================================================================================+
| Query ID                     | Big Integer        | Display a link to the profiled query.                                                                                                                                      |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Node ID                      | Big Integer        | Displays the ID of the relevant node.                                                                                                                                      |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parent ID                    | Big Integer        | Displays the ID of the node's tree parent.                                                                                                                                 |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Node type                    | Text               | Displays the type of the relevant node, such as **Filter** or **Read Table**.                                                                                              |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Elapsed time                 | Datetime           | Displays the total active wall-clock time in milliseconds.                                                                                                                 |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Total compute time           | Big Integer        | Displays the total active compute time in milliseconds of all chunks passing through this CP. Can be greater than the elapsed time when multiple machines are utilized.    |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Total Wait time              | Big Integer        |                                                                                                                                                                            |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Rows produced                | Big Integer        | Displays the number of rows output by the node per chunk producer.                                                                                                         |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Chunks produced              | Big Integer        | Displays the number of chunks output by the node per chunk producer.                                                                                                       |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data read                    | Big Integer        | Displays the amount of data read from the disk (including temp).                                                                                                           |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data written                 | Big Integer        | Displays the amount of data read from the disk (including temp).                                                                                                           |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Output size                  | Big Integer        | Displays the amount of data sent over the network.                                                                                                                         |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Additional info              | Text               | Displays additional information per node type, such as information about which table was read for **ReadTable**.                                                           |
+------------------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Permissions
=============
**Comment** - *What are the permissions?*