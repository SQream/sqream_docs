:orphan:

.. _describe_query:

**************
DESCRIBE QUERY
**************

Displays information about query execution for monitoring and troubleshooting purposes.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: postgres

   DESC[RIBE] QUERY [SESSION ID <'session-id'>] QUERY ID <'query-id'>
   
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
     - Filters by session ID. If none specified, current session ID is used
   * - ``QUERY ID``
     - :ref:`STRING literal<literals>`	
     - ID of the query
	 
	 
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``query_id``
     - ``TEXT``
     - Displays the ID of the query
   * - ``rtc_name``
     - ``TEXT``
     - Total Run-Time Container duration 
   * - ``node_id``
     - ``INTEGER``
     - Displays the ID of the node
   * - ``parent_id``
     - ``INTEGER``
     - Displays the ID of the parent
   * - ``node_type``
     - ``TEXT``
     - Displays the node type
   * - ``elapsed_time``
     - ``INTEGER``
     - Displays the elapsed query time	 
   * - ``total_compute_time``
     - ``INTEGER``
     - Displays the query's total compute time
   * - ``total_waiting_time``
     - ``INTEGER`` 
     - Displays the query's total waiting time
   * - ``rows_produced``
     - ``INTEGER``
     - Displays the amount of rows produced by the query
   * - ``chunks_produced``
     - ``INTEGER``		 
     - Displays the amount of chunks produced by the query
   * - ``data_read``
     - ``INTEGER``
     - Displays the amount of data read by the query
   * - ``data_written``
     - ``INTEGER``
     - Displays the amount of data written by the query
   * - ``output``
     - ``INTEGER``
     - Displays the query output
   * - ``additional_info``
     - ``TEXT``
     - Displays additional information
   * - ``time``
     - ``TEXT``
     - Query execution time
   * - ``status``
     - ``INTEGER``
     - Query status
	 
Example
=======

.. code-block:: postgres

	DESCRIBE QUERY SESSION ID '6a4d1389-0330-4d54-9d52-439ff0b4c74c' QUERY ID '9';
   
	query_id                              |rtc_name                        |node_id|parent_id|node_type     |elapsed_time|total_compute_time|total_waiting_time|rows_produced|chunks_produced|data_read|data_written|output   |additional_info    |time               |status|
	--------------------------------------+--------------------------------+-------+---------+--------------+------------+------------------+------------------+-------------+---------------+---------+------------+---------+-------------------+-------------------+------+
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|1      |-1       |CloudRSend    |4.333333333 |4.333333333       |0                 |4613734      |13             |0        |0           |197467814| (single)          |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|1      |-1       |CloudRSend    |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)          |2023-01-01 11:08:22|-1    |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|1      |-1       |CloudRSend    |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)          |2023-01-01 11:08:22|-1    |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|2      |1        |Rechunk       |0.001536630 |0.001536630       |0                 |4613734      |13             |0        |0           |119957084|                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|2      |1        |Rechunk       |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|2      |1        |Rechunk       |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |



Permissions
===========

Users may execute ``DESCRIBE QUERY`` on their own sessions.

``SUPERUSER`` may execute ``DESCRIBE QUERY`` on any session.


