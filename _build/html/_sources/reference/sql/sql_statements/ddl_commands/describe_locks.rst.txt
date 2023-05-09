.. _describe_locks:

*****************
DESCRIBE LOCKS
*****************
The ``DESCRIBE LOCKS`` command replaces the `SHOW_LOCKS <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_locks.html>`_ command. You can use it to return a list of locks from across your cluster.

Syntax
==========
The following is the syntax for the ``DESCRIBE LOCKS`` command:

.. code-block:: postgres

   DESCRIBE LOCKS
   
Parameters
============
``DESCRIBE LOCKS`` command has no input parameters.

    
Output
=============
Using the **DESCRIBE CLUSTER STATUS** command generates the following output:

+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Column                | Type      | Comments                                                                                                                                                        |
+=======================+===========+=================================================================================================================================================================+
| statement_id          | Text      | Displays the statement ID that caused the lock.                                                                                                                 |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| username              | Text      | Displays the the user that executed the statement.                                                                                                              |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| server		        | Text      | Displays the the server name                                                                                                                                    |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| port  		        | Text      | Displays the the port number                                                                                                                                    |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| locked_object         | Text      | Displays the the full qualified name of the object being locked, separated with $ (e.g. table$t$public$nba2 for table nba2 in schema public, in database t).    |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lockmode              | Text      | Displays the the locking mode (inclusive or exclusive).                                                                                                         |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| statement_start_time  | Datetime  | Displays the timestamp the statement started.                                                                                                                   |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
| lock_start_time       | Datetime  | Displays the timestamp the lock was obtained.                                                                                                                   |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| statement_string      | Text      | The SQL syntax that triggered this lock.                                                                                                                        |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Permissions
=============
Using the ``DESCRIBE LOCKS`` command requires ``SUPERUSER`` permissions.