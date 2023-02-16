.. _current_method_modification_methods:

**************************
System Configuration Methods
**************************
 
For optimal performance, it is recommended that all SQream workers are similarly configured. To facilitate this, we provide a **worker configuration file** which allows users to make persistent cross-system changes that will be applied to all workers. However, for some operations it might be preferable to configure some workers differently from others. In such cases, the "legacy configuration file" can be used to configure specific workers within a cluster differently.

.. contents:: 
   :local:
   :depth: 1

Modifying Configurations Using the Worker Configuration File
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

Modifying Configurations Using a Legacy Configuration File
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

Reviewing Current System Configurations
---------------------------------------

Use the following command to review a list of currently configured flags, their values, default values, scope, and description.

.. code-block:: postgres
	
	SELECT * FROM sqream_catalog.parameters
	
	