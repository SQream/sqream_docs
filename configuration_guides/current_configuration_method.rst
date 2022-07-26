.. _current_configuration_method:

**************************
Configuring SQream
**************************
The **Configuring SQream** page describes how to configure your instance of SQream and includes the following topics:

.. contents:: 
   :local:
   :depth: 1

Configuration Levels
===========
SQream's configuration parameters are based on the following hierarchy:

.. contents:: 
   :local:
   :depth: 1

Cluster-Based Configuration
--------------
Cluster-based configuration lets you centralize configurations for all workers on the cluster. Only flags set to the regular or cluster flag type have access to cluster-based configuration. Configurations made on the cluster level are persistent and stored at the metadata level. The parameter settings in this file are applied globally to all workers connected to it.

.. note:: While cluster-based configuration was designed for configuring Workers, you can only configure Worker values set to the Regular or Cluster type.

Worker-Based Configuration
--------------
**Comment** - *Need to populate.*

Session-Based Configuration
--------------
Session-based configurations are not persistent and are deleted when your session ends. This method enables you to modify all required configurations while avoiding conflicts between flag attributes modified on different devices at different points in time. The **SET flag_name** command is used to modify flag values on the session level. Any modifications you make with the **SET flag_name** command apply only to your open session, and are not saved when it ends.

For example, when the query below has completed executing, the values configured will be restored to its previous setting: 

.. code-block:: console
   
   set spoolMemoryGB=700;
   select * from table a where date='2021-11-11'
   
Flag Types
===========
SQream uses three flag types, **Cluster**, **Worker**, and **Regular**. Each of these flag types is associated with one of three hierarchical configuration levels described earlier, making it easier to configure your system.

The highest level in the hierarchy is Cluster, which lets you set configurations across all workers in a given cluster. Modifying cluster values is **persistent**, meaning that any configurations you set are retained after shutting down your system. Configurations set at the Cluster level take the highest priority and override settings made on the Regular and Worker level **Comment** - *Confirm*. This is known as **cluster-based configuration**. Note that Cluster-based configuration lets you modify Cluster *and* Regular flag types. An example of a Cluster flag is **persisting your cache directory.**

The second level is Worker, which lets you configure individual workers. Modifying Worker values are also **persistent**. This is known as **worker-based configuration**. Some examples of Worker flags includes **setting total device memory usage** and **setting metadata server connection port**.

The lowest level is Regular, which means that modifying values of Regular flags affects only your current session and are not persistent. This means that they are automatically restored to their default value when the session ends. This is known as **session-based configuration**. Some examples of Regular flags includes **setting your bin size** and **setting CUDA memory**.

To see each flag's default value, see one of the following:

* The **Default Value** column in the :ref:`All Configurations<all_configurations>` section.

   ::
   
* The flag's individual description page, such as :ref:`Setting CUDA Memory<check_cuda_memory>`.

Configuration Roles
===========
SQream divides flags into the following roles, each with their own set of permissions:

* :ref:`admin_flags` - can be modified by administrators on a session and cluster basis using the ``ALTER SYSTEM SET`` command: **Comment** - *I don't think we need to mention the command here, as it's described below, and also not mentioned for Generic Flags.*
   
   * Regular
   * Worker
   * Cluster
   
* :ref:`generic_flags` - can be modified by standard users on a session basis:

   * Regular
   * Worker

Modification Methods
==========
SQream provides two different ways to modify your configurations. The current method is based on hierarchical configuration as described above. This method is based on making modifications on the **worker configuration file**, while you can still make modifications using the previous method using the **legacy configuration file**, both described below:

.. contents:: 
   :local:
   :depth: 1

Modifying Your Configuration Using the Worker Configuration File
-------------------
You can modify your configuration using the **worker configuration file (config.json)**. Changes that you make to worker configuration files are persistent. Note that you can only set the attributes in your worker configuration file **before** initializing your SQream worker, and while your worker is active these attributes are read-only.

The following is an example of a worker configuration file:

.. code-block:: postgres
   
   {
       “cluster”: “/home/test_user/sqream_testing_temp/sqreamdb”,
       “gpu”:  0,
       “licensePath”: “home/test_user/SQream/tests/license.enc”,
       “machineIP”: “127.0.0.1”,
       “metadataServerIp”: “127.0.0.1”,
       “metadataServerPort”: “3105,
       “port”: 5000,
       “useConfigIP”” true,
       “legacyConfigFilePath”: “home/SQream_develop/SqrmRT/utils/json/legacy_congif.json”
   }

You can access the legacy configuration file from the ``legacyConfigFilePath`` parameter shown above. If all (or most) of your workers require the same flag settings, you can set the ``legacyConfigFilePath`` attribute to the same legacy file.

Modifying Your Configuration Using a Legacy Configuration File
---------------------
You can modify your configuration using a legacy configuration file.

The Legacy configuration file provides access to the read/write flags used in SQream’s previous configuration method. A link to this file is provided in the **legacyConfigFilePath** parameter in the worker configuration file.

The following is an example of the legacy configuration file:

.. code-block:: postgres
   
   {
      “developerMode”: true,
      “reextentUse”: false,
      “useClientLog”: true,
      “useMetadataServer”” false
   }
For more information on using the previous configuration method, see :ref:`previous_configuration_method`.

Configuring Your Parameter Values
==============================
The method you must use to configure your parameter values depends on the configuration level. Each configuration level has its own command or set of commands used to configure values, as shown below:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Configuration Level**                                                                                                                                                                                                                                                                                         |
+=================================================================================================================================================================================================================================================================================================================+
| **Regular, Worker, and Cluster**                                                                                                                                                                                                                                                                                |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Command**                                         | **Description**                                                                                                                           | **Example**                                                                                                   |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``SET <flag_name>``                                 | Used for modifying flag attributes.                                                                                                       | ``SET developerMode=true``                                                                                    |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``SHOW <flag-name> / ALL``                          | Used to preset either a specific flag value or all flag values.                                                                           | ``SHOW <heartbeatInterval>``                                                                                  |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``SHOW ALL LIKE``                                   | Used as a wildcard character for flag names.                                                                                              | ``SHOW <heartbeat*>``                                                                                         |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``show_conf_UF``                                    | Used to print all flags with the following attributes:                                                                                    | ``rechunkThreshold,90,true,RND,regular``                                                                      |
|                                                     |                                                                                                                                           |                                                                                                               |
|                                                     | * Flag name                                                                                                                               |                                                                                                               |
|                                                     | * Default value                                                                                                                           |                                                                                                               |
|                                                     | * Is Developer Mode (Boolean)                                                                                                             |                                                                                                               |
|                                                     | * Flag category                                                                                                                           |                                                                                                               |
|                                                     | * Flag type                                                                                                                               |                                                                                                               |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``show_conf_extended UF``                           | Used to print all information output by the show_conf UF command, in addition to description, usage, data type, default value and range.  | ``rechunkThreshold,90,true,RND,regular``                                                                      |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``show_md_flag UF``                                 | Used to show a specific flag/all flags stored in the metadata file.                                                                       |* Example 1: ``* master=> ALTER SYSTEM SET heartbeatTimeout=111;``                                             |
|                                                     |                                                                                                                                           |* Example 2: ``* master=> select show_md_flag(‘all’); heartbeatTimeout,111``                                   |
|                                                     |                                                                                                                                           |* Example 3: ``* master=> select show_md_flag(‘heartbeatTimeout’); heartbeatTimeout,111``                      |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Worker and Cluster**                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``ALTER SYSTEM SET <flag-name>``                    | Used for storing or modifying flag attributes in the metadata file.                                                                       |  ``ALTER SYSTEM SET <heartbeatInterval=12;>``                                                                 |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``ALTER SYSTEM RESET <flag-name / ALL>``            | Used to remove a flag or all flag attributes from the metadata file.                                                                      |  ``ALTER SYSTEM RESET <heartbeatInterval ALTER SYSTEM RESET ALL>``                                            |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

Command Examples
==========
This section includes the following command examples:

.. contents:: 
   :local:
   :depth: 1
   
Running a Regular Flag Type Command
---------------------
The following is an example of running a **Regular** flag type command:

.. code-block:: console
   
   SET spoolMemoryGB= 11;
   executed
   
Running a Worker Flag Type Command
---------------------
The following is an example of running a **Worker** flag type command:

.. code-block:: console
   
   SHOW spoolMemoryGB;

Running a Cluster Flag Type Command
---------------------
The following is an example of running a **Cluster** flag type command:

.. code-block:: console
   
   ALTER SYSTEM RESET useMetadataServer;
   executed

Showing All Flags in the Catalog Table
=======
SQream uses the **sqream_catalog.parameters** catalog table for showing all flags, providing the scope (default, cluster and session), description, default value and actual value.

The following is the correct syntax for a catalog table query:

.. code-block:: console
   
   SELECT * FROM sqream_catalog.settings

The following is an example of a catalog table query:

.. code-block:: console
   
   externalTableBlobEstimate, 100, 100, default,
   varcharEncoding, ascii, ascii, default, Changes the expected encoding for Varchar columns
   useCrcForTextJoinKeys, true, true, default,
   hiveStyleImplicitStringCasts, false, false, default,

.. _all_configurations:

All Configurations
================
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
	 
	 

   * - ``varcharIdentifiers``
     - Admin
     - Regular
     - Activates using varchar as an identifier.
     - boolean
     - ``true`` 

	 
	 
   * - ``extentStorageFileSizeMB``
     - Admin
     - Cluster
     - Sets the minimum size in mebibytes of extents for table bulk data.
     - uint
     - ``20``	 
	 
   * - ``gatherMemStat``
     - Admin
     - Regular
     - Monitors all pinned allocations and all **memcopies** to/from device, and prints a report of pinned allocations that were not memcopied to/from the device using the **dump_pinned_misses** utility function.
     - boolean
     - ``FALSE``	 
	 
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
	 
   * - ``leveldbWriteBufferSize``
     - Admin
     - Regular
     - Sets the buffer size.
     - uint
     - ``524288``	 	 
	 
   * - ``machineIP``
     - Admin
     - Worker
     - Manual setting of reported IP.
     - string
     - ``127.0.0.1``		 
	 

	 
	 
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

   * - ``flipJoinOrder``
     - Generic
     - Regular
     - Reorders join to force equijoins and/or equijoins sorted by table size.
     - boolean
     - ``FALSE``

   * - ``limitQueryMemoryGB``
     - Generic
     - Worker
     - Prevents a query from processing more memory than the flag’s value.
     - uint
     - ``100000``
	 
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

   * - ``maxAvgBlobSizeToCompressOnGpu``
     - Generic
     - Regular
     - Sets the CPU to compress columns with size above (flag’s value) * (row count).
     - uint
     - ``120``
	 

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