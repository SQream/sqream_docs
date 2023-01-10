.. _current_method_configuration_levels:

**************************
Configuration Levels
**************************
SQream's configuration parameters are based on the following hierarchy:

.. contents:: 
   :local:
   :depth: 1

Cluster-Based Configuration
--------------
Cluster-based configuration lets you centralize configurations for all workers on the cluster. Only :ref:`Regular and Cluster flag types<current_method_flag_types>` can be modified on the cluster level. These modifications are persistent and stored at the metadata level, which are applied globally to all workers in the cluster.

.. note:: While cluster-based configuration was designed for configuring Workers, you can only configure Worker values set to the Regular or Cluster type.

Worker-Based Configuration
--------------
Worker-based configuration lets you modify individual workers using a worker configuration file. Worker-based configuration modifications are persistent.

For more information on making configurations from the worker configuration file, see `Modifying Your Configuration Using a Legacy Configuration File <https://docs.sqream.com/en/latest/configuration_guides/current_configuration_method.html#modifying-your-configuration-using-a-legacy-configuration-file>`_.

Session-Based Configuration
--------------
Session-based configurations are not persistent and are deleted when your session ends. This method enables you to modify all required configurations while avoiding conflicts between flag attributes modified on different devices at different points in time. The **SET flag_name** command is used to modify flag values on the session level. Any modifications you make with the **SET flag_name** command apply only to your open session, and are not saved when it ends.

For example, when the query below has completed executing, the values configured will be restored to its previous setting: 

.. code-block:: console
   
   set spoolMemoryGB=700;
   select * from table a where date='2021-11-11'