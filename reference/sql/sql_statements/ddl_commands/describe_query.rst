.. _describe_query:

*****************
DESCRIBE QUERY
*****************
The ``DESCRIBE QUERY`` command replaces the `SHOW_NODE_INFO <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_node_info.html>`_ command. You can use it to display information about query execution for monitoring and troubleshooting purposes.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
==========
The following is the syntax for the ``DESCRIBE QUERY`` command:

.. code-block:: postgres

   DESCRIBE QUERY [SESSION ID <session-id>] QUERY ID <query-id>;
   
Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE QUERY** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``SESSION ID``
     - ``session_id``
     - (Optional) The session ID of the query. If not supplied current session ID is used.
     - Int
   * - ``QUERY ID``
     - ``query-id``
     - The query ID of the user.
     - Text
	 
	 
Output
=============
Using the ``DESCRIBE QUERY`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``query_id``
     - Displays the ID of the query.
     - Text
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097:3
   * - ``node_id``
     - Displays the ID of the node.
     - Integer
     - 1
   * - ``parent_id``
     - Displays the ID of the parent.
     - Integer
     - -1
   * - ``node_type``
     - Displays the node type.
     - Text
     - ParallelReadMetadata	 
   * - ``elapsed_time``
     - Displays the elapsed query time.
     - Integer
     - 0	 	 
   * - ``total_compute_time``
     - Displays the query's total compute time.
     - Integer
     - 0
   * - ``total_waiting_time``
     - Displays the query's total waiting time.
     - Integer
     - 0	 
   * - ``rows_produced``
     - Displays the amount of rows produced by the query.
     - Integer
     - 0
   * - ``chunks_produced``
     - Displays the amount of chunks produced by the query.
     - Integer
     - 0		 
   * - ``data_read``
     - Displays the amount of data read by the query.
     - Integer
     - 0
   * - ``data_written``
     - Displays the amount of data written by the query.
     - Integer
     - 0
   * - ``output``
     - Displays the query output.
     - Integer
     - 0
   * - ``additional_info``
     - Displays additional information.
     - Text
     - public.t1
   * - ``time``
     - Query execution time
     - Integer
     - 2023-01-01 11:08:22
   * - ``status``
     - Query status
     - Integer
     - 1
	 
Example
==============
The following is an example of the ``DESCRIBE QUERY`` command:

.. code-block:: postgres

   DESCRIBE QUERY SESSION ID '6a4d1389-0330-4d54-9d52-439ff0b4c74c' QUERY ID 9;
   
The following is an example of the ``DESCRIBE QUERY`` command output:

 .. code-block:: console
   
	query_id                              |rtc_name                        |node_id|parent_id|node_type     |elapsed_time|total_compute_time|total_waiting_time|rows_produced|chunks_produced|data_read|data_written|output   |additional_info    |time               |status|
	--------------------------------------+--------------------------------+-------+---------+--------------+------------+------------------+------------------+-------------+---------------+---------+------------+---------+-------------------+-------------------+------+
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|1      |-1       |CloudRSend    |4.333333333 |4.333333333       |0                 |4613734      |13             |0        |0           |197467814| (single)          |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|1      |-1       |CloudRSend    |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)          |2023-01-01 11:08:22|-1    |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|1      |-1       |CloudRSend    |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)          |2023-01-01 11:08:22|-1    |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|2      |1        |Rechunk       |0.001536630 |0.001536630       |0                 |4613734      |13             |0        |0           |119957084|                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|2      |1        |Rechunk       |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|2      |1        |Rechunk       |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|3      |2        |ReorderInput  |0.001182357 |0.001182357       |0                 |4613734      |13             |0        |0           |119957084|                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|3      |2        |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|3      |2        |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|4      |3        |DeferredGather|0.032412838 |0.032412838       |0                 |4613734      |13             |0        |0           |138412020|                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|4      |3        |DeferredGather|0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|4      |3        |DeferredGather|0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|5      |4        |ReorderInput  |0.001415770 |0.001415770       |0                 |5033164      |14             |0        |0           |58117572 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|5      |4        |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|5      |4        |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|6      |5        |GpuToCpu      |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|6      |5        |GpuToCpu      |0.006428069 |0.006428069       |0                 |5033164      |14             |0        |0           |45298476 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|6      |5        |GpuToCpu      |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|7      |6        |ReorderInput  |0.001485682 |0.001485682       |0                 |5033164      |14             |0        |0           |45298476 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|7      |6        |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|7      |6        |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|8      |7        |Filter        |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|8      |7        |Filter        |0.004193985 |0.004193985       |0                 |5033164      |14             |0        |0           |50331640 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|8      |7        |Filter        |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|9      |8        |GpuTransform  |0.003437200 |0.003437200       |0                 |12582910     |14             |0        |0           |125829100|                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|9      |8        |GpuTransform  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|9      |8        |GpuTransform  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|10     |9        |GpuDecompress |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|10     |9        |GpuDecompress |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|10     |9        |GpuDecompress |0.005545857 |0.005545857       |0                 |12582910     |14             |0        |0           |113246190|                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|11     |10       |GpuTransform  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|11     |10       |GpuTransform  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|11     |10       |GpuTransform  |0.002736228 |0.002736228       |0                 |12582910     |14             |0        |0           |55165840 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|12     |11       |CpuToGpu      |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|12     |11       |CpuToGpu      |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|12     |11       |CpuToGpu      |0.002053339 |0.002053339       |0                 |12582910     |14             |0        |0           |4834200  |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|13     |12       |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|13     |12       |ReorderInput  |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|13     |12       |ReorderInput  |0.001914057 |0.001914057       |0                 |12582910     |14             |0        |0           |4834200  |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|14     |13       |Rechunk       |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|14     |13       |Rechunk       |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|14     |13       |Rechunk       |0.002404408 |0.002404408       |0                 |12582910     |14             |0        |0           |17653296 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|15     |14       |CpuDecompress |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|15     |14       |CpuDecompress |0           |0                 |0                 |0            |0              |0        |0           |0        |                   |2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|15     |14       |CpuDecompress |0.001846970 |0.001846970       |0                 |12582910     |14             |0        |0           |17653296 |                   |2023-01-01 11:08:22|1     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-f6ps7|16     |15       |ReadTable     |0           |0                 |0                 |0            |0              |0        |0           |0        |public.cool_animals|2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-rcpgn|16     |15       |ReadTable     |0           |0                 |0                 |0            |0              |0        |0           |0        |public.cool_animals|2023-01-01 11:08:22|2     |
	6a4d1389-0330-4d54-9d52-439ff0b4c74c:9|sqream-worker-0-58f59bcc96-xh6tx|16     |15       |ReadTable     |0.011688731 |0.011688731       |0                 |12582910     |14             |34384215 |0           |17653296 |public.cool_animals|2023-01-01 11:08:22|1     |


Permissions
=============
Users may execute ``DESCRIBE QUERY`` on their own sessions.

``SUPERUSER`` may execute ``DESCRIBE QUERY`` on any session.


