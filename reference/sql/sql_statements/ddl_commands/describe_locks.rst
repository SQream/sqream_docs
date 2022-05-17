.. _describe_locks:

*****************
DESCRIBE LOCKS
*****************
The ``DESCRIBE LOCKS`` command replaces the `SHOW_LOCKS <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_locks.html>`_ command. You can use it to return a list of locks from across your cluster.

Syntax
==========
The following is the syntax for the ``DESCRIBE LOCKS`` command::

.. code-block:: postgres

   DESCRIBE LOCKS [SESSION ID <session-id>}]

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
     - The session ID of the user.
     - (Optional) If blank, use the current session.	 
	 
Example
==============
The following is an example of the **DESCRIBE SESSIONS** command:

.. code-block:: postgres

   DESCRIBE LOCKS SESSION ID session-id;
    
Output
=============
Using the **DESCRIBE CLUSTER STATUS** command generates the following output:

+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Column                | Type      | Comments                                                                                                                                                        |
+=======================+===========+=================================================================================================================================================================+
| statement_id          | Text      | Displays the statement ID that caused the lock.                                                                                                                 |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| statement_sql         | Text      | Displays the statement text.                                                                                                                                    |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| username              | Text      | Displays the the user that executed the statement.                                                                                                              |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| locked_object         | Text      | Displays the the full qualified name of the object being locked, separated with $ (e.g. table$t$public$nba2 for table nba2 in schema public, in database t).    |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lockmode              | Text      | Displays the the locking mode (inclusive or exclusive).                                                                                                         |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| statement_start_time  | Datetime  | Displays the timestamp the statement started.                                                                                                                   |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
| lock_start_time       | Datetime  | Displays the timestamp the lock was obtained.                                                                                                                   |
+-----------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Permissions
=============
**Comment** - *What are the permissions?*