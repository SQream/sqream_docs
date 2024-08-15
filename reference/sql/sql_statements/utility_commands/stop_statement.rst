:orphan:

.. _stop_statement:

********************
STOP_STATEMENT
********************

``STOP_STATEMENT`` stops or aborts an active statement.

Syntax
==========

.. code-block:: sql

	stop_statement_statement ::=
	SELECT STOP_STATEMENT(stmt_id)
	   
	stmt_id ::= bigint

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``stmt_id``
     - The statement ID to stop


Notes
=====

This utility always succeeds even if the statement does not exist, or has already stopped.

Example
=======

1. Check your server status:

.. code-block:: psql

	SELECT SHOW_SERVER_STATUS();
	service | instanceid | connection_id | serverip      | serverport | database_name | user_name        | clientip      | statementid | statement                                                                                             | statementstarttime  | statementstatus | statementstatusstart
	--------+------------+---------------+---------------+------------+---------------+------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------+---------------------+-----------------+---------------------
	sqream  | sqream_2   |  19           | 192.168.0.111 |       5000 | master        | etl              | 192.168.0.011 |2484923      | SELECT t1.account, t1.msisd from table a t1 join table b t2 on t1.id = t2.id where t1.msid='123123';  | 17-01-2022 16:19:31 | Executing       | 17-01-2022 16:19:32
	sqream  | sqream_1   |  2            | 192.168.1.112 |       5000 | master        | etl              | 192.168.1.112 |2484924      | select show_server_status();                                                                          | 17-01-2022 16:19:39 | Executing       | 17-01-2022 16:19:39
	sqream  | None       |  248          | 192.168.1.112 |       5007 | master        | maintenance_user | 192.168.1.112 |2484665      | select * from  sqream_catalog.tables;                                                                 | 17-01-2022 15:55:01 | In Queue        | 17-01-2022 15:55:02

2. Retrieve stuck statement ID:

.. code-block:: psql

	SELECT SHOW_CONNECTIONS();
	
	ip            | conn_id  | conn_start_time     | stmt_id | stmt_start_time     | stmt                     
	--------------+----------+---------------------+---------+---------------------+-----------------------------------------------------------------------------------------------------
	192.168.0.111 |      19  | 2022-01-17 15:50:05 | 2484923 | 2022-01-17 16:19:31 | SELECT t1.account, t1.msisd from table a t1 join table b t2 on t1.id = t2.id where t1.msid='123123';
	192.168.1.112 |      2   | 2022-01-17 15:50:05 | 2484924 | 2022-01-17 16:19:39 | select show_server_status();                           
	192.168.1.112 |      248 | 2022-01-17 15:50:05 | 2484665 | 2022-01-17 15:55:01 | select * from  sqream_catalog.tables;                                                    

3. Stop stuck query:

.. code-block:: sql

	SELECT STOP_STATEMENT(2484923);

Permissions
=============

The role must have the ``SUPERUSER`` permissions.