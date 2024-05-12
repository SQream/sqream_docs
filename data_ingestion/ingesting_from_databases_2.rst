.. _ingesting_from_databases_2:

******************
External Databases
******************

The **SQLoader** is a java service that enables you to load data into SQreamDB from other DBMS and DBaaS through HTTP requests using network insert.

**SQLoader** supports Oracle, Postgresql, Teradata, Microsoft SQL Server, and SAP HANA.

.. contents:: 
   :local:
   :depth: 1
   
Before You Begin
================

It is essential that you have the following:

* Java 17
* SQLoader configuration files
* SQLoader.jar file



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

The SQLoader sizing is determined by the number of concurrent tables and threads based on the available CPU cores, limiting it to the number of cores minus one, with the remaining core reserved for the operating system. Each SQLoader instance runs on a single table, meaning concurrent imports of multiple tables require multiple instances. Additionally, when dealing with partitioned tables, each partition consumes a thread, so users should consider the table's partition count when managing thread allocation for efficient performance.

Getting the SQLoader Configuration and JAR Files
================================================

1. Download the ``.tar`` file using the following command:

.. code-block:: linux

	curl -O https://sq-ftp-public.s3.amazonaws.com/sqloader-v7.12.tar

2. Extract the ``.tar`` file using the following command:

.. code-block:: linux

	tar -xf sqloader-7.12.tar.gz

A folder named ``sqloader`` with the following files is created:
   
.. list-table:: SQLoader Files
   :widths: auto
   :header-rows: 1
   
   * - File
     - Description
   * - ``sqream-mapping.json``
     - Maps foreign DBMS and DBaaS data types into SQreamDB data types during ingestion
   * - ``sqload-jdbc.properties``
     - Used for defining a connection string and may also be used to reconfigure data loading
   * - ``reserved_words.txt``
     - A list of reserved words which cannot be used as table and/or column names. 
   * - ``sqloader.jar``
     - The SQLoader package file 
   
Connection String
=================

The ``sqload-jdbc.properties`` file contains a connection string that must be configured to enable data loading into SQreamDB.

1. Open the ``sqload-jdbc.properties`` file.
2. Configure connection parameters for:

   a. Either Postgresql, Oracle, Teradata, Microsoft SQL Server, SAP HANA or SQreamDB connection strings
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

Using SQLoader Service
======================

When the service initializes, it looks for the variable ``DEFAULT_PROPERTIES``, which corresponds to the default ``sqload-jdbc.properties`` file.

``DEFAULT_PROPERTIES`` can be configured using one of two ways:

* Setting as an environment variable:

   .. code-block::
   
    export DEFAULT_PROPERTIES=/home/avivs/branches/java/sqloader-service/config/sqload-jdbc.properties
   
   Followed by service execution:
   
   .. code-block::
   
    java -jar target/sqloaderService-8.0.jar
   
* Appending to -D flag when executing the jar:

  .. code-block::
  
   java -jar -DDEFAULT_PROPERTIES=/home/avivs/branches/java/sqloader-service/config/sqload-jdbc.properties target/sqloaderService-8.0.jar
   
  .. note:: 
  
   ``-D`` flags are not dynamically adjustable at runtime. Once the service is running with a specified properties file, this setting will remain unchanged as long as the service is operational. To modify it, you must shut down the service, edit the properties file, and then restart the service. Alternatively, you can modify it via a POST request, but this change will only affect the specific load request and not the default setting for all requests.

Supported POST Requests
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - POST
     - Description
     - Example
   * - ``load``
     - Send request to service and return
     - 
   * - ``syncLoad``
     - Send request to service and return once the request is done
     - 
   * - ``filterLogs``
     - Get logs for a specific request id
     - 
   * - ``getActiveLoads``
     - Get a list of all active loads currently running in shared queue
     - 
   * - ``cancelRequest``
     - Cancel an ``async`` request by request id
     - 

Loading Data into SQreamDB Tables
---------------------------------

1. Run the ``sqloader.jar`` file using the following CLI command:

.. code-block:: console

	java -jar sqloader.jar
	
2. You may load the entire data of a source table using the following CLI command:

.. code-block:: console 

	java -jar sqloader.jar -table source_table_name
	
3. You may customize the data load either by using each of the following parameters within a CLI command or by configuring the ``properties`` file:

.. list-table:: SQLoader Service Parameters
   :widths: auto
   :header-rows: 1
   
   * - CLI Parameter
     - State
     - Default
     - Type 
     - Description
   * - ``-configFile``
     - Optional
     - ``sqload-jdbc.properties``
     -  
     - Defines the path to the configuration file you wish to use. This parameter may be defined using only the CLI. If not specified, the service will use ``DEFAULT_PROPERTIES`` parameter
   * - ``-connectionStringSqream``
     - Optional
     - 
     -  
     - JDBC connection string to SQreamDB
   * - ``-connectionStringSource``
     - Optional
     - 
     -  
     - JDBC connection string to source database
   * - ``-connectionStringCatalog``
     - Optional
     - 
     -  
     - JDBC connection string to catalog database
   * - ``-cdcCatalogTable``
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
   * - ``-batchSize``
     - Optional
     - ``10.000``
     - 
     - The number of records to be inserted into SQreamDB at once. Please note that the configured batch size may impact chunk sizes.
   * - ``-caseSensitive``
     - Optional
     - ``false``
     - 
     - If ``true``, keeps table name uppercase and lowercase characters when table is created in SQreamDB
   * - ``-checkCdcChain``
     - Optional
     - ``false``
     - 
     - Check CDC chain between tracking table and source table 
   * - ``-chunkSize``
     - Optional
     - ``0``
     - 
     - The number of records read at once from the source database
   * - ``columnListFilePath``
     - Optional
     - 
     - ``.txt``
     - The name of the file that contains all column names. Columns must be separated using ``\n``. Expected file type is ``.txt`` 
   * - ``-columns``
     - Optional
     - All columns
     - 
     - The name or names of columns to be loaded into SQreamDB ("col1,col2, ..."). For column names containing uppercase characters, maintain the uppercase format, avoid using double quotes or apostrophes, and ensure that the ``caseSensitive`` parameter is set to true
   * - ``-configDir``
     - Optional
     - ``java -jar target/sqloaderService-8.0.jar --configDir=</path/to/directory/>``
     - 
     - Defines the path to the folder containing both the data type mapping and the reserved words files. The defined folder must contain both files or else you will receive an error. This flag affects the mapping and reserved words files and does not affect the properties file 
   * - ``-count``
     - Optional
     - ``true``
     - 
     - Defines whether or not table rows will be counted before being loaded into SQreamDB 
   * - ``-cdcDelete``
     - Optional
     - ``true``
     - 
     - Defines whether or not loading using Change Data Capture (CDC) includes deleted rows
   * - ``-drop``
     - Optional
     - ``true``
     - 
     - Defines whether or not a new target table in SQreamDB is created. If ``false``, you will need to configure a target table name using the ``-target`` parameter
   * - ``-fetchSize``
     - Optional
     - ``100000``
     - 
     - The number of records to be read at once from source database. 
   * - ``-filter``
     - Optional
     - ``1=1``
     - 
     - Defines whether or not only records with SQL conditions are loaded
   * - ``-h, --help``
     - Optional
     - 
     - 
     - Displays the help menu and exits
   * - ``-limit``
     - Optional
     - ``0`` (no limit)
     - 
     - Limits the number of rows to be loaded
   * - ``-loadDttm``
     - Optional
     - ``true``
     - 
     - Add an additional ``load_dttm`` column that defines the time and date of loading
   * - ``-lockCheck``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader will check source table is locked before the loading starts
   * - ``-lockTable``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader will lock target table before the loading starts
   * - ``-log_dir``
     - Optional
     - ``logs``
     - ``java -jar -DLOG_DIR=/path/to/log/directory target/sqloaderService-8.0.jar``
     - Defines the path of log directory created when loading data. If no value is specified, a ``logs`` folder is created under the same location as the ``sqloader.jar`` file 
   * - ``-partitionName``
     - Optional
     - 
     - Partition identifier ``string``
     - Specifies the number of table partitions. If configured, ``-partition`` ensures that data is loaded according to the specified partition. You may configure the ``-thread`` parameter for parallel loading of your table partitions. If you do, please ensure that the number of threads does not exceed the number of partitions.
   * - ``-rowid``
     - Optional
     - ``false``
     - 
     - Defines whether or not SQLoader will get row IDs from Oracle tables
   * - ``-sourceDatabaseName``
     - Optional
     - ``ORCL``
     - 
     - Defines the source database name. It does not modify the database connection string but impacts the storage and retrieval of data within catalog tables.
   * - ``-splitByColumn``
     - Optional
     - 
     - Column name ``string``
     - Column name for split (required for multi-thread loads)
   * - ``-sourceTable``
     - Mandatory
     - 
     - Table name ``string``
     - Source table name to load data from
   * - ``-sqreamTable``
     - Optional
     - Target table name
     - Table name ``string``
     - Target table name to load data into
   * - ``-threadCount``
     - Optional
     - ``1``
     - 
     - Number of threads to use for loading. Using multiple threads can significantly improve the loading performance, especially when dealing with columns that have metadata statistics (e.g., min/max values). SQLoader will automatically divide the data into batches based on the specified thread number, allowing for parallel processing. You may use ``-thread`` both for tables that are partitioned and tables that are not. See :ref:`Sizing Guidelines<sqloader_thread_sizing_guidelines>`
   * - ``-truncate``
     - Optional
     - ``false``
     - 
     - Truncate target table before loading
   * - ``-loadTypeName``
     - Optional
     - ``full``
     - 
     - Defines a loading type that affects the table that is created in SQreamDB. Options are ``full``, ``cdc``, or ``inc``. Please note that ``cdc``, and ``inc`` are supported only for Oracle
   * - ``-useDbmsLob``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader uses ``dbms_lob_substr`` function for ``CLOB`` and ``BLOB`` data types
   * - ``-usePartitions``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader uses partitions in ``SELECT`` statements
	 
-- Add new flags, review new description and CamelCase for all flags. 
-- All new flags are optional 

Using the ``type`` Parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the ``type`` parameter you may define a loading type that affects the table that is created in SQreamDB. 

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
	 
Using the SQLoader Java Service Web Interface
==================================================

The SQLoader Admin Server is a web-based administration tool specifically designed to manage and monitor the SQLoader service. It provides a user-friendly interface for monitoring data loading processes, managing configurations, and troubleshooting issues related to data loading into SQreamDB.

Initiating SQLoader Service Web Interface
-----------------------------------------

.. code-block::

	java -jar sqloader-admin-server-0.0.1-SNAPSHOT.jar --server.port=<PORT> Default 7070
	
The SQLoader Service should utilize the ``--spring.boot.admin.client.url`` flag to connect to the admin server.

Example:

.. code-block::

	java -jar sqloaderService-8.0.jar --spring.boot.admin.client.url=http://localhost:7070

Grouping Services
-----------------

Hazelcast cluster name refers to a group of interconnected Hazelcast instances across different JVMs or machines. By default, these instances automatically connect to the same cluster on the network, enabling all SQLoader services within a network to connect to each other and share the same queue. To exert control over how services are grouped, you can use the ``--hzClusterName=<TEXT>`` flag.

Example:

.. code-block::


SQLoader Service Web Interface Features
---------------------------------------

* Monitor Services:

	* Health Checks: Monitor the health status of services to ensure they are functioning properly.
	* Metrics: Monitor real-time performance metrics, including CPU usage, memory usage, and response times.
	* Logging: View logs generated by services for troubleshooting and debugging purposes, and dynamically modify log levels during runtime to adjust verbosity for troubleshooting or performance monitoring.
	
* Manage Active Load Requests:

	* View a list of currently active data loading requests, including their status, progress, and relevant metadata.

Creating Summary Tables
========================

Summary tables are pre-aggregated tables that store summarized or aggregated data, which can help improve query performance and reduce the need for complex calculations during runtime. 

Summary tables are part of the schema within the database catalog.

Creating a Summary Table
--------------------------

This summary table uses Oracle syntax. 

Moving to SQLoader service, add the following column:

.. code-block: sql

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


Creating a Change Data Capture Table
--------------------------------------

Change Data Capture (CDC) tables are supported only for Oracle.

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

The **SQLoader** automatically maps data types used in  Oracle, Postgresql, Teradata, Microsoft SQL Server, and SAP HANA tables that are loaded into SQreamDB.

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
^^^^^^^^^^^

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

SAP HANA
^^^^^^^^^
	 
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
		
.. code-block:: json
	
		{
		  "type": ["char","nchar","varchar","varchar2","nvarchar","nvarchar2","character"],
		  "sqream": "text",
		  "java": "string",
		  "length": true
		},
		{
		  "type": ["date","datetime"],
		  "sqream": "datetime",
		  "java": "datetime",
		  "length": false
		},
		{
		  "type": ["timestamp"],
		  "sqream": "datetime",
		  "java": "timestamp",
		  "length": false
		},
		{
		  "type": ["date"],
		  "sqream": "date",
		  "java": "datetime",
		  "length": false
		},
		{
		  "type": ["boolean"],
		  "sqream": "bool",
		  "java": "boolean",
		  "length": false
		},
		{
		  "type": ["number"],
		  "sqream": "numeric",
		  "java": "bigdecimal",
		  "length": true,
		  "prec": true
		},
		{
		  "type": ["float","double"],
		  "sqream": "double",
		  "java": "double",
		  "length": false
		},
		{
		  "type": ["clob"],
		  "sqream": "text",
		  "java": "clob",
		  "length": false
		},
		{
		  "type": ["blob"],
		  "sqream": "text",
		  "java": "blob",
		  "length": false
		}
	  ]
	}
	 
CLI Examples
============

Loading data into a CDC table using the ``type`` and ``limit`` parameters:

.. code-block:: console 

	java -jar sqloader.jar -table source_table_name -type cdc -limit 100

Loading data into a table using your own configuration file (this will override the default configuration file):

.. code-block:: console

	java -jar sqloader.jar -config path/to/your/config/file
	
Loading data into a table using a custom configuration file:

.. code-block:: console

	java -jar -config MyConfigFile.properties -table source_table_name -type cdc -target target_table_name -drop true -lock_check false

Loading data into a table using a the ``filter`` parameter:

.. code-block:: console

	java -jar sqloader.jar -table source_table_name -filter column_name>50
