.. _current_method_modification_methods:

**************************
Modification Methods
**************************

.. _modifying_your_configuration_using_the_worker_configuration_file:

Worker Configuration File
--------------------------

You can modify your configuration using the **worker configuration file (config.json)**. Changes that you make to worker configuration files are persistent. Note that you can only set the attributes in your worker configuration file **before** initializing your SQream worker, and while your worker is active these attributes are read-only.

The following is an example of the default worker configuration file:

.. code-block:: json
   
   {
    "cluster": "/home/sqream/sqream_storage",
    "cudaMemQuota": 96,
    "gpu": 0,
    "cpu": -1,
    "legacyConfigFilePath": "sqream_config_legacy.json",
    "licensePath": "/etc/sqream/license.enc",
    "limitQueryMemoryGB": 30,
    "parquetReaderThreads" : 8,
    "machineIP": "127.0.0.1",
    "metadataServerIp": "127.0.0.1",
    "metadataServerPort": 3105,
    "port": 5000,
    "instanceId": "sqream_0_1",
    "portSsl": 5100,
    "initialSubscribedServices": "sqream",
    "useConfigIP": true
    "logFormat": "csv","json"
   }

You can access the legacy configuration file from the ``legacyConfigFilePath`` parameter shown above. If all (or most) of your workers require the same flag settings, you can set the ``legacyConfigFilePath`` attribute to the same legacy file.

.. _modifying_your_configuration_using_a_legacy_configuration_file:

Cluster and Session Configuration File
--------------------------------------

You can modify your configuration using a legacy configuration file.

The Legacy configuration file provides access to the read/write flags. A link to this file is provided in the **legacyConfigFilePath** parameter in the worker configuration file.

The following is an example of the default cluster and session configuration file:

.. code-block:: json
   
   {
    "diskSpaceMinFreePercent": 1,
    "DefaultPathToLogs": "/home/sqream/sqream_storage/tmp_logs/",
    "enableLogDebug": false,
    "insertCompressors": 8,
    "insertParsers": 8,
    "isUnavailableNode": false,
    "logBlackList": "webui",
    "logDebugLevel": 6,
    "nodeInfoLoggingSec": 60,
    "useClientLog": true,
    "useMetadataServer": true,
    "spoolMemoryGB": 28,
    "waitForClientSeconds": 18000
   }


Metadata Configuration File
---------------------------

When attempting to free up disk space in Oracle Object Store by executing ``DELETE``, ``cleanup``, ``TRUNCATE``, or ``DROP``, ensure that the following four flags are consistently configured in both the :ref:`Worker<modifying_your_configuration_using_the_worker_configuration_file>` and Metadata configuration files.

.. list-table::
   :widths: auto 
   :header-rows: 1

   * - Flag Name
     - Who May Configure
     - Description
     - Data Type
     - Default Value 
   * - ``OciBaseRegion``
     - SUPERUSER
     - Sets your Oracle Cloud Infrastructure (OCI) region
     - String 
     - NA  
   * - ``OciVerifySsl``
     - SUPERUSER
     - Controls whether SSL certificates are verified. By default, verification is enabled. To disable it, set the variable to ``FALSE``
     - boolean
     - ``TRUE``  
   * - ``OciAccessKey``
     - SUPERUSER
     - Sets your Oracle Cloud Infrastructure (OCI) access key
     - String 
     - NA  
   * - ``OciAccessSecret``
     - SUPERUSER
     - Sets your Oracle Cloud Infrastructure (OCI) access secret 
     - String 
     - NA  

The following is an example of the metadata configuration file:

.. code-block:: json
   
   {
    "OciBaseRegion": "us-ashburn-1",
    "OciVerifySsl": false,
    "OciAccessKey": "587f59dxxxxxxxxxxxxxxxxxxxxxxxxx",
    "OciAccessSecret": "LrSEb+RZgxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   }







