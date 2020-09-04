.. _monitoring_query_performance:

*********************************
Monitoring query performance
*********************************

When analyzing options for query tuning, the first step is to analyze the query plan and execution.

The query plan and execution details explains how SQream DB processes a query and where time is spent.

This document details how to analyze query performance with execution plans.

This guide focuses specifically on identifying bottlenecks and possible optimization techniques to improve query performance.

Performance tuning options for each query are different. You should adapt the recommendations and tips for your own workloads.

.. contents:: In this section:
   :local:

Setting up the system for monitoring
=================================================

By default, SQream DB logs execution details for every statement that runs for more than 60 seconds.
If you want to see the execution details for a currently running statement, see :ref:`using_show_node_info` below.


Adjusting the logging frequency
---------------------------------------

To adjust the frequency of logging for statements, you may want to reduce the interval from 60 seconds down to, say, 5 or 10 seconds. Modify the configuration files and set the ``nodeInfoLoggingSec`` parameter as you see fit:

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

The :ref:`show_node_info` result, just like the periodically-logged execution plans described above, are an at-the-moment view of the compiler's execution plan and runtime statistics for the specified statement.

To inspect a currently running statement, execute the ``show_node_info`` utility function in a SQL client like :ref:`sqream sql<sqream_sql_cli_reference>`, the :ref:`SQream Studio Editor<studio_editor>`, or any other :ref:`third party SQL terminal<third_party_tools>`.

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
   
   The total spool used by this query is around 20GB.

Common solutions for reducing spool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 
   Increase the amount of spool memory available for the workers, as a proportion of the maximum statement memory.
   When the amount of spool memory is increased, SQream DB may not need to write to disk.
   
   This setting is called ``spoolMemoryGB``. Refer to the :ref:`configuration` guide.

* Reduce the amount of **workers** per host, and increase the amount of spool available to the (now reduced amount of) active workers. This may reduce the amount of concurrent statements, but will improve performance for heavy statements.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Reduce the effect of the preparation time. Avoid selecting unnecessary columns (``SELECT * FROM...``), or reduce the result set size by using more filters.


.. 
   3. Inefficient filtering
   --------------------------------

   4. Join on text / varchar keys
   -----------------------------------
   
   5. Sort on text fields
   --------------------------

   6. Non-ANSI join performance
   ----------------------------------

   7. Performance of unsorted data in joins
   ------------------------------------------

   8. High selectivity data
   --------------------------

   Selectivity is the ratio of cardinality to the number of records of an Indexed column.
   Selectivity = (Distinct Values/Total number of records)
   
   9. Manual join reordering
   --------------------------------



