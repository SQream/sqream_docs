.. _current_configuration_method:

**************************
Configuring SQream
**************************
The **Configuring SQream** page describes SQream’s method for configuring your instance of SQream and includes the following topics:

.. contents:: 
   :local:
   :depth: 1

Overview
-----
Modifications that you make to your configurations are persistent based on whether they are made at the session or cluster level. Persistent configurations are modifications made to attributes that are retained after shutting down your system.

Modifying Your Configuration
----
The **Modifying Your Configuration** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Modifying Your Configuration Using the Worker Configuration File
~~~~~~~~~~~
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
~~~~~~~~~~~
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
	 
Session vs Cluster Based Configuration
==============================
.. contents:: 
   :local:
   :depth: 1
   
Cluster-Based Configuration
--------------
SQream uses cluster-based configuration, enabling you to centralize configurations for all workers on the cluster. Only flags set to the regular or cluster flag type have access to cluster-based configuration. Configurations made on the cluster level are persistent and stored at the metadata level. The parameter settings in this file are applied globally to all workers connected to it.

For more information, see the following:

* `Using SQream SQL <https://docs.sqream.com/en/v2020-1/reference/cli/sqream_sql.html#using-sqream-sql>`_ - modifying flag attributes from the CLI.
* `SQream Acceleration Studio <https://docs.sqream.com/en/v2020-1/guides/operations/sqream_studio_5.4.0.html>`_ - modifying flag attributes from Studio.

For more information on flag-based access to cluster-based configuration, see **Configuration Flag Types** below.

Session-Based Configuration
----------------
Session-based configurations are not persistent and are deleted when your session ends. This method enables you to modify all required configurations while avoiding conflicts between flag attributes modified on different devices at different points in time.

The **SET flag_name** command is used to modify flag attributes. Any modifications you make with the **SET flag_name** command apply only to your open session, and are not saved when it ends

For example, when the query below has completed executing, the values configured will be restored to its previous setting: 

.. code-block:: console
   
   set spoolMemoryGB=700;
   select * from table a where date='2021-11-11'

For more information, see the following:

* `Using SQream SQL <https://docs.sqream.com/en/v2020-1/reference/cli/sqream_sql.html#using-sqream-sql>`_ - modifying flag attributes from the CLI.
* `SQream Acceleration Studio <https://docs.sqream.com/en/v2020-1/guides/operations/sqream_studio_5.4.0.html>`_ - modifying flag attributes from Studio.

Configuration Flag Types
==========
The flag type attribute can be set for each flag and determines its write access as follows:

* **Administration:** session-based read/write flags that can be stored in the metadata file.
* **Cluster:** global cluster-based read/write flags that can be stored in the metadata file.
* **Worker:** single worker-based read-only flags that can be stored in the worker configuration file.

The flag type determines which files can be accessed and which commands or commands sets users can run.

The following table describes the file or command modification rights for each flag type:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1
   
   * - **Flag Type**
     - **Legacy Configuration File**
     - **ALTER SYSTEM SET**
     - **Worker Configuration File**
   * - :ref:`Regular<regular_flag_types>`
     - Can modify
     - Can modify
     - Cannot modify
   * - :ref:`Cluster<cluster_flag_types>`
     - Cannot modify
     - Can modify
     - Cannot modify
   * - :ref:`Worker<worker_flag_types>`
     - Cannot modify
     - Cannot modify
     - Can modify

.. _regular_flag_types:

Regular Flag Types
---------------------
The following is an example of the correct syntax for running a **Regular** flag type command:

.. code-block:: console
   
   SET spoolMemoryGB= 11;
   executed
   
The following table describes the Regular flag types:

.. list-table::
   :widths: 2 5 10
   :header-rows: 1
   
   * - **Command**
     - **Description**
     - **Example**
   * - ``SET <flag_name>``
     - Used for modifying flag attributes.
     - ``SET developerMode=true``
   * - ``SHOW <flag-name> / ALL``
     - Used to preset either a specific flag value or all flag values.
     - ``SHOW <heartbeatInterval>``
   * - ``SHOW ALL LIKE``
     - Used as a wildcard character for flag names.
     - ``SHOW <heartbeat*>``
   * - ``show_conf_UF``
     - Used to print all flags with the following attributes:
	 	 
	   * Flag name
	   * Default value
	   * Is developer mode (Boolean)
	   * Flag category
	   * Flag type
     - ``rechunkThreshold,90,true,RND,regular``
   * - ``show_conf_extended UF``
     - Used to print all information output by the show_conf UF command, in addition to description, usage, data type, default value and range.
     - ``compilerGetsOnlyUFs,false,generic,regular,Makes runtime pass to compiler only``
	   ``utility functions names,boolean,true,false``
   * - ``show_md_flag UF``
     - Used to show a specific flag/all flags stored in the metadata file.
     - 	 	 
	   * Example 1: ``* master=> ALTER SYSTEM SET heartbeatTimeout=111;``
	   * Example 2: ``* master=> select show_md_flag(‘all’); heartbeatTimeout,111``
	   * Example 3: ``* master=> select show_md_flag(‘heartbeatTimeout’); heartbeatTimeout,111``

.. _cluster_flag_types:

Cluster Flag Types
---------------------
The following is an example of the correct syntax for running a **Cluster** flag type command:

.. code-block:: console
   
   ALTER SYSTEM RESET useMetadataServer;
   executed
   
The following table describes the Cluster flag types:

.. list-table::
   :widths: 1 5 10
   :header-rows: 1
   
   * - **Command**
     - **Description**
     - **Example**
   * - ``ALTER SYSTEM SET <flag-name>``
     - Used to storing or modifying flag attributes in the metadata file.
     - ``ALTER SYSTEM SET <heartbeatInterval=12;>``
   * - ``ALTER SYSTEM RESET <flag-name / ALL>``
     - Used to remove a flag or all flag attributes from the metadata file.
     - ``ALTER SYSTEM RESET <heartbeatInterval ALTER SYSTEM RESET ALL>``
   * - ``SHOW <flag-name> / ALL``
     - Used to print the value of a specified value or all flag values.
     - ``SHOW <heartbeatInterval>``
   * - ``SHOW ALL LIKE``
     - Used as a wildcard character for flag names.
     - ``SHOW <heartbeat*>``
   * - ``show_conf_UF``
     - Used to print all flags with the following attributes:
	 	 
	   * Flag name
	   * Default value
	   * Is developer mode (Boolean)
	   * Flag category
	   * Flag type
     - ``rechunkThreshold,90,true,RND,regular``
   * - ``show_conf_extended UF``
     - Used to print all information output by the show_conf UF command, in addition to description, usage, data type, default value and range.
     - ``compilerGetsOnlyUFs,false,generic,regular,Makes runtime pass to compiler only``
	     ``utility functions names,boolean,true,false``
   * - ``show_md_flag UF``
     - Used to show a specific flag/all flags stored in the metadata file.
     - 	 	 
	   * Example 1: ``* master=> ALTER SYSTEM SET heartbeatTimeout=111;``
	   * Example 2: ``* master=> select show_md_flag(‘all’); heartbeatTimeout,111``
	   * Example 3: ``* master=> select show_md_flag(‘heartbeatTimeout’); heartbeatTimeout,111``

.. _worker_flag_types:

Worker Flag Types
---------------------
The following is an example of the correct syntax for running a **Worker** flag type command:

.. code-block:: console
   
   SHOW spoolMemoryGB;
   
The following table describes the Worker flag types:

.. list-table::
   :widths: 1 5 10
   :header-rows: 1
   
   * - **Command**
     - **Description**
     - **Example**
   * - ``ALTER SYSTEM SET <flag-name>``
     - Used to storing or modifying flag attributes in the metadata file.
     - ``ALTER SYSTEM SET <heartbeatInterval=12;>``
   * - ``ALTER SYSTEM RESET <flag-name / ALL>``
     - Used to remove a flag or all flag attributes from the metadata file.
     - ``ALTER SYSTEM RESET <heartbeatInterval ALTER SYSTEM RESET ALL>``
   * - ``SHOW <flag-name> / ALL``
     - Used to print the value of a specified value or all flag values.
     - ``SHOW <heartbeatInterval>``
   * - ``SHOW ALL LIKE``
     - Used as a wildcard character for flag names.
     - ``SHOW <heartbeat*>``
   * - ``show_conf_UF``
     - Used to print all flags with the following attributes:
	 	 
	   * Flag name
	   * Default value
	   * Is developer mode (Boolean)
	   * Flag category
	   * Flag type
     - ``rechunkThreshold,90,true,RND,regular``
   * - ``show_conf_extended UF``
     - Used to print all information output by the show_conf UF command, in addition to description, usage, data type, default value and range.
     - 
	   ``compilerGetsOnlyUFs,false,generic,regular,Makes runtime pass to compiler only``
	   ``utility functions names,boolean,true,false``
   * - ``show_md_flag UF``
     - Used to show a specific flag/all flags stored in the metadata file.
     - 	 	 
	   * Example 1: ``* master=> ALTER SYSTEM SET heartbeatTimeout=111;``
	   * Example 2: ``* master=> select show_md_flag(‘all’); heartbeatTimeout,111``
	   * Example 3: ``* master=> select show_md_flag(‘heartbeatTimeout’); heartbeatTimeout,111``


All Configurations
---------------------
The following table describes the **Generic** and **Administration** configuration flags:

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
     - Administration
     - Regular
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - string
     - 
	   ``16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,``	   
	   ``131072,262144,524288,1048576,2097152,4194304,8388608,16777216,``
	   ``33554432,67108864,134217728,268435456,536870912,786432000,107374,``
	   ``1824,1342177280,1610612736,1879048192,2147483648,2415919104,``
	   ``2684354560,2952790016,3221225472``
	   
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
	 
   * - ``cacheEvictionMilliseconds``
     - Generic
     - Regular
     - Sets how long the cache stores contents before being flushed.
     - size_t
     - ``2000``
	 
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
     - Administration
     - Regular
     - Sets the pad device memory allocations with safety buffers to catch out-of-bounds writes.
     - boolean
     - ``FALSE``

   * - ``compilerGetsOnlyUFs``
     - Administration
     - Regular
     - Sets the runtime to pass only utility functions names to the compiler.
     - boolean
     - ``FALSE``
	 
   * - ``copyToRestrictUtf8``
     - Administration
     - Regular
     - Sets the custom bin size in the cache to enable high granularity bin control.
     - boolean
     - ``FALSE``	 
	 
   * - ``cpuReduceHashtableSize``
     - Administration
     - Regular
     - Sets the hash table size of the CpuReduce.
     - uint
     - ``10000``		 
	 
   * - ``csvLimitRowLength``
     - Administration
     - Cluster
     - Sets the maximum supported CSV row length.
     - uint
     - ``100000`` 
	 
   * - ``cudaMemcpyMaxSizeBytes``
     - Administration
     - Regular
     - Sets the chunk size for copying from CPU to GPU. If set to 0, do not divide.
     - uint
     - ``0`` 	 
	 
   * - ``CudaMemcpySynchronous``
     - Administration
     - Regular
     - Indicates if copying from/to GPU is synchronous.
     - boolean
     - ``FALSE`` 	 
	 
   * - ``cudaMemQuota``
     - Administration
     - Worker
     - Sets the percentage of total device memory to be used by the instance.
     - uint
     - ``90`` 	 
	 
   * - ``developerMode``
     - Administration
     - Regular
     - Enables modifying R&D flags.
     - boolean
     - ``FALSE`` 	 
	 
   * - ``enableDeviceDebugMessages``
     - Administration
     - Regular
     - Activates the Nvidia profiler (nvprof) markers.
     - boolean
     - ``FALSE`` 

   * - ``enableLogDebug``
     - Administration
     - Regular
     - Enables creating and logging in the clientLogger_debug file.
     - boolean
     - ``TRUE``

   * - ``enableNvprofMarkers``
     - Administration
     - Regular
     - Activates the Nvidia profiler (nvprof) markers.
     - boolean
     - ``FALSE``	 
	 
   * - ``endLogMessage``
     - Administration
     - Regular
     - Appends a string at the end of every log line.
     - string
     - ``EOM`` 
	 
	 


 

	 
	 
   * - ``extentStorageFileSizeMB``
     - Administration
     - Cluster
     - Sets the minimum size in mebibytes of extents for table bulk data.
     - uint
     - ``20``
	 
   * - ``flipJoinOrder``
     - Generic
     - Regular
     - Reorders join to force equijoins and/or equijoins sorted by table size.
     - boolean
     - ``FALSE``


	 
   * - ``gatherMemStat``
     - Administration
     - Regular
     - Monitors all pinned allocations and all **memcopies** to/from device, and prints a report of pinned allocations that were not memcopied to/from the device using the **dump_pinned_misses** utility function.
     - boolean
     - ``FALSE``	 
	 
   * - ``increaseChunkSizeBeforeReduce``
     - Administration
     - Regular
     - Increases the chunk size to reduce query speed.
     - boolean
     - ``FALSE``		 
	 
   * - ``increaseMemFactors``
     - Administration
     - Regular
     - Adds rechunker before expensive chunk producer.
     - boolean
     - ``TRUE``	 
	 
   * - ``leveldbWriteBufferSize``
     - Administration
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
     - Administration
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
	 	 
	 
   * - ``memoryResetTriggerMB``
     - Administration
     - Regular
     - Sets the size of memory used during a query to trigger aborting the server.
     - uint
     - ``0``		 
 
   * - ``metadataServerPort``
     - Administration
     - Worker
     - Sets the port used to connect to the metadata server. SQream recommends using port ranges above 1024† because ports below 1024 are usually reserved, although there are no strict limitations. Any positive number (1 - 65535) can be used.
     - uint
     - ``3105``	 

   * - ``mtRead``
     - Administration
     - Regular
     - Splits large reads to multiple smaller ones and executes them concurrently.
     - boolean
     - ``FALSE``	 

   * - ``mtReadWorkers``
     - Administration
     - Regular
     - Sets the number of workers to handle smaller concurrent reads.
     - uint
     - ``30``	

   * - ``orcImplicitCasts``
     - Administration
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
     - Administration
     - Regular
     - Sets the timeout (seconds) for acquiring object locks before executing statements.
     - uint
     - ``3``
	 

   * - ``useConfigIP``
     - Administration
     - Worker
     - Activates the machineIP (true). Setting to false ignores the machineIP and automatically assigns a local network IP. This cannot be activated in a cloud scenario (on-premises only).
     - boolean
     - ``FALSE``

   * - ``useLegacyDecimalLiterals``
     - Administration
     - Regular
     - Interprets decimal literals as **Double** instead of **Numeric**. Used to preserve legacy behavior in existing customers.
     - boolean
     - ``FALSE``

   * - ``useLegacyStringLiterals``
     - Administration
     - Regular
     - Interprets ASCII-only strings as **VARCHAR** instead of **TEXT**. Used to preserve legacy behavior in existing customers.
     - boolean
     - ``FALSE``
	 
   * - ``varcharIdentifiers``
     - Administration
     - Regular
     - Activates using varchar as an identifier.
     - boolean
     - ``true``

Configuration Commands
~~~~~~~~~~~~~~~	 
The configuration commands are associated with particular flag types based on permissions.

The following table describes the commands or command sets that can be run based on their flag type. Note that the flag names described in the following table are described in the :ref:`Configuration Roles<configuration_roles>` section below.

.. list-table::
   :header-rows: 1
   :widths: 1 2 10 17
   :class: my-class
   :name: my-name

   * - Flag Type
     - Command
     - Description
     - Example
   * - Regular
     - ``SET <flag_name>``
     - Used for modifying flag attributes.
     - ``SET developerMode=true``
   * - Cluster
     - ``ALTER SYSTEM SET <flag-name>``
     - Used to storing or modifying flag attributes in the metadata file.
     - ``ALTER SYSTEM SET <heartbeatInterval=12;>``
   * - Cluster
     - ``ALTER SYSTEM RESET <flag-name / ALL>``
     - Used to remove a flag or all flag attributes from the metadata file.
     - ``ALTER SYSTEM RESET <heartbeatInterval ALTER SYSTEM RESET ALL>``
   * - Regular, Cluster, Worker
     - ``SHOW <flag-name> / ALL``
     - Used to print the value of a specified value or all flag values.
     - ``SHOW <heartbeatInterval>``
   * - Regular, Cluster, Worker
     - ``SHOW ALL LIKE``
     - Used as a wildcard character for flag names.
     - ``SHOW <heartbeat*>``
   * - Regular, Cluster, Worker
     - ``show_conf_UF``
     - Used to print all flags with the following attributes:
	 
       * Flag name
       * Default value
       * Is developer mode (Boolean)
       * Flag category
       * Flag type
	 

	   
     - ``rechunkThreshold,90,true,RND,regular``
   * - Regular, Cluster, Worker
     - ``show_conf_extended UF``
     - Used to print all information output by the show_conf UF command, in addition to description, usage, data type, default value and range.
     - ``spoolMemoryGB,15,false,generic,regular,Amount of memory (GB)``
       ``the server can use for spooling,”Statement that perform “”group by””,``
       ``“”order by”” or “”join”” operation(s) on large set of data will run``
       ``much faster if given enough spool memory, otherwise disk spooling will``
       ``be used resulting in performance hit.”,uint,,0-5000``
   * - Regular, Cluster, Worker
     - ``show_md_flag UF``
     - Used to show a specific flag/all flags stored in the metadata file.
     - 	 	 
	   * Example 1: ``* master=> ALTER SYSTEM SET heartbeatTimeout=111;``
	   * Example 2: ``* master=> select show_md_flag(‘all’); heartbeatTimeout,111``
	   * Example 3: ``* master=> select show_md_flag(‘heartbeatTimeout’); heartbeatTimeout,111``




.. _configuration_roles:

Configuration Roles
~~~~~~~~~~~~~~~
SQream divides flags into the following roles, each with their own set of permissions:


* `Administration flags <https://docs.sqream.com/en/v2020-1/configuration_guides/admin_flags.html>`_: can be modified by administrators on a session and cluster basis using the ``ALTER SYSTEM SET`` command.
* `Generic flags <https://docs.sqream.com/en/v2020-1/configuration_guides/generic_flags.html>`_: can be modified by standard users on a session basis.

Showing All Flags in the Catalog Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SQream uses the **sqream_catalog.parameters** catalog table for showing all flags, providing the scope (default, cluster and session), description, default value and actual value.

The following is the correct syntax for a catalog table query:

.. code-block:: console
   
   SELECT * FROM sqream_catalog.settings

The following is an example of a catalog table query:

.. code-block:: console
   
   externalTableBlobEstimate, 100, 100, default,
   textEncoding, ascii, ascii, default, Changes the expected encoding for text columns
   useCrcForTextJoinKeys, true, true, default,
   hiveStyleImplicitStringCasts, false, false, default,

This guide covers the configuration files and the ``SET`` statement.