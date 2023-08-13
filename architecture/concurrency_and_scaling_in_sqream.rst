.. _concurrency_and_scaling_in_sqream:

******
Sizing 
******

Concurrency and Scaling in SQreamDB
===================================

A SQreamDB cluster can execute one statement per worker process while also supporting the concurrent operation of multiple workers. Utility functions that require little resources such as :ref:`show_server_status`, will be executed regardless of load.

.. list-table:: Minimum Resource Required Per Worker
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
     - 10 cores per 30 Workers
     - 128 per 1T rows (accumulated for all tables)
     - 	10
   * - SqreamDB Acceleration Studio
     - 16
     - 16
     - 	50
   * - Server Picker
     - 8
     - 8
     - 	
	 
.. list-table:: Maximum Workers Per GPU
   :widths: auto
   :header-rows: 1
   
   * - NVIDIA Tesla T4 (16GB)
     - NVIDIA Tesla V100 (32GB)
     - NVIDIA Tesla A100 (40GB) 
     - NVIDIA Tesla A100 (80GB)
   * - 1
     - 2
     - 3	
     - 6
	 

.. rubric:: The GPU you are using is not on the list?

Visit `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ for additional information.

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

From the SQreamDB Acceleration Studio you can allocate the amount of memory (GB) available to the server for spooling using the :ref:`spoolMemoryGB flag<spool_memory_gb>`. SQreamDB recommends setting the ``spoolMemoryGB`` flag to 90% of the ``limitQueryMemoryGB`` flag. The ``limitQueryMemoryGB`` flag is the total memory you’ve allocated for processing queries.

In addition, the ``limitQueryMemoryGB`` defines how much total system memory is used by each worker.

Note that ``spoolMemoryGB`` must bet set to less than the ``limitQueryMemoryGB``.

Example Configurations
----------------------

Setting Spool Memory
~~~~~~~~~~~~~~~~~~~~

The following is an example of setting ``spoolMemoryGB`` value per-worker for 512GB of RAM and 4 workers:

.. code-block:: console
     
   {
       “cluster”: “/home/test_user/sqream_testing_temp/sqreamdb”,
       “gpu”:  0,
       “licensePath”: “home/test_user/SQream/tests/license.enc”,
       “machineIP”: “127.0.0.1”,
       “metadataServerIp”: “127.0.0.1”,
       “metadataServerPort”: “3105,
       “port”: 5000,
       “useConfigIP”” true,
       “limitQueryMemoryGB" : 121,
       “spoolMemoryGB" : 108
       “legacyConfigFilePath”: “home/SQream_develop/SqrmRT/utils/json/legacy_congif.json”
   }

Recommended Settings
~~~~~~~~~~~~~~~~~~~~

The following is an example of the recommended settings for a machine with 512GB of RAM and 4 workers:

.. code-block:: console
     
   limitQueryMemoryGB - ⌊(512 * 0.95 / 4)⌋ → ~ 486 / 4 → 121
   spoolMemoryGB - ⌊( 0.9 * limitQueryMemoryGB )⌋ → ⌊( 0.9 * 121 )⌋ → 108
   
.. rubric:: Need help?

Visit `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ for additional information.
