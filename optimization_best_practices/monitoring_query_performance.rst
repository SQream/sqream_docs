.. _monitoring_query_performance:

****************************
Monitoring Query Performance
****************************

This document aims to provide guidance on analyzing query performance through the examination of execution plans. The emphasis is on pinpointing bottlenecks and exploring potential optimization techniques to enhance overall query performance. When delving into query tuning options, the initial step involves a comprehensive analysis of the query plan and execution. The query plan and execution details provide insights into how BLUE processes a query and where the majority of processing time is allocated. 

It's crucial to recognize that performance tuning options vary for each query. Recommendations and tips should be tailored to suit the specifics of individual workloads. Additionally, referring to our :ref:`sql_best_practices` guide is advisable for a deeper understanding of considerations related to data loading and other best practices.

Using the ``DESCRIBE QUERY`` Command
====================================

The :ref:`DESCRIBE QUERY<describe_query>` command provides instantaneous and historical overview of the current query plan by presenting a real-time depiction of the compiler's execution strategy and performance metrics for the designated query.

For example:

.. code-block:: sql
   
   DESCRIBE SESSION QUERIES SESSION ID  '75b64bd1-f237-4336-8011-3d29239bd9bb';
   
Output:

.. code-block:: none

	query_id|query_status|query_type|sql_text                                                                                                                                                                                            |role                 |session_id                          |start_time         |end_time           |duration|time_in_queue|compilation_time|execution_time|total_compute_time                                  |rows_read|rows produced|data produced|data_read_compressed|data_read_uncompressed|client_info   |query_error|pool_name|
	--------+------------+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------+-------------------+-------------------+--------+-------------+----------------+--------------+----------------------------------------------------+---------+-------------+-------------+--------------------+----------------------+--------------+-----------+---------+
	29      |COMPLETE    |SELECT    |SELECT nation,o_year,Sum(amount)AS sum_profit FROM( SELECT n_name AS nation,Datepart(year,o_orderdate) AS o_year,(l_extendedprice / 100.0) *(1 - l_discount / 100.0) -(ps_supplycost / 100.0) * l_qu|taliar@sqreamtech.com|25b6cec3-b991-454e-8996-9f6b7273af80|2024-05-23T07:56:31|2024-05-23T07:56:41|10069   |0            |1076            |8864          |7.52003778600000227783084483235143125057220458984375|0        |25           |808          |0                   |                      |SQream Node.js|	         |SQream   |
	[...]

.. code-block:: sql

	describe QUERY SESSION ID '25b6cec3-b991-454e-8996-9f6b7273af80' QUERY ID 29;
	
.. code-block:: none

	query_id                               |rtc_name                       |node_id|parent_id|node_type              |elapsed_time|total_compute_time|total_waiting_time|rows_produced|chunks_produced|data_read|data_written|output   |additional_info                     |time               |status|
	---------------------------------------+-------------------------------+-------+---------+-----------------------+------------+------------------+------------------+-------------+---------------+---------+------------+---------+------------------------------------+-------------------+------+
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|1      |-1       |CloudRSend             |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)                           |2024-05-23 07:56:33|-1    |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|1      |-1       |CloudRSend             |0.333333333 |0.333333333       |0                 |25           |1              |0        |0           |100475   | (single)                           |2024-05-23 07:56:40|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|1      |-1       |CloudRSend             |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)                           |2024-05-23 07:56:33|-1    |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|2      |1        |Rechunk                |0.000034471 |0.000034471       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|2      |1        |Rechunk                |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|2      |1        |Rechunk                |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|3      |2        |ReorderInput           |0.000019789 |0.000019789       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|3      |2        |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|3      |2        |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|4      |3        |DeferredGather         |0.001807381 |0.001807381       |0                 |25           |1              |0        |0           |823      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|4      |3        |DeferredGather         |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|4      |3        |DeferredGather         |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|5      |4        |ReorderInput           |0.000017811 |0.000017811       |0                 |25           |1              |0        |0           |823      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|5      |4        |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|5      |4        |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|6      |5        |GpuToCpu               |0.000060910 |0.000060910       |0                 |25           |1              |0        |0           |100      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|6      |5        |GpuToCpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|6      |5        |GpuToCpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|7      |6        |Top                    |0.000085179 |0.000085179       |0                 |25           |1              |0        |0           |100      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|7      |6        |Top                    |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|7      |6        |Top                    |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|8      |7        |GpuTransform           |0.000062565 |0.000062565       |0                 |25           |1              |0        |0           |100      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|8      |7        |GpuTransform           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|8      |7        |GpuTransform           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|9      |8        |CpuToGpu               |0.000015649 |0.000015649       |0                 |25           |1              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|9      |8        |CpuToGpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|9      |8        |CpuToGpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|10     |9        |ReorderInput           |0.000023903 |0.000023903       |0                 |25           |1              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|10     |9        |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|10     |9        |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|11     |10       |Rechunk                |0.000044850 |0.000044850       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|11     |10       |Rechunk                |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|11     |10       |Rechunk                |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|12     |11       |SortMerge              |0.000121462 |0.000121462       |0                 |25           |1              |0        |0           |723      | (single)                           |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|12     |11       |SortMerge              |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)                           |2024-05-23 07:56:33|-1    |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|12     |11       |SortMerge              |0           |0                 |0                 |0            |0              |0        |0           |0        | (single)                           |2024-05-23 07:56:33|-1    |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|13     |12       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|13     |12       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|13     |12       |ReorderInput           |0.000079979 |0.000079979       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|14     |13       |DeferredGather         |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|14     |13       |DeferredGather         |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|14     |13       |DeferredGather         |0.001312765 |0.001312765       |0                 |25           |1              |0        |0           |823      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|15     |14       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|15     |14       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|15     |14       |ReorderInput           |0.000056979 |0.000056979       |0                 |25           |1              |0        |0           |823      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|16     |15       |GpuToCpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|16     |15       |GpuToCpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|16     |15       |GpuToCpu               |0.001526691 |0.001526691       |0                 |25           |1              |0        |0           |598      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|17     |16       |TakeRowsFromChunk      |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|17     |16       |TakeRowsFromChunk      |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|17     |16       |TakeRowsFromChunk      |0.000094487 |0.000094487       |0                 |25           |1              |0        |0           |598      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|18     |17       |Sort                   |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|18     |17       |Sort                   |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|18     |17       |Sort                   |0.002517770 |0.002517770       |0                 |25           |1              |0        |0           |598      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|19     |18       |GpuTransform           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|19     |18       |GpuTransform           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|19     |18       |GpuTransform           |0.000171497 |0.000171497       |0                 |25           |1              |0        |0           |598      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|20     |19       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|20     |19       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|20     |19       |ReorderInput           |0.000127323 |0.000127323       |0                 |25           |1              |0        |0           |498      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|21     |20       |Rechunk                |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|21     |20       |Rechunk                |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|21     |20       |Rechunk                |0.000309048 |0.000309048       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|22     |21       |ReduceMerge            |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|22     |21       |ReduceMerge            |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|22     |21       |ReduceMerge            |0.231800818 |0.231800818       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|23     |22       |GpuToCpu               |0.000105777 |0.000105777       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|23     |22       |GpuToCpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|23     |22       |GpuToCpu               |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|24     |23       |GpuReduceMerge         |0.000013218 |0.000013218       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|24     |23       |GpuReduceMerge         |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|24     |23       |GpuReduceMerge         |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|25     |24       |Reduce                 |0.001362257 |0.001362257       |0                 |25           |1              |0        |0           |723      |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|25     |24       |Reduce                 |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|25     |24       |Reduce                 |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|26     |25       |ReorderInput           |0.000021782 |0.000021782       |0                 |77440        |1              |0        |0           |2240344  |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|26     |25       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-4ldqm|26     |25       |ReorderInput           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-g9sv4|27     |26       |GpuTransform           |0.000333297 |0.000333297       |0                 |77440        |1              |0        |0           |2550104  |                                    |2024-05-23 07:56:39|2     |
	25b6cec3-b991-454e-8996-9f6b7273af80:29|sqream-worker-0-8ffc96576-rk725|27     |26       |GpuTransform           |0           |0                 |0                 |0            |0              |0        |0           |0        |                                    |2024-05-23 07:56:38|2     |
	[...]

Alternatively, you may also :ref:`retrieve the query execution plan output<retrieving_execution_plan_output_using_studio>` using your Workbench.


Commonly Seen Nodes
-------------------

.. list-table:: Node types
   :widths: auto
   :header-rows: 1
   
   * - Column name
     - Execution location
     - Description
   * - ``CpuDecompress``
     - CPU
     - Decompression operation, common for longer ``TEXT`` types
   * - ``CpuLoopJoin``
     - CPU
     - A non-indexed nested loop join, performed on the CPU
   * - ``CpuReduce``
     - CPU
     - A reduce process performed on the CPU, primarily with ``DISTINCT`` aggregates (e.g. ``COUNT(DISTINCT ...)``)
   * - ``CpuToGpu``, ``GpuToCpu``
     - 
     - An operation that moves data to or from the GPU for processing
   * - ``CpuTransform``
     - CPU
     - A transform operation performed on the CPU, usually a :ref:`scalar function<scalar_functions>`
   * - ``DeferredGather``
     - CPU
     - Merges the results of GPU operations with a result set
   * - ``Distinct``
     - GPU
     - Removes duplicate rows (usually as part of the ``DISTINCT`` operation)
   * - ``Distinct_Merge``
     - CPU
     - The merge operation of the ``Distinct`` operation
   * - ``Filter``
     - GPU
     - A filtering operation, such as a ``WHERE`` or ``JOIN`` clause
   * - ``GpuDecompress``
     - GPU
     - Decompression operation
   * - ``GpuReduceMerge``
     - GPU
     - An operation to optimize part of the merger phases in the GPU
   * - ``GpuTransform``
     - GPU
     - A transformation operation such as a type cast or :ref:`scalar function<scalar_functions>`
   * - ``LocateFiles``
     - CPU
     - Validates external file paths for foreign data wrappers, expanding directories and GLOB patterns
   * - ``LoopJoin``
     - GPU
     - A non-indexed nested loop join, performed on the GPU
   * - ``ParseCsv``
     - CPU
     - A CSV parser, used after ``ReadFiles`` to convert the CSV into columnar data
   * - ``PushToNetworkQueue``
     - CPU
     - Sends result sets to a client connected over the network
   * - ``ReadFiles``
     - CPU
     - Reads external flat-files
   * - ``ReadTable``
     - CPU
     - Reads data from a standard table stored on disk
   * - ``Rechunk``
     - 
     - Reorganize multiple small :ref:`chunks<chunks_and_extents>` into a full chunk. Commonly found after ``JOIN`` operations 
   * - ``Reduce``
     - GPU
     - A reduction operation, such as a ``GROUP BY``
   * - ``ReduceMerge``
     - GPU
     - A merge operation of a reduction operation, helps operate on larger-than-RAM data
   * - ``ReorderInput``
     - 
     - Change the order of arguments in preparation for the next operation
   * - ``SeparatedGather``
     - GPU
     - Gathers additional columns for the result
   * - ``Sort``
     - GPU
     - Sort operation
   * - ``TakeRowsFromChunk``
     - 
     - Take the first N rows from each chunk, to optimize ``LIMIT`` when used alongside ``ORDER BY``
   * - ``Top``
     - 
     - Limits the input size, when used with ``LIMIT`` (or its alias ``TOP``)
   * - ``UdfTransform``
     - CPU
     - Executes a :ref:`user defined function<python_functions>`
   * - ``UnionAll``
     -
     - Combines two sources of data when ``UNION ALL`` is used
   * - ``Window``
     - GPU
     - Executes a non-ranking :ref:`window function<window_functions>`
   * - ``WindowRanking``
     - GPU
     - Executes a ranking :ref:`window function<window_functions>`
   * - ``WriteTable``
     - CPU 
     - Writes the result set to a standard table stored on disk


Examples
========

In general, looking at the top three longest running nodes (as is detailed in the ``elapsed_time`` column) can indicate the biggest bottlenecks.
In the following examples you will learn how to identify and solve some common issues.
   
Use the ``blue_sample_data`` database.

.. code-block:: postgres

	USE DATABASE blue_sample_data;

   
Queries with Large Result Sets
------------------------------

When queries have large result sets, you may see a node called ``DeferredGather``.
This gathering occurs when the result set is assembled, in preparation for sending it to the client.

Identifying the Offending Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Run a query.
     
   For example, a modified query from the TPC-H benchmark:

.. code-block:: postgres
      
	-- Use the blue_sample_data database:
	USE DATABASE blue_sample_data;
	  
	SELECT
	  s.*,
	  l.*,
	  r.*,
	  n1.*,
	  n2.*,
	  p.*,
	  o.*,
	  c.*
	FROM
	  tpch_blue100.lineitem l
	  JOIN tpch_blue100.part p ON p_partkey = CAST (l_partkey AS INT)
	  JOIN tpch_blue100.orders o ON l_orderkey = o_orderkey
	  JOIN tpch_blue100.customer c ON o_custkey = c_custkey
	  JOIN tpch_blue100.nation n1 ON c_nationkey = n1.n_nationkey
	  JOIN tpch_blue100.region r ON n1.n_regionkey = r_regionkey
	  JOIN tpch_blue100.supplier s ON s_suppkey = l_suppkey
	  JOIN tpch_blue100.nation n2 ON s_nationkey = n2.n_nationkey
	WHERE
	  r_name = 'AMERICA'
	  AND o_orderdate BETWEEN '1995-01-01' AND '1996-12-31'
	;

2. Observe the execution information using the ``DESCRIBE QUERY`` command.
   
   .. code-block:: sql
   
    DESCRIBE QUERY SESSION ID '8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d' QUERY ID 1;
   
The execution below has been shortened, but note the highlighted rows for ``DeferredGather``:
	
Output:

.. code-block:: none
   :emphasize-lines: 7, 9, 10, 11
   
	query_id                              |rtc_name                       |node_id|parent_id|node_type              |elapsed_time|total_compute_time|total_waiting_time|rows_produced|chunks_produced|data_read |data_written|output      |additional_info                       |time               |status|
	--------------------------------------+-------------------------------+-------+---------+-----------------------+------------+------------------+------------------+-------------+---------------+----------+------------+------------+--------------------------------------+-------------------+------+
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-6x5xn|18     |17       |Rechunk                |0.307011528 |0.307011528       |0                 |1145886      |1              |0         |0           |1250266658  |                                      |2024-05-23 11:27:49|1     |
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-d6btp|18     |17       |Rechunk                |0.102665414 |0.102665414       |0                 |1107266      |1              |0         |0           |1207404198  |                                      |2024-05-23 11:27:49|1     |
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-lplvl|18     |17       |Rechunk                |0           |0                 |0                 |0            |0              |0         |0           |0           |                                      |2024-05-23 11:27:47|2     |
	[...]
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-6x5xn|84     |83       |DeferredGather         |27.85352083 |27.85352083       |0                 |31750980     |176            |0         |0           |16001778300 |                                      |2024-05-23 11:26:36|1     |
	[...]
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-lplvl|100    |99       |DeferredGather         |13.27289655 |13.27289655       |0                 |26169355     |108            |0         |0           |9352334168  |                                      |2024-05-23 11:24:59|2     |
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-6x5xn|100    |99       |DeferredGather         |56.20922714 |56.20922714       |0                 |103600166    |432            |0         |0           |37024061784 |                                      |2024-05-23 11:26:34|1     |
	8cd41d78-9d12-4f5b-a7b5-1db1e0c5ef8d:1|sqream-worker-0-8ffc96576-d6btp|100    |99       |DeferredGather         |28.45778916 |28.45778916       |0                 |114148419    |473            |0         |0           |40794151056 |                                      |2024-05-23 11:27:29|1     |

  
When you see ``DeferredGather`` operations taking more than a few seconds, that's a sign that you're selecting too much data.

In this case, the ``DeferredGather`` with node ID 100 took over 56 seconds.
   
3. Modify the statement to see the difference.

   Altering the select clause to be more restrictive will reduce the deferred gather time back to a few milliseconds.
   
.. code-block:: sql
      
   SELECT DATEPART(year, o_orderdate) AS o_year,
          l_extendedprice * (1 - l_discount / 100.0) as volume,
          n2.n_name as nation
   FROM ...

Common Solutions for Reducing Gather Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reduce the effect of the preparation time. Avoid selecting unnecessary columns (``SELECT * FROM...``), or reduce the result set size by using more filters.

Inefficient Filtering
---------------------

When running statements, BLUE tries to avoid reading data that is not needed for the statement by skipping chunks.

If statements do not include efficient filtering, BLUE will read a lot of data off disk.
In some cases, you need the data and there's nothing to do about it. However, if most of it gets pruned further down the line, it may be efficient to skip reading the data altogether by using the :ref:`metadata<metadata_system>`.

Identifying the Situation
^^^^^^^^^^^^^^^^^^^^^^^^^

We consider the filtering to be inefficient when the ``Filter`` node shows that the number of rows processed is less
than a third of the rows passed into it by the ``ReadParquet`` node.

For example:

1. Run a query.
     
   In this example, we execute a modified query from the TPC-H benchmark.
   Our ``lineitem`` table contains 600,037,902 rows.

   .. code-block:: postgres
      
	-- Use the blue_sample_data database:
	USE DATABASE blue_sample_data;
	  
	SELECT
	  o_year,
	  SUM(
	    CASE
	      WHEN nation = 'BRAZIL' THEN volume
	      ELSE 0
	    END
	  ) / SUM(volume) AS mkt_share
	FROM
	  (
	    SELECT
	      datepart(YEAR, o_orderdate) AS o_year,
	      l_extendedprice * (1 - l_discount / 100.0) AS volume,
	      n2.n_name AS nation
	    FROM
	      tpch_blue100.lineitem
	      JOIN tpch_blue100.part ON p_partkey = CAST (l_partkey AS INT)
	      JOIN tpch_blue100.orders ON l_orderkey = o_orderkey
	      JOIN tpch_blue100.customer ON o_custkey = c_custkey
	      JOIN tpch_blue100.nation n1 ON c_nationkey = n1.n_nationkey
	      JOIN tpch_blue100.region ON n1.n_regionkey = r_regionkey
	      JOIN tpch_blue100.supplier ON s_suppkey = l_suppkey
	      JOIN tpch_blue100.nation n2 ON s_nationkey = n2.n_nationkey
	    WHERE
	      r_name = 'AMERICA'
	      AND lineitem.l_quantity = 3
	      AND o_orderdate BETWEEN '1995-01-01' AND '1996-12-31'
	  ) AS all_nations
	GROUP BY
	  o_year
	ORDER BY
	  o_year;

2. Observe the execution information by using the ``DESCRIBE QUERY`` command.
   
   The execution below has been shortened.
   
   .. code-block:: psql
   
      DESCRIBE QUERY SESSION ID 'd250da61-b842-4048-b72e-0268da741c3f' QUERY ID 9;
	  
   .. code-block:: none
      :linenos: 
      :emphasize-lines: 6, 8, 10, 12   
	  
	query_id                              |rtc_name                        |node_id|parent_id|node_type              |elapsed_time|total_compute_time|total_waiting_time|rows_produced|chunks_produced|data_read  |data_written|output     |additional_info                       |time               |status|
	--------------------------------------+--------------------------------+-------+---------+-----------------------+------------+------------------+------------------+-------------+---------------+-----------+------------+-----------+--------------------------------------+-------------------+------+
	d250da61-b842-4048-b72e-0268da741c3f:9|sqream-worker-0-6ccdbbc755-f8fgr|103    |102      |ReorderInput           |0.002684156 |0.002684156       |0                 |12007447     |25             |0          |0           |60037235   |                                      |2024-05-27 07:38:52|2     |
	d250da61-b842-4048-b72e-0268da741c3f:9|sqream-worker-0-6ccdbbc755-f8fgr|104    |103      |Join                   |13.54319014 |13.54319014       |0                 |12007447     |25             |0          |0           |20569392926|inner(swapped sides)                  |2024-05-27 07:38:52|2     |
	[...]
	d250da61-b842-4048-b72e-0268da741c3f:9|sqream-worker-0-6ccdbbc755-f8fgr|109    |108      |Filter                 |0.002930426 |0.002930426       |0                 |20000000     |1              |0          |0           |200000000  |                                      |2024-05-27 07:38:33|2     |
	[...]
	d250da61-b842-4048-b72e-0268da741c3f:9|sqream-worker-0-6ccdbbc755-f8fgr|113    |112      |ReadParquet            |2.475944065 |2.475944065       |0                 |20000000     |1              |87425365   |0           |180000000  |blue_sample_data.tpch_blue100.part    |2024-05-27 07:38:33|2     |
	[...]
	d250da61-b842-4048-b72e-0268da741c3f:9|sqream-worker-0-6ccdbbc755-f8fgr|120    |119      |Filter                 |0.203168817 |0.203168817       |0                 |12007447     |25             |0          |0           |300186175  |                                      |2024-05-27 07:38:52|2     |
	[...]
	d250da61-b842-4048-b72e-0268da741c3f:9|sqream-worker-0-6ccdbbc755-f8fgr|126    |125      |ReadParquet            |1.627808877 |1.627808877       |0                 |600037902    |25             |14085157260|0           |32402046708|blue_sample_data.tpch_blue100.lineitem|2024-05-27 07:38:52|2     |


      

The ``Filter`` on line 10 has processed 12,007,447 rows as shown under ``rows_produced``, but the output of ``ReadParquet`` on ``public.lineitem`` on line 12 processed 600,037,902 rows. This means that it has filtered out 98% (:math:`1 - \dfrac{600,037,902}{12,007,447} = 98\%`) of the data, but the entire table was read.
   
3. Modify the statement to see the difference.

   Altering the statement to have a ``WHERE`` condition on the clustered ``l_orderkey`` column of the ``lineitem`` table will help BLUE skip reading the data.
   
   .. code-block:: sql
      :emphasize-lines: 26
      
	SELECT
	  o_year,
	  SUM(
	    CASE
	      WHEN nation = 'BRAZIL' THEN volume
	      ELSE 0
	    END
	  ) / SUM(volume) AS mkt_share
	FROM
	  (
	    SELECT
	      datepart(YEAR, o_orderdate) AS o_year,
	      l_extendedprice * (1 - l_discount / 100.0) AS volume,
	      n2.n_name AS nation
	    FROM
	      tpch_blue100.lineitem
	      JOIN tpch_blue100.part ON p_partkey = CAST (l_partkey AS INT)
	      JOIN tpch_blue100.orders ON l_orderkey = o_orderkey
	      JOIN tpch_blue100.customer ON o_custkey = c_custkey
	      JOIN tpch_blue100.nation n1 ON c_nationkey = n1.n_nationkey
	      JOIN tpch_blue100.region ON n1.n_regionkey = r_regionkey
	      JOIN tpch_blue100.supplier ON s_suppkey = l_suppkey
	      JOIN tpch_blue100.nation n2 ON s_nationkey = n2.n_nationkey
	    WHERE
	      r_name = 'AMERICA'
	      AND lineitem.l_orderkey > 4500000
	      AND o_orderdate BETWEEN '1995-01-01' AND '1996-12-31'
	  ) AS all_nations
	GROUP BY
	  o_year
	ORDER BY
	  o_year;

   .. code-block:: sql

      DESCRIBE QUERY SESSION ID 'd250da61-b842-4048-b72e-0268da741c3f' QUERY ID 2;
	  
   .. code-block:: none	  
      :emphasize-lines: 6, 12
	  
	query_id                              |rtc_name                        |node_id|parent_id|node_type              |elapsed_time|total_compute_time|total_waiting_time|rows_produced|chunks_produced|data_read  |data_written|output     |additional_info                       |time               |status|
	--------------------------------------+--------------------------------+-------+---------+-----------------------+------------+------------------+------------------+-------------+---------------+-----------+------------+-----------+--------------------------------------+-------------------+------+
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|1      |-1       |CloudRSend             |1           |1                 |0                 |2            |1              |0          |0           |28         | (single)                             |2024-05-27 10:22:02|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|2      |1        |Rechunk                |0.000080347 |0.000080347       |0                 |2            |1              |0          |0           |28         |                                      |2024-05-27 10:22:02|2     |
	[...]
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|120    |119      |Filter                 |0.198936066 |0.198936066       |0                 |595537319    |21             |0          |0           |14292895656|                                      |2024-05-27 10:21:53|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|121    |120      |GpuTransform           |0.259940836 |0.259940836       |0                 |600037902    |21             |0          |0           |14400909648|                                      |2024-05-27 10:21:53|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|122    |121      |GpuTransform           |0.017064677 |0.017064677       |0                 |600037902    |21             |0          |0           |13800871746|                                      |2024-05-27 10:21:53|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|123    |122      |CpuToGpu               |3.054507271 |3.054507271       |0                 |600037902    |21             |0          |0           |11400720138|                                      |2024-05-27 10:21:53|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|124    |123      |ReorderInput           |0.002183775 |0.002183775       |0                 |600037902    |21             |0          |0           |11400720138|                                      |2024-05-27 10:21:53|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|125    |124      |Rechunk                |0.002407714 |0.002407714       |0                 |600037902    |21             |0          |0           |27001705590|                                      |2024-05-27 10:21:53|2     |
	e5bd9284-bf05-47e8-8542-79d05600a1cf:1|sqream-worker-0-6ccdbbc755-sw8px|126    |125      |ReadParquet            |1.115767795 |1.115767795       |0                 |600037902    |21             |13633732149|0           |27001705590|blue_sample_data.tpch_blue100.lineitem|2024-05-27 10:21:53|2     |
	[...]
	  
   In this example, the ``Filter`` processed 595,537,319 rows, while the output of ``ReadParquet`` on ``public.lineitem`` was 600,037,902 rows. This means that it has filtered out all but 0.01% (:math:`1- \dfrac{494621593}{494927872} = 0.01\%`)
   of the data that was read.
   
   The metadata skipping has performed very well, and has pre-filtered the data for us by pruning unnecessary chunks.
      
Common Solutions for Improving Filtering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Use :ref:`clustering keys and naturally ordered data<cluster_by>` in your filters.
* Avoid full table scans when possible

Identifying the Situation
^^^^^^^^^^^^^^^^^^^^^^^^^

This is easily identifiable - when the amount of average of rows in a chunk is small, following a ``Filter`` operation.
Consider this execution plan:

.. code-block:: psql
   
   SELECT show_node_info(30);
   
.. code-block:: none

   stmt_id | node_id | node_type         | rows      | chunks | avg_rows_in_chunk | time                | parent_node_id | read  | write | comment    | timeSum
   --------+---------+-------------------+-----------+--------+-------------------+---------------------+----------------+-------+-------+------------+--------
   [...]
        30 |      38 | Filter            |     18160 |     74 |               245 | 2020-09-10 12:17:09 |             37 |       |       |            |   0.012
   [...]
        30 |      44 | ReadTable         |  77000000 |     74 |           1040540 | 2020-09-10 12:17:09 |             43 | 277MB |       | public.dim |   0.058

The table was read entirely - 77 million rows into 74 chunks.
The filter node reduced the output to just 18,160 relevant rows, but they're distributed across the original 74 chunks.
All of these rows could fit in one single chunk, instead of spanning 74 rather sparse chunks.

