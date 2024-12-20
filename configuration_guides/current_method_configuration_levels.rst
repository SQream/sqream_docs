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

	ALTER SYSTEM SET <flagName>

Session flag syntax:

.. code-block:: sql

	SET <flagName>

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
   * - ``binSizes`` 
     - SUPERUSER
     - Session
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - string
     - 
	   ``16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,``	   
	   ``131072,262144,524288,1048576,2097152,4194304,8388608,16777216,``
	   ``33554432,67108864,134217728,268435456,536870912,786432000,107374,``
	   ``1824,1342177280,1610612736,1879048192,2147483648,2415919104,``
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
     - bigint
     - Any legal string
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
     - Anyone
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
     - Cluster
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
   * - ``enableLogDebug`` 
     - SUPERUSER
     - Session
     - Enables creating and logging in the clientLogger_debug file.
     - boolean
     - ``TRUE``	 
   * - ``enableNvprofMarkers`` 
     - SUPERUSER
     - Session
     - Activates the Nvidia profiler (nvprof) markers.
     - boolean
     - ``FALSE``
   * - ``endLogMessage`` 
     - SUPERUSER
     - Session
     - Appends a string at the end of every log line.
     - string
     - ``EOM`` 
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
   * - ``leveldbWriteBufferSize`` 
     - SUPERUSER
     - Session
     - Sets the buffer size.
     - uint
     - ``524288``
   * - ``logClientLevel``
     - SUPERUSER
     - Cluster
     - Used to control which :ref:`log level<information_level>` should appear in the logs. Value range: ``0`` - ``6``
     - int
     - Default value: ``4``
	 
	Acceptable values:
	 	 
	``0`` - Only SYSTEM level logs
	 
	``1`` - SYSTEM and FATAL
	
	``2`` - SYSTEM, FATAL, and ERROR level logs
	 
	``3`` - SYSTEM, FATAL, ERROR, and WARNING level logs
	 
	``4`` - SYSTEM, FATAL, ERROR, WARNING, and INFO level logs
	 
	``5`` - SYSTEM, FATAL, ERROR, WARNING, INFO, and DEBUG level logs
	 
	``6`` - SYSTEM, FATAL, ERROR, WARNING, INFO, DEBUG, and TRACE level logs
   * - ``logFileRotateTimeFrequency``
     - SUPERUSER
     - Cluster
     - Specifies when the system begins writing to a new log file. SQreamDB recommends using the ``logFileRotateTimeFrequency`` flag (rather than the ``logMaxFilesSizeMB`` flag) to configure when a new log file is created, as this flag does not limit the number of log files.
     - string
     - ``daily``. Acceptable values: ``daily``, ``weekly``, or ``monthly``
   * - ``logMaxFilesSizeMB``
     - SUPERUSER
     - Cluster
     - Specifies when the system begins writing to a new log file. When configured with the ``logMaxFilesSizeMB`` flag, the system maintains up to 13 log files. Once the 13th file is complete, the oldest log file is overwritten by the newly created log file. SQreamDB recommends using the ``logFileRotateTimeFrequency`` flag to configure when a new log file is created, as this flag does not limit the number of log files.
     - int
     - ``100`` (Megabyte)
   * - ``logSysLevel`` 
     - Anyone
     - Session
     - 
	   Determines the client log level:
	   0 - L_SYSTEM,
	   1 - L_FATAL,
	   2 - L_ERROR,
	   3 - L_WARN,
	   4 - L_INFO,
	   5 - L_DEBUG,
	   6 - L_TRACE	   
     - uint
     - ``100000``	
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
     - Any legal string
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
   * - ``externalTableBlobEstimate``
     - ?
     - Session
     - ?
     - ?
     - ?
   * - ``maxPinnedPercentageOfTotalRAM``
     - SUPERUSER
     - Session
     - Sets the maximum percentage CPU RAM that pinned memory can use.
     - uint
     - ``70``
   * - ``memMergeBlobOffsetsCount``
     - SUPERUSER
     - Session
     - Sets the size of memory used during a query to trigger aborting the server.
     - uint
     - ``0``
   * - ``queueTimeoutMinutes``
     - Anyone
     - Session 
     - Terminates queries that have exceeded a predefined time limit in the queue.
     - integer
     - Default value: 0. Minimum values: 1 minute. Maximum value: 4320 minutes (72 hours) 

