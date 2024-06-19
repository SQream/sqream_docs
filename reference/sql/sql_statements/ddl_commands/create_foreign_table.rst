.. _create_foreign_table:

********************
CREATE FOREIGN TABLE
********************

``CREATE FOREIGN TABLE`` creates a new foreign table in an existing database.

Syntax
======

.. code-block:: postgres

	CREATE [ OR REPLACE ] FOREIGN TABLE [ "<schema_name>" ]."<table_name>" (
	  [ column_def [, ...] ] -- When creating foreign tables using CSV source files, it is mandatory to provide the complete table DDL
	)
	  [ FOREIGN DATA ] WRAPPER fdw_name
	  [ OPTIONS ( option_def [, ...  ] ) ]

	fdw_name ::= 
	  { csv_fdw | orc_fdw | parquet_fdw }
   
	option_def ::= 
	  LOCATION = '{ path_spec }'
	 [
	  | DELIMITER = '{ field_delimiter }' -- for CSV only
	  | RECORD_DELIMITER = '{ record_delimiter }' -- for CSV only
	  | AWS_ID '{ AWS ID }'
	  | AWS_SECRET '{ AWS SECRET }'
	  | QUOTE = {'C' | E'\ooo') -- for CSV only	  
	 ]
   
	path_spec ::= { GS URI | S3 URI | HDFS URI }
   
	field_delimiter ::= delimiter_character
   
	record_delimiter ::= delimiter_character
      
	column_def ::= 
	  { column_name type_name [ default ] [ column_constraint ] }

	column_name ::= identifier
   
	column_constraint ::=
	  { NOT NULL | NULL }
   
	default ::=
	  DEFAULT default_value
	  | IDENTITY [ ( start_with [ , increment_by ] ) ]

.. _cft_parameters:

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``OR REPLACE``
     - Create a new table, and overwrite any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check the table contents or structure, only the table name
   * - ``schema_name``
     - The name of the schema in which to create the table
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name and datatype. Other column constraints and default values may optionally be added. When creating foreign tables using CSV source files, it is mandatory to provide the complete table DDL
   * - ``WRAPPER ...``
     - Specifies the format of the source files, such as ``parquet_fdw``, ``orc_fdw``, ``json_fdw``, or ``csv_fdw``
   * - ``LOCATION = ...``
     - Specifies a path or URI of the source files, such as ``/path/to/*.parquet``
   * - ``DELIMITER = ...``
     - Specifies the field delimiter for CSV files. Defaults to ``,``
   * - ``RECORD_DELIMITER = ...``
     - Specifies the record delimiter for CSV files. Defaults to a newline, ``\n``
   * - ``AWS_ID``, ``AWS_SECRET``
     - Credentials for authenticated S3 access
   * - ``OFFSET``
     - Used to specify the number of rows to skip from the beginning of the result set
   * - ``CONTINUE_ON_ERROR``
     - Specifies if errors should be ignored or skipped. When set to ``true``, the transaction continues despite rejected data and rows containing partially faulty data are skipped entirely. This parameter should be set together with ``ERROR_COUNT``. When reading multiple files, if an entire file can’t be opened it will be skipped. Default value: ``false``. Value range: ``true`` or ``false``
   * - ``ERROR_COUNT``
     - Specifies the threshold for the maximum number of faulty records that will be ignored. This setting must be used in conjunction with ``CONTINUE_ON_ERROR``. Default value: ``unlimited``. Value range: 1 to 2147483647
   * - ``QUOTE``
     - Specifies an alternative quote character. The quote character must be a single, 1-byte printable ASCII character, and the equivalent octal syntax of the copy command can be used. The quote character cannot be contained in the field delimiter, the record delimiter, or the null marker. QUOTE can be used with ``csv_fdw`` in ``COPY FROM`` and foreign tables. The following characters cannot be an alternative quote character: ``"-.:\\0123456789abcdefghijklmnopqrstuvwxyzN"``
	 
Usage Notes
===========

The automatic foreign table DDL resolution feature supports Parquet, ORC, JSON, and Avro files, while using it with CSV files generates an error. You can activate this feature when you create a foreign table by omitting the column list, described in the **Syntax** section below.

Using this feature the path you specify in the ``LOCATION`` option must point to at least one existing file. If no files exist for the schema to read, an error will be generated. You can specify the schema manually even in the event of the error above.

.. note:: When using this feature, SQream assumes that all files in the path use the same schema.

Examples
========

Creating a Tab-Delimited Table
------------------------------

.. code-block:: postgres

	CREATE
	OR REPLACE FOREIGN TABLE nba_new(
	  "player_name" text null,
	  "team_name" text null,
	  "jersey_number" int null,
	  "position" text null,
	  "age" int null,
	  "height" text null,
	  "weight" int null,
	  "college" text null,
	  "salary" int null
	)
	WRAPPER
	  csv_fdw
	OPTIONS
	   (LOCATION = 'gs://blue_docs/nba.csv',
	   DELIMITER = '\t'
	  );


Creating a Table Located In a HDFS Directory
--------------------------------------------

.. code-block:: postgres

	CREATE FOREIGN TABLE users (
	  id INT NOT NULL,
	  name TEXT(30) NOT NULL,
	  email TEXT(50) NOT NULL
	)
	WRAPPER
	  parquet_fdw
	OPTIONS
	  (
	    LOCATION = 'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
	  );

Creating a Table Located Within a S3 Bucket of ORC Files
--------------------------------------------------------

.. code-block:: postgres

	CREATE FOREIGN TABLE users (
	  id INT NOT NULL,
	  name TEXT(30) NOT NULL,
	  email TEXT(50) NOT NULL
	)
	WRAPPER
	  orc_fdw
	OPTIONS
	  (
	    LOCATION = 's3://pp-secret-bucket/users/*.orc',
	    AWS_ID = 'our_aws_id',
	    AWS_SECRET = 'our_aws_secret'
	  );


Converting a Foreign Table to an Internal Table
-----------------------------------------------

Using a foreign table allows you to perform ETL-like operations by applying SQL functions and operations to raw files.

.. code-block:: postgres

	CREATE TABLE
	  real_table AS
	SELECT
	  *
	FROM
	  some_foreign_table;
	
Using the ``OFFSET`` Parameter
------------------------------

The ``OFFSET`` parameter may be used with Parquet and CSV textual formats. 

.. code-block::

	CREATE FOREIGN TABLE users7 (
	  id INT NOT NULL, 
	  name TEXT NOT NULL, 
	  email TEXT NOT NULL
	)
	WRAPPER
	  parquet_fdw
	OPTIONS
	  (
	    LOCATION = 'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet',
	    OFFSET = 2
	  );

Using the ``CONTINUE_ON_ERROR`` and ``ERROR_COUNT`` Parameters
----------------------------------------------------------------

.. code-block::

	CREATE
	OR REPLACE FOREIGN TABLE cool_animalz (
	  id INT NOT NULL,
	  name TEXT NOT NULL,
	  weight FLOAT NOT NULL
	)
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = '/home/rhendricks/cool_animals.csv',
	    DELIMITER = '\t',
	    CONTINUE_ON_ERROR = true,
	    ERROR_COUNT = 3
	  );
	 
Customizing Quotations Using Alternative Characters
---------------------------------------------------

.. code-block::

	CREATE
	OR REPLACE FOREIGN TABLE cool_animalz (
	  id INT NOT NULL,
	  name text(30) NOT NULL,
	  weight FLOAT NOT NULL
	)
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = '/home/rhendricks/cool_animals.csv',
	    DELIMITER = '\t',
	    QUOTE = '@'
	  );

Permissions
===========

The role must have the ``CREATE`` permission at the database level.

The automatic foreign table DDL resolution feature requires **Read** permissions.