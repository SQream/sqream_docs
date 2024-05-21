.. _sqloader_as_a_service:

*********************
SQLoader As a Service
*********************

The **SQLoader** is a Java service that enables you to ingest data into SQreamDB from other DBMS and DBaaS through HTTP requests using network insert.

**SQLoader** supports ingesting data from the following DBMSs:

* Greenplum
* Microsoft SQL Server
* Oracle
* Postgresql
* SAP HANA
* Sybase
* Teradata

.. contents:: 
   :local:
   :depth: 1
   
Before You Begin
================

It is essential that you have the following:

* Java 17
* :ref:`SQLoader configuration files<getting_the_sqloader_configuration_and_jar_files>`
* :ref:`SQLoader.jar file<getting_the_sqloader_configuration_and_jar_files>`

Minimum Hardware Requirements
------------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Component
     - Type
   * - CPU cores
     - 16
   * - RAM
     - 32GB

.. _sqloader_thread_sizing_guidelines:

Sizing Guidelines 
------------------

The SQLoader sizing is determined by the number of concurrent tables and threads based on the available CPU cores, limiting it to the number of cores minus one, with the remaining core reserved for the operating system. Each SQLoader request runs on a single table, meaning concurrent imports of multiple tables require multiple requests. Additionally, it is important to note that for partitioned tables, each partition consumes a thread. Therefore, for performance efficiency, considering the table's partition count when managing thread allocation is a must.

Compute formula: :math:`⌊ 0.8 * (TotalMemory - 4) ⌋`

Installation and Connectivity
=============================

.. _getting_the_sqloader_configuration_and_jar_files:

Getting All Configuration and JAR Files
---------------------------------------

Extract the ``.tar`` file using the following command:

.. code-block:: linux

	tar -xf sqloader_srv_v8.0.tar.gz

A folder named ``sqloader`` with the following files is created:
   
.. code-block:: 

	├── sqloader-v1.sh
	├── bin
	│   ├── sqloader-admin-server-1.0.jar
	│   └── sqloader-service-8.0.jar
	├── config
		├── reserved_words.txt
		├── sqload-jdbc.properties
		└── sqream-mapping.json
   
.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - File Name
     - Description
   * - ``sqream-mapping.json``
     - Maps foreign DBMS and DBaaS data types into SQreamDB data types during ingestion
   * - ``sqload-jdbc.properties``
     - Used for defining a connection string and may also be used to reconfigure data loading
   * - ``reserved_words.txt``
     - A list of reserved words which cannot be used as table and/or column names. 
   * - ``sqloader-service-8.0.jar``
     - The SQLoader service JAR file 
   * - ``sqloader-admin-server-1.0.jar``
     - The SQLoader admin server JAR file
   * - ``sqloader-v1.sh``
     - SQLoader service installer bash file
	 
Installation
------------

Parameters
^^^^^^^^^^

``-D`` flags are not dynamically adjustable at runtime. 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - State
     - Default
     - Type 
     - Description
   * - ``configDir``
     - Optional
     - ``java -jar sqloaderService-8.0.jar configDir=</path/to/directory/>``
     - 
     - Defines the path to the folder containing both the data type mapping and the reserved words files. The defined folder must contain both files or else you will receive an error. This flag affects the mapping and reserved words files and does not affect the properties file 
   * - ``hzClusterName=<TEXT>``
     - Optional
     - 
     - 
     - In Hazelcast, a cluster refers to a group of connected Hazelcast instances across different JVMs or machines. By default, these instances connect to the same cluster on the network level, meaning that all SQLoader services that start on a network will connect to each other and share the same queue. An admin can connect to only one Hazelcast cluster at a time. If you start multiple clusters and want to connect them to the admin service, you will need to start multiple admin services, with each service connecting to one of your clusters. It is essential that this flag has the same name used here and across all SQLLoader instances.
   * - ``LOG_DIR``
     - Optional
     - ``logs``
     - ``-D``
     - Defines the path of log directory created when loading data. If no value is specified, a ``logs`` folder is created under the same location as the ``sqloader.jar`` file
   * - ``spring.boot.admin.client.url``
     - Optional
     - ``http://localhost:7070``
     - 
     - SQLoader admin server connection flag
   * - ``Xmx``
     - Optional
     - 
     - 
     - We recommend using the ``Xmx`` flag to set the maximum heap memory allocation for the service. If a single service is running on the machine, we suggest allocating 80% of the total memory minus approximately 4GB, which the service typically needs on average. If multiple services are running on the same machine, calculate the recommended heap size for one service and then divide it by the number of services. Compute formula: :math:`⌊ 0.8 * (TotalMemory - 4) ⌋`
   * - ``DEFAULT_PROPERTIES``
     - Mandatory
     - ``sqload-jdbc.properties``
     - ``-D``
     - When the service initializes, it looks for the variable DEFAULT_PROPERTIES, which corresponds to the default sqload-jdbc.properties file. Once the service is running with a specified properties file, this setting will remain unchanged as long as the service is operational. To modify it, you must shut down the service, edit the properties file, and then restart the service. Alternatively, you can modify it via a POST request, but this change will only affect the specific load request and not the default setting for all requests.
	 
Installing the Admin Server and SQLoader Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	 
1. To install the admin server, run the following command (install it only once on one machine):

.. code-block:: 

	sudo ./sqloader-v1.sh -admin
	
Output:

.. code-block::

	##################################################################################
	Welcome to SQloader Admin-Service installation
	##################################################################################
	Please Enter JAVA_HOME PATH
	/opt/java
	##################################################################################
	The default PATH to install SQloader Admin Service is /usr/local/sqloader-admin
	Do you want to change the default PATH ? (y/N)
	##################################################################################
	The default PATH to SQloader-Admin logs directory is /var/log/sqloader-admin/logs
	Do you want to change the default? (y/N)
	##################################################################################
	Please enter HZCLUSTERNAME
	sqcluster
	##################################################################################
	SQloader-Admin default port is 7070 , Do you want to change the default port ? (y/N)
	##################################################################################
	JAVA_HOME=/opt/java
	BINDIR=/usr/local/sqloader-admin/
	LOG_DIR=/var/log/sqloader-admin/
	JAR=sqloader-admin-server-1.0.jar
	ADMINPORT=7070
	HZCLUSTERNAME=sqcluster
	##################################################################################
	############# SQLoader-Admin Service installed successfuly #######################
	##################################################################################
	To Start SQLoader-Admin Service: sudo systemctl start sqloader-admin
	To View SQLoader-Admin Service status: sudo systemctl status sqloader-admin
	##################################################################################
	
2. To start the admin server, run the following command:

.. code-block::

	sudo systemctl start sqloader-admin
	
3. To verify admin server start status, run the following command (optional):

.. code-block::

	sudo systemctl status sqloader-admin
	
4. To install SQLoader service, run the following command (you can install per machine):

.. code-block:: 
	
	sudo ./sqloader-v1.sh -service
   
Output:

.. code-block::

	##################################################################################
	Welocome to SQloader service installation
	##################################################################################
	Please Enter JAVA_HOME Path
	/opt/java
	##################################################################################
	The Default PATH to install SQloader Service is /usr/local/sqloader
	Do you want to change the default? (y/N)
	##################################################################################
	The default PATH to SQloader Service logs directory is /var/log/sqloader-service
	Do you want to change The default? (y/N)
	##################################################################################
	Please enter SQloader Admin IP address
	192.168.5.234
	##################################################################################
	Please enter SQloader MEM size in GB
	20
	##################################################################################
	Please enter HZCLUSTERNAME
	sqcluster
	##################################################################################
	Default CONFDIR is /usr/local/sqloader/config , Do you want to change the default CONFDIR ? (y/N)
	##################################################################################
	Default SQloader Admin port is 7070 , Do you want to change the default port ? (y/N)
	##################################################################################
	Default SQloader Service port is 6060 , Do you want to change the default port ? (y/N)
	##################################################################################
	Default sqload-jdbc.properties is /usr/local/sqloader/config, Do you want to change the default? (y/N)
	Using default sqload-jdbc.properties PATH
	/usr/local/sqloader/config
	##################################################################################
	##################################################################################
	Using /usr/local/sqloader/config/sqload-jdbc.properties
	##################################################################################
	JAVA_HOME=/opt/java
	BINDIR=/usr/local/sqloader/bin
	LOG_DIR=/var/log/sqloader-service
	CONFDIR=/usr/local/sqloader/config
	JAR=sqloader-service-8.0.jar
	PROPERTIES_FILE=/usr/local/sqloader/config/sqload-jdbc.properties
	PORT=6060
	ADMINIP=192.168.5.234
	ADMINPORT=7070
	MEM=20
	HZCLUSTERNAME=sqcluster
	##################################################################################
	############# SQLoader Service installed successfuly #######################
	##################################################################################
	To Start SQLoader Service: sudo systemctl start sqloader-service
	To View SQLoader Service status: sudo systemctl status sqloader-service
	##################################################################################

5. To start the SQLoader service, run the following command:

.. code-block::

	sudo systemctl start sqloader-service
	
6. To verify SQLoader service start status, run the following command (optional):

.. code-block::

	sudo systemctl status sqloader-service
   
Reconfiguration
---------------

**Admin server**

You may reconfigure the admin server even after you have started it.


1. To get the configuration path, run the following command:

.. code-block::

	cat /usr/lib/systemd/system/sqloader-admin.service | grep 'EnvironmentFile'
	
Output:
	
.. code-block::

	EnvironmentFile=/usr/local/sqloader-admin/config/sqloader_admin.conf

2. Restart the admin server:

.. code-block::

	sudo systemctl restart sqloader-admin

**SQLoader service**

You may reconfigure the SQLoader service even after you have started it.

1. To get the configuration path, run the following command:

.. code-block::

	cat /usr/lib/systemd/system/sqloader-service.service | grep 'EnvironmentFile'
	
Output:
	
.. code-block::

	EnvironmentFile=/usr/local/sqloader/config/sqloader_service.conf

2. Restart the SQLoader service:

.. code-block::

	sudo systemctl restart sqloader-service
   
Connection String
-----------------

It is recommended that the ``sqload-jdbc.properties`` file will contain a connection string.

1. Open the ``sqload-jdbc.properties`` file.
2. Configure connection parameters for:

   a. Either Greenplum, Microsoft SQL Server, Oracle, Postgresql, SAP HANA, Sybase, Teradata, or SQreamDB connection strings
   b. Optionally, Oracle or SQreamDB catalogs (recommended)

.. list-table:: Connection String Parameters
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``HostIp:port``
     - The host and IP address number
   * - ``database_name``
     - The name of the database from which data is loaded
   * - ``user``
     - Username of a role to use for connection
   * - ``password``
     - Specifies the password of the selected role
   * - ``ssl``
     - Specifies SSL for this connection

.. literalinclude:: connection_string.java
    :language: java
    :caption: Properties File Sample
    :linenos:

SQLoader Service Deployment and Interface
=========================================

Supported HTTP Requests
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Request Type
     - Request Name
     - cURL Command
     - Description
     - Example
   * - POST
     - ``load``
     - ``curl --header "Content-Type: application/json" --request POST --data '{}' http://127.0.0.1:6060/load``
     - Sends a request to the service and returns immediately. This HTTP request is utilized within a load-balancing queue shared across multiple instances. This setup ensures efficient resource utilization by distributing incoming load requests evenly across all available instances. Additionally, the system incorporates :ref:`high availability<high_availability>` mechanisms to recover failed jobs in case an instance crashes, ensuring continuous operation and reliability even during instance failures. Note that if all instances crash, at least one instance must remain operational to recover and execute pending jobs.
     - ``curl --header "Content-Type: application/json" --request POST --data '{"sourceTable": "AVIV_INC", "sqreamTable": "t_inc", "limit":2000, "loadTypeName":"full"}' http://127.0.0.1:6060/load``
   * - POST
     - ``syncLoad``
     - ``curl --header "Content-Type: application/json" --request POST --data '{}' http://127.0.0.1:6060/syncLoad``
     - Sends a request to the service and returns once the request is complete. There's no load-balancing queue shared across multiple instances; therefore, it's advised that ``syncLoad`` requests be monitored by the user and not heavily sent. Monitor using the ``getActiveLoads`` cURL.
     - ``curl --header "Content-Type: application/json" --request POST --data '{"sourceTable": "AVIV_INC", "sqreamTable": "t_inc", "limit":2000, "loadTypeName":"full"}' http://127.0.0.1:6060/syncLoad``
   * - POST
     - ``filterLogs``
     - ``curl --header "Content-Type: application/json" --request POST --data '{"requestId":"", "outputFilePath": ""}' http://127.0.0.1:6060/filterLogs``
     - Retrieves logs for a specific request ID
     - ``curl --header "Content-Type: application/json" --request POST --data '{"requestId":"request-1-6a2884a3", "outputFilePath": "/home/avivs/sqloader_request.log"}' http://127.0.0.1:6060/filterLogs``
   * - GET
     - ``getActiveLoads``
     - ``curl --header "Content-Type: application/json" --request GET http://127.0.0.1:6060/getActiveLoads``
     - Returns a list of all active loads currently running across all services
     - 
   * - GET
     - ``cancelRequest``
     - ``curl --request GET http://127.0.0.1:6061/cancelRequest/<RequestId>``
     - Cancels an active request by request ID
     - ``curl --request GET http://127.0.0.1:6061/cancelRequest/request-2-6aa3c53d``

.. _high_availability:

High Availability
-----------------

SQLoader as a service supports high availability for asynchronous load requests only. When a service crashes, another service will take over the tasks and execute them from the beginning. However, there are some limited cases where high availability will not provide coverage:

* **At least one service must remain operational**: After a crash, at least one service must be up and running to ensure that tasks can be recovered and executed.

* **Clustered flag requirement**: The SQLoader ``clustered`` flag must be set to ``true`` to enable high availability.

* **Limitations for specific tasks**: A task involving a full load with ``truncate=false`` and ``drop=false`` will not rerun to prevent data duplication. In this type of load, data is inserted directly into the target table rather than a temporary table, making it impossible to determine if any data was inserted before the crash.

This setup ensures that asynchronous load requests are handled reliably, even in the event of service failures.

Log Rotation
------------

Log rotation is based on time and size. At midnight (00:00) or when the file reaches 100MB, rotation occurs. Rotation means the log file ``SQLoader_service.log`` is renamed to ``SQLoader_service_%d_%i.log`` (%d=date, %i=rotation number), and a new, empty ``SQLoader_service.log`` file is created for the SQLoader service to continue writing to.

Log Automatic cleanup
^^^^^^^^^^^^^^^^^^^^^

The maximum number of archived log files to keep is set to 360, so Logback will retain the latest 360 log files in the logs directory. Additionally, the total file size in the directory is limited to 50 GB. If the total size of archived log files exceeds this limit, older log files will be deleted to make room for new ones.

SQLoader Request Parameters
---------------------------



.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - HTTP Parameter
     - State
     - Default
     - Type 
     - Description
   * - ``clustered``
     - Optional
     - ``true``
     -  
     - This flag is relevant only for ``load`` requests (``async``), not for ``syncLoad``. Note that this flag affects :ref:`high availability<high_availability>`. When set to ``true``: the request is directed to one of the available instances within a cluster, often through a load balancer. When set to ``false``: the request goes directly to the specified host without load balancing.
   * - ``configFile``
     - Optional
     - ``sqload-jdbc.properties``
     -  
     - Defines the path to the configuration file you wish to use. If not specified, the service will use the default path provided upon service deployment.
   * - ``connectionStringSqream``
     - Mandatory
     - 
     -  
     - JDBC connection string to SQreamDB
   * - ``connectionStringSource``
     - Mandatory
     - 
     -  
     - JDBC connection string to source database
   * - ``connectionStringCatalog``
     - Mandatory
     - 
     -  
     - JDBC connection string to catalog database
   * - ``cdcCatalogTable``
     - Optional
     - 
     -  
     - Part of the schema within the catalog database. Holds all inc/cdc tables and their settings
   * - ``cdcTrackingTable``
     - Optional
     - 
     -  
     - Part of the schema within the catalog database. Holds the last tracking value for every inc/cdc table from ``cdcCatalogTable`` table	 
   * - ``cdcPrimaryKeyTable``
     - Optional
     - 
     -  
     - Part of the schema within the catalog database. Holds all primary keys for every inc/cdc table from ``cdcCatalogTable`` table	 
   * - ``loadSummaryTable``
     - Optional
     - 
     -  
     - Part of the schema within the catalog database. Pre-aggregated table that stores summarized loads which can help monitoring and analyzing load	 
   * - ``batchSize``
     - Optional
     - ``10.000``
     - 
     - The number of records to be inserted into SQreamDB at once. Please note that the configured batch size may impact chunk sizes.
   * - ``caseSensitive``
     - Optional
     - ``false``
     - 
     - If ``true``, keeps table name uppercase and lowercase characters when table is created in SQreamDB
   * - ``checkCdcChain``
     - Optional
     - ``false``
     - 
     - Check CDC chain between tracking table and source table 
   * - ``chunkSize``
     - Optional
     - ``0``
     - 
     - The number of records read at once from the source database
   * - ``columnListFilePath``
     - Optional
     - 
     - ``.txt``
     - The name of the file that contains all column names. Columns must be separated using ``\n``. Expected file type is ``.txt`` 
   * - ``columns``
     - Optional
     - All columns
     - 
     - The name or names of columns to be loaded into SQreamDB ("col1,col2, ..."). For column names containing uppercase characters, maintain the uppercase format, avoid using double quotes or apostrophes, and ensure that the ``caseSensitive`` parameter is set to true
   * - ``count``
     - Optional
     - ``true``
     - 
     - Defines whether or not table rows will be counted before being loaded into SQreamDB 
   * - ``cdcDelete``
     - Optional
     - ``true``
     - 
     - Defines whether or not loading using Change Data Capture (CDC) includes deleted rows
   * - ``drop``
     - Optional
     - ``true``
     - 
     - Defines whether or not a new target table in SQreamDB is created. If ``false``, you will need to configure a target table name using the ``target`` parameter
   * - ``fetchSize``
     - Optional
     - ``100000``
     - 
     - The number of records to be read at once from source database. 
   * - ``filter``
     - Optional
     - ``1=1``
     - 
     - Defines whether or not only records with SQL conditions are loaded
   * - ``h, help``
     - Optional
     - 
     - 
     - Displays the help menu and exits
   * - ``limit``
     - Optional
     - ``0`` (no limit)
     - 
     - Limits the number of rows to be loaded
   * - ``loadDttm``
     - Optional
     - ``true``
     - 
     - Add an additional ``load_dttm`` column that defines the time and date of loading
   * - ``loadTypeName``
     - Optional
     - ``full``
     - 
     - Defines a loading type that affects the table that is created in SQreamDB. Options are ``full``, ``cdc``, or ``inc``. Please note that ``cdc``, and ``inc`` are supported only for Oracle
   * - ``lockCheck``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader will check source table is locked before the loading starts
   * - ``lockTable``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader will lock target table before the loading starts
   * - ``partitionName``
     - Optional
     - 
     - Partition identifier ``string``
     - Specifies the number of table partitions. If configured, ``partition`` ensures that data is loaded according to the specified partition. You may configure the ``thread`` parameter for parallel loading of your table partitions. If you do, please ensure that the number of threads does not exceed the number of partitions.
   * - ``port``
     - Optional
     - ``6060``
     - 
     - 
   * - ``rowid``
     - Optional
     - ``false``
     - 
     - Defines whether or not SQLoader will get row IDs from Oracle tables
   * - ``sourceDatabaseName``
     - Optional
     - ``ORCL``
     - 
     - Defines the source database name. It does not modify the database connection string but impacts the storage and retrieval of data within catalog tables.
   * - ``splitByColumn``
     - Optional
     - 
     - Column name ``string``
     - Column name for split (required for multi-thread loads)
   * - ``sourceTable``
     - Mandatory
     - 
     - Table name ``string``
     - Source table name to load data from
   * - ``sqreamTable``
     - Optional
     - Target table name
     - Table name ``string``
     - Target table name to load data into
   * - ``threadCount``
     - Optional
     - ``1``
     - 
     - Number of threads to use for loading. Using multiple threads can significantly improve the loading performance, especially when dealing with columns that have metadata statistics (e.g., min/max values). SQLoader will automatically divide the data into batches based on the specified thread number, allowing for parallel processing. You may use ``thread`` both for tables that are partitioned and tables that are not. See :ref:`Sizing Guidelines<sqloader_thread_sizing_guidelines>`
   * - ``truncate``
     - Optional
     - ``false``
     - 
     - Truncate target table before loading
   * - ``typeMappingPath``
     - Optional
     - ``config/sqream-mapping.json``
     - 
     - A mapping file that converts source data types into SQreamDB data types.
   * - ``useDbmsLob``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader uses ``dbms_lob_substr`` function for ``CLOB`` and ``BLOB`` data types
   * - ``usePartitions``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader uses partitions in ``SELECT`` statements
   * - ``validateSourceTable``
     - Optional
     - ``true``
     - 
     - Allows control over the validation of table existence during the load.

.. _load_type_name:

Using the ``loadTypeName`` Parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the ``loadTypeName`` parameter, you can define how you wish records' changes to be made to data in order to track inserts, updates, and deletes for data synchronization and auditing purposes.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Loading Type
     - Parameter Option
     - Description
   * - Full Table
     - ``full``
     - The entire data of the source table is loaded into SQreamDB
   * - Change Data Capture (CDC)
     - ``cdc``
     - Only changes made to the source table data since last load will be loaded into SQreamDB. Changes include transactions of ``INSERT``, ``UPDATE``, and ``DELETE`` statements. SQLoader recognizes tables by table name and metadata. Supported for Oracle only
   * - Incremental
     - ``inc``
     - Only changes made to the source table data since last load will be loaded into SQreamDB. Changes include transactions of ``INSERT`` statement. SQLoader recognizes the table by table name and metadata. Supported for Oracle only
	


	
Using the SQLoader Service Web Interface
----------------------------------------

The SQLoader Admin Server is a web-based administration tool specifically designed to manage and monitor the SQLoader service. It provides a user-friendly interface for monitoring data loading processes, managing configurations, and troubleshooting issues related to data loading into SQreamDB.


SQLoader Service Web Interface Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Monitor Services:

	* Health Checks: Monitor the health status of services to ensure they are functioning properly.
	* Metrics: Monitor real-time performance metrics, including CPU usage, memory usage, and response times.
	* Logging: View logs generated by services for troubleshooting and debugging purposes, and dynamically modify log levels during runtime to adjust verbosity for troubleshooting or performance monitoring.
	
* Manage Active Load Requests:

	* View a list of currently active data loading requests, including their status, progress, and relevant metadata.

Creating Summary and Catalog Tables
===================================

The summary and catalog tables are pre-aggregated tables that store summarized or aggregated data.

Creating a Summary Table
------------------------

The summary table is part of the schema within the database catalog.

The following summary table DDL uses Oracle syntax. 

.. note:: 

  If you are migrating from :ref:`SQLoader as a process<ingesting_from_databases>` to **SQLoader as a service**, as described on this page, it is highly recommended that you add the following column to your existing summary table instead of re-creating it.

  .. code-block:: sql

    REQUEST_ID TEXT (200 BYTE) VISIBLE DEFAULT NULL

.. code-block:: sql


  CREATE TABLE public.SQLOAD_SUMMARY (
    DB_NAME TEXT(200 BYTE) VISIBLE,
    SCHEMA_NAME TEXT(200 BYTE) VISIBLE,
    TABLE_NAME TEXT(200 BYTE) VISIBLE,
    TABLE_NAME_FULL TEXT(200 BYTE) VISIBLE,
    LOAD_TYPE TEXT(200 BYTE) VISIBLE,
    UPDATED_DTTM_FROM DATE VISIBLE,
    UPDATED_DTTM_TO DATE VISIBLE,
    LAST_VAL_INT NUMBER(22,0) VISIBLE,
    LAST_VAL_TS DATE VISIBLE,
    START_TIME TIMESTAMP(6) VISIBLE,
    FINISH_TIME TIMESTAMP(6) VISIBLE,
    ELAPSED_SEC NUMBER VISIBLE,
    ROW_COUNT NUMBER VISIBLE,
    SQL_FILTER TEXT(200 BYTE) VISIBLE,
    PARTITION TEXT(200 BYTE) VISIBLE,
    STMT_TYPE TEXT(200 BYTE) VISIBLE,
    STATUS TEXT(200 BYTE) VISIBLE,
    LOG_FILE TEXT(200 BYTE) VISIBLE,
    DB_URL TEXT(200 BYTE) VISIBLE,
    PARTITION_COUNT NUMBER VISIBLE DEFAULT 0,
    THREAD_COUNT NUMBER VISIBLE DEFAULT 1,
    ELAPSED_MS NUMBER VISIBLE DEFAULT 0,
    STATUS_CODE NUMBER VISIBLE DEFAULT 0,
    ELAPSED_SOURCE_MS NUMBER(38,0) DEFAULT NULL,
    ELAPSED_SOURCE_SEC NUMBER(38,0) DEFAULT NULL,
    ELAPSED_TARGET_MS NUMBER(38,0) DEFAULT NULL,
    ELAPSED_TARGET_SEC NUMBER(38,0) DEFAULT NULL,
    TARGET_DB_URL VARCHAR2(200) DEFAULT NULL,
    SQLOADER_VERSION VARCHAR2(20) DEFAULT NULL,
    HOST VARCHAR2(200) DEFAULT NULL,
    REQUEST_ID TEXT (200 BYTE) VISIBLE DEFAULT NULL
  );


Creating Catalog Tables
-----------------------

CDC (Change Data Capture) and Incremental tables are database tables that record changes made to data in order to track inserts, updates, and deletes for data synchronization and auditing purposes.

See :ref:`load_type_name`

Change Data Capture (CDC) and Incremental tables are supported only for Oracle.

.. code-block:: sql

	CREATE TABLE public.CDC_TABLES (
	  DB_NAME TEXT(200 BYTE) VISIBLE,
	  SCHEMA_NAME TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME_FULL TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME_CDC TEXT(200 BYTE) VISIBLE,
	  INC_COLUMN_NAME TEXT(200 BYTE) VISIBLE,
	  INC_COLUMN_TYPE TEXT(200 BYTE) VISIBLE,
	  LOAD_TYPE TEXT(200 BYTE) VISIBLE,
	  FREQ_TYPE TEXT(200 BYTE) VISIBLE,
	  FREQ_INTERVAL NUMBER(22,0) VISIBLE,
	  IS_ACTIVE NUMBER VISIBLE DEFAULT 0,
	  STATUS_LOAD NUMBER VISIBLE DEFAULT 0,
	  INC_GAP_VALUE NUMBER VISIBLE DEFAULT 0
	);

	CREATE TABLE public.CDC_TRACKING (
	  DB_NAME TEXT(200 BYTE) VISIBLE,
	  SCHEMA_NAME TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME_FULL TEXT(200 BYTE) VISIBLE,
	  LAST_UPDATED_DTTM DATE VISIBLE,
	  LAST_VAL_INT NUMBER(22,0) VISIBLE DEFAULT 0,
	  LAST_VAL_TS TIMESTAMP(6) VISIBLE,
	  LAST_VAL_DT DATE VISIBLE
	);

	CREATE TABLE public.CDC_TABLE_PRIMARY_KEYS (
	  DB_NAME TEXT(200 BYTE) VISIBLE,
	  SCHEMA_NAME TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME TEXT(200 BYTE) VISIBLE,
	  TABLE_NAME_FULL TEXT(200 BYTE) VISIBLE,
	  CONSTRAINT_NAME TEXT(200 BYTE) VISIBLE,
	  COLUMN_NAME TEXT(200 BYTE) VISIBLE,
	  IS_NULLABLE NUMBER VISIBLE DEFAULT 0
	);


Data Type Mapping 
=================

.. contents:: 
   :local:
   :depth: 1

Automatic Mapping
------------------

The **SQLoader** automatically maps data types used in Greenplum, Microsoft SQL Server, Oracle, Postgresql, Sybase, SAP HANA, and Teradata tables that are loaded into SQreamDB.

Greenplum
^^^^^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Greenplum Type
     - SQreamDB Type
   * - ``CHAR``, ``VARCHAR``, ``CHARACTER``
     - ``TEXT``
   * - ``TEXT``
     - ``TEXT``
   * - ``INT``, ``SMALLINT``, ``BIGINT``, ``INT2``, ``INT4``, ``INT8`` 
     - ``BIGINT``
   * - ``DATETIME``, ``TIMESTAMP``
     - ``DATETIME``
   * - ``DATE``
     - ``DATE``
   * - ``BIT``, ``BOOL``
     - ``BOOL``
   * - ``DECIMAL``, ``NUMERIC``
     - ``NUMERIC``
   * - ``FLOAT``, ``DOUBLE``
     - ``DOUBLE``
   * - ``REAL``, ``FLOAT4``
     - ``REAL``

Microsoft SQL Server
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Microsoft SQL Server Type
     - SQreamDB Type
   * - ``CHAR``, ``NCHAR``, ``VARCHAR``, ``NVARCHAR``, ``NVARCHAR2``, ``CHARACTER``, ``TEXT``, ``NTEXT``
     - ``TEXT``
   * - ``BIGINT``, ``INT``, ``SMALLINT``, ``INT``, ``TINYINT``
     - ``BIGINT``
   * - ``DATETIME``, ``TIMESTAMP``, ``SMALLDATETIME``, ``DATETIMEOFFSET``, ``DATETIME2``
     - ``DATETIME``
   * - ``DATE``
     - ``DATE``
   * - ``BIT``
     - ``BOOL``
   * - ``DECIMAL``, ``NUMERIC``
     - ``NUMERIC``
   * - ``FLOAT``, ``DOUBLE``
     - ``DOUBLE``
   * - ``REAL``
     - ``REAL``
   * - ``VARBINARY``
     - ``TEXT``

Oracle
^^^^^^^ 

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Oracle Type
     - SQreamDB Type
   * - ``BIGINT``, ``INT``, ``SMALLINT``, ``INTEGE``
     - ``BIGINT``
   * - ``CHAR``, ``NCHAR``, ``VARCHAR``, ``VARCHAR2``, ``NVARCHAR``, ``CHARACTER``
     - ``TEXT``
   * - ``DATE``, ``DATETIME``
     - ``DATETIME``
   * - ``TIMESTAMP``
     - ``DATETIME``
   * - ``DATE``
     - ``DATE``
   * - ``BOOLEAN``
     - ``BOOL``
   * - ``NUMERIC``
     - ``NUMERIC``
   * - ``FLOAT``, ``DOUBLE``
     - ``DOUBLE``
   * - ``CLOB``
     - ``TEXT``
   * - ``BLOB``
     - ``TEXT``
   * - ``RAW``
     - ``TEXT``


Postgresql
^^^^^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Postgresql Type
     - SQreamDB Type
   * - ``CHAR``, ``VARCHAR``, ``CHARACTER``
     - ``TEXT``
   * - ``TEXT``
     - ``TEXT``
   * - ``INT``, ``SMALLINT``, ``BIGINT``, ``INT2``, ``INT4``, ``INT8`` 
     - ``BIGINT``
   * - ``DATETIME``, ``TIMESTAMP``
     - ``DATETIME``
   * - ``DATE``
     - ``DATE``
   * - ``BIT``, ``BOOL``
     - ``BOOL``
   * - ``DECIMAL``, ``NUMERIC``
     - ``NUMERIC``
   * - ``FLOAT``, ``DOUBLE``
     - ``DOUBLE``
   * - ``REAL``, ``FLOAT4``
     - ``REAL``

SAP HANA
^^^^^^^^
	 
.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - SAP HANA Type
     - SQreamDB Type
   * - ``BIGINT``, ``INT``, ``SMALLINT``, ``INTEGER``, ``TINYINT``
     - ``BIGINT``
   * - ``CHAR``, ``VARCHAR``, ``NVARCHAR``, ``TEXT``, ``VARCHAR2``, ``NVARCHAR2``
     - ``TEXT``
   * - ``DATETIME``, ``TIMESTAMP``, ``SECONDDATE``
     - ``DATETIME``
   * - ``DATE``
     - ``DATE``
   * - ``BOOLEAN``
     - ``TEXT``
   * - ``DECIMAL``, ``SMALLDECIMAL``, ``BIGDECIMAL``
     - ``NUMERIC``
   * - ``DOUBLE``, ``REAL``
     - ``FLOAT``
   * - ``TEXT``
     - ``TEXT``
   * - ``BIGINT``
     - ``BIGINT``
   * - ``INT``
     - ``INT``
   * - ``SMALLINT``
     - ``SMALLINT``
   * - ``TINYINT``
     - ``TINYINT``
   * - ``DATETIME``
     - ``DATETIME``
   * - ``DATE``
     - ``DATE``
   * - ``BOOL``
     - ``BOOL``
   * - ``NUMERIC``
     - ``NUMERIC``
   * - ``DOUBLE``
     - ``DOUBLE``
   * - ``FLOAT``
     - ``FLOAT``
   * - ``REAL``
     - ``REAL``	 
	 
Sybase
^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Sybase Type
     - SQreamDB Type
   * - ``CHAR``, ``VARCHAR``, ``LONG VARCHAR``, ``CHARACTER``, ``TEXT``
     - ``TEXT``
   * - ``TINYINT``
     - ``TINYINT``
   * - ``SMALLINT``
     - ``SMALLINT``   
   * - ``INT``, ``INTEGER``
     - ``INT``
   * - ``BIGINT``
     - ``BIGINT``
   * - ``DECIMAL``, ``NUMERIC``
     - ``NUMERIC``   
   * - ``NUMERIC(126,38)``
     - ``NUMERIC(38,10)``
   * - ``FLOAT``, ``DOUBLE``
     - ``DOUBLE``
   * - ``DATE``
     - ``DATE``   
   * - ``DATETIME``, ``TIMESTAMP``, ``TIME``
     - ``DATETIME``   
   * - ``BIT``
     - ``BOOL``   
   * - ``VARBINARY``, ``BINARY``, ``LONG BINARY``
     - ``TEXT``   

Teradata
^^^^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Teradata Type
     - SQreamDB Type
   * - ``F``
     - ``DOUBLE``
   * - ``N``, ``D``
     - ``NUMERIC``
   * - ``CO``
     - ``TEXT``
   * - ``BO``
     - ``TEXT``
   * - ``A1``, ``AN``, ``AT``, ``BF``, ``BV``, ``CF``, ``CV``, ``JN``, ``PD``, ``PM``, ``PS``, ``PT``, ``PZ``, ``SZ``, ``TZ``
     - ``TEXT``
   * - ``I``, ``I4``, ``I(4)``  
     - ``INT``
   * - ``I2``, ``I(2)``
     - ``SMALLINT``
   * - ``I1``, ``I(1)``
     - ``TINYINT``
   * - ``DH``, ``DM``, ``DS``, ``DY``, ``HM``, ``HS``, ``HR``, ``I8``, ``MO``, ``MS``, ``MI``, ``SC``, ``YM``, ``YR``
     - ``BIGINT``
   * - ``TS``, ``DATETIME``
     - ``DATETIME``
   * - ``DA``
     - ``DATE``
   * - ``BIT``
     - ``BOOL``
   * - ``REAL``, ``DOUBLE``
     - ``DOUBLE``

Manually Adjusting Mapping
----------------------------

You have the possibility to adjust the mapping process according to your specific needs, using any of the following methods.

``names`` Method
^^^^^^^^^^^^^^^^^

To specify that you want to map one or more columns in your table to a specific data type, duplicate the code block which maps to the SQreamDB data type you want and include the ``names`` parameter in your code block. The SQLoader will map the specified columns to the specified SQreamDB data type. After the specified columns are mapped, the SQLoader continue to search for how to convert other data types to the same data type of the specified columns. 

In this example, ``column1``, ``column2``, and ``column3`` are mapped to ``BIGINT`` and the Oracle data types ``BIGINT``, ``INT``, ``SMALLINT``, ``INTEGER`` are also mapped to ``BIGINT``.

.. code-block:: json

	{
	  "oracle": [
		{
		  "names": ["column1", "column2", "column3"],
		  "sqream": "bigint",
		  "java": "int",
		  "length": false
		},
		{
		  "type": ["bigint","int","smallint","integer"],
		  "sqream": "bigint",
		  "java": "int",
		  "length": false
		}
	}	
		

	 

