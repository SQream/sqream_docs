:orphan:

.. _select_health_check_monitoring:

.. role:: red
   :class: red-text
   
.. role:: green
   :class: green-text

.. raw:: html

   <style>
   .red-text {
       color: red !important;
   }
   
   .green-text {
       color: green !important;
   }
   </style>

*******************************
HEALTH-CHECK MONITORING
*******************************

The ``SELECT health_check_monitoring`` command empowers system administrators to comprehensively monitor the database's health across multiple *categories*. 

In the ``storage`` domain, it provides insights into cluster storage chunks and their fragmentation, helping to prevent table reading bottlenecks by alerting in the case of a fragmentation scenario. Additionally, it gives indications per table on when to trigger cleanup executions (to free up storage and improve reading performance). The ``metadata_stats`` category offers information on Worker and metadata reactivity, enabling the identification of system performance during peak loads and the revelation of potential concurrent issues. Addressing licensing concerns, the command gives details on the customer's ``license``, including storage capacity and restrictions, and proactively alerts administrators before reaching limitations. Lastly, under ``self_healing``, it supplies essential details on ETL and load processes, monitors query execution flow, tracks Workers per service, identifies idle Workers, and detects issues like stuck snapshots—crucial for regular monitoring and offering clear insights during the Root Cause Analysis (RCA) process for optimal resource allocation.

Here, you can discover details on configuring the monitoring for each of the four categories, along with instructions on how to access and interpret the log files for each category.

.. contents::
   :local:
   :depth: 2
	
Before You Begin
==================

* Download the Health-Check Monitor :download:`input.json </_static/samples/input.json>` configuration file and save it anywhere you want.
* The ``SELECT health_check_monitoring`` command requires ``SUPERUSER`` permissions.

Configuration
--------------

There are two types of Health-Check Monitor metrics: one is configurable, and the second is non-configurable. Non-configurable metrics provide information about the system, such as total storage capacity measured in Gigabytes. Configurable metrics are set with low, high, or both thresholds within a valid range to be reported in case of deviation. For example, this could include the number of days remaining on your SQreamDB license.

Default Metric Values
----------------------

The Health-Check Monitor configuration file comes pre-configured with best practices. However, as mentioned before, you have the flexibility to customize any default metric values based on your preferences. All metrics presented below are defined with valid ranges, so any value outside the range triggers a warning. It's important to note that configuring only one threshold will make the Health-Check Monitor assume the ignored threshold is set to *infinity*.

.. code-block:: json

	{
	   "totalNumberOfFragmentedChunks":{
		  "from":0,
		  "to":100
	   },
	   "percentageStorageCapacity":{
		  "from":0,
		  "to":0.9
	   },
	   "daysForLicenseExpire":{
		  "from":60
	   },
	   "stuckSnapshots":{
		  "from":0,
		  "to":2
	   },
	   "queriesInQueue":{
		  "from":0,
		  "to":100
	   },
	   "availableWorkers":{
		  "from":0,
		  "to":5
	   },
	   "nodeHeartbeatMsgMaxResponseTimeMS":{
		  "from":0,
		  "to":1000
	   },
	   "checkLocksMsgMaxResponseTimeMS":{
		  "from":0,
		  "to":1000
	   },
	   "keysAndValuesNMaxResponseTimeMS":{
		  "from":0,
		  "to":1000
	   },
	   "keysWithPrefixMsgMaxResponseTimeMS":{
		  "from":0,
		  "to":1000
	   },
	   "nodeHeartbeatMsgVariance":{
		  "from":0,
		  "to":1000
	   },
	   "checkLocksMsgVariance":{
		  "from":0,
		  "to":1000
	   },
	   "keysAndValuesNVariance":{
		  "from":0,
		  "to":1000
	   },
	   "keysWithPrefixMsgVariance":{
		  "from":0,
		  "to":1000
	   }
	}

General Syntax
===============

.. code-block:: postgres

	SELECT health_check_monitoring('<category>', '<input_file>', '<export_path>')
	
	category :: = { storage | metadata_stats | license | self_healing }

.. list-table:: Parameters
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``category``
     - Specifies the system domain for which health information is to be retrieved.
   * - ``input_file``
     - Specifies the path to the configuration file of the designated *category* for which you want to obtain information.
   * - ``export_path``
     - Specifies the directory path where you want the monitoring log file to be extracted.


Health-Check Log Structure
=============================

After executing the ``SELECT health_check_monitoring`` command, a health-check log file and a CLI result set are generated. When reading your health-check log through the CLI, in addition to the metric values, it also showcases your initially set metric range configuration and the location of your exported log file. It's important to note that logs are separately generated for each of the four Health-Check Monitor *categories*. 

The log file and the result set both output the following information:

.. list-table:: Log Output
   :widths: auto
   :header-rows: 1

   * - Log Column Name
     - Description
   * - ``metric_time``
     - The time when the specific metric was checked
   * - ``metric_category``
     - The system domain for which health information is retrieved; either ``storage``, ``metadata_stats``, ``license``, or ``self_healing``
   * - ``metric_name``
     - The specific metric that is being evaluated
   * - ``metric_description``
     - For metrics that need a detailed analysis breakdown, this column will showcase the breakdown alongside any additional information 	 
   * - ``metric_value``
     - The value of the specific metric
   * - ``metric_validation_status``
     - One of three statuses: 
	 * :green:`info`, metric value is within its defined valid range
	 * none, the metric provides information about the system and has no valid range 
	 * :red:`warn`, metric deviates from its defined valid range
   * - ``response_time_sec``
     - Indicates the time taken to gather information for a specific metric. This is helpful for timing health-check executions 

Handling Warnings
-------------------

Upon reviewing your log output, you'll observe that the ``metric_validation_status`` column reflects one of three potential statuses: :green:`info`, none, or :red:`warn`. This section offers guidance on effectively managing warnings whenever a :red:`warn` status is encountered.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Health-Check Category
     - Metric Name
     - How to Handle :red:`warn`
   * - Storage
     - ``No. fragmented chunks``
     - Recreating the table for triggering defragmentation
   * - Metadata Statistics
     - ``NodeHeartbeatMsg``, ``CheckLocksMsg``, ``KeysAndValuesNMsg``, ``KeysWithPrefixMsg``
     - Gather your metadata statistics by executing the following commands and send the information to `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_:
	 
       .. code-block:: sql
	   
          SELECT export_leveldb_stats('<EXPORT_FILE_PATH>');
          SELECT export_statement_queue_stats('<EXPORT_FILE_PATH>');
          SELECT export_conn_stats('<EXPORT_FILE_PATH>'); 	      
   * - License
     - ``% of used storage capacity``, ``License expiration date``
     - Contact `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ for license expansion	
   * - Self Healing
     - ``Queries in queue``
     - To prevent bottlenecks in the service, reallocate service Workers. Distributing or reallocating service Workers strategically can help optimize performance and mitigate potential bottlenecks. Learn more about :ref:`Worker allocation<workload_manager>`	
   * - Self Healing
     - ``Available workers per service``
     - Efficiently utilize resources by reallocating idle workers to a busier service. This approach optimizes resource consumption and helps balance the workload across services.	Learn more about :ref:`Worker allocation<workload_manager>`	
   * - Self Healing
     - ``Stuck snapshots``
     - The Healer is designed to autonomously address stuck snapshots based on its configured timeout. The session flag, :ref:`healerDetectionFrequencySeconds<healer_detection_frequency_seconds>`, determines when the Healer detects and takes corrective actions for stuck snapshots. To manually address a situation, execute a :ref:`graceful shutdown<shutdown_server_command>` of the statement's Worker  		 

Health-Check Category Specifications
========================================

Storage
--------

Provides insights into cluster storage chunks and their fragmentation process. Offers an indication of irrelevant storage files in the cluster, preventing potential bottlenecks in chunk iteration during table readings in advance.

``storage`` monitoring has a lengthy execution time, necessitating low-frequency checks to prevent undue strain on your environment.

.. code-block:: sql

	SELECT health_check_monitoring('storage', 'path/to/my/input.json', 'directory/where/i/save/logs')

When monitoring your storage health, you may also filter information retrieval by database, schema, table, or all three.  

.. code-block:: sql

	SELECT health_check_monitoring('storage', 'master', 'path/to/my/input.json', 'path/to/where/i/save/logs')
	
	SELECT health_check_monitoring('storage', 'master', 'schema1', 'path/to/my/input.json', 'path/to/where/i/save/logs')	
	
	SELECT health_check_monitoring('storage', 'master', 'schema1', 'table1', 'path/to/my/input.json', 'path/to/where/i/save/logs')

.. list-table:: Storage Metrics
   :widths: auto
   :header-rows: 1
   
   * - Metric
     - Configuration Flag
     - Default Value
     - Description
   * - ``No. storage chunks``
     - NA
     - NA
     - Chunk status; categorized as either ``clean``, ``mixed``, or ``deleted``. This classification aids in comprehending potential slowdowns when reading from a table. ``Clean`` indicates that your table is free of physically lingering deleted data. ``Mixed`` suggests that your table contains data marked for deletion but not yet purged (awaiting the removal of deleted data). Meanwhile, ``deleted`` signifies that the table has undergone the cleanup process. This categorization proves valuable for scrutinizing deletion and clean-up practices, particularly when visualizing data through dedicated tools 
   * - ``No. fragmented chunks``
     - ``totalNumberOfFragmentedChunks``
     - ``"from":0, "to":100``
     - Defines the number of fragmented chunks

Metadata Statistics
--------------------

Provides information on Worker and metadata reactivity. Regular monitoring allows for the identification of the system's performance during peak loads, indicating periods of heavy system load. This insight can be invaluable for uncovering potential concurrent issues.

.. code-block:: sql

	SELECT health_check_monitoring('metadata_stats', 'path/to/my/input.json', 'directory/where/i/save/logs')

.. list-table:: Metadata Statistics Metrics
   :widths: auto
   :header-rows: 1
   
   * - Metric
     - Configuration Flag
     - Default Value
     - Description
   * - ``NodeHeartbeatMsg``
     - ``nodeHeartbeatMsgMaxResponseTimeMS``, ``nodeHeartbeatMsgVariance``
     - ``"from":0, "to":1000``
     - Ensures worker vitality through metadata pings. ``max response time`` indicates the peak time for the monitored *category*, while ``variance`` represents the standard deviation between the peak time and the monitoring time.	 
   * - ``CheckLocksMsg``
     - ``checkLocksMsgMaxResponseTimeMS``, ``checkLocksMsgVariance``
     - ``"from":0, "to":1000``
     - Provides details on current locks at the metadata to determine the feasibility of executing the statement. ``max response time`` indicates the peak time for the monitored *category*, while ``variance`` represents the standard deviation between the peak time and the monitoring time.	 
   * - ``KeysAndValuesNMsg``
     - ``keysAndValuesNMaxResponseTimeMS``, ``keysAndValuesNVariance``
     - ``"from":0, "to":1000``
     - Iterates through metadata keys and values. ``max response time`` indicates the peak time for the monitored *category*, while ``variance`` represents the standard deviation between the peak time and the monitoring time.	 
   * - ``KeysWithPrefixMsg``
     - ``keysWithPrefixMsgMaxResponseTimeMS``, ``keysWithPrefixMsgVariance``
     - ``"from":0, "to":1000``
     - Iterates through metadata keys and values with a specific prefix. ``max response time`` indicates the peak time for the monitored *category*, while ``variance`` represents the standard deviation between the peak time and the monitoring time.


License
--------

Provides details about the customer's license, including database storage capacity and licensing restrictions. Proactively alerts the customer before reaching license limitations, ensuring awareness and timely action.

.. code-block:: sql

	SELECT health_check_monitoring('license', 'path/to/my/input.json', 'directory/where/i/save/logs')

.. list-table:: License Metrics
   :widths: auto
   :header-rows: 1
   
   * - Metric
     - Configuration Flag
     - Default Value
     - Description
   * - ``Total storage capacity``
     - NA
     - NA
     - Indicates your licensed storage capacity, outlining the permissible limit for your usage
   * - ``Used storage capacity``
     - NA
     - NA
     - Indicates current storage utilization
   * - ``% of used storage capacity``
     - ``percentageStorageCapacity``
     - ``"from":0, "to":0.9``
     - Indicates current storage utilization percentage
   * - ``License expiration date``
     - ``daysForLicenseExpire``
     - ``"from":60``
     - Indicates how many days until your license expires

self_healing
--------------

Supplies details on customer ETLs and loads, monitors the execution flow of queries over time, tracks the number of Workers per service, identifies idle Workers, and detects potential issues such as stuck snapshots. It is imperative to regularly monitor this data. During the Root Cause Analysis (RCA) process, it provides a clear understanding of executed operations at specific times, offering customers guidance on optimal resource allocation, particularly in terms of Workers per service.

Monitoring ``self_healing`` frequently is a best practice to maximize its value.

.. code-block:: sql

	SELECT health_check_monitoring('self_healing', 'path/to/my/input.json', 'directory/where/i/save/logs')


.. list-table:: self_healing Metrics
   :widths: auto
   :header-rows: 1
   
   * - Metric
     - Configuration Flag
     - Default Value
     - Description
   * - ``Queries in queue``
     - ``queriesInQueue``
     - ``"from":0, "to":100``
     - Indicates the number of currently queued queries
   * - ``Available workers per service``
     - ``availableWorkers``
     - ``"from":0, "to":5``
     - Indicates the number of unused Workers per service
   * - ``Stuck snapshots``
     - ``stuckSnapshots``
     - ``"from":0, "to":2``
     - Indicates the number of currently stuck snapshots


