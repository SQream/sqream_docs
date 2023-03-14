.. _current_method_all_configurations:

**************************
All Configurations
**************************
The following table describes all **Generic** and **Administration** configuration flags:

.. list-table::
   :header-rows: 1
   :widths: 1 2 1 15 1 20
   :class: my-class
   :name: my-name

   * - Flag Name
     - Access Control
     - Modification Type
     - Description
     - Data Type
     - Default Value

   * - ``binSizes``
     - Admin
     - Regular
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - string
     - 
	   ``16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,``	   
	   ``131072,262144,524288,1048576,2097152,4194304,8388608,16777216,``
	   ``33554432,67108864,134217728,268435456,536870912,786432000,107374,``
	   ``1824,1342177280,1610612736,1879048192,2147483648,2415919104,``
	   ``2684354560,2952790016,3221225472``

   * - ``cacheEvictionMilliseconds``
     - Generic
     - Regular
     - Sets how long the cache stores contents before being flushed.
     - size_t
     - ``2000``
	 

   * - ``cacheDiskDir``
     - Generic
     - Regular
     - Sets the ondisk directory location for the spool to save files on.
     - size_t
     - Any legal string
	 

   * - ``cacheDiskGB``
     - Generic
     - Regular
     - Sets the amount of memory (GB) to be used by Spool on the disk.
     - size_t
     - ``128``
	 
   * - ``cachePartitions``
     - Generic
     - Regular
     - Sets the number of partitions that the cache is split into.
     - size_t
     - ``4``
	 

   * - ``cachePersistentDir``
     - Generic
     - Regular
     - Sets the persistent directory location for the spool to save files on.
     - string
     - Any legal string
	 

   * - ``cachePersistentGB``
     - Generic
     - Regular
     - Sets the amount of data (GB) for the cache to store persistently.
     - size_t
     - ``128``


   * - ``cacheRamGB``
     - Generic
     - Regular
     - Sets the amount of memory (GB) to be used by Spool InMemory.
     - size_t
     - ``16``



   * - ``checkCudaMemory``
     - Admin
     - Regular
     - Sets the pad device memory allocations with safety buffers to catch out-of-bounds writes.
     - boolean
     - ``FALSE``

   * - ``compilerGetsOnlyUFs``
     - Admin
     - Regular
     - Sets the runtime to pass only utility functions names to the compiler.
     - boolean
     - ``FALSE``
	 
   * - ``copyToRestrictUtf8``
     - Admin
     - Regular
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - boolean
     - ``FALSE``	 
	 
   * - ``cpuReduceHashtableSize``
     - Admin
     - Regular
     - Sets the hash table size of the CpuReduce.
     - uint
     - ``10000``		 
	 
   * - ``csvLimitRowLength``
     - Admin
     - Cluster
     - Sets the maximum supported CSV row length.
     - uint
     - ``100000`` 
	 
   * - ``cudaMemcpyMaxSizeBytes``
     - Admin
     - Regular
     - Sets the chunk size for copying from CPU to GPU. If set to 0, do not divide.
     - uint
     - ``0`` 	 
	 
   * - ``CudaMemcpySynchronous``
     - Admin
     - Regular
     - Indicates if copying from/to GPU is synchronous.
     - boolean
     - ``FALSE`` 	 
	 
   * - ``cudaMemQuota``
     - Admin
     - Worker
     - Sets the percentage of total device memory to be used by the instance.
     - uint
     - ``90`` 	 
	 
   * - ``developerMode``
     - Admin
     - Regular
     - Enables modifying R&D flags.
     - boolean
     - ``FALSE`` 	 
	 
   * - ``enableDeviceDebugMessages``
     - Admin
     - Regular
     - Activates the Nvidia profiler (nvprof) markers.
     - boolean
     - ``FALSE`` 

   * - ``enableLogDebug``
     - Admin
     - Regular
     - Enables creating and logging in the clientLogger_debug file.
     - boolean
     - ``TRUE``

   * - ``enableNvprofMarkers``
     - Admin
     - Regular
     - Activates the Nvidia profiler (nvprof) markers.
     - boolean
     - ``FALSE``	 
	 
   * - ``endLogMessage``
     - Admin
     - Regular
     - Appends a string at the end of every log line.
     - string
     - ``EOM`` 
	 
	 

 

	 
	 
   * - ``extentStorageFileSizeMB``
     - Admin
     - Cluster
     - Sets the minimum size in mebibytes of extents for table bulk data.
     - uint
     - ``20``


   * - ``externalTableBlobEstimate``
     - ?
     - Regular
     - ?
     - ?
     - ?





   * - ``flipJoinOrder``
     - Generic
     - Regular
     - Reorders join to force equijoins and/or equijoins sorted by table size.
     - boolean
     - ``FALSE``

 
	 
   * - ``gatherMemStat``
     - Admin
     - Regular
     - Monitors all pinned allocations and all **memcopies** to/from device, and prints a report of pinned allocations that were not memcopied to/from the device using the **dump_pinned_misses** utility function.
     - boolean
     - ``FALSE``


   * - ``healerMaxInactivityHours``
     - Admin
     - Worker
     - Defines the threshold for creating a log recording a slow statement.
     - size_t
     - ``5``	


	 
	 
   * - ``increaseChunkSizeBeforeReduce``
     - Admin
     - Regular
     - Increases the chunk size to reduce query speed.
     - boolean
     - ``FALSE``		 
	 
   * - ``increaseMemFactors``
     - Admin
     - Regular
     - Adds rechunker before expensive chunk producer.
     - boolean
     - ``TRUE``	 


   * - ``isHealerOn``
     - Admin
     - Worker
     - Periodically examines the progress of running statements and logs statements exceeding the ``healerMaxInactivityHours`` flag setting.
     - boolean
     - ``TRUE``	 




	 
   * - ``leveldbWriteBufferSize``
     - Admin
     - Regular
     - Sets the buffer size.
     - uint
     - ``524288``

   * - ``limitQueryMemoryGB``
     - Generic
     - Worker
     - Prevents a query from processing more memory than the flag’s value.
     - uint
     - ``100000``




   * - ``loginMaxRetries``
     - Admin
     - Worker
     - Sets the permitted log-in attempts.
     - size_t
     - ``5``

	

   * - ``logSysLevel``
     - Generic
     - Regular
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




	 
   * - ``machineIP``
     - Admin
     - Worker
     - Manual setting of reported IP.
     - string
     - ``127.0.0.1``		 
	 

   * - ``maxAvgBlobSizeToCompressOnGpu``
     - Generic
     - Regular
     - Sets the CPU to compress columns with size above (flag’s value) * (row count).
     - uint
     - ``120``


   * - ``maxPinnedPercentageOfTotalRAM``
     - Admin
     - Regular
     - Sets the maximum percentage CPU RAM that pinned memory can use.
     - uint
     - ``70``



   * - ``memMergeBlobOffsetsCount``
     - Admin
     - Regular
     - Sets the size of memory used during a query to trigger aborting the server.
     - uint
     - ``0``


	 
   * - ``memoryResetTriggerMB``
     - Admin
     - Regular
     - Sets the size of memory used during a query to trigger aborting the server.
     - uint
     - ``0``		 
 
   * - ``metadataServerPort``
     - Admin
     - Worker
     - Sets the port used to connect to the metadata server. SQream recommends using port ranges above 1024† because ports below 1024 are usually reserved, although there are no strict limitations. Any positive number (1 - 65535) can be used.
     - uint
     - ``3105``	 

   * - ``mtRead``
     - Admin
     - Regular
     - Splits large reads to multiple smaller ones and executes them concurrently.
     - boolean
     - ``FALSE``	 

   * - ``mtReadWorkers``
     - Admin
     - Regular
     - Sets the number of workers to handle smaller concurrent reads.
     - uint
     - ``30``	

   * - ``orcImplicitCasts``
     - Admin
     - Regular
     - Sets the implicit cast in orc files, such as **int** to **tinyint** and vice versa.
     - boolean
     - ``TRUE``	


   * - ``sessionTag``
     - Generic
     - Regular
     - Sets the name of the session tag.
     - string
     - Any legal string
	 


   * - ``spoolMemoryGB``
     - Generic
     - Regular
     - Sets the amount of memory (GB) to be used by the server for spooling.
     - uint
     - ``8``


   * - ``statementLockTimeout``
     - Admin
     - Regular
     - Sets the timeout (seconds) for acquiring object locks before executing statements.
     - uint
     - ``3``	

   * - ``useConfigIP``
     - Admin
     - Worker
     - Activates the machineIP (true). Setting to false ignores the machineIP and automatically assigns a local network IP. This cannot be activated in a cloud scenario (on-premises only).
     - boolean
     - ``FALSE``

   * - ``useLegacyDecimalLiterals``
     - Admin
     - Regular
     - Interprets decimal literals as **Double** instead of **Numeric**. Used to preserve legacy behavior in existing customers.
     - boolean
     - ``FALSE``

   * - ``useLegacyStringLiterals``
     - Admin
     - Regular
     - Interprets ASCII-only strings as **VARCHAR** instead of **TEXT**. Used to preserve legacy behavior in existing customers.
     - boolean
     - ``FALSE``


	 
	 

	 



   * - ``blockNewVarcharObjects``
     - Admin
     - Regular
     - Disables the creation of new tables, views, external tables containing Varchar columns, and the creation of user-defined functions with Varchar arguments or a Varchar return value.
     - boolean
     - ``FALSE``