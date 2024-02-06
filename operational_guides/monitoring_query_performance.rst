.. _monitoring_query_performance:

****************************
Monitoring Query Performance
****************************

This document aims to provide guidance on analyzing query performance through the examination of execution plans. The emphasis is on pinpointing bottlenecks and exploring potential optimization techniques to enhance overall query performance. When delving into query tuning options, the initial step involves a comprehensive analysis of the query plan and execution. The query plan and execution details provide insights into how BLUE processes a query and where the majority of processing time is allocated. 

It's crucial to recognize that performance tuning options vary for each query. Recommendations and tips should be tailored to suit the specifics of individual workloads. Additionally, referring to our :ref:`sql_best_practices` guide is advisable for a deeper understanding of considerations related to data loading and other best practices.


Setting Up the System for Monitoring
====================================

SQream logs all executed statements and their execution details. This data is logged in five second intervals, allowing you to view it both while a statement is executing, and historically.

For more information about setting up your system for monitoring, see the following:

* Get a list of queries executed per session - :ref:`DESCRIBE SESSION QUERIES<describe_session_queries>`.
   
* See more details about the query execution process for troubleshooting purposes - :ref:`DESCRIBE_QUERY<describe_query>`.

Reading Execution Plans with a Foreign Table
--------------------------------------------

First, create a foreign table for the logs.

.. code-block:: sql

   CREATE FOREIGN TABLE logs 
   (
     start_marker      TEXT,
     row_id            BIGINT,
     timestamp         DATETIME,
     message_level     TEXT,
     thread_id         TEXT,
     worker_hostname   TEXT,
     worker_port       INT,
     connection_id     INT,
     database_name     TEXT,
     user_name         TEXT,
     statement_id      INT,
     service_name      TEXT,
     message_type_id   INT,
     message           TEXT,
     end_message       TEXT
   )
   WRAPPER csv_fdw
   OPTIONS
     (
        LOCATION = '/home/rhendricks/sqream_storage/logs/**/sqream*.log',
        DELIMITER = '|'
     )
   ;
Once you've defined the foreign table, you can run queries to observe the previously logged execution plans.
This is recommended over looking at the raw logs.

.. code-block:: sql

   t=> SELECT message
   .     FROM logs
   .     WHERE message_type_id = 200
   .     AND timestamp BETWEEN '2020-06-11' AND '2020-06-13';
   
   
   message                                                                                                                          
   ---------------------------------------------------------------------------------------------------------------------------------
   SELECT *,coalesce((depdelay > 15),false) AS isdepdelayed FROM ontime WHERE year IN (2005, 2006, 2007, 2008, 2009, 2010)
    : 
    : 1,PushToNetworkQueue  ,10354468,10,1035446,2020-06-12 20:41:42,-1,,,,13.55
    : 2,Rechunk             ,10354468,10,1035446,2020-06-12 20:41:42,1,,,,0.10
    : 3,ReorderInput        ,10354468,10,1035446,2020-06-12 20:41:42,2,,,,0.00
    : 4,DeferredGather      ,10354468,10,1035446,2020-06-12 20:41:42,3,,,,1.23
    : 5,ReorderInput        ,10354468,10,1035446,2020-06-12 20:41:41,4,,,,0.01
    : 6,GpuToCpu            ,10354468,10,1035446,2020-06-12 20:41:41,5,,,,0.07
    : 7,GpuTransform        ,10354468,10,1035446,2020-06-12 20:41:41,6,,,,0.02
    : 8,ReorderInput        ,10354468,10,1035446,2020-06-12 20:41:41,7,,,,0.00
    : 9,Filter              ,10354468,10,1035446,2020-06-12 20:41:41,8,,,,0.07
    : 10,GpuTransform        ,10485760,10,1048576,2020-06-12 20:41:41,9,,,,0.07
    : 11,GpuDecompress       ,10485760,10,1048576,2020-06-12 20:41:41,10,,,,0.03
    : 12,GpuTransform        ,10485760,10,1048576,2020-06-12 20:41:41,11,,,,0.22
    : 13,CpuToGpu            ,10485760,10,1048576,2020-06-12 20:41:41,12,,,,0.76
    : 14,ReorderInput        ,10485760,10,1048576,2020-06-12 20:41:40,13,,,,0.11
    : 15,Rechunk             ,10485760,10,1048576,2020-06-12 20:41:40,14,,,,5.58
    : 16,CpuDecompress       ,10485760,10,1048576,2020-06-12 20:41:34,15,,,,0.04
    : 17,ReadTable           ,10485760,10,1048576,2020-06-12 20:41:34,16,832MB,,public.ontime,0.55



Using the ``DESCRIBE QUERY`` Command
====================================

The :ref:`describe_query` command returns a snapshot of the current query plan, similar to ``EXPLAIN ANALYZE`` from other databases.

The :ref:`describe_query` result, just like the periodically-logged execution plans described above, are an at-the-moment view of the compiler's execution plan and runtime statistics for the specified statement.

The following is an example of a query inspecting a statement with a statement ID of **7**:

.. code-block:: sql
   
   DESCRIBE QUERY SESSION ID '6a4d1389-0330-4d54-9d52-439ff0b4c74c' QUERY ID 9;
   
Output:

.. code-block:: none

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
   


Alternatively, you may also :ref:`retrieve the query execution plan output<retrieving_execution_plan_output_using_studio>` using your Workbench.

Understanding the Query Execution Plan Output
=============================================

Both :ref:`describe_query`  and the logged execution plans represents the query plan as a graph hierarchy, with data separated into different columns.

Each row represents a single logical database operation, which is also called a **node** or **chunk producer**. A node reports several metrics during query execution, such as how much data it has read and written, how many chunks and rows, and how much time has elapsed.

Consider the example show_node_info presented above. The source node with ID **#16** (``ParallelReadWorker``), has a parent node ID **#15** (``CpuDecompress``).
   
The last node, also called the sink, has a parent node ID of **-1**, meaning it has no parent. This is typically a node that sends data over the network or into a table.
   
   
.. 
   source for the graph above, in graphviz
   
   digraph G {
   rankdir=tb;
   ranksep=0.95;
   node[shape=box3d, width=3.0, height=0.6, fontname="Consolas", fillcolor=SteelBlue2, style=filled];
     PushToNetworkQueue [shape=house, fillcolor=SeaGreen1, style=filled];
     
   ReadTable->CpuDecompress;
   CpuDecompress->Rechunk;
   Rechunk->ReorderInput;
   ReorderInput->CpuToGpu;
   CpuToGpu->GpuTransform;
   GpuTransform->GpuDecompress;
   GpuDecompress->GpuTransform2;
   GpuTransform2->Filter;
   Filter->ReorderInput2;
   ReorderInput2->GpuTransform3;
   GpuTransform3->GpuToCpu;
   GpuToCpu->ReorderInput3;
   ReorderInput3->DeferredGather;
   DeferredGather->ReorderInput4;
   ReorderInput4->Rechunk2;
   Rechunk2->PushToNetworkQueue;
       Rechunk2[label="Rechunk"];
       ReorderInput4[label="ReorderInput"];
       ReorderInput3[label="ReorderInput"];
       ReorderInput2[label="ReorderInput"];
       GpuTransform2[label="GpuTransform"];
       GpuTransform3[label="GpuTransform"];
     
     ReadTable [shape=house, style=filled, fillcolor=SeaGreen4];
         
   }
When using :ref:`describe_query`, a tabular representation of the currently running statement execution is presented.
See the examples below to understand how the query execution plan is instrumental in identifying bottlenecks and optimizing long-running statements.

Information Presented in the Execution Plan
-------------------------------------------

.. include:: /reference/sql/sql_statements/monitoring_commands/show_node_info.rst
   :start-line: 47
   :end-line: 78

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

.. tip:: The full list of nodes appears in the :ref:`Node types table<node_types>`, as part of the :ref:`describe_query` reference.

Examples
========

In general, looking at the top three longest running nodes (as is detailed in the ``timeSum`` column) can indicate the biggest bottlenecks.
In the following examples you will learn how to identify and solve some common issues.


Spooling to Disk
----------------

When there is not enough RAM to process a statement, SQream DB will spill over data to the ``temp`` folder in the storage disk.
While this ensures that a statement can always finish processing, it can slow down the processing significantly.
It's worth identifying these statements, to figure out if the cluster is configured correctly, as well as potentially reduce
the statement size. 
You can identify a statement that spools to disk by looking at the ``write`` column in the execution details.
A node that spools will have a value, shown in megabytes in the ``write`` column.
Common nodes that write spools include ``Join`` or ``LoopJoin``.

Identifying the Offending Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. 
   Run a query.
     
   For example, a query from the TPC-H benchmark:

   .. code-block:: postgres
      
      SELECT o_year,
             SUM(CASE WHEN nation = 'BRAZIL' THEN volume ELSE 0 END) / SUM(volume) AS mkt_share
      FROM (SELECT datepart(YEAR,o_orderdate) AS o_year,
                   l_extendedprice*(1 - l_discount / 100.0) AS volume,
                   n2.n_name AS nation
            FROM lineitem
              JOIN part ON p_partkey = CAST (l_partkey AS INT)
              JOIN orders ON l_orderkey = o_orderkey
              JOIN customer ON o_custkey = c_custkey
              JOIN nation n1 ON c_nationkey = n1.n_nationkey
              JOIN region ON n1.n_regionkey = r_regionkey
              JOIN supplier ON s_suppkey = l_suppkey
              JOIN nation n2 ON s_nationkey = n2.n_nationkey
            WHERE o_orderdate BETWEEN '1995-01-01' AND '1996-12-31') AS all_nations
      GROUP BY o_year
      ORDER BY o_year;
#. 
   
   Observe the execution information by using the foreign table, or use ``show_node_info``
   
   This statement is made up of 199 nodes, starting from a ``ReadTable``, and finishes by returning only 2 results to the client.
   
   The execution below has been shortened, but note the highlighted rows for ``LoopJoin``:
   
.. code-block:: sql
   
      :emphasize-lines: 33,35,37,39
   
      SELECT message FROM logs WHERE message_type_id = 200 LIMIT 1;
      message                                                                                  
      -----------------------------------------------------------------------------------------
      SELECT o_year,                                                                           
             SUM(CASE WHEN nation = 'BRAZIL' THEN volume ELSE 0 END) / SUM(volume) AS mkt_share
       : FROM (SELECT datepart(YEAR,o_orderdate) AS o_year,
       :              l_extendedprice*(1 - l_discount / 100.0) AS volume,
       :              n2.n_name AS nation
       :       FROM lineitem
       :         JOIN part ON p_partkey = CAST (l_partkey AS INT)
       :         JOIN orders ON l_orderkey = o_orderkey
       :         JOIN customer ON o_custkey = c_custkey
       :         JOIN nation n1 ON c_nationkey = n1.n_nationkey
       :         JOIN region ON n1.n_regionkey = r_regionkey
       :         JOIN supplier ON s_suppkey = l_suppkey
       :         JOIN nation n2 ON s_nationkey = n2.n_nationkey
       :       WHERE o_orderdate BETWEEN '1995-01-01' AND '1996-12-31') AS all_nations
       : GROUP BY o_year
       : ORDER BY o_year
       : 1,PushToNetworkQueue  ,2,1,2,2020-09-04 18:32:50,-1,,,,0.27
       : 2,Rechunk             ,2,1,2,2020-09-04 18:32:50,1,,,,0.00
       : 3,SortMerge           ,2,1,2,2020-09-04 18:32:49,2,,,,0.00
       : 4,GpuToCpu            ,2,1,2,2020-09-04 18:32:49,3,,,,0.00
       : 5,Sort                ,2,1,2,2020-09-04 18:32:49,4,,,,0.00
       : 6,ReorderInput        ,2,1,2,2020-09-04 18:32:49,5,,,,0.00
       : 7,GpuTransform        ,2,1,2,2020-09-04 18:32:49,6,,,,0.00
       : 8,CpuToGpu            ,2,1,2,2020-09-04 18:32:49,7,,,,0.00
       : 9,Rechunk             ,2,1,2,2020-09-04 18:32:49,8,,,,0.00
       : 10,ReduceMerge         ,2,1,2,2020-09-04 18:32:49,9,,,,0.03
       : 11,GpuToCpu            ,6,3,2,2020-09-04 18:32:49,10,,,,0.00
       : 12,Reduce              ,6,3,2,2020-09-04 18:32:49,11,,,,0.64
       [...]
       : 49,LoopJoin            ,182369485,7,26052783,2020-09-04 18:32:36,48,1915MB,1915MB,inner,4.94
       [...]
       : 98,LoopJoin            ,182369485,12,15197457,2020-09-04 18:32:16,97,2191MB,2191MB,inner,5.01
       [...]
       : 124,LoopJoin            ,182369485,8,22796185,2020-09-04 18:32:03,123,3064MB,3064MB,inner,6.73
       [...]
       : 150,LoopJoin            ,182369485,10,18236948,2020-09-04 18:31:47,149,12860MB,12860MB,inner,23.62
       [...]
       : 199,ReadTable           ,20000000,1,20000000,2020-09-04 18:30:33,198,0MB,,public.part,0.83
   Because of the relatively low amount of RAM in the machine and because the data set is rather large at around 10TB, SQream DB needs to spool.  
   
   The total spool used by this query is around 20GB (1915MB + 2191MB + 3064MB + 12860MB).

Common Solutions for Reducing Spool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 
   Increase the amount of spool memory available for the workers, as a proportion of the maximum statement memory.
   When the amount of spool memory is increased, SQream DB may not need to write to disk.
   
   This setting is called ``spoolMemoryGB``. Refer to the :ref:`configuration` guide.
* 
   Reduce the amount of **workers** per host, and increase the amount of spool available to the (now reduced amount of) active workers.
   This may reduce the amount of concurrent statements, but will improve performance for heavy statements.
   
Queries with Large Result Sets
------------------------------

When queries have large result sets, you may see a node called ``DeferredGather``.
This gathering occurs when the result set is assembled, in preparation for sending it to the client.

Identifying the Offending Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. 
   Run a query.
     
   For example, a modified query from the TPC-H benchmark:

.. code-block:: sql
      
      SELECT s.*,
             l.*,
             r.*,
             n1.*,
             n2.*,
             p.*,
             o.*,
             c.*
      FROM lineitem l
        JOIN part p ON p_partkey = CAST (l_partkey AS INT)
        JOIN orders o ON l_orderkey = o_orderkey
        JOIN customer c ON o_custkey = c_custkey
        JOIN nation n1 ON c_nationkey = n1.n_nationkey
        JOIN region r ON n1.n_regionkey = r_regionkey
        JOIN supplier s ON s_suppkey = l_suppkey
        JOIN nation n2 ON s_nationkey = n2.n_nationkey
      WHERE r_name = 'AMERICA'
      AND   o_orderdate BETWEEN '1995-01-01' AND '1996-12-31'
	  ;
2. 
   
   Observe the execution information by using the foreign table, or use ``show_node_info``
   
   This statement is made up of 221 nodes, containing 8 ``ReadTable`` nodes, and finishes by returning billions of results to the client.
   
   The execution below has been shortened, but note the highlighted rows for ``DeferredGather``:
   
.. code-block:: sql
   
      :emphasize-lines: 7,9,11
   
      SELECT show_node_info(494);
      stmt_id | node_id | node_type            | rows      | chunks | avg_rows_in_chunk | time                | parent_node_id | read    | write | comment         | timeSum
      --------+---------+----------------------+-----------+--------+-------------------+---------------------+----------------+---------+-------+-----------------+--------
          494 |       1 | PushToNetworkQueue   |    242615 |      1 |            242615 | 2020-09-04 19:07:55 |             -1 |         |       |                 |    0.36
          494 |       2 | Rechunk              |    242615 |      1 |            242615 | 2020-09-04 19:07:55 |              1 |         |       |                 |       0
          494 |       3 | ReorderInput         |    242615 |      1 |            242615 | 2020-09-04 19:07:55 |              2 |         |       |                 |       0
          494 |       4 | DeferredGather       |    242615 |      1 |            242615 | 2020-09-04 19:07:55 |              3 |         |       |                 |    0.16
          [...]
          494 |     166 | DeferredGather       |   3998730 |     39 |            102531 | 2020-09-04 19:07:47 |            165 |         |       |                 |   21.75
          [...]
          494 |     194 | DeferredGather       |    133241 |     20 |              6662 | 2020-09-04 19:07:03 |            193 |         |       |                 |    0.41
          [...]
          494 |     221 | ReadTable            |  20000000 |     20 |           1000000 | 2020-09-04 19:07:01 |            220 | 20MB    |       | public.part     |     0.1
  
   When you see ``DeferredGather`` operations taking more than a few seconds, that's a sign that you're selecting too much data.
   In this case, the DeferredGather with node ID 166 took over 21 seconds.
   
#. Modify the statement to see the difference
   Altering the select clause to be more restrictive will reduce the deferred gather time back to a few milliseconds.
   
   .. code-block:: sql
      
      SELECT DATEPART(year, o_orderdate) AS o_year,
             l_extendedprice * (1 - l_discount / 100.0) as volume,
             n2.n_name as nation
      FROM ...

Common Solutions for Reducing Gather Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Reduce the effect of the preparation time. Avoid selecting unnecessary columns (``SELECT * FROM...``), or reduce the result set size by using more filters.
.. ``

Inefficient Filtering
---------------------

When running statements, SQream DB tries to avoid reading data that is not needed for the statement by :ref:`skipping chunks<chunks_and_extents>`.
If statements do not include efficient filtering, SQream DB will read a lot of data off disk.
In some cases, you need the data and there's nothing to do about it. However, if most of it gets pruned further down the line,
it may be efficient to skip reading the data altogether by using the :ref:`metadata<metadata_system>`.

Identifying the Situation
^^^^^^^^^^^^^^^^^^^^^^^^^

We consider the filtering to be inefficient when the ``Filter`` node shows that the number of rows processed is less
than a third of the rows passed into it by the ``ReadTable`` node.
For example:

#. 
   Run a query.
     
   In this example, we execute a modified query from the TPC-H benchmark.
   Our ``lineitem`` table contains 600,037,902 rows.

   .. code-block:: postgres
      
      SELECT o_year,
             SUM(CASE WHEN nation = 'BRAZIL' THEN volume ELSE 0 END) / SUM(volume) AS mkt_share
      FROM (SELECT datepart(YEAR,o_orderdate) AS o_year,
                   l_extendedprice*(1 - l_discount / 100.0) AS volume,
                   n2.n_name AS nation
            FROM lineitem
              JOIN part ON p_partkey = CAST (l_partkey AS INT)
              JOIN orders ON l_orderkey = o_orderkey
              JOIN customer ON o_custkey = c_custkey
              JOIN nation n1 ON c_nationkey = n1.n_nationkey
              JOIN region ON n1.n_regionkey = r_regionkey
              JOIN supplier ON s_suppkey = l_suppkey
              JOIN nation n2 ON s_nationkey = n2.n_nationkey
            WHERE r_name = 'AMERICA'
            AND   lineitem.l_quantity = 3
            AND   o_orderdate BETWEEN '1995-01-01' AND '1996-12-31') AS all_nations
      GROUP BY o_year
      ORDER BY o_year;
#. 
   
   Observe the execution information by using the foreign table, or use ``show_node_info``
   
   The execution below has been shortened, but note the highlighted rows for ``ReadTable`` and ``Filter``:
   
   .. code-block:: psql
      :linenos:
      :emphasize-lines: 9,17,19,27
   
      SELECT show_node_info(559);
	  
   .. code-block:: none	  
	  
      stmt_id | node_id | node_type            | rows      | chunks | avg_rows_in_chunk | time                | parent_node_id | read   | write | comment         | timeSum
      --------+---------+----------------------+-----------+--------+-------------------+---------------------+----------------+--------+-------+-----------------+--------
          559 |       1 | PushToNetworkQueue   |         2 |      1 |                 2 | 2020-09-07 11:12:01 |             -1 |        |       |                 |    0.28
          559 |       2 | Rechunk              |         2 |      1 |                 2 | 2020-09-07 11:12:01 |              1 |        |       |                 |       0
          559 |       3 | SortMerge            |         2 |      1 |                 2 | 2020-09-07 11:12:01 |              2 |        |       |                 |       0
          559 |       4 | GpuToCpu             |         2 |      1 |                 2 | 2020-09-07 11:12:01 |              3 |        |       |                 |       0
      [...]
          559 |     189 | Filter               |  12007447 |     12 |           1000620 | 2020-09-07 11:12:00 |            188 |        |       |                 |     0.3
          559 |     190 | GpuTransform         | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            189 |        |       |                 |    0.02
          559 |     191 | GpuDecompress        | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            190 |        |       |                 |    0.16
          559 |     192 | GpuTransform         | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            191 |        |       |                 |    0.02
          559 |     193 | CpuToGpu             | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            192 |        |       |                 |    1.47
          559 |     194 | ReorderInput         | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            193 |        |       |                 |       0
          559 |     195 | Rechunk              | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            194 |        |       |                 |       0
          559 |     196 | CpuDecompress        | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            195 |        |       |                 |       0
          559 |     197 | ReadTable            | 600037902 |     12 |          50003158 | 2020-09-07 11:12:00 |            196 | 7587MB |       | public.lineitem |     0.1
      [...]
          559 |     208 | Filter               |    133241 |     20 |              6662 | 2020-09-07 11:11:57 |            207 |        |       |                 |    0.01
          559 |     209 | GpuTransform         |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            208 |        |       |                 |    0.02
          559 |     210 | GpuDecompress        |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            209 |        |       |                 |    0.03
          559 |     211 | GpuTransform         |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            210 |        |       |                 |       0
          559 |     212 | CpuToGpu             |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            211 |        |       |                 |    0.01
          559 |     213 | ReorderInput         |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            212 |        |       |                 |       0
          559 |     214 | Rechunk              |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            213 |        |       |                 |       0
          559 |     215 | CpuDecompress        |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            214 |        |       |                 |       0
          559 |     216 | ReadTable            |  20000000 |     20 |           1000000 | 2020-09-07 11:11:57 |            215 | 20MB   |       | public.part     |       0
      
   * 
      The ``Filter`` on line 9 has processed 12,007,447 rows, but the output of ``ReadTable`` on ``public.lineitem`` 
      on line 17 was 600,037,902 rows. This means that it has filtered out 98% (:math:`1 - \dfrac{600037902}{12007447} = 98\%`)
      of the data, but the entire table was read.
      
   * 
      The ``Filter`` on line 19 has processed 133,000 rows, but the output of ``ReadTable`` on ``public.part`` 
      on line 27 was 20,000,000 rows.  This means that it has filtered out >99% (:math:`1 - \dfrac{133241}{20000000} = 99.4\%`)
      of the data, but the entire table was read. However, this table is small enough that we can ignore it.
   
#. Modify the statement to see the difference
   Altering the statement to have a ``WHERE`` condition on the clustered ``l_orderkey`` column of the ``lineitem`` table will help SQream DB skip reading the data.
   
   .. code-block:: sql
      :emphasize-lines: 15
      
      SELECT o_year,
             SUM(CASE WHEN nation = 'BRAZIL' THEN volume ELSE 0 END) / SUM(volume) AS mkt_share
      FROM (SELECT datepart(YEAR,o_orderdate) AS o_year,
                   l_extendedprice*(1 - l_discount / 100.0) AS volume,
                   n2.n_name AS nation
            FROM lineitem
              JOIN part ON p_partkey = CAST (l_partkey AS INT)
              JOIN orders ON l_orderkey = o_orderkey
              JOIN customer ON o_custkey = c_custkey
              JOIN nation n1 ON c_nationkey = n1.n_nationkey
              JOIN region ON n1.n_regionkey = r_regionkey
              JOIN supplier ON s_suppkey = l_suppkey
              JOIN nation n2 ON s_nationkey = n2.n_nationkey
            WHERE r_name = 'AMERICA'
            AND   lineitem.l_orderkey > 4500000
            AND   o_orderdate BETWEEN '1995-01-01' AND '1996-12-31') AS all_nations
      GROUP BY o_year
      ORDER BY o_year;

   .. code-block:: sql
      :linenos:
      :emphasize-lines: 5,13
      
      SELECT show_node_info(586);
	  
   .. code-block:: none	  
	  
      stmt_id | node_id | node_type            | rows      | chunks | avg_rows_in_chunk | time                | parent_node_id | read   | write | comment         | timeSum
      --------+---------+----------------------+-----------+--------+-------------------+---------------------+----------------+--------+-------+-----------------+--------
      [...]
          586 |     190 | Filter               | 494621593 |      8 |          61827699 | 2020-09-07 13:20:45 |            189 |        |       |                 |    0.39
          586 |     191 | GpuTransform         | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            190 |        |       |                 |    0.03
          586 |     192 | GpuDecompress        | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            191 |        |       |                 |    0.26
          586 |     193 | GpuTransform         | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            192 |        |       |                 |    0.01
          586 |     194 | CpuToGpu             | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            193 |        |       |                 |    1.86
          586 |     195 | ReorderInput         | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            194 |        |       |                 |       0
          586 |     196 | Rechunk              | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            195 |        |       |                 |       0
          586 |     197 | CpuDecompress        | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            196 |        |       |                 |       0
          586 |     198 | ReadTable            | 494927872 |      8 |          61865984 | 2020-09-07 13:20:44 |            197 | 6595MB |       | public.lineitem |    0.09
      [...]
   In this example, the filter processed 494,621,593 rows, while the output of ``ReadTable`` on ``public.lineitem`` 
   was 494,927,872 rows. This means that it has filtered out all but 0.01% (:math:`1 - \dfrac{494621593}{494927872} = 0.01\%`)
   of the data that was read.
   
   The metadata skipping has performed very well, and has pre-filtered the data for us by pruning unnecessary chunks.
      
Common Solutions for Improving Filtering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Use :ref:`clustering keys and naturally ordered data<data_clustering>` in your filters.
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

Performance of unsorted data in joins
-------------------------------------

When data is not well-clustered or naturally ordered, a join operation can take a long time. 

Identifying the Situation
^^^^^^^^^^^^^^^^^^^^^^^^^

When running a statement, inspect it with :ref:`describe_query`. If you see ``Join`` and ``DeferredGather`` among your 
top five longest running nodes, there is a potential issue.
In this case, we're also interested in the number of chunks produced by these nodes.

Consider this execution plan:

.. code-block:: sql
   :emphasize-lines: 6,11
   
   SELECT show_node_info(30);
   
.. code-block:: none

   stmt_id | node_id | node_type         | rows      | chunks | avg_rows_in_chunk | time                | parent_node_id | read  | write | comment    | timeSum
   --------+---------+-------------------+-----------+--------+-------------------+---------------------+----------------+-------+-------+------------+--------
   [...]
        30 |      13 | ReorderInput      | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             12 |       |       |            |   4.681
        30 |      14 | DeferredGather    | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             13 |       |       |            |  29.901
        30 |      15 | ReorderInput      | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             14 |       |       |            |   3.053
        30 |      16 | GpuToCpu          | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             15 |       |       |            |   5.798
        30 |      17 | ReorderInput      | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             16 |       |       |            |   2.899
        30 |      18 | ReorderInput      | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             17 |       |       |            |   3.695
        30 |      19 | Join              | 181582598 |  70596 |              2572 | 2020-09-10 12:17:10 |             18 |       |       | inner      |  22.745
   [...]
        30 |      38 | Filter            |     18160 |     74 |               245 | 2020-09-10 12:17:09 |             37 |       |       |            |   0.012
   [...]
        30 |      44 | ReadTable         |  77000000 |     74 |           1040540 | 2020-09-10 12:17:09 |             43 | 277MB |       | public.dim |   0.058
* ``Join`` is the node that matches rows from both table relations.
* ``DeferredGather`` gathers the required column chunks to decompress
Pay special attention to the volume of data removed by the ``Filter`` node.
The table was read entirely - 77 million rows into 74 chunks.
The filter node reduced the output to just 18,160 relevant rows, but they're distributed across the original 74 chunks.
All of these rows could fit in one single chunk, instead of spanning 74 rather sparse chunks.

Manual Join Reordering
----------------------

When joining multiple tables, you may wish to change the join order to join the smallest tables first.

Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^

When joining more than two tables, the ``Join`` nodes will be the most time-consuming nodes.

Changing the Join Order
^^^^^^^^^^^^^^^^^^^^^^^

Always prefer to join the smallest tables first.
.. note:: 
   We consider small tables to be tables that only retain a small amount of rows after conditions
   are applied. This bears no direct relation to the amount of total rows in the table.
Changing the join order can reduce the query runtime significantly. In the examples below, we reduce the time
from 27.3 seconds to just 6.4 seconds.

.. code-block:: postgres
   :caption: Original query
   
   -- This variant runs in 27.3 seconds
   SELECT SUM(l_extendedprice / 100.0*(1 - l_discount / 100.0)) AS revenue,
          c_nationkey
   FROM lineitem --6B Rows, ~183GB
     JOIN orders --1.5B Rows, ~55GB 
     ON   l_orderkey = o_orderkey
     JOIN customer --150M Rows, ~12GB
     ON   c_custkey = o_custkey
     
   WHERE c_nationkey = 1
         AND   o_orderdate >= DATE '1993-01-01'
         AND   o_orderdate < '1994-01-01'
         AND   l_shipdate >= '1993-01-01'
         AND   l_shipdate <= dateadd(DAY,122,'1994-01-01')
   GROUP BY c_nationkey

.. code-block:: postgres
   :caption: Modified query with improved join order
   
   -- This variant runs in 6.4 seconds
   SELECT SUM(l_extendedprice / 100.0*(1 - l_discount / 100.0)) AS revenue,
          c_nationkey
   FROM orders --1.5B Rows, ~55GB 
     JOIN customer --150M Rows, ~12GB
     ON   c_custkey = o_custkey
     JOIN lineitem --6B Rows, ~183GB
     ON   l_orderkey = o_orderkey
     
   WHERE c_nationkey = 1
         AND   o_orderdate >= DATE '1993-01-01'
         AND   o_orderdate < '1994-01-01'
         AND   l_shipdate >= '1993-01-01'
         AND   l_shipdate <= dateadd(DAY,122,'1994-01-01')
   GROUP BY c_nationkey

Further Reading
===============

See our :ref:`sql_best_practices` guide for more information about query optimization and data loading considerations.