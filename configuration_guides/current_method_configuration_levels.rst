.. _current_method_configuration_levels:

**************************
Configuring Your SQream Workflow
**************************

When configuring the SQream system and workflow, you have the option to use flags that apply to either the entire cluster or a specific session. Cluster configurations involve metadata and are persistent. Persistent modifications refer to changes made to a system or component that are saved and retained even after the system is restarted or shut down, allowing the modifications to persist over time.

Session-based flags only apply to a specific session and are not persistent. Changes made using session-based flags are not visible to other users, and once the session ends, the flags return to their default values.

Cluster-based flag syntax:

.. code-block:: postgress

	ALTER SYSTEM SET <flagName>

Session-based flag syntax:

.. code-block:: postgress

	SET <flagName>

.. list-table::
   :header-rows: 1
   :widths: 1 2 1 15 1 20
   :class: my-class
   :name: my-name

   * - Flag Name
     - Who May Configure
     - Cluster / Session
     - Description
     - Data Type
     - Default Value

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

   * - ``cacheEvictionMilliseconds`` 
     - Anyone
     - Session
     - Sets how long the cache stores contents before being flushed. Allowed values: 1-4000000000.
     - bigint
     - ``2000``
	 

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
	 
   * - ``copyToRestrictUtf8`` 
     - SUPERUSER
     - Session
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - boolean
     - ``FALSE``	 
	 
   * - ``cpuReduceHashtableSize``
     - SUPERUSER
     - Session
     - Sets the hash table size of the CpuReduce.
     - uint
     - ``10000``		 
	 
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


   * - ``externalTableBlobEstimate``
     - ?
     - Session
     - ?
     - ?
     - ?





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

   * - ``useLegacyStringLiterals`` 
     - SUPERUSER
     - Session
     - Interprets ASCII-only strings as **VARCHAR** instead of **TEXT**. Used to preserve legacy behavior in existing customers.
     - boolean
     - ``FALSE``


	 
	 

	 



   * - ``blockNewVarcharObjects`` 
     - SUPERUSER
     - Session
     - Disables the creation of new tables, views, external tables containing Varchar columns, and the creation of user-defined functions with Varchar arguments or a Varchar return value.
     - boolean
     - ``FALSE``
   * - ``defaultGracefulShutdownTimeoutMinutes``
     - SUPERUSER
     - Cluster
     - Used for setting the amount of time to pass before SQream performs a graceful server shutdown. Allowed values - 1-4000000000. Related flags: ``is_healer_on`` and ``healer_max_inactivity_hours``
     - bigint
     - ``5``
   * - ``limitQueryMemoryGB``
     - SUPERUSER
     - Cluster
     - Prevents a query from processing more memory than the defined value.
     - uint
     - ``100000``