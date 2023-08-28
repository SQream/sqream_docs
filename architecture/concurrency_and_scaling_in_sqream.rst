.. _concurrency_and_scaling_in_sqream:

******
Sizing 
******

Concurrency and Scaling in SQreamDB
===================================

A SQreamDB cluster can execute one statement per worker process while also supporting the concurrent operation of multiple workers. Utility functions with minimal resource requirements, such as :ref:`show_server_status`, :ref:`show_locks`, and :ref:`show_node_info` will be executed regardless of the workload.

Minimum Resource Required Per Worker:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Component
     - CPU Cores
     - RAM (GB)
     - Local Storage (GB)
   * - Worker
     - 8
     - 128
     - 10	 
   * - Metadata Server
     - 16 cores per 100 Workers
     - 20 GB RAM for every 1 trillion rows
     - 	10 
   * - SqreamDB Acceleration Studio
     - 16
     - 16
     - 	50
   * - Server Picker
     - 1
     - 2
     - 	

 
Lightweight queries, such as :ref:`copy_to` and :ref:`Clean-Up<delete_guide>` require 64 RAM (GB).	  

Maximum Workers Per GPU:
	 
.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - GPU
     - Workers
   * - NVIDIA Tesla T4 (16GB) 
     - 1
   * - NVIDIA Tesla V100 (32GB)
     - 2
   * - NVIDIA Tesla A100 (40GB)	
     - 3
   * - NVIDIA Tesla A100 (80GB)	
     - 6
   * - NVIDIA Tesla H100 (80GB)	
     - 6
	 


.. tip:: Your GPU is not on the list? Visit `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ for additional information.


Scaling When Data Sizes Grow
----------------------------

For many statements, SQreamDB scales linearly when adding more storage and querying on large data sets. It uses optimized 'brute force' algorithms and implementations, which don't suffer from sudden performance cliffs at larger data sizes.

Scaling When Queries Are Queuing
--------------------------------

SQreamDB scales well by adding more workers, GPUs, and nodes to support more concurrent statements.

What To Do When Queries Are Slow
--------------------------------

Adding more workers or GPUs does not boost the performance of a single statement or query. 

To boost the performance of a single statement, start by examining the :ref:`best practices<sql_best_practices>` and ensure the guidelines are followed.

Adding additional RAM to nodes, using more GPU memory, and faster CPUs or storage can also sometimes help.

Spooling Configuration
======================

:math:`limitQueryMemoryGB=\frac{\text{Total RAM - Internal Operation - metadata Server - Server picker}}{\text{Number of Workers}}`

:math:`spoolMemoryGB=limitQueryMemoryGB - 50GB`

SQreamDB recommends setting the ``spoolMemoryGB`` flag to 90% of the ``limitQueryMemoryGB`` flag. The ``limitQueryMemoryGB`` flag is the total memory you’ve allocated for processing queries. In addition, the ``limitQueryMemoryGB`` defines how much total system memory is used by each worker. Note that ``spoolMemoryGB`` must bet set to less than the ``limitQueryMemoryGB``.

Example
-------

Setting Spool Memory
~~~~~~~~~~~~~~~~~~~~

The following examples are for 2T of RAM and 9 workers running on 3 A100(40) GPUs:

Configuring the ``limitQueryMemoryGB`` using the Worker configuration file:

.. code-block:: console
     
   {
       “cluster”: “/home/test_user/sqream_testing_temp/sqreamdb”,
       “gpu”:  0,
       “licensePath”: “home/test_user/SQream/tests/license.enc”,
       “machineIP”: “127.0.0.1”,
       “metadataServerIp”: 127.0.0.1,
       “metadataServerPort”: 3105,
       “port”: 5000,
       “useConfigIP”: true,
       “limitQueryMemoryGB" : 201,
   }

Configuring the ``spoolMemoryGB`` using the legacy configuration file:

.. code-block:: console

	{
		"diskSpaceMinFreePercent": 10,
		"enableLogDebug": false,
		"insertCompressors": 8,
		"insertParsers": 8,
		"isUnavailableNode": false,
		"logBlackList": "webui",
		"logDebugLevel": 6,
		"nodeInfoLoggingSec": 60,
		"useClientLog": true,
		"useMetadataServer": true,
		"spoolMemoryGB": 151,
		"waitForClientSeconds": 18000,
		"enablePythonUdfs": true
	}
   
.. rubric:: Need help?

Visit `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ for additional information.
