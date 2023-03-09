.. _current_method_flag_types:

**************************
<<<<<<< Updated upstream
System Operation 
**************************

When configuring how your system operates, you may choose to configure your entire cluster; meaning how all clients operate, or you may choose to configure only how the system works for a specific session. Any configurations made to the entire cluster are persistant, meaning that any alteration will continue to be valid for the duration of the session and also after the session is terminated. Persistant configurations are valid after downtime and restart.

SQream uses three flag types, **Cluster**, **Worker**, and **Regular**. Each of these flag types is associated with one of three hierarchical configuration levels described earlier, making it easier to configure your system.
=======
Configuring Workers
**************************
>>>>>>> Stashed changes

Workers can be individually configured using a worker configuration file, which allows for persistent modifications to be made. Persistent modification refers to changes made to a system or component that are saved and retained even after the system is restarted or shut down, allowing the modifications to persist over time. 

It is worth noting that the worker configuration file is not subject to frequent changes on a daily basis, providing stability to the system's configuration.


.. list-table::
   :widths: auto
   :header-rows: 1

   * - Flag Name
     - Who May Configure
     - Description
     - Data Type
     - Default Value
   * - ``cudaMemQuota``
     - SUPERUSER
     - Sets the percentage of total device memory used by your instance of SQream.
     - uint
     - ``90`` 
   * - ``healerMaxInactivityHours``
     - SUPERUSER
     - Used for defining the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.
     - bigint
     - ``5``
   * - ``isHealerOn``
     - SUPERUSER
     - Enables the Query Healer, which periodically examines the progress of running statements and logs statements exceeding the ``healerMaxInactivityHours`` flag setting.
     - boolean
     - ``TRUE``	 
   * - ``limitQueryMemoryGB``
     - Anyone
     - Prevents a query from processing more memory than the defined value.
     - uint
     - ``100000``
   * - ``loginMaxRetries``
     - SUPERUSER
     - Sets the permitted log-in attempts.
     - bigint
     - ``5``	 
   * - ``machineIP``
     - SUPERUSER
     - Enables you to manually set the reported IP.
     - string
     - ``127.0.0.1``	
   * - ``metadataServerPort``
     - SUPERUSER
     - Sets the port used to connect to the metadata server. SQream recommends using port ranges above 1024 because ports below 1024 are usually reserved, although there are no strict limitations. You can use any positive number (1 - 65535) while setting this flag.
     - uint
     - ``3105``	 
   * - ``useConfigIP``
     - SUPERUSER
     - Activates the machineIP (``TRUE``). Setting this flag to ``FALSE`` ignores the machineIP and automatically assigns a local network IP. This cannot be activated in a cloud scenario (on-premises only).
     - boolean
     - ``FALSE``	 












