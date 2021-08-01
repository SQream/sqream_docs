.. _configuration:

***********************
Configuration
***********************

This guide covers the configuration files and the ``SET`` statement.

Configuration Files
==========================

By default, configuration files are stored in ``/etc/sqream``.

A very minimal configuration file looks like this:

.. code-block:: json

   {
       "compileFlags": {
       },
       "runtimeFlags": {
       },
       "runtimeGlobalFlags": {
       },
       "server": {
           "gpu": 0,
           "port": 5000,
           "cluster": "/home/sqream/sqream_storage",
           "licensePath": "/etc/sqream/license.enc"
       }
   }

* Each SQream DB worker (``sqreamd``) has a dedicated configuration file. 

* The configuration file contains four distinct sections, ``compileFlags``, ``runtimeFlags``, ``runtimeGlobalFlags``, and ``server``.

In the example above, the worker will start on port 5000, and will use GPU #0.

Frequently Set Parameters
============================

.. todo
    list-table:: Compiler Flags
      :widths: auto
      :header-rows: 1
      
      * - Name
        - Section
        - Description
        - Default
        - Value range
        - Example
      * -
        -
        -
        -
        -
        -

.. list-table:: Server Flags
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Section
     - Description
     - Default
     - Value range
     - Example
   * - ``gpu``
     - ``server``
     - Controls the GPU ordinal to use
     - ✗
     - 0 to (number of GPUs in the machine -1). Check with ``nvidia-smi -L``
     - ``"gpu": 0``
   * - ``port``
     - ``server``
     - Controls the TCP port to listen on
     - ✗
     - 1024 to 65535
     - ``"port" : 5000``
   * - ``ssl_port``
     - ``server``
     - Controls the SSL TCP port to listen on. Must be different from ``port``
     - ✗
     - 1024 to 65535
     - ``"ssl_port" : 5100``
   * - ``cluster``
     - ``server``
     - Specifies the cluster path root
     - ✗
     - Valid local system path
     - ``"cluster" : "/home/sqream/sqream_storage"``
   * - ``license_path``
     - ``server``
     - Specifies the license file for this worker
     - ✗
     - Valid local system path to license file
     - ``"license_path" : "/etc/sqream/license.enc"``

.. list-table:: Runtime Global Flags
   :widths: 10 22 16 10 22 16
   :header-rows: 1
   
   * - Name
     - Section
     - Description
     - Default
     - Value range
     - Example
   * - ``spoolMemoryGb``
     - ``runtimeGlobalFlags``
     - Modifies RAM allocated for the worker for intermediate results. Statements that use more memory than this setting will spool to disk, which could degrade performance. We recommend not to exceed the amount of RAM in the machine. This setting must be set lower than the ``limitQueryMemoryGB`` setting.
     - ``128``
     - 1 to maximum available RAM in gigabytes. 
     - ``"spoolMemoryGb": 250``
   * - ``WriteToFileThreads``
     - ``runtimeGlobalFlags``
     - Configures the number of threads in the **WriteToFile** function
     - ``16``
     -  
     - 
   * - ``limitQueryMemoryGB``
     - ``runtimeGlobalFlags``
     - Modifies the maximum amount of RAM allocated for a query. The recommended value for this is ``total host memory`` / ``sqreamd workers on host``. For example, for a machine with 512GB of RAM and 4 workers, the recommended setting is ``512/4 → 128``.
     - ``10000``
     - ``1`` to ``10000``
     - ``"limitQueryMemoryGB" : 128``
   * - ``cudaMemQuota``
     - ``runtimeGlobalFlags``
     - Modifies the maximum amount of GPU RAM allocated for a worker. The recommended value is 99% for a GPU with a single worker, or 49% for a GPU with two workers.
     - ``90`` %
     - ``1`` to ``99``
     - ``"cudaMemQuota" : 99``
   * - ``showFullExceptionInfo``
     - ``runtimeGlobalFlags``
     - Shows complete error message with debug information. Use this for debugging.
     - ``false``
     - ``true`` or ``false``
     - ``"showFullExceptionInfo" : true``
   * - ``initialSubscribedServices``
     - ``runtimeGlobalFlags``
     - Comma separated list of :ref:`service queues<workload_manager>` that the worker is subscribed to
     - ``"sqream"``
     - Comma separated list of service names, with no spaces. Services that don't exist will be created.
     - ``"initialSubscribedServices": "sqream,etl,management"``
   * - ``logClientLevel``
     - ``runtimeGlobalFlags``
     - Used to control which log level should appear in the logs
     - ``4`` (``INFO``)
     - ``0`` SYSTEM (lowest) - ``4`` INFO (highest). See :ref:`information level table<information_level>` for explanation about these log levels.
     - ``"logClientLevel" : 3``
   * - ``nodeInfoLoggingSec``
     - ``runtimeGlobalFlags``
     - Sets an interval for automatically logging long-running statements' :ref:`show_node_info` output. Output is written as a message type ``200``.
     - ``60`` (every minute)  
     - Positive whole number >=1.
     - ``"nodeInfoLoggingSec" : 5``
   * - ``useLogMaxFileSize``
     - ``runtimeGlobalFlags``
     - Defines whether SQream logs should be cycled when they reach ``logMaxFileSizeMB`` size. When ``true``, set the ``logMaxFileSizeMB`` accordingly.
     - ``false``
     - ``false`` or ``true``
     - ``"useLogMaxFileSize" : true``
   * - ``logMaxFileSizeMB``
     - ``runtimeGlobalFlags``
     - Sets the size threshold in megabytes after which a new log file will be opened.
     - ``20``
     - ``1`` to ``1024`` (1MB to 1GB)
     - ``"logMaxFileSizeMB" : 250``
   * - ``logFileRotateTimeFrequency``
     - ``runtimeGlobalFlags``
     - Control frequency of log rotation
     - ``never``
     - ``daily``, ``weekly``, ``monthly``, ``never``
     - ``"logClientLevel" : 3``
   * - ``useMetadataServer``
     - ``runtimeGlobalFlags``
     - Specifies if this worker connects to a cluster (``true``) or is standalone (``false``). If set to ``true``, also set ``metadataServerIp``
     - ``true``
     - ``false`` or ``true``
     - ``"useMetadataServer" : true``
   * - ``metadataServerIp``
     - ``runtimeGlobalFlags``
     - Specifies the hostname or IP of the metadata server, when ``useMetadataServer`` is set to ``true``.
     - ``127.0.0.1``
     - A valid IP or hostname
     - ``"metadataServerIp": "127.0.0.1"``
   * - ``useConfigIP``
     - ``runtimeGlobalFlags``
     - Specifies if the metadata should use a pre-determined hostname or IP to refer to this worker. If set to ``true``, set the ``machineIp`` configuration accordingly.
     - ``false`` - automatically derived by the TCP socket
     - ``false`` or ``true``
     - ``"useConfigIP" : true``
   * - ``machineIP``
     - ``runtimeGlobalFlags``
     - Specifies the worker's external IP or hostname, when used from a remote network.
     - No default
     - A valid IP or hostname
     - ``"machineIP": "10.0.1.4"``
   * - ``tempPath``
     - ``runtimeGlobalFlags``
     - Specifies an override for the temporary file path on the local machine. Set this to a local path to improve performance for spooling.
     - Defaults to the central storage's built-in temporary folder
     - A valid path to a folder on the local machine
     - ``"tempPath": "/mnt/nvme0/temp"``



.. list-table:: Runtime Flags
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Section
     - Description
     - Default
     - Value range
     - Example
   * - ``insertParsers``
     - ``runtimeFlags``
     - Sets the number of CSV parsing threads launched during bulk load
     - 4
     - 1 to 32
     - ``"insertParsers" : 8``
   * - ``insertCompressors``
     - ``runtimeFlags``
     - Sets the number of compressor threads launched during bulk load
     - 4
     - 1 to 32
     - ``"insertCompressors" : 8``
   * - ``statementLockTimeout``
     - ``runtimeGlobalFlags``
     - Sets the delay in seconds before SQream DB will stop waiting for a lock and return an error
     - 3
     - >=1
     - ``"statementLockTimeout" : 10``


.. list the main configuration options and how they are used

.. point to the best practices as well

.. warning:: JSON files can't contain any comments

Recommended On-Premises Configuration File
=====================================
The following is the recommended on-premises configuration file:

.. code-block::  json

   { 
      "compileFlags":{ 
      },
      "runtimeFlags":{ 
         "insertParsers": 16,
         "insertCompressors": 8 
      },
      "runtimeGlobalFlags":{ 
         "limitQueryMemoryGB" : 121,
         "spoolMemoryGB" : 108,
         "cudaMemQuota": 90,
         "initialSubscribedServices" : "sqream",
         "useMetadataServer": true,
         "metadataServerIp": "127.0.0.1",
         "useConfigIP": false,
         "machineIP": "127.0.0.1"
      },
      "server":{ 
         "gpu":0,
         "port":5000,
         "ssl_port": 5100,
         "cluster":"/home/sqream/sqream_storage",
         "licensePath":"/etc/sqream/license.enc"
      }
   }
   
Recommended Cloud Configuration File
=====================================
The following is the recommended Cloud configuration file:

.. code-block::  json

   { 
      "compileFlags":{ 
      },
      "runtimeFlags":{ 
         "insertParsers": 16,
         "insertCompressors": 8 
      },
      "runtimeGlobalFlags":{ 
         "limitQueryMemoryGB" : 121,
         "spoolMemoryGB" : 108,
         "cudaMemQuota": 90,
         "initialSubscribedServices" : "sqream",
         "useMetadataServer": true,
         "metadataServerIp": "127.0.0.1",
         "useConfigIP": true,
         "machineIP": "127.0.0.1"
      },
      "server":{ 
         "gpu":0,
         "port":5000,
         "ssl_port": 5100,
         "cluster":"/home/sqream/sqream_storage",
         "licensePath":"/etc/sqream/license.enc"
      }
   }


.. note:: When setting your Cloud configuration, you must provide your public IP for the ``machineIP`` parameter.


Changing Settings Temporarily
===================================

The ``SET`` statement can modify one of the configuration settings for the session or connection.

For example, to set the query plan's logging interval to "every 3 seconds" for subsequent statements:

.. code-block:: psql
   
   t=> SET nodeInfoLoggingSec=3; SELECT * FROM nba;
