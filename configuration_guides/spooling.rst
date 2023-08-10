.. _spooling:

********************************
Configuring the Spooling Feature
********************************

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
