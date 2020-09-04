.. _monitoring_query_performance:

*********************************
Monitoring query performance
*********************************

When analyzing options for query tuning, the first step is to analyze the query plan and execution.

The query plan and execution details explains how SQream DB processes a query and where time is spent.

This document details how to analyze query performance with execution plans.

This guide focuses specifically on identifying bottlenecks and possible optimization techniques to improve query performance.

Performance tuning options for each query are different. You should adapt the recommendations and tips for your own workloads.

.. contents:: In this topic:
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

:ref:`show_node_info` returns a snapshot of the current query plan, similar to ``EXPLAIN ANALYZE`` from other databases.

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

Understanding the query plan output
==================================================

Both :ref:`show_node_info`  and the logged execution plans represents the query plan as a graph hierarchy, with data separated into different columns.

Each row represents a single logical database operation.

.. include:: /reference/sql/sql_statements/monitoring_commands/show_node_info.rst
   :start-line: 47
   :end-line: 78

Examples
==================

Spooling to disk
-----------------------

Queries with large result sets
------------------------------------

Deferred Gather

Inefficient filtering
--------------------------------

Join on text / varchar keys
-----------------------------------

Sort on text fields
--------------------------

Non-ANSI join performance
----------------------------------

Performance of unsorted data in joins
----------------------------------------

High selectivity data
------------------------

Selectivity is the ratio of cardinality to the number of records of an Indexed column.
Selectivity = (Distinct Values/Total number of records)

Manual join reordering
--------------------------------



