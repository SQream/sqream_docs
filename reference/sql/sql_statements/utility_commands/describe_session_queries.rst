.. _describe_session_queries:

************************
DESCRIBE SESSION QUERIES
************************

The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries.
A session is opened per connection or per Workbench tab.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE SESSION QUERIES`` command:

.. code-block:: postgres

   DESC[RIBE] SESSION QUERIES  [SESSION ID '<session-id>'] 

Parameters
==========

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
     - The session ID of the query
     - ``TEXT``
	 
.. note:: The ``SESSION_ID`` parameter is optional. If you do not specify a session ID, SQream uses the session ID of the current session.
	 
   	 
Output
======

Using the ``DESCRIBE SESSION QUERIES`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``query_id``
     - Displays the query ID
     - ``TEXT``
     - ``b6173e04-6e2a-4266-bef0-6fc9b8ffc097:3``
   * - ``query_status``
     - Displays the query status
     - ``TEXT``
     - ``EXECUTION_FAILED``
   * - ``query_type``
     - Displays the query type
     - ``TEXT``
     - ``SELECT``
   * - ``sql_text``
     - Selects the defined SQL text from the specified table
     - ``TEXT``
     - ``SELECT * FROM t1``
   * - ``role``
     - The role who executed the query
     - ``TEXT``
     - ``sqream``	 
   * - ``session_id``
     - Selects the session ID
     - ``TEXT``
     - ``b6173e04-6e2a-4266-bef0-6fc9b8ffc097``
   * - ``start_time``
     - Displays query execution date and time
     - ``DATETIME``
     - ``2022-05-02T15:32:49``
   * - ``end_time``
     - Displays query end date and time
     - ``DATETIME``
     - ``2024-01-09T10:37:04``	 
   * - ``duration``
     - Query duration time
     - ``INTEGER``
     - ``64``	 
   * - ``time_in_queue``
     - Query time in queue (milliseconds)
     - ``INTEGER``
     - ``0``	 
   * - ``compilation_time``
     - Query compilation time (milliseconds)
     - ``INTEGER``
     - ``18``	 
   * - ``execution_time``
     - The execution time (milliseconds)
     - ``INTEGER``   
     - ``0``	 
   * - ``total_compute_time``
     - The total compute time during which the system actively engaged (milliseconds)
     - ``INTEGER``
     - ``0``	 
   * - ``rows_read``
     - The number of rows read by the query
     - ``INTEGER``
     - ``1456``	 
   * - ``rows produced``
     - The number of rows returned by the query 
     - ``INTEGER``
     - ``65``	 
   * - ``data produced``
     - The amount of data produced by the query (MegaBytes)
     - ``INTEGER``
     - ``813``	 
   * - ``data_read_compressed``
     - The amount of compresses read data
     - ``INTEGER``
     - ``0``	 
   * - ``data_read_uncompressed``
     - The amount of uncompressed read data
     - ``INTEGER``
     - ``0``	 
   * - ``client_info``
     - Displays information about the client
     - ``TEXT``
     - ``SQream JDBC v0.1.33`` 
   * - ``query_error``
     - The reason for query failure
     - ``TEXT``
     - ``Error in compilation process: : Wrapped CalciteException Cause: org.apache.calcite.sql.validate.SqlValidatorException: Object 'master.public.talia' not found``
   * - ``pool_name``
     - The resource pool used for executing the statement
     - ``TEXT``
     - ``BI``	 	 

Example
=======

The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: sql

   DESCRIBE SESSION QUERIES SESSION ID  '683256f5-66b7-4d8c-b1a2-456dddcb6dee';
   
.. code-block:: none

	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|query_id|query_status|query_type|sql_text                                             |role                 |session_id                          |start_time         |end_time           |duration|time_in_queue|compilation_time|execution_time|total_compute_time                                      |rows_read|rows produced|data produced|data_read_compressed|data_read_uncompressed|client_info   |query_error|pool_name|
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|6       |COMPLETE    |SELECT    |SELECT * FROM MyTable ORDER BY salary DESC LIMIT 5   |taliar@sqreamtech.com|683256f5-66b7-4d8c-b1a2-456dddcb6dee|2024-01-11T10:47:53|2024-01-11T10:47:55|2137    |0            |139             |1673          |0.56312761833333324634764949223608709871768951416015625 |50       |5            |245          |1624                |                      |SQream Node.js|           |sqream   |
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|5       |COMPLETE    |UPDATE    |UPDATE MyTable SET salary = 55000 WHERE name = 'John'|taliar@sqreamtech.com|683256f5-66b7-4d8c-b1a2-456dddcb6dee|2024-01-11T10:47:49|2024-01-11T10:47:51|1958    |0            |258             |789           |0.2553759140000000371628630091436207294464111328125     |50       |0            |0            |874                 |                      |SQream Node.js|           |sqream   |
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|4       |COMPLETE    |SELECT    |SELECT * FROM MyTable ORDER BY age DESC LIMIT 10000  |taliar@sqreamtech.com|683256f5-66b7-4d8c-b1a2-456dddcb6dee|2024-01-11T10:47:46|2024-01-11T10:47:49|2417    |0            |114             |1727          |0.57934194233333347057168793980963528156280517578125    |50       |50           |1720         |1624                |                      |SQream Node.js|           |sqream   |
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|3       |COMPLETE    |SELECT    |select 1 LIMIT 10000                                 |taliar@sqreamtech.com|683256f5-66b7-4d8c-b1a2-456dddcb6dee|2024-01-11T10:47:44|2024-01-11T10:47:45|1373    |0            |122             |708           |0.33468688299999993507327644692850299179553985595703125 |0        |1            |65           |0                   |                      |SQream Node.js|           |BI       |
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|2       |COMPLETE    |SELECT    |SELECT AVG(salary)  AS  average_salary  FROM  MyTable|taliar@sqreamtech.com|683256f5-66b7-4d8c-b1a2-456dddcb6dee|2024-01-11T10:47:04|2024-01-11T10:47:07|2738    |0            |476             |1764          |0.457902023999999963077556230928166769444942474365234375|50       |1            |72           |250                 |                      |SQream Node.js|           |BI       |
	|        |            |          |LIMIT 10000                                          |                     |                                    |                   |                   |        |             |                |              |                                                        |         |             |             |                    |                      |              |           |         |
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	|1       |COMPLETE    |SELECT    |select * from mytable LIMIT 10000                    |taliar@sqreamtech.com|683256f5-66b7-4d8c-b1a2-456dddcb6dee|2024-01-11T10:46:56|2024-01-11T10:46:58|2481    |0            |202             |1694          |0.651208106333333258675111210322938859462738037109375   |50       |50           |1720         |1624                |                      |SQream Node.js|           |sqream   |
	+--------+------------+----------+-----------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+--------------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+

To list the **Jobs** session queries:

1. Go to **Settings** > **Access Token Management** and locate the **Jobs** connection **Client Role**.
2. Run the ``DESCRIBE SESSION`` statement using the ``USER`` parameter and the retrieved client role:

.. code-block::

	DESCRIBE SESSIONS USER "<jobs_client_role>";
	
3. From the ``DESCRIBE SESSION`` result set, copy the relevant session id.
4. Run the ``DESCRIBE SESSION QUERIES`` statement using the ``SESSION ID`` parameter and the retrieved session id. 

Permissions
===========

A user may execute ``DESCRIBE SESSION QUERIES`` on his sessions.

``SUPERUSER`` may execute ``DESCRIBE SESSION QUERIES`` on any session.