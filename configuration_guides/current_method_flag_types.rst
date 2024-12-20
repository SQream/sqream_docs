.. _current_method_flag_types:

*******
Workers
*******

Workers can be individually configured using the :ref:`worker configuration file<modifying_your_configuration_using_the_worker_configuration_file>`, which allows for persistent modifications to be made. Persistent modification refers to changes made to a system or component that are saved and retained even after the system is restarted or shut down, allowing the modifications to persist over time. 

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
   * - ``healerDetectionFrequencySeconds``
     - SUPERUSER
     - Determines the default frequency for the healer to check that its conditions are met.
     - 
     - ``86,400`` (seconds)
   * - ``isHealerOn``
     - SUPERUSER
     - Enables the Query Healer, which periodically examines the progress of running statements and logs statements exceeding the ``healerMaxInactivityHours`` flag setting.
     - boolean
     - ``TRUE``	
   * - ``logFormat``
     - SUPERUSER
     - Determines the file format of the log files. Format may by ``csv``, ``json``, or both (all logs will be written saved both as ``csv`` and ``json`` files) 
     - string
     - ``csv``	
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
   * - ``maxConnectionInactivitySeconds``
     - SUPERUSER
     - Determines the maximum period of session idleness, after which the connection is terminated.
     - bigint
     - ``86,400`` (seconds)
   * - ``maxConnections``
     - SUPERUSER
     - Defines the maximum allowed connections per Worker.
     - bigint
     - ``1000``	
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
	 
	 
   * - ``healerMaxInactivityHours``
     - SUPERUSER
     - Used for defining the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.
     - bigint
     - ``5``
   * - ``limitQueryMemoryGB``
     - Anyone
     - Prevents a query from processing more memory than the defined value.
     - uint
     - ``100000``
	 












