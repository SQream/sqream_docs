.. _show_node_info:

********************
SHOW_NODE_INFO
********************

``SHOW_NODE_INFO`` returns a snapshot of the current query plan, similar to ``EXPLAIN ANALYZE`` from other databases.

The snapshot provides information about execution which can be used for monitoring and troubleshooting slow running statements by helping identify long-running execution nodes (components that process data), etc.

See also :ref:`explain`, :ref:`show_server_status`.

Permissions
=============

The role must have the ``SUPERUSER`` permissions.

Syntax
==========

.. code-block:: postgres

   show_node_info_statement ::=
       SELECT SHOW_NODE_INFO(stmt_id)
       ;
   
   stmt_id ::= bigint

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``stmt_id``
     - The statement ID to explore

Returns
=========

This utility returns details of the execution nodes, if the statement is still running.

If the statement has finished, or the statment ID does not exist, the utility returns an empty result set.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1
   
   * - Column name
     - Description
   * - ``stmt_id``
     - The ID for the statement
   * - ``node_id``
     - This node's ID in this execution plan
   * - ``node_type``
     - The node type
   * - ``rows``
     - Total number of rows this node has processed
   * - ``chunks``
     - Number of chunks this node has processed
   * - ``avg_rows_in_chunk``
     - Average amount of rows that this node processes in each chunk (``rows / chunks``)
   * - ``time``
     - Timestamp for this node's creation
   * - ``parent_node_id``
     - The ``node_id`` of this node's parent
   * - ``read``
     - Total data read from disk
   * - ``write``
     - Total data written to disk
   * - ``comment``
     - Additional information (e.g. table name for ``ReadTable``)
   * - ``timesum``
     - Total elapsed time for this execution node's processing

Node type
=============

This is a partial list of node types.

.. list-table:: Common node types
   :widths: auto
   :header-rows: 1
   
   * - Column name
     - Execution location
     - Description
   * - ``CpuToGpu``, ``GpuToCpu``
     - 
     - An operation that moves data to or from the GPU for processing
   * - ``DecompressorCpu``
     - CPU
     - Decompression operation, common for longer ``VARCHAR`` types
   * - ``DecompressorGpu``
     - GPU
     - Decompression operation
   * - ``LoopJoin``
     - GPU
     - A ``JOIN`` operation
   * - ``Filter``
     - GPU
     - A filtering operation, such as a ``WHERE`` or ``JOIN`` clause
   * - ``GpuTransform``
     - GPU
     - A transformation operation such as a type cast or :ref:`scalar function<scalar_functions>`
   * - ``PushToNetworkQueue``
     - 
     - Sends data to a client connected over the network
   * - ``Rechunk``
     - 
     - Reorganize multiple small chunks into a full chunk. Commonly found after joins and where :ref:`HIGH_SELECTIVITY<high_selectivity>` is used
   * - ``ReadTable``
     - CPU
     - Data read from a standard table
   * - ``ReadParquet``
     - CPU
     - Data read from a Parquet file
   * - ``ReadOrc``
     - CPU
     - Data read from an ORC file
   * - ``Reduce``
     - GPU
     - A reduction operation, such as a ``GROUP BY``
   * - ``ReorderInput``
     - 
     - Change the order of arguments in preparation for the next operation
   * - ``SeparatedGather``
     - GPU
     - Gathers additional columns for the result[#f0]_
   * - ``Sort``
     - 
     - Sort operation [#f1]_

.. rubric:: Footnotes

.. [#f0] Gathers columns which should be returned. This node typically spends most of the time on decompressing additional columns.

.. [#f1] A GPU sort operation can be added by the statement compiler before ``GROUP BY`` or ``JOIN`` operations.

Statement statuses
=======================

.. include:: /reference/sql/sql_statements/monitoring_commands/show_server_status.rst
   :start-line: 67
   :end-line: 84
   
Notes
===========

* This utility shows the execution information for active statements. Once a query has finished execution, the information is no longer available using this utility. See :ref:`logging` for more information about extracting the information from the logs.

* This utility is primarily intended for troubleshooting with SQream support.

Examples
===========

Getting execution details for a statement
------------------------------------------------


.. code-block:: psql
   
   t=> SELECT SHOW_SERVER_STATUS();
   service | instanceid | connection_id | serverip     | serverport | database_name | user_name | clientip     | statementid | statement                                                       | statementstarttime  | statementstatus | statementstatusstart
   --------+------------+---------------+--------------+------------+---------------+-----------+--------------+-------------+-----------------------------------------------------------------+---------------------+-----------------+---------------------
   sqream  |            |           152 | 192.168.1.91 |       5000 | t            | sqream    | 192.168.1.91 |         176 | SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | 25-12-2019 23:53:13 | Executing       | 25-12-2019 23:53:13
   sqream  |            |           151 | 192.168.1.91 |       5000 | t            | sqream    | 192.168.0.1  |         177 | SELECT show_server_status()                                     | 25-12-2019 23:51:31 | Executing       | 25-12-2019 23:53:13 


The statement ID we want to reserach is ``176``, running on worker ``192.168.1.91``.

The query text is ``SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1;``

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

