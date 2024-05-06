:orphan:

.. _abort:

********************
ABORT
********************

The ``ABORT`` command performs a graceful stop, known as an **abort**, on an active statement. This is useful for queries that are stuck or which have been run unintentionally.

The **ABORT** page describes the following:


Syntax
==========

.. code-block:: sql

   ABORT( <'session_id'> , <'query_id'>)

Parameters
============

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1   
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - Session ID
     - ``session_id``
     - The unique ID of the session.
     - TEXT
   * - Query ID
     - ``query_id``
     - The unique ID of the aborted query.
     - TEXT
	 
To retrieve a list of all queries per session, see :ref:`describe_session_queries`.

Output
=========

The ``ABORT`` command does not return any value. As long as the session and query ID that you specify exist, the ``ABORT`` command successfully initiates an abort.

Notes
===========

The ``ABORT`` command may take a few moments to completely stop and free up all resources executing statements.

Example
===========

1. Retrieve your session and query ID:

.. code-block:: sql

	DESCRIBE session queries;
	
Output:
	
.. code-block:: sql
	
	query_id|query_status     |query_type|sql_text                |session_id                          |start_time         |client_info        |
	--------+-----------------+----------+------------------------+------------------------------------+-------------------+-------------------+
	1       |EXECUTION_SUCCEED|SELECT    |select * from nba¶      |ed59dc5e-2fdd-4ba5-b912-c152a4562134|2022-07-24T07:30:43|SQream JDBC v0.1.33|
	2       |NEW              |DESCRIBE  |describe session queries|ed59dc5e-2fdd-4ba5-b912-c152a4562134|2022-07-24T07:30:57|SQream JDBC v0.1.33|
	3       |EXECUTING        |DESCRIBE  |describe session queries|ed59dc5e-2fdd-4ba5-b912-c152a4562134|2022-07-24T07:34:54|SQream JDBC v0.1.33|
	  
2. Abort stuck query:

.. code-block:: psql

	ABORT('ed59dc5e-2fdd-4ba5-b912-c152a4562134', '3')

Permissions
=============

The role must have the ``SUPERUSER`` permissions.
