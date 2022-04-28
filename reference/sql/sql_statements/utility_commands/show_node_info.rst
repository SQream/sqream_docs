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


.. _node_types:

Node types
=============

This is a full list of node types:

.. list-table:: Node types
   :widths: auto
   :header-rows: 1
   
   * - Column name
     - Execution location
     - Description
   * - ``AddChunkId``
     - 
     - Used during insert operations
   * - ``AddSequences``
     -
     - Used during insert operations, with :ref:`identity columns<identity>`
   * - ``AddMinMaxMetadata``
     - 
     - Used to calculate ranges for the :ref:`chunk metadata system<metadata_system>`
   * - ``AddTopSortFilters``
     - 
     - An operation to optimize ``LIMIT`` when used alongside ``ORDER BY``
   * - ``Compress``
     - CPU and GPU
     - Compress data with both CPU and GPU schemes
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
   * - ``CrossJoin``
     - 
     - A join without a join condition
   * - ``DeferredGather``
     - CPU
     - Merges the results of GPU operations with a result set [#f0]_
   * - ``Distinct``
     - GPU
     - Removes duplicate rows (usually as part of the ``DISTINCT`` operation)
   * - ``Distinct_Merge``
     - CPU
     - The merge operation of the ``Distinct`` operation
   * - ``Filter``
     - GPU
     - A filtering operation, such as a ``WHERE`` or ``JOIN`` clause
   * - ``GpuCopy``
     - GPU
     - Copies data between GPUs or within a single GPU
   * - ``GpuDecompress``
     - GPU
     - Decompression operation
   * - ``GpuReduceMerge``
     - GPU
     - An operation to optimize part of the merger phases in the GPU
   * - ``GpuTransform``
     - GPU
     - A transformation operation such as a type cast or :ref:`scalar function<scalar_functions>`
   * - ``Hash``
     - CPU
     - Hashes the output result. Used internally.
   * - ``JoinSideMarker``
     - 
     - Used internally.
   * - ``LiteralValues``
     - CPU
     - Creates a virtual relation (table), when :ref:`values` is used
   * - ``LocateFiles``
     - CPU
     - Validates external file paths for foreign data wrappers, expanding directories and GLOB patterns
   * - ``LoopJoin``
     - GPU
     - A non-indexed nested loop join, performed on the GPU
   * - ``MarkMatchedJoinRows``
     - 
     - Used in outer joins, matches rows for larger join operations
   * - ``NullifyDuplicates``
     - 
     - Replaces duplicate values with ``NULL`` to calculate distinct aggregates
   * - ``NullSink``
     - CPU
     - Used internally
   * - ``ParseCsv``
     - CPU
     - A CSV parser, used after ``ReadFiles`` to convert the CSV into columnar data
   * - ``PopNetworkQueue``
     - CPU
     - Fetches data from the network queue (e.g. when used with :ref:`insert`)
   * - ``PushToNetworkQueue``
     - CPU
     - Sends result sets to a client connected over the network
   * - ``ReadCatalog``
     - CPU
     - Converts the :ref:`catalog<catalog_reference>` into a relation (table)
   * - ``ReadFiles``
     - CPU
     - Reads external flat-files
   * - ``ReadOrc``
     - CPU
     - Reads data from an ORC file
   * - ``ReadParquet``
     - CPU
     - Reads data from a Parquet file
   * - ``ReadTable``
     - CPU
     - Reads data from a standard table stored on disk
   * - ``ReadTableMetadata``
     - CPU
     - Reads only table metadata as an optimization
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
     - Sort operation [#f1]_
   * - ``SortMerge``
     - CPU
     - A merge operation of a sort operation, helps operate on larger-than-RAM data
   * - ``SortMergeJoin``
     - GPU
     - A sort-merge join, performed on the GPU
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
   * - ``VarCharJoiner``
     - 
     - Used internally
   * - ``VarCharSplitter``
     -
     - Used intenrally
   * - ``Window``
     - GPU
     - Executes a non-ranking :ref:`window function<window_functions>`
   * - ``WindowRanking``
     - GPU
     - Executes a ranking :ref:`window function<window_functions>`
   * - ``WriteTable``
     - CPU 
     - Writes the result set to a standard table stored on disk

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

