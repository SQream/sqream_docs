.. _describe_sessions:

*****************
DESCRIBE SESSIONS
*****************
The ``DESCRIBE SESSIONS`` command replaces the `SHOW_SERVER_STATUS <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_server_status.html>`_ command, and lets you display a list of sessions:

* Actively connected sessions with no running statements
* Sessions with queued queries
* Closed sessions

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE SESSIONS [USER <username>]
   
**Comment** - *The source doc had no syntax example. Can you please provide one?*

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE CLUSTER STATUS** command:

**Comment** - *Parameter table must be based on the example when provided. The following table is just a space holder.*

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``username``
     - Displays the name of the user.
	 
Examples
==============
The following is an example of the **DESCRIBE SESSIONS** command:

.. code-block:: postgres

   EXAMPLE
   
**Comment** - *The source doc had no example. Can you please provide one?*
	 
Output
=============
Using the **DESCRIBE CLUSTER STATUS** command generates the following output:

+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Field             | Type      | Comments                                                                                                                         |
+===================+===========+==================================================================================================================================+
| Start time        | datetime  | The time at which the connection was opened.                                                                                     |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| End time          | datetime  | The time in which the connection was closed. ``null`` if active.                                                                 |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Database          | Text      |                                                                                                                                  |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Role              | Text      |                                                                                                                                  |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Source IP         | Text      |                                                                                                                                  |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Client            | Text      | Name and version of SQream driver or client used for executing the statement, such as SQream JDBC v3.4, SQream Studio v2.3)      |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Status            | Text      | One of the following:                                                                                                            |
|                   |           |                                                                                                                                  |
|                   |           |  * Active                                                                                                                        |
|                   |           |  * Closed                                                                                                                        |
|                   |           |  * Rejected                                                                                                  	         	   |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Rejection reason  | Text      | Error message                                                                                                                    |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
| Session ID        | Text      | Null for failed logins                                                                                                           |
+-------------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+

Permissions
=============
**Comment** - *What are the permissions?*