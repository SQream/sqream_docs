.. _current_method_configuration_levels:

*******************
Cluster and Session 
*******************

When configuring your SQreamDB environment, you have the option to use flags that apply to either the entire cluster or a specific session. Cluster configuration involve metadata and is persistent. Persistent modifications refer to changes made to a system or component that are saved and retained even after the system is restarted or shut down, allowing the modifications to persist over time. Session flags only apply to a specific session and are not persistent. Changes made using session flags are not visible to other users, and once the session ends, the flags return to their default values.

Setting the flags
=================

Syntax
------

You may set both cluster and session flags using the following syntax on SQreamDB Acceleration Studio and Console: 

Cluster flag syntax:

.. code-block:: sql

	ALTER SYSTEM SET <flagName> = <value>

Session flag syntax:

.. code-block:: sql

	SET <flagName> = <value>

Configuration file
------------------

You may set session flags within your :ref:`Legacy Configuration File<modifying_your_configuration_using_a_legacy_configuration_file>`.

Flag List
=========

.. list-table::
   :header-rows: 1
   :widths: auto
   :name: my-name

   * - Flag Name
     - Who May Configure
     - Cluster / Session
     - Description
     - Data Type
     - Default Value and Value Range
   * - ``aggregateBelowRank``
     - SUPERUSER
     - Session
     - Places an aggregation below a rank window function, so that the window sorts groups rather than rows. Off by default, because the compiler cannot tell in advance how many groups the lower aggregation produces.
     - boolean
     - ``FALSE``
   * - ``binSizes`` 
     - SUPERUSER
     - Session
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - string
     - 
	   ``16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,``	   
	   ``131072,262144,524288,1048576,2097152,4194304,8388608,16777216,``
	   ``33554432,67108864,134217728,268435456,536870912,786432000,1073741824,``
	   ``1342177280,1610612736,1879048192,2147483648,2415919104,``
	   ``2684354560,2952790016,3221225472``
   * - ``blockNewVarcharObjects`` 
     - SUPERUSER
     - Session
     - Disables the creation of new tables, views, external tables containing Varchar columns, and the creation of user-defined functions with Varchar arguments or a Varchar return value.
     - boolean
     - ``FALSE``
   * - ``cacheDiskDir`` 
     - Anyone
     - Session
     - Sets the ondisk directory location for the spool to save files on. Allowed values: Any legal string.
     - string
     - ``/tmp``
   * - ``cacheDiskGB`` 
     - Anyone
     - Session
     - Sets the amount of memory (GB) to be used by Spool on the disk. Allowed values: 0-4000000000.
     - bigint
     - ``128``
   * - ``cacheEvictionMilliseconds`` 
     - Anyone
     - Session
     - Sets how long the cache stores contents before being flushed. Allowed values: 1-4000000000.
     - bigint
     - ``2000``
   * - ``cachePartitions`` 
     - Anyone
     - Session
     - Sets the number of partitions that the cache is split into. Allowed values: 1-4000000000.
     - bigint
     - ``4``
   * - ``cachePersistentDir`` 
     - Anyone
     - Session
     - Sets the persistent directory location for the spool to save files on. Allowed values: Any legal string.
     - string
     - ``/tmp``
   * - ``cachePersistentGB`` 
     - Anyone
     - Session
     - Sets the amount of data (GB) for the cache to store persistently. Allowed values: 0-4000000000.
     - bigint
     - ``128``
   * - ``cacheRamGB`` 
     - Anyone
     - Session
     - Sets the amount of memory (GB) to be used by Spool InMemory. Allowed values: 0-4000000000.
     - bigint
     - ``16``
   * - ``checkCudaMemory`` 
     - SUPERUSER
     - Session
     - Sets the pad device memory allocations with safety buffers to catch out-of-bounds writes.
     - boolean
     - ``FALSE``
   * - ``compilerGetsOnlyUFs`` 
     - SUPERUSER
     - Session
     - Sets the runtime to pass only utility functions names to the compiler.
     - boolean
     - ``FALSE``
   * - ``clientReconnectionTimeout``
     - SUPERUSER
     - Cluster
     - Reconnection time out for the system in seconds.
     - Integer
     - ``30``
   * - ``copyToRestrictUtf8`` 
     - SUPERUSER
     - Session
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - boolean
     - ``FALSE``
   * - ``csvLimitRowLength`` 
     - SUPERUSER
     - Cluster
     - Sets the maximum supported CSV row length. Allowed values: 1-4000000000
     - uint
     - ``100000``
   * - ``cudaMemcpyMaxSizeBytes`` 
     - SUPERUSER
     - Session
     - Sets the chunk size for copying from CPU to GPU. If set to 0, do not divide.
     - uint
     - ``0``
   * - ``CudaMemcpySynchronous`` 
     - SUPERUSER
     - Session
     - Indicates if copying from/to GPU is synchronous.
     - boolean
     - ``FALSE`` 	 
   * - ``defaultGracefulShutdownTimeoutMinutes``
     - SUPERUSER
     - Session
     - Used for setting the amount of time to pass before SQream performs a graceful server shutdown. Allowed values - 1-4000000000. Related flags: ``is_healer_on`` and ``healer_max_inactivity_hours``
     - bigint
     - ``5``
   * - ``developerMode`` 
     - SUPERUSER
     - Session
     - Enables modifying R&D flags.
     - boolean
     - ``FALSE`` 
   * - ``enableDeviceDebugMessages`` 
     - SUPERUSER
     - Session
     - Checks for CUDA errors after producing each chunk.
     - boolean
     - ``FALSE``
   * - ``enableNvprofMarkers`` 
     - SUPERUSER
     - Session
     - Activates the Nvidia profiler (nvprof) markers.
     - boolean
     - ``FALSE`` 
   * - ``extentStorageFileSizeMB`` 
     - SUPERUSER
     - Cluster
     - Sets the minimum size in mebibytes of extents for table bulk data.
     - uint
     - ``20``
   * - ``flipJoinOrder`` 
     - Anyone
     - Session
     - Reorders join to force equijoins and/or equijoins sorted by table size.
     - boolean
     - ``FALSE``
   * - ``gatherMemStat`` 
     - SUPERUSER
     - Session
     - Monitors all pinned allocations and all **memcopies** to/from device, and prints a report of pinned allocations that were not memcopied to/from the device using the ``dump_pinned_misses`` utility function.
     - boolean
     - ``FALSE`` 
   * - ``increaseChunkSizeBeforeReduce`` 
     - SUPERUSER
     - Session
     - Increases the chunk size to reduce query speed.
     - boolean
     - ``FALSE``
   * - ``increaseMemFactors`` 
     - SUPERUSER
     - Session
     - Adds rechunker before expensive chunk producer.
     - boolean
     - ``TRUE``
   * - ``inListJoinMaxMetadataFilters``
     - SUPERUSER
     - Session
     - Sets the largest number of distinct values per column that an ``IN`` list compiled as a join keeps as metadata filters, so that the scan still skips chunks. Allowed values: ``0`` or any positive integer, where ``0`` keeps no per-value filters.
     - int
     - ``1000``
   * - ``inListJoinMaxMetadataRanges``
     - SUPERUSER
     - Session
     - Sets the largest number of ranges kept as metadata filters for a column whose distinct values outnumber ``inListJoinMaxMetadataFilters``. Allowed values: ``0`` or any positive integer, where ``0`` keeps no ranges.
     - int
     - ``32``
   * - ``inListJoinThreshold``
     - SUPERUSER
     - Session
     - Sets the number of values above which an ``IN`` list is compiled as an inner join against the listed values, instead of being expanded into a chain of equality comparisons. Allowed values: any positive integer.
     - int
     - ``100``
   * - ``inListRangeMaxMissingPercent``
     - SUPERUSER
     - Session
     - Sets the share of a range, as a percentage, that may be missing from a list compiled as a range. Allowed values: ``0`` to ``100``, where ``0`` requires no missing values.
     - int
     - ``10``
   * - ``inListRangeMinValues``
     - SUPERUSER
     - Session
     - Sets the number of distinct values from which an ``IN`` list on a nearly consecutive ``INT`` or ``DATE`` column is compiled as the range its values span. Allowed values: ``0`` or any positive integer, where ``0`` turns the range form off.
     - int
     - ``20``
   * - ``inListRangeMissingMultiplier``
     - SUPERUSER
     - Session
     - Caps the values missing from a list compiled as a range: the missing values times this flag may not exceed ``inListJoinThreshold``. Allowed values: ``0`` or any positive integer, where ``0`` lifts the cap.
     - int
     - ``2``
   * - ``leveldbWriteBufferSize``
     - SUPERUSER
     - Session
     - Sets the buffer size.
     - uint
     - ``67108864`` (64 MB)	
   * - ``maxAvgBlobSizeToCompressOnGpu`` 
     - Anyone
     - Session
     - Sets the CPU to compress columns with size above (flag’s value) * (row count).
     - uint
     - ``120``
   * - ``memoryResetTriggerMB`` 
     - SUPERUSER
     - Session
     - Sets the size of memory used during a query to trigger aborting the server.
     - uint
     - ``0``
   * - ``mtRead`` 
     - SUPERUSER
     - Session
     - Splits large reads to multiple smaller ones and executes them concurrently.
     - boolean
     - ``FALSE``
   * - ``mtReadWorkers`` 
     - SUPERUSER
     - Session
     - Sets the number of workers to handle smaller concurrent reads.
     - uint
     - ``30``
   * - ``orcImplicitCasts`` 
     - SUPERUSER
     - Session
     - Sets the implicit cast in orc files, such as **int** to **tinyint** and vice versa.
     - boolean
     - ``TRUE``	
   * - ``QueryTimeoutMinutes``
     - Anyone
     - Session
     - Terminates queries that have exceeded a predefined execution time limit, ranging from ``1`` to ``4,320`` minutes (72 hours).
     - integer
     - ``0`` (no query timeout)	 
   * - ``sessionTag`` 
     - Anyone
     - Session
     - Sets the name of the session tag. Allowed values: Any legal string.
     - string
     - ``default``
   * - ``spoolMemoryGB`` 
     - Anyone
     - Session
     - Sets the amount of memory (GB) to be used by the server for spooling.
     - uint
     - ``8``
   * - ``statementLockTimeout`` 
     - SUPERUSER
     - Session
     - Sets the timeout (seconds) for acquiring object locks before executing statements.
     - uint
     - ``3``
   * - ``useLegacyDecimalLiterals`` 
     - SUPERUSER
     - Session
     - Interprets decimal literals as **Double** instead of **Numeric**. Used to preserve legacy behavior in existing customers.
     - boolean
     - ``FALSE``	 
	 
	 
	 
	 
   * - ``cpuReduceHashtableSize``
     - SUPERUSER
     - Session
     - Sets the hash table size of the CpuReduce.
     - uint
     - ``10000``
   * - ``maxPinnedPercentageOfTotalRAM``
     - SUPERUSER
     - Session
     - Sets the maximum percentage CPU RAM that pinned memory can use.
     - uint
     - ``70``
   * - ``queueTimeoutMinutes``
     - Anyone
     - Session 
     - Terminates queries that have exceeded a predefined time limit in the queue.
     - integer
     - Default value: 0. Minimum values: 1 minute. Maximum value: 4320 minutes (72 hours) 
   * - ``timezone``
     - Anyone
     - Session 
     - The timezone flag dictates the timezone context used when SQDB encounters ``DATETIME2`` values during data ingestion. This includes overriding any existing timezone information within those values.
     - Text
     - Default value: ``null``. ``local`` local system timezone of the SQDB server. ``+hh:mm`` or ``-hh:mm`` explicitly defines the timezone for all incoming ``DATETIME2`` values, overriding any existing timezone information.

