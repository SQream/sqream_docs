.. _abort_statement:

********************
ABORT_STATEMENT
********************
The ``ABORT_STATEMENT`` command performs a graceful stop, known as an **abort**, on an active statement. This is useful for queries that are stuck or which have been run unintentionally.

The **ABORT_STATEMENT** page describes the following:

.. contents:: 
   :local:
   :depth: 1   

For more information on getting a list of session and query ID's, see :ref:`describe_session_queries`.

.. note:: The ABORT_STATEMENT command may take a few moments to completely stop and free up all resources executing statements.

Syntax
==========
The following is the syntax for the ``ABORT_STATEMENT`` command:

.. code-block:: postgres

   ABORT( <session_id> , <query_id>)

Parameters
============
The following table describes the ``ABORT_STATEMENT`` parameters:

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1   
   
   * - **Parameter Name**
     - **Parameter Value**
     - **Description**
     - **Type**
   * - Session ID
     - ``session_id``
     - The unique ID of the aborted session.
     - Text
   * - Query ID
     - ``query_id``
     - The unique ID of the aborted query.
     - Text

Output
=========
The ``ABORT_STATEMENT`` command does not return any value, it always succeeds in providing the provided session and query IDs exist.

**Comment** - *I wasn't exactly sure what this meant, and maybe it should be reworded.*

**Comment** - *The internal Confluence doc says the following:*

*Possible return values:*

 * *abort request succesfully initated*

 * *Session ID not found*

 * *Query ID not found*

 * *Query ID in not in running state*

Notes
===========
The ``ABORT_STATEMENT`` command has no notes.

Example
===========
This section includes an example of outputting and aborting your session and query ID's:

1. Output your session and query ID's:

   .. code-block:: psql

      describe session queries;
      query_id|query_status     |query_type|sql_text                |session_id                          |start_time         |client_info        |
      --------+-----------------+----------+------------------------+------------------------------------+-------------------+-------------------+
      1       |EXECUTION_SUCCEED|SELECT    |select * from nba¶      |ed59dc5e-2fdd-4ba5-b912-c152a4562134|2022-07-24T07:30:43|SQream JDBC v0.1.33|
      2       |NEW              |DESCRIBE  |describe session queries|ed59dc5e-2fdd-4ba5-b912-c152a4562134|2022-07-24T07:30:57|SQream JDBC v0.1.33|
      3       |EXECUTING        |DESCRIBE  |describe session queries|ed59dc5e-2fdd-4ba5-b912-c152a4562134|2022-07-24T07:34:54|SQream JDBC v0.1.33|
	  
2. In our example, abort session ID **ed59dc5e-2fdd-4ba5-b912-c152a4562134**, corresponding to query ID **3**:

   .. code-block:: psql

      abort('ed59dc5e-2fdd-4ba5-b912-c152a4562134', '3')

Permissions
=============
The role must have the ``SUPERUSER`` permissions.

For more information, see `Supported Permissions <https://docs.sqream.com/en/2022.3_preview/reference/sql/sql_statements/access_control_commands/alter_default_permissions.html#supported-permissions>`_.