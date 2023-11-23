.. _select_health_check_monitoring:

*******************************
SELECT HEALTH CHECK MONITORING
*******************************

The ``SELECT health_check_monitoring`` command empowers system administrators to comprehensively monitor the database's health across multiple *categories*. 

In the ``storage`` domain, it provides insights into cluster storage chunks and their fragmentation, helping prevent bottlenecks during table readings by identifying irrelevant files. The ``metadata_stats`` category offers information on Worker and metadata reactivity, enabling the identification of system performance during peak loads and the revelation of potential concurrent issues. Addressing licensing concerns, the command gives details on the customer's ``license``, including storage capacity and restrictions, and proactively alerts administrators before reaching limitations. Lastly, under ``self_healing``, it supplies essential details on ETL and load processes, monitors query execution flow, tracks Workers per service, identifies idle Workers, and detects issues like stuck snapshots—crucial for regular monitoring and offering clear insights during the Root Cause Analysis (RCA) process for optimal resource allocation.

Here you can find information about how to configure and execute each of the 4 monitoring categories.   
	 
.. contents::
   :local:
   :depth: 2
	 
Syntax
==========

.. code-block:: sql

	SELECT health_check_monitoring('<category>', '<input_file>', '<export_path>')

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - State
     - Description
   * - ``category``
     - Mandatory
     - Specifies the system domain for which to get health information about. The 4 categories are: ``storage``, ``metadata_stats``, ``license``, and ``self_healing``
   * - ``input_file``
     - Mandatory
     - The path to the specific configuration file of the *category* you wish to get information about
   * - ``export_path``
     - Mandatory
     - The path to the directory you wish to have your monitoring log file to extracted to

Configuration File
===================

The Health-Check Monitor has a default configuration file. To reconfigure any of the default metric values, navigate to the ``input.json`` file located under... and modify according to your personal preferences.

Some of the metrics, such as ``percentageStorageCapacity`` and ``daysForLicenseExpire`` require valid range configuration. Keep in mind that your default configuration file is best-practice configured. 

Default Metric Values
----------------------

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

Log File
=========

Some of the metrics, such as ``percentageStorageCapacity`` and ``daysForLicenseExpire`` require valid range configuration. Valid range metrics will show one of three different metric statuses in the log file: ``info``, ``warning``, or ``none``.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Metric Status
     - Description
   * - ``info``
     - If the metric falls within the valid range, the metric status will be logged as ``info``
   * - ``warning``
     -  If the metric exceeds the valid range, the metric status will be logged as ``warning``
   * - ``none``
     - If the metric does not have a valid range, the metric status will be logged as ``none``

Category Specifications
========================

Storage
--------

Provides insights into cluster storage chunks and their fragmentation process. Offers an indication of irrelevant storage files in the cluster, preventing potential bottlenecks in chunk iteration during table readings in advance.

You may filter ``storage`` health-check by database, schema, and table.

Execution Example
^^^^^^^^^^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('storage', '', '')

Metrics
^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Metric
     - Configuration Flag
     - Default Value
     - Description
   * - ``No. storage chunks``
     - NA
     - NA
     - 
   * - ``No. fragmented chunks``
     - ``totalNumberOfFragmentedChunks``
     - 
     - 

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``metric_time``
     - 
   * - ``metric_category``
     - 
   * - ``metric_name``
     - 
   * - ``metric_description``
     - 	 
   * - ``metric_value``
     - 
   * - ``metric_validation_status``
     - 
   * - ``response_time_sec``
     - 

	 
Metadata Statistics
--------------------

Provides information on Worker and metadata reactivity. Regular monitoring allows for the identification of the system's performance during peak loads, indicating periods of heavy system load. This insight can be invaluable for uncovering potential concurrent issues.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -
   

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('metadata_stats', '', '')

License
--------

Provides details about the customer's license, including database storage capacity and licensing restrictions. Proactively alerts the customer before reaching license limitations, ensuring awareness and timely action.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('license', '', '')

self_healing
--------------


Supplies details on customer ETLs and loads, monitors the execution flow of queries over time, tracks the number of Workers per service, identifies idle Workers, and detects potential issues such as stuck snapshots. It is imperative to regularly monitor this data. During the Root Cause Analysis (RCA) process, it provides a clear understanding of executed operations at specific times, offering customers guidance on optimal resource allocation, particularly in terms of workers per service.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('self_healing', '', '')



Permissions
=============

Using the ``SELECT health_check_monitoring`` command requires ``SUPERUSER`` permissions.