.. _describe_session_queries:

*****************
DESCRIBE SESSION QUERIES
*****************
The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries.
A session is opened per connection or per tab.

Syntax
==========
The following is the syntax for the ``DESCRIBE SESSION QUERIES`` command:

.. code-block:: postgres

   DESCRIBE SESSION QUERIES  [SESSION ID <session-id>] 

Parameters
============
The following parameters can be used with the ``DESCRIBE SESSION QUERIES`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``SESSION ID``
     - ``session_id``
     - The session ID of the query.
     - Text
	 
.. note:: The ``SESSION_ID`` parameter is optional. If you do not specify a session ID, SQream uses the session ID of the current session.
	 
   	 
Output
=============
Using the ``DESCRIBE SESSIONS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``query_id``
     - Displays the query ID.
     - Text
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097:3
   * - ``query_status``
     - Displays the query status.
     - Text
     - EXECUTION_FAILED
   * - ``query_type``
     - Displays the query type.
     - Text
     - SELECT
   * - ``sql_text``
     - Selects the defined SQL text from the specified table.
     - Text
     - select * from t1
   * - ``session_id``
     - Selects the session ID.
     - Text
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097
   * - ``start_time``
     - Displays the start date and time.
     - Type
     - 2022-05-02T15:32:49
   * - ``client_info``
     - Displays information about the client.
     - Type
     - SQream JDBC v0.1.33 

Example
==============
The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSION QUERIES SESSION ID  '9a034b00-bbfc-4c5f-8e84-bdddc057e9fe';
   

+-----------+--------------------+-------------+---------------------------------------------------------------+---------------------------------------+---------------------+---------------------+------------+-----------------------+
| query_id  | query_status       | query_type  | sql_text                                                      | session_id                            | start_time          | end_time            | user_name  | client_info           |
+===========+====================+=============+===============================================================+=======================================+=====================+=====================+============+=======================+
| 34        | NEW                | DESCRIBE    | describe session queries                                      | 9a034b00-bbfc-4c5f-8e84-bdddc057e9fe  | 2022-09-14 5:37:34  | null                | sqream     | SQream JDBC v0.1.33   |
+-----------+--------------------+-------------+---------------------------------------------------------------+---------------------------------------+---------------------+---------------------+------------+-----------------------+
| 33        | EXECUTION_SUCCEED  | DESCRIBE    | DESCRIBE ROLES LIKE 'sq%'                                     | 9a034b00-bbfc-4c5f-8e84-bdddc057e9fe  | 2022-09-14 5:37:27  | 2022-09-14 5:37:27  | sqream     | SQream JDBC v0.1.33   |
+-----------+--------------------+-------------+---------------------------------------------------------------+---------------------------------------+---------------------+---------------------+------------+-----------------------+
| 32        | EXECUTION_SUCCEED  | DESCRIBE    | describe saved queries list DATABASE master like 'select%'    | 9a034b00-bbfc-4c5f-8e84-bdddc057e9fe  | 2022-09-14 5:37:16  | 2022-09-14 5:37:16  | sqream     | SQream JDBC v0.1.33   |
+-----------+--------------------+-------------+---------------------------------------------------------------+---------------------------------------+---------------------+---------------------+------------+-----------------------+
| 31        | EXECUTION_SUCCEED  | SELECT      | SELECT id, name, weight FROM cool_animals where weight > 10;  | 9a034b00-bbfc-4c5f-8e84-bdddc057e9fe  | 2022-09-14 5:37:08  | 2022-09-14 5:37:09  | sqream     | SQream JDBC v0.1.33   |
+-----------+--------------------+-------------+---------------------------------------------------------------+---------------------------------------+---------------------+---------------------+------------+-----------------------+
| 30        | COMPILATION_FAILED | SELECT      | select * from external_tables                                 | 9a034b00-bbfc-4c5f-8e84-bdddc057e9fe  | 2022-09-14 5:37:01  | 2022-09-14 5:37:01  | sqream     | SQream JDBC v0.1.33   |
+-----------+--------------------+-------------+---------------------------------------------------------------+---------------------------------------+---------------------+---------------------+------------+-----------------------+


Permissions
=============
A user may execute ``DESCRIBE SESSION QUERIES`` on his sessions.

``SUPERUSER`` may execute ``DESCRIBE SESSION QUERIES`` on any session.