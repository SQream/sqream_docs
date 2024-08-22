:orphan:

.. _remove_lock:

***********
REMOVE LOCK
***********

The ``REMOVE LOCK`` utility function clears orphaned locks that block file cleanup and prevent operations on locked objects within the system.

To remove all existing locks, see :ref:`remove_statement_locks`

Read more about locks in :ref:`concurrency_and_locks`.

Syntax
======

.. code-block:: postgres

	SELECT REMOVE_LOCK(<locked_object>, <stmt_id> [, <ignore_stmt_exists> ])

Example
=======

#. Get locked object names:

   .. code-block:: postgres

	SELECT SHOW_LOCKS();
	
   Output:

   .. code-block:: console

	statement id |statement string                  |username |server       |port |locked object             |lock mode |statement start time |lock start time     |is_statement_active |is_snapshot_active
	-------------+----------------------------------+---------+-------------+-----+--------------------------+----------+---------------------+--------------------+--------------------+------------------
	0            |COPY schema.table FROM WRAPPER .. |sqream   |192.168.4.35 |5000 |database$master           |Inclusive |29-10-2023 14:20:08  |2023-10-29 14:20:08 |1                   |1
	0            |COPY schema.table FROM WRAPPER .. |sqream   |192.168.4.35 |5000 |schema$master$schema      |Inclusive |29-10-2023 14:20:08  |2023-10-29 14:20:08 |1                   |1
	0            |COPY schema.table FROM WRAPPER .. |sqream   |192.168.4.35 |5000 |table$master$schema$table |Inclusive |29-10-2023 14:20:08  |2023-10-29 14:20:08 |1                   |1

#. Show server status:

   .. code-block:: postgres

	SELECT SHOW_SERVER_STATUS();
	
   Output:

   .. code-block:: console

	service |instanceid |connection_id |serverip     |serverport |database_name |user_name |clientip     |statementid |statement                                                                                                                      |statementstarttime  |statementstatus |statementstatusstart
	--------+-----------+--------------+-------------+-----------+--------------+----------+-------------+------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------+----------------+--------------------
	sqream  |node_9383  |1             |192.168.4.35 |5000       |master        |sqream    |192.168.4.35 |0           |COPY schema.table FROM WRAPPER parquet_fdw OPTIONS (location='/abc/*.c000', CONTINUE_ON_ERROR=true, ERROR_LOG='/abc/log_out'); |29-10-2023 14:20:08 |Executing       |29-10-2023 14:20:08

#. Remove a specific lock:

   .. code-block:: postgres

	SELECT REMOVE_LOCK ('database$master', 0);

   .. code-block:: postgres

	SELECT REMOVE_LOCK ('schema$master$schema', 0);

   .. code-block:: postgres

	SELECT REMOVE_LOCK ('table$master$schema$table', 0);





Permissions
===========

This utility function requires a ``SUPERUSER`` permission on the database level.
