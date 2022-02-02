.. _monitoring_query_performance:

*********************************
Monitoring Query Performance
*********************************

When analyzing options for query tuning, the first step is to analyze the query plan and execution. 

The query plan and execution details explains how SQream DB processes a query and where time is spent.

This document details how to analyze query performance with execution plans.

This guide focuses specifically on identifying bottlenecks and possible optimization techniques to improve query performance.

Performance tuning options for each query are different. You should adapt the recommendations and tips for your own workloads.

See also our :ref:`sql_best_practices` guide for more information about data loading considerations and other best practices.

.. contents:: In this section:
   :local:

Setting up the system for monitoring
=================================================

By default, SQream DB logs execution details for every statement that runs for more than 60 seconds.
If you want to see the execution details for a currently running statement, see :ref:`using_show_node_info` below.


Adjusting the logging frequency
---------------------------------------

To adjust the frequency of logging for statements, you may want to reduce the interval from 60 seconds down to, 
say, 5 or 10 seconds. Modify the configuration files and set the ``nodeInfoLoggingSec`` parameter as you see fit:

.. code-block::  json
   :emphasize-lines: 7
   
   { 
      "compileFlags":{ 
      },
      "runtimeFlags":{ 
      },
      "runtimeGlobalFlags":{ 
         "nodeInfoLoggingSec" : 5,
      },
      "server":{ 
      }
   }

After restarting the SQream DB cluster, the execution plan details will be logged to the :ref:`standard SQream DB logs directory<logging>`, as a message of type ``200``.

You can see these messages with a text viewer or with queries on the log :ref:`external_tables`.

Reading execution plans with a foreign table
-----------------------------------------------------

First, create a foreign table for the logs

.. code-block:: postgres

   CREATE FOREIGN TABLE logs 
   (
     start_marker      VARCHAR(4),
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
     end_message       VARCHAR(5)
   )
   WRAPPER cdv_fdw
   OPTIONS
     (
        LOCATION = '/home/rhendricks/sqream_storage/logs/**/sqream*.log',
        DELIMITER = '|'
     )
   ;

Once you've defined the foreign table, you can run queries to observe the previously logged execution plans.
This is recommended over looking at the raw logs.

.. code-block:: psql

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

.. _using_show_node_info:

The ``SHOW_NODE_INFO`` command
=====================================

The :ref:`show_node_info` command returns a snapshot of the current query plan, similar to ``EXPLAIN ANALYZE`` from other databases.

The :ref:`show_node_info` result, just like the periodically-logged execution plans described above, are an at-the-moment 
view of the compiler's execution plan and runtime statistics for the specified statement.

To inspect a currently running statement, execute the ``show_node_info`` utility function in a SQL client like
 :ref:`sqream sql<sqream_sql_cli_reference>`, the :ref:`SQream Studio Editor<studio_editor>`, or any other :ref:`third party SQL terminal<third_party_tools>`.

In this example, we inspect a statement with statement ID of 176. The command looks like this:

.. code-block:: psql
   
   t=> SELECT SHOW_NODE_INFO(176);
   stmt_id | node_id | node_type          | rows | chunks | avg_rows_in_chunk | time                | parent_node_id | read | write | comment    | timeSum
   --------+---------+--------------------+------+--------+-------------------+---------------------+----------------+------+-------+------------+--------
       176 |       1 | PushToNetworkQueue |    1 |      1 |                 1 | 2019-12-25 23:53:13 |             -1 |      |       |            |  0.0025
       176 |       2 | Rechunk            |    1 |      1 |                 1 | 2019-12-25 23:53:13 |              1 |      |       |            |       0
       176 |       3 | GpuToCpu           |    1 |      1 |                 1 | 2019-12-25 23:53:13 |              2 |      |       |            |       0
       176 |       4 | ReorderInput       |    1 |      1 |                 1 | 2019-12-25 23:53:13 |              3 |      |       |            |       0
       176 |       5 | Filter             |    1 |      1 |                 1 | 2019-12-25 23:53:13 |              4 |      |       |            |  0.0002
       176 |       6 | GpuTransform       |  457 |      1 |               457 | 2019-12-25 23:53:13 |              5 |      |       |            |  0.0002
       176 |       7 | GpuDecompress      |  457 |      1 |               457 | 2019-12-25 23:53:13 |              6 |      |       |            |       0
       176 |       8 | CpuToGpu           |  457 |      1 |               457 | 2019-12-25 23:53:13 |              7 |      |       |            |  0.0003
       176 |       9 | Rechunk            |  457 |      1 |               457 | 2019-12-25 23:53:13 |              8 |      |       |            |       0
       176 |      10 | CpuDecompress      |  457 |      1 |               457 | 2019-12-25 23:53:13 |              9 |      |       |            |       0
       176 |      11 | ReadTable          |  457 |      1 |               457 | 2019-12-25 23:53:13 |             10 | 4MB  |       | public.nba |  0.0004

Understanding the query execution plan output
==================================================

Both :ref:`show_node_info`  and the logged execution plans represents the query plan as a graph hierarchy, with data separated into different columns.

Each row represents a single logical database operation, which is also called a **node** or **chunk producer**. A node reports 
several metrics during query execution, such as how much data it has read and written, how many chunks and rows, and how much time has elapsed.

Consider the example show_node_info presented above. The source node with ID #11 (``ReadTable``), has a parent node ID #10 
(``CpuDecompress``). If we were to draw this out in a graph, it'd look like this:

.. figure:: /_static/images/show_node_info_graph.png
   :height: 70em
   :align: center
   
   This graph explains how the query execution details are arranged in a logical order, from the bottom up.
   
   
The last node, also called the sink, has a parent node ID of -1, meaning it has no parent. This is typically a node that sends data over the network or into a table.
   
   
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


When using :ref:`show_node_info`, a tabular representation of the currently running statement execution is presented.

See the examples below to understand how the query execution plan is instrumental in identifying bottlenecks and optimizing long-running statements.

Information presented in the execution plan
----------------------------------------------------
.. include:: /reference/sql/sql_statements/monitoring_commands/show_node_info.rst
   :start-line: 47
   :end-line: 78

Commonly seen nodes
----------------------

.. list-table:: Node types
   :widths: auto
   :header-rows: 1
   
   * - Column name
     - Execution location
     - Description
   * - ``CpuDecompress``
     - CPU
     - Decompression operation, common for longer ``VARCHAR`` types
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
     - Reorganize multiple small :ref:`chunks<chunks_and_extents>` into a full chunk. Commonly found after joins and when :ref:`HIGH_SELECTIVITY<high_selectivity>` is used
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

.. tip:: The full list of nodes appears in the :ref:`Node types table<node_types>`, as part of the :ref:`show_node_info` reference.


Examples
==================

In general, looking at the top three longest running nodes (as is detailed in the ``timeSum`` column) can indicate the biggest bottlenecks.

In the following examples you will learn how to identify and solve some common issues.

.. contents:: In this section:
   :local:

1. Spooling to disk
-----------------------

When there is not enough RAM to process a statement, SQream DB will spill over data to the ``temp`` folder in the storage disk.
While this ensures that a statement can always finish processing, it can slow down the processing significantly.

It's worth identifying these statements, to figure out if the cluster is configured correctly, as well as potentially reduce
the statement size. 

You can identify a statement that spools to disk by looking at the ``write`` column in the execution details.
A node that spools will have a value, shown in megabytes in the ``write`` column.

Common nodes that write spools include ``Join`` or ``LoopJoin``.

Identifying the offending nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
   
   .. code-block:: psql
      :emphasize-lines: 33,35,37,39
   
      t=> SELECT message FROM logs WHERE message_type_id = 200 LIMIT 1;
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

Common solutions for reducing spool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 
   Increase the amount of spool memory available for the workers, as a proportion of the maximum statement memory.
   When the amount of spool memory is increased, SQream DB may not need to write to disk.
   
   This setting is called ``spoolMemoryGB``. Refer to the :ref:`configuration` guide.

* 
   Reduce the amount of **workers** per host, and increase the amount of spool available to the (now reduced amount of) active workers.
   This may reduce the amount of concurrent statements, but will improve performance for heavy statements.

2. Queries with large result sets
------------------------------------

When queries have large result sets, you may see a node called ``DeferredGather``.

This gathering occurs when the result set is assembled, in preparation for sending it to the client.

Identifying the offending nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. 
   Run a query.
     
   For example, a modified query from the TPC-H benchmark:

   .. code-block:: postgres
      
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
      AND   high_selectivity(p_type = 'ECONOMY BURNISHED NICKEL');

#. 
   
   Observe the execution information by using the foreign table, or use ``show_node_info``
   
   This statement is made up of 221 nodes, containing 8 ``ReadTable`` nodes, and finishes by returning billions of results to the client.
   
   The execution below has been shortened, but note the highlighted rows for ``DeferredGather``:
   
   .. code-block:: psql
      :emphasize-lines: 7,9,11
   
      t=> SELECT show_node_info(494);
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
   
   .. code-block:: postgres
      
      SELECT DATEPART(year, o_orderdate) AS o_year,
             l_extendedprice * (1 - l_discount / 100.0) as volume,
             n2.n_name as nation
      FROM ...

Common solutions for reducing gather time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Reduce the effect of the preparation time. Avoid selecting unnecessary columns (``SELECT * FROM...``), or reduce the result set size by using more filters.

.. ``


3. Inefficient filtering
--------------------------------

When running statements, SQream DB tries to avoid reading data that is not needed for the statement by :ref:`skipping chunks<chunks_and_extents>`.

If statements do not include efficient filtering, SQream DB will read a lot of data off disk.
In some cases, you need the data and there's nothing to do about it. However, if most of it gets pruned further down the line,
it may be efficient to skip reading the data altogether by using the :ref:`metadata<metadata_system>`.

Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
            AND   o_orderdate BETWEEN '1995-01-01' AND '1996-12-31'
            AND   high_selectivity(p_type = 'ECONOMY BURNISHED NICKEL')) AS all_nations
      GROUP BY o_year
      ORDER BY o_year;

#. 
   
   Observe the execution information by using the foreign table, or use ``show_node_info``
   
   The execution below has been shortened, but note the highlighted rows for ``ReadTable`` and ``Filter``:
   
   .. code-block:: psql
      :linenos:
      :emphasize-lines: 9,17,19,27
   
      t=> SELECT show_node_info(559);
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
   
   .. code-block:: postgres
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
            AND   o_orderdate BETWEEN '1995-01-01' AND '1996-12-31'
            AND   high_selectivity(p_type = 'ECONOMY BURNISHED NICKEL')) AS all_nations
      GROUP BY o_year
      ORDER BY o_year;

   .. code-block:: psql
      :linenos:
      :emphasize-lines: 5,13
      
      t=> SELECT show_node_info(586);
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
      
Common solutions for improving filtering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Use :ref:`clustering keys and naturally ordered data<data_clustering>` in your filters.

* Avoid full table scans when possible


4. Joins with ``varchar`` keys
-----------------------------------

Joins on long text keys, such as ``varchar(100)`` do not perform as well as numeric data types or very short text keys.


Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a join is inefficient, you may note that a query spends a lot of time on the ``Join`` node.

For example, consider these two table structures:
   
.. code-block:: postgres

   CREATE TABLE t_a 
   (
     amt            FLOAT NOT NULL,
     i              INT NOT NULL,
     ts             DATETIME NOT NULL,
     country_code   VARCHAR(3) NOT NULL,
     flag           VARCHAR(10) NOT NULL,
     fk             VARCHAR(50) NOT NULL
   );

   CREATE TABLE t_b 
   (
     id          VARCHAR(50) NOT NULL
     prob        FLOAT NOT NULL,
     j           INT NOT NULL,
   );

#. 
   Run a query.
     
   In this example, we will join ``t_a.fk`` with ``t_b.id``, both of which are ``VARCHAR(50)``.
   
   .. code-block:: postgres
      
      SELECT AVG(t_b.j :: BIGINT),
             t_a.country_code
      FROM t_a
        JOIN t_b ON (t_a.fk = t_b.id)
      GROUP BY t_a.country_code

#. 
   
   Observe the execution information by using the foreign table, or use ``show_node_info``
   
   The execution below has been shortened, but note the highlighted rows for ``Join``.
   The ``Join`` node is by far the most time-consuming part of this statement - clocking in at 69.7 seconds
   joining 1.5 billion records.
   
   .. code-block:: psql
      :linenos:
      :emphasize-lines: 8
      
      t=> SELECT show_node_info(5);
      stmt_id | node_id | node_type            | rows       | chunks | avg_rows_in_chunk | time                | parent_node_id | read  | write | comment    | timeSum
      --------+---------+----------------------+------------+--------+-------------------+---------------------+----------------+-------+-------+------------+--------
      [...]
            5 |      19 | GpuTransform         | 1497366528 |    204 |           7340032 | 2020-09-08 18:29:03 |             18 |       |       |            |    1.46
            5 |      20 | ReorderInput         | 1497366528 |    204 |           7340032 | 2020-09-08 18:29:03 |             19 |       |       |            |       0
            5 |      21 | ReorderInput         | 1497366528 |    204 |           7340032 | 2020-09-08 18:29:03 |             20 |       |       |            |       0
            5 |      22 | Join                 | 1497366528 |    204 |           7340032 | 2020-09-08 18:29:03 |             21 |       |       | inner      |    69.7
            5 |      24 | AddSortedMinMaxMet.. |    6291456 |      1 |           6291456 | 2020-09-08 18:26:05 |             22 |       |       |            |       0
            5 |      25 | Sort                 |    6291456 |      1 |           6291456 | 2020-09-08 18:26:05 |             24 |       |       |            |    2.06
      [...]
            5 |      31 | ReadTable            |    6291456 |      1 |           6291456 | 2020-09-08 18:26:03 |             30 | 235MB |       | public.t_b |    0.02
      [...]
            5 |      41 | CpuDecompress        |   10000000 |      2 |           5000000 | 2020-09-08 18:26:09 |             40 |       |       |            |       0
            5 |      42 | ReadTable            |   10000000 |      2 |           5000000 | 2020-09-08 18:26:09 |             41 | 14MB  |       | public.t_a |       0
   

Improving query performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* In general, try to avoid ``VARCHAR`` as a join key. As a rule of thumb, ``BIGINT`` works best as a join key.

* 
   Convert text values on-the-fly before running the query. For example, the :ref:`crc64` function takes a text
   input and returns a ``BIGINT`` hash.
   
   For example:
   
   .. code-block:: postgres
      
         SELECT AVG(t_b.j :: BIGINT),
               t_a.country_code
         FROM t_a
         JOIN t_b ON (crc64_join(t_a.fk) = crc64_join(t_b.id))
         GROUP BY t_a.country_code

   The execution below has been shortened, but note the highlighted rows for ``Join``.
   The ``Join`` node went from taking nearly 70 seconds, to just 6.67 seconds for joining 1.5 billion records.

   .. code-block:: psql
      :linenos:
      :emphasize-lines: 8
      
      t=> SELECT show_node_info(6);
         stmt_id | node_id | node_type            | rows       | chunks | avg_rows_in_chunk | time                | parent_node_id | read  | write | comment    | timeSum
         --------+---------+----------------------+------------+--------+-------------------+---------------------+----------------+-------+-------+------------+--------
         [...]
               6 |      19 | GpuTransform         | 1497366528 |     85 |          17825792 | 2020-09-08 18:57:04 |             18 |       |       |            |    1.48
               6 |      20 | ReorderInput         | 1497366528 |     85 |          17825792 | 2020-09-08 18:57:04 |             19 |       |       |            |       0
               6 |      21 | ReorderInput         | 1497366528 |     85 |          17825792 | 2020-09-08 18:57:04 |             20 |       |       |            |       0
               6 |      22 | Join                 | 1497366528 |     85 |          17825792 | 2020-09-08 18:57:04 |             21 |       |       | inner      |    6.67
               6 |      24 | AddSortedMinMaxMet.. |    6291456 |      1 |           6291456 | 2020-09-08 18:55:12 |             22 |       |       |            |       0
         [...]
               6 |      32 | ReadTable            |    6291456 |      1 |           6291456 | 2020-09-08 18:55:12 |             31 | 235MB |       | public.t_b |    0.02
         [...]
               6 |      43 | CpuDecompress        |   10000000 |      2 |           5000000 | 2020-09-08 18:55:13 |             42 |       |       |            |       0
               6 |      44 | ReadTable            |   10000000 |      2 |           5000000 | 2020-09-08 18:55:13 |             43 | 14MB  |       | public.t_a |       0
   
* You can map some text values to numeric types by using a dimension table. Then, reconcile the values when you need them by joining the dimension table.


5. Sorting on big ``VARCHAR`` fields
---------------------------------------

In general, SQream DB automatically inserts a ``Sort`` node which arranges the data prior to reductions and aggregations.

When running a ``GROUP BY`` on large ``VARCHAR`` fields, you may see nodes for ``Sort`` and ``Reduce`` taking a long time.


Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When running a statement, inspect it with :ref:`show_node_info`. If you see ``Sort`` and ``Reduce`` among 
your top five longest running nodes, there is a potential issue.

For example:

#. 
   Run a query to test it out.
     
   
   Our ``t_inefficient`` table contains 60,000,000 rows, and the structure is simple, but with an oversized ``country_code`` column:
   
   .. code-block:: postgres
      :emphasize-lines: 5
   
      CREATE TABLE t_inefficient (
         i INT NOT NULL,
         amt DOUBLE NOT NULL,
         ts DATETIME NOT NULL,
         country_code VARCHAR(100) NOT NULL,
         flag VARCHAR(10) NOT NULL,
         string_fk VARCHAR(50) NOT NULL
      );
   
   We will run a query, and inspect it's execution details:
   
   .. code-block:: psql
      
      t=> SELECT country_code,
      .          SUM(amt)
      .   FROM t_inefficient
      .   GROUP BY country_code;
      executed
      time: 47.55s
      
      country_code | sum       
      -------------+-----------
      VUT          | 1195416012
      GIB          | 1195710372
      TUR          | 1195946178
      [...]
      
   
   .. code-block:: psql
      :emphasize-lines: 8,9
      
      t=> select show_node_info(30);
      stmt_id | node_id | node_type          | rows     | chunks | avg_rows_in_chunk | time                | parent_node_id | read  | write | comment              | timeSum
      --------+---------+--------------------+----------+--------+-------------------+---------------------+----------------+-------+-------+----------------------+--------
           30 |       1 | PushToNetworkQueue |      249 |      1 |               249 | 2020-09-10 16:17:10 |             -1 |       |       |                      |    0.25
           30 |       2 | Rechunk            |      249 |      1 |               249 | 2020-09-10 16:17:10 |              1 |       |       |                      |       0
           30 |       3 | ReduceMerge        |      249 |      1 |               249 | 2020-09-10 16:17:10 |              2 |       |       |                      |    0.01
           30 |       4 | GpuToCpu           |     1508 |     15 |               100 | 2020-09-10 16:17:10 |              3 |       |       |                      |       0
           30 |       5 | Reduce             |     1508 |     15 |               100 | 2020-09-10 16:17:10 |              4 |       |       |                      |    7.23
           30 |       6 | Sort               | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |              5 |       |       |                      |    36.8
           30 |       7 | GpuTransform       | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |              6 |       |       |                      |    0.08
           30 |       8 | GpuDecompress      | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |              7 |       |       |                      |    2.01
           30 |       9 | CpuToGpu           | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |              8 |       |       |                      |    0.16
           30 |      10 | Rechunk            | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |              9 |       |       |                      |       0
           30 |      11 | CpuDecompress      | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |             10 |       |       |                      |       0
           30 |      12 | ReadTable          | 60000000 |     15 |           4000000 | 2020-09-10 16:17:10 |             11 | 520MB |       | public.t_inefficient |    0.05

#. We can look to see if there's any shrinking we can do on the ``GROUP BY`` key
   
   .. code-block:: psql
      
      t=> SELECT MAX(LEN(country_code)) FROM t_inefficient;
      max
      ---
      3

   With a maximum string length of just 3 characters, our ``VARCHAR(100)`` is way oversized.

#. 
   We can recreate the table with a more restrictive ``VARCHAR(3)``, and can examine the difference in performance:
   
   .. code-block:: psql

      t=> CREATE TABLE t_efficient 
      .     AS SELECT i,
      .              amt,
      .              ts,
      .              country_code::VARCHAR(3) AS country_code,
      .              flag
      .         FROM t_inefficient;
      executed
      time: 16.03s
      
      t=> SELECT country_code,
      .      SUM(amt::bigint)
      .   FROM t_efficient
      .   GROUP BY country_code;
      executed
      time: 4.75s
      country_code | sum       
      -------------+-----------
      VUT          | 1195416012
      GIB          | 1195710372
      TUR          | 1195946178
      [...]
   
   This time, the entire query took just 4.75 seconds, or just about 91% faster.

Improving sort performance on text keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using VARCHAR, ensure that the maximum length defined in the table structure is as small as necessary.
For example, if you're storing phone numbers, don't define the field as ``VARCHAR(255)``, as that affects sort performance.
   
You can run a query to get the maximum column length (e.g. ``MAX(LEN(a_column))``), and potentially modify the table structure.


.. _high_selectivity_data_opt:

6. High selectivity data
--------------------------

Selectivity is the ratio of cardinality to the number of records of a chunk. We define selectivity as :math:`\frac{\text{Distinct values}}{\text{Total number of records in a chunk}}`

SQream DB has a hint called ``HIGH_SELECTIVITY``, which is a function you can wrap a condition in.

The hint signals to SQream DB that the result of the condition will be very sparse, and that it should attempt to rechunk
the results into fewer, fuller chunks.

.. note::
   SQream DB doesn't do this automatically because it adds a significant overhead on naturally ordered and
   well-clustered data, which is the more common scenario.

Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is easily identifiable - when the amount of average of rows in a chunk is small, following a ``Filter`` operation.

Consider this execution plan:

.. code-block:: psql
   
   t=> select show_node_info(30);
   stmt_id | node_id | node_type         | rows      | chunks | avg_rows_in_chunk | time                | parent_node_id | read  | write | comment    | timeSum
   --------+---------+-------------------+-----------+--------+-------------------+---------------------+----------------+-------+-------+------------+--------
   [...]
        30 |      38 | Filter            |     18160 |     74 |               245 | 2020-09-10 12:17:09 |             37 |       |       |            |   0.012
   [...]
        30 |      44 | ReadTable         |  77000000 |     74 |           1040540 | 2020-09-10 12:17:09 |             43 | 277MB |       | public.dim |   0.058


The table was read entirely - 77 million rows into 74 chunks.

The filter node reduced the output to just 18,160 relevant rows, but they're distributed across the original 74 chunks.
All of these rows could fit in one single chunk, instead of spanning 74 rather sparse chunks.

Improving performance with high selectivity hints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 
   Use when there's a ``WHERE`` condition on an :ref:`unclustered column<data_clustering>`, and when you expect the filter
   to cut out more than 60% of the result set.

* Use when the data is uniformly distributed or random


7. Performance of unsorted data in joins
------------------------------------------

When data is not well-clustered or naturally ordered, a join operation can take a long time. 

Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When running a statement, inspect it with :ref:`show_node_info`. If you see ``Join`` and ``DeferredGather`` among your 
top five longest running nodes, there is a potential issue.

In this case, we're also interested in the number of chunks produced by these nodes.

Consider this execution plan:

.. code-block:: psql
   :emphasize-lines: 6,11
   
   t=> select show_node_info(30);
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

Improving join performance when data is sparse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can tell SQream DB to reduce the amount of chunks involved, if you know that the filter is going to be quite
agressive by using the :ref:`HIGH_SELECTIVITY<high_selectivity>` hint described :ref:`above<high_selectivity_data_opt>`.
This forces the compiler to rechunk the data into fewer chunks.

To tell SQream DB to rechunk the data, wrap a condition (or several) in the ``HIGH_SELECTIVITY`` hint:

.. code-block:: postgres
   :emphasize-lines: 13
   
   -- Without the hint
   SELECT *
   FROM cdrs
   WHERE 
         RequestReceiveTime BETWEEN '2018-01-01 00:00:00.000' AND '2018-08-31 23:59:59.999' 
         AND EnterpriseID=1150 
         AND MSISDN='9724871140341';
   
   -- With the hint
   SELECT *
   FROM cdrs
   WHERE 
         HIGH_SELECTIVITY(RequestReceiveTime BETWEEN '2018-01-01 00:00:00.000' AND '2018-08-31 23:59:59.999')
         AND EnterpriseID=1150 
         AND MSISDN='9724871140341';


8. Manual join reordering
--------------------------------

When joining multiple tables, you may wish to change the join order to join the smallest tables first.

Identifying the situation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When joining more than two tables, the ``Join`` nodes will be the most time-consuming nodes.

Changing the join order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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



Further reading
==================

See our :ref:`sql_best_practices` guide for more information about query optimization and data loading considerations.