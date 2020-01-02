.. _configuration:

***********************
Configuration
***********************

SQream DB has configuration files to modify the system's default behaviour.

Configuration files
==========================

By default, configuration files are stored in ``/etc/sqream``.

A very basic configuration file looks like this:

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

Each SQream DB worker has a dedicated configuration file. 

The configuration file contains four distinct sections, ``compileFlags``, ``runtimeFlags``, ``runtimeGlobalFlags``, and ``server``.

In the example above, the worker will start on port 5000, and will use GPU #0.

Frequently set parameters
============================

.. list-table:: Log fields
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
   * - ``spoolMemoryGb``
     - ``runtimeGlobalFlags``
     - Modifies RAM allocated for the worker for intermediate results. Statements that use more memory will spool to disk. We recommend not to exceed the amount of RAM in the machine.
     - ``128``
     - 1 to maximum available RAM in gigabytes
     - ``"spoolMemoryGb": 250``
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
   * - ``useLogMaxFileSize``
     - ``runtimeGlobalFlags``
     - Defines whether SQream logs should be cycled every logMaxFileSizeMB size
     - ``false``
     - ``false`` or ``true``
     - ``"useLogMaxFileSize" : true``
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
     - Rotate log files once they reach a certain file size. When ``true``, set the ``logMaxFileSizeMB`` accordingly.
     - ``false``
     - ``false`` or ``true``.
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

.. list the main configuration options and how they are used

.. point to the best practices as well

.. warning:: JSON files can't contain any comments

Recommended configuration file
=====================================

.. code-block::  json

   { 
      "compileFlags":{ 
      },
      "runtimeFlags":{ 
         "insertParsers": 16, 
         "insertCompressors": 16 
      },
      "runtimeGlobalFlags":{ 
         "spoolMemoryGB": 250, 
         "initialSubscribedServices" : "sqream"
      },
      "server":{ 
         "gpu":0,
         "port":5000,
         "ssl_port": 5100,
         "cluster":"/home/sqream/sqream_storage",
         "licensePath":"/etc/sqream/license.enc"
      }
   }
   
Changing settings temporarily
===================================

The ``SET`` statement can modify one of the configuration settings for the session or connection.

For example:

.. code-block:: psql
   
   t=> SET nodeInfoLoggingSec=3; SELECT * FROM nba;