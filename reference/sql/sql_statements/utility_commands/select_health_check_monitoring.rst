.. _select_health_check_monitoring:

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


Health-Check Logs
===================

After executing the ``SELECT health_check_monitoring`` command, a health-check log file and a CLI result set are generated. When reading your health-check log through the CLI, in addition to the metric values, it also showcases your initially set metric range configuration and the location of your exported log file. It's important to note that logs are separately generated for each of the four Health-Check Monitor *categories*. 

The log file and the result set both output the following metrics:

.. list-table:: Log Metrics
   :widths: auto
   :header-rows: 1

   * - Metric
     - Description
   * - ``metric_time``
     - The time when the specific metric was checked
   * - ``metric_category``
     - The system domain for which health information is retrieved; either ``storage``, ``metadata_stats``, ``license``, or ``self_healing``
   * - ``metric_name``
     - 
   * - ``metric_description``
     - 	 
   * - ``metric_value``
     - The value of the specific metric
   * - ``metric_validation_status``
     - One of three statuses: ``info``, metric value is within its defined valid range, ``none``, the metric provides information about the system and has no valid range, and ``warn``, metric deviates from its defined valid range
   * - ``response_time_sec``
     - Indicates the time taken to gather information for a specific metric. This is helpful for timing health-check executions 

Health-Check Category Specifications
========================================

Storage
--------

Provides insights into cluster storage chunks and their fragmentation process. Offers an indication of irrelevant storage files in the cluster, preventing potential bottlenecks in chunk iteration during table readings in advance.

.. code-block:: sql

	SELECT health_check_monitoring('storage', 'path/to/my/input.json', 'directory/where/i/save/logs')

When monitoring your storage health, you may also filter information retrieval by database, schema, table, or all three.  

.. code-block:: sql

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

``max response time`` indicates the peak time for the monitored *category*, while ``variance`` represents the standard deviation between the peak time and the monitoring time.

.. list-table:: Metadata Statistics Metrics
   :widths: auto
   :header-rows: 1
   
   * - Metric
     - Configuration Flag
     - Default Value
     - Description
   * - ``NodeHeartbeatMsg``
     - ``nodeHeartbeatMsgMaxResponseTimeMS``
     - ``"from":0, "to":1000``
     - 
   * - ``NodeHeartbeatMsg``
     - ``nodeHeartbeatMsgVariance``
     - ``"from":0, "to":1000``
     - 
   * - ``CheckLocksMsg``
     - ``checkLocksMsgMaxResponseTimeMS``
     - ``"from":0, "to":1000``
     - 
   * - ``CheckLocksMsg``
     - ``checkLocksMsgVariance``
     - ``"from":0, "to":1000``
     - 
   * - ``KeysAndValuesNMsg``
     - ``keysAndValuesNMaxResponseTimeMS``
     - ``"from":0, "to":1000``
     - 
   * - ``KeysAndValuesNMsg``
     - ``keysAndValuesNVariance``
     - ``"from":0, "to":1000``
     - 
   * - ``KeysWithPrefixMsg``
     - ``keysWithPrefixMsgMaxResponseTimeMS``
     - ``"from":0, "to":1000``
     - 
   * - ``KeysWithPrefixMsg``
     - ``keysWithPrefixMsgVariance``
     - ``"from":0, "to":1000``
     - 

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


