.. _ingesting_from_databases:

*********************
SQLoader As a Process
*********************

The **SQLoader** is a CLI program that enables you to load data into SQreamDB from other DBMS and DBaaS.

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
-----------------------------

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
-----------------

The SQLoader sizing is determined by the number of concurrent tables and threads based on the available CPU cores, limiting it to the number of cores minus one, with the remaining core reserved for the operating system. Each SQLoader instance runs on a single table, meaning concurrent imports of multiple tables require multiple instances. Additionally, when dealing with partitioned tables, each partition consumes a thread, so users should consider the table's partition count when managing thread allocation for efficient performance.

---------------------------------

Installation and Connection
===========================

Getting the SQLoader Configuration and JAR Files
------------------------------------------------

1. Download the ``.tar`` file using the following command:

   .. code-block:: console

	  curl -O https://sq-ftp-public.s3.amazonaws.com/sqloader-v7.12.tar

2. Extract the ``.tar`` file using the following command:

   .. code-block:: console

	   tar -xf sqloader-7.12.tar.gz

   A folder named ``sqloader`` with the following files is created:
   
.. list-table::
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
   
Establishing a Connection
-------------------------

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

.. literalinclude:: connection_string.ini
    :language: ini
    :caption: Properties File Sample
    :linenos:
	
Starting SQLoader
-----------------

To start SQLoader, run the ``sqloader.jar`` file:

.. code-block:: console

	java -jar sqloader.jar

---------------------------------

Loading Data into SQreamDB
==========================
	
To load data into SQreamDB using SQLoader, you must specify a source table name at minimum. Executing the command below will generate a SQreamDB table using the specified source table's DDL and load all its data:

.. code-block:: console 

	java -jar sqloader.jar -table <source_table_name>
	
.. contents:: 
   :local:
   :depth: 1
	
Customizing Data Load
---------------------
	
While specifying a source table name is mandatory for data loading, you have the option to customize the loading process by utilizing *optional* parameters. These parameters can be configured either within a CLI command or by adjusting settings in the properties file. 

Please note that any customization done through the CLI will override configurations made using the properties file.

.. list-table:: SQLoader CLI Parameters
   :widths: auto
   :header-rows: 1
   
   * - CLI Parameter
     - State
     - Default
     - Type 
     - Description
   * - ``-batchsize``
     - Optional
     - ``10.000``
     - 
     - The number of records to be inserted into SQreamDB at once. Please note that the configured batch size may impact chunk sizes
   * - ``-casesensative``
     - Optional
     - ``false``
     - 
     - If ``true``, keeps table name uppercase and lowercase characters when table is created in SQreamDB
   * - ``-check_cdc_chain``
     - Optional
     - ``false``
     - 
     - Check CDC chain between tracking table and source table 
   * - ``-chunkSize``
     - Optional
     - ``0``
     - 
     - The number of records read at once from the source database
   * - ``-columnlist``
     - Optional
     - *None*
     - ``.txt``
     - The name of the file that contains all column names. Columns must be separated using ``\n``
   * - ``-columns``
     - Optional
     - All columns
     - 
     - The name or names of columns to be loaded into SQreamDB ("col1,col2, ..."). For column names containing uppercase characters, maintain the uppercase format, avoid using double quotes or apostrophes, and ensure that the ``caseSensitive`` parameter is set to true
   * - ``-config``
     - Optional
     - ``/home/username/downloads/config/sqload-jdbc.properties``
     - 
     - Defines the path to the configuration file you wish to use. This parameter may be defined using only the CLI
   * - ``-config_dir``
     - Optional
     - ``/home/username/downloads/config``
     - 
     - Defines the path to the folder containing both the data type mapping and the reserved words files. The defined folder must contain both files or else you will receive an error
   * - ``-count``
     - Optional
     - ``true``
     - 
     - Defines whether or not table rows will be counted before being loaded into SQreamDB 
   * - ``-delete``
     - Optional
     - ``true``
     - 
     - Defines whether or not loading using Change Data Capture (CDC) includes deleted rows
   * - ``-drop``
     - Optional
     - ``true``
     - 
     - 
	 Assuming we're loading into table ``x``: 
	 
	 * ``true`` essentially allows for the replacement of the existing table with the newly loaded data by triggering the following actions:
	 
	   * Creating or replacing a temporary table named ``x_temp``
	   * The data you intend to load is inserted into the ``x_temp`` table
	   * If a table named ``x`` already exists, it will be renamed to ``x_old``. (If ``x`` exists as a view, the view will be dropped)
	   * The ``x_temp`` table, which now contains your loaded data, is renamed to ``x``
	   * Any previously existing table named ``x_old`` is dropped from the database
	   
	 * ``false`` (requires using ``- target``) essentially allows for appending data to an existing table without performing any deletion or replacement operations by triggering the following actions:
	 
	   * SQLoader first checks if the target table exists and raises an exception if it does not
	   * If ``truncate`` is set to false, SQLoader appends more data to the existing table without using any staging tables
	   * If ``truncate`` is set to true, a temporary table, ``x_temp``, is created based on the existing table, but no data is initially loaded. If ``x_temp`` exists, an error is raised since ``CREATE OR REPLACE`` is not used
	   * Data is loaded into the temporary table
	   * Target table is renamed to ``x_old``
	   * The temporary table ``x_temp`` is renamed to the target table name ``x``
	   * ``x_old`` is dropped
   * - ``-fetchsize``
     - Optional
     - ``100000``
     - 
     - The number of records to be read at once from source database
   * - ``-filter``
     - Optional
     - ``1=1``
     - 
     - Defines whether or not only records with SQL conditions are loaded
   * - ``-h, --help``
     - Optional
     - *No input*
     - 
     - Displays the help menu and exits
   * - ``-limit``
     - Optional
     - ``0`` (no limit)
     - 
     - Limits the number of rows to be loaded
   * - ``-load_dttm``
     - Optional
     - ``true``
     - 
     - Add an additional ``load_dttm`` column that defines the time and date of loading
   * - ``-lock_check``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader will check source table is locked before the loading starts
   * - ``-lock_table``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader will lock target table before the loading starts
   * - ``-log_dir``
     - Optional
     - ``logs``
     - 
     - Defines the path of log directory created when loading data. If no value is specified, a ``logs`` folder is created under the same location as the ``sqloader.jar`` file 
   * - ``-partition``
     - Optional
     - *None*
     - Partition identifier ``string``
     - Specifies the number of table partitions. If configured, ``-partition`` ensures that data is loaded according to the specified partition. You may configure the ``-thread`` parameter for parallel loading of your table partitions. If you do, please ensure that the number of threads does not exceed the number of partitions
   * - ``-rowid``
     - Optional
     - ``false``
     - 
     - Defines whether or not SQLoader will get row IDs from Oracle tables
   * - ``-source_db``
     - Optional
     - ``ORCL``
     - 
     - Defines the source database name. It does not modify the database connection string but impacts the storage and retrieval of data within catalog tables
   * - ``-split``
     - Optional
     - *None*
     - Column name ``string``
     - Column name for split (required for multi-thread loads)
   * - ``-table``
     - Mandatory
     - *None*
     - Table name ``string``
     - Source table name to load data from
   * - ``-target``
     - Optional
     - Target table name
     - Table name ``string``
     - Target table name to load data into
   * - ``-thread``
     - Optional
     - ``1``
     - 
     - Number of threads to use for loading. Using multiple threads can significantly improve the loading performance, especially when dealing with columns that have metadata statistics (e.g., min/max values). SQLoader will automatically divide the data into batches based on the specified thread number, allowing for parallel processing. You may use ``-thread`` both for tables that are partitioned and tables that are not. See :ref:`Sizing Guidelines<sqloader_thread_sizing_guidelines>`
   * - ``-truncate``
     - Optional
     - ``false``
     - 
     - Truncate target table before loading
   * - ``-type``
     - Optional
     - ``full``
     - 
     - Defines a loading type that affects the table that is created in SQreamDB. Options are: 
	 
	* ``full``: The entire data of the source table is loaded into SQreamDB
	
	* ``cdc`` (Change Data Capture): Only changes made to the source table data since last load will be loaded into SQreamDB. Changes include transactions of ``INSERT``, ``UPDATE``, and ``DELETE`` statements. SQLoader recognizes tables by table name and metadata
	
	* ``inc``: Only changes made to the source table data since last load will be loaded into SQreamDB. Changes include transactions of ``INSERT`` statement. SQLoader recognizes the table by table name and metadata
	Please note that ``cdc``, and ``inc`` are supported only for Oracle
   * - ``-use_dbms_lob``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader uses ``dbms_lob_substr`` function for ``CLOB`` and ``BLOB`` data types
   * - ``-use_partitions``
     - Optional
     - ``true``
     - 
     - Defines whether or not SQLoader uses partitions in ``SELECT`` statements
	  
Data Types and Mapping 
----------------------

SQLoader automatically assigns data types during the data loading process. Nevertheless, you retain the choice to manually specify the preferred data type you want to map to during the loading operation.

.. contents:: 
   :local:
   :depth: 1

Automatic Mapping
^^^^^^^^^^^^^^^^^

Oracle
"""""" 

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
""""""""""

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
""""""""

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
""""""""""""""""""""

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
""""""""
	 
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
	 
Manual Mapping
^^^^^^^^^^^^^^

You have the possibility to adjust the SQLoader mapping process according to your specific needs using the ``names`` Method.

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
	 
---------------------------------	 
	 
Creating Summary Tables
=======================

Summary tables are pre-aggregated tables that store summarized or aggregated data, which can help improve query performance and reduce the need for complex calculations during runtime. 

Summary tables are part of the schema within the database catalog.

Examples
--------

The following examples use Oracle syntax. 

A Summary Table
^^^^^^^^^^^^^^^

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
    HOST VARCHAR2(200) DEFAULT NULL
  );


Change Data Capture Summary Tables
----------------------------------

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

-------------------------------------------------------
	
CLI Examples
============

Loading data into a CDC table using the ``type`` and ``limit`` parameters:

.. code-block:: console 

	java -jar sqloader.jar -table <source_table_name> -type cdc -limit 100

Loading data into a table using your own configuration file (this will override the default configuration file):

.. code-block:: console

	java -jar sqloader.jar -config path/to/your/config/file
	
Loading data into a table using a custom configuration file:

.. code-block:: console

	java -jar -config MyConfigFile.properties -table <source_table_name> -type cdc -target <target_table_name> -drop true -lock_check false

Loading data into a table using a the ``filter`` parameter:

.. code-block:: console

	java -jar sqloader.jar -table <source_table_name> -filter column_name>50
	
	
	
.. toctree::
   :maxdepth: 1
   :glob:
   
   preparing_oracle_for_data_migration
