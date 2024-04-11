.. _describe_session_queries:

************************
DESCRIBE SESSION QUERIES
************************

The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries.
A session is opened per connection or per Workbench tab.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: postgres

	DESC[RIBE] SESSION QUERIES [SESSION ID '<sessionId>' | ALL] [STATUS IN (
	   { QUEUED,
	   | EXECUTING,
	   | EXECUTION_SUCCEED,
	   | EXECUTION_FAILED,
	   | CLOSED,
	   | COMPILATION_FAILED,
	   | ABORTED,
	   | FETCHING_RESULTS,
	   | COMPILING,
	   | COMPLETE }
	   )]



Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``SESSION ID``
     - :ref:`STRING literal<literals>`	
     - The session ID of the query. If not specified the current session ID is provided
   * - ``ALL``
     - 
     - Specifies that the operation should apply to all sessions. This parameter requires ``SUPERUSER`` permissions
   * - ``STATUS IN``
     -  
     - A filter that allows you to specify a subset of statuses from the list provided (e.g., ``QUEUED``, ``EXECUTING``, ``EXECUTION_SUCCEED``, etc.) 
	 
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``query_id``
     - ``TEXT``
     - Displays the query ID
   * - ``query_status``
     - ``TEXT``
     - Displays the query status
   * - ``query_type``
     - ``TEXT``
     - Displays the query type
   * - ``sql_text``
     - ``TEXT``
     - Displays the defined SQL text from the specified query
   * - ``role``
     - ``TEXT``
     - The role who executed the query	 
   * - ``session_id``
     - ``TEXT``
     - Displays the session ID
   * - ``start_time``
     - ``DATETIME``
     - Displays query execution date and time
   * - ``end_time``
     - ``DATETIME``
     - Displays query end date and time	 
   * - ``duration``
     - ``INTEGER``
     - Query duration time (milliseconds)
   * - ``time_in_queue``
     - ``INTEGER``
     - Query time in queue (milliseconds)
   * - ``compilation_time``
     - ``INTEGER``
     - Query compilation time (milliseconds)
   * - ``execution_time``
     - ``INTEGER``    
     - The execution time (milliseconds)
   * - ``total_compute_time``
     - ``INTEGER``	 
     - The total compute time is the period when the system is actively working, measured in milliseconds. If multiple workers are handling a query, the compute time might be longer than the time it takes to execute the query
   * - ``rows_read``
     - ``INTEGER``	
     - The number of rows read by the query	 
   * - ``rows produced``
     - ``INTEGER`` 
     - The number of rows returned by the query 
   * - ``data produced``
     - ``INTEGER``	 
     - The data size produced by the query (MegaBytes)
   * - ``data_read_compressed``
     - ``INTEGER`` 
     - The size of compressed read data (MegaBytes)
   * - ``data_read_uncompressed``
     - ``INTEGER``	 
     - The size of uncompressed read data (MegaBytes)
   * - ``client_info``
     - ``TEXT``
     - Displays information about the client driver type and version
   * - ``query_error``
     - ``TEXT``
     - The reason for query failure
   * - ``pool_name``
     - ``TEXT``	 
     - The resource pool used for executing the statement

Example
=======

.. code-block:: postgres

	DESCRIBE SESSION QUERIES SESSION ID  '683256f5-66b7-4d8c-b1a2-456dddcb6dee';

Output:

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

.. code-block:: postgres

	DESCRIBE SESSIONS USER "<jobs_client_role>";
	
3. From the ``DESCRIBE SESSION`` result set, copy the relevant session id.
4. Run the ``DESCRIBE SESSION QUERIES`` statement using the ``SESSION ID`` parameter and the retrieved session id. 

Permissions
===========

A user may execute ``DESCRIBE SESSION QUERIES`` on his sessions.

``SUPERUSER`` may execute ``DESCRIBE SESSION QUERIES`` on any session.