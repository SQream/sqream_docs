.. _spooling:

**************************
Configuring the Spooling Feature
**************************
The **Configuring the Spooling Feature** page includes the following topics:

.. contents:: 
   :local:
   :depth: 1

Overview
--------
From the SQream Acceleration Studio you can allocate the amount of memory (GB) available to the server for spooling using the ``spoolMemoryGB`` flag. SQream recommends setting the ``spoolMemoryGB`` flag to 90% of the ``limitQueryMemoryGB`` flag. The ``limitQueryMemoryGB`` flag is the total memory you’ve allocated for processing queries.

In addition, the ``limitQueryMemoryGB`` defines how much total system memory is used by each worker. SQream recommends setting ``limitQueryMemoryGB`` to 5% less than the total host memory divided by the amount of ``sqreamd`` workers on host.

Note that ``spoolMemoryGB`` must bet set to less than the ``limitQueryMemoryGB``.

Example Configurations
----------
The **Example Configurations** section shows the following example configurations:

.. contents:: 
   :local:
   :depth: 1

Example 1 - Recommended Settings
~~~~~~~~~~~
The following is an example of the recommended settings for a machine with 512GB of RAM and 4 workers:

.. code-block:: console
     
   limitQueryMemoryGB - ⌊(512 * 0.95 / 4)⌋ → ~ 486 / 4 → 121
   spoolMemoryGB - ⌊( 0.9 * limitQueryMemoryGB )⌋ → ⌊( 0.9 * 121 )⌋ → 108

Example 2 - Setting Spool Memory
~~~~~~~~~~~
The following is an example of setting ``spoolMemoryGB`` value in the current configuration method per-worker for 512GB of RAM and 4 workers:

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
   
The following is an example of setting ``spoolMemoryGB`` value in the previous configuration method per-worker for 512GB of RAM and 4 workers:

.. code-block:: console
     
   “runtimeFlags”: {
   “limitQueryMemoryGB” : 121,
   “spoolMemoryGB” : 108


For more information about configuring the ``spoolMemoryGB`` flag, see the following:

* `Current configuration method <https://docs.sqream.com/en/v2020.3.2/configuration_guides/spool_memory_gb.html>`_
* `Previous configuration method <https://docs.sqream.com/en/v2020.3.2/configuration_guides/previous_configuration_method.html#id2>`_