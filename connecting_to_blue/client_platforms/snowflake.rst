:orphan:

.. _snowflake:

**********************
Snowflake Connectivity
**********************



Syntax
======

.. code-block:: postgres

	CREATE [ OR REPLACE ] FOREIGN TABLE [schema_name].table_name (
	  { column_def [, ...] }
	   )
	  [ FOREIGN DATA ] WRAPPER snowflake_fdw
	  [ OPTIONS ( option_def [, ...  ] ) ]

	option_def ::=
	{
	  ACCOUNT_NAME = '<account_name>',
	  USER = '<username>',
	  PASSWORD = '<password>',
	  SFWAREHOUSE = '<warehouse_name>',
	  DATABASE = '<database_name>',
	  DBTABLE = '<table_name>',
	  [ SCHEMA = '<schema_name>' ] /* Optional - will use default schema "public" if not specified. */
	}

	column_def ::=
	{ column_name type_name [ default ] [ column_constraint ] }

	column_constraint ::=
	{ NOT NULL | NULL }

	default ::=
	DEFAULT default_value
	| IDENTITY [ ( start_with [ , increment_by ] ) ]
		
	schema_name ::= identifier

	table_name ::= identifier
	
	column_name ::= identifier
		
.. code-block:: postgres
		
	DROP TABLE [ IF EXISTS ] [schema_name.]table_name

	schema_name ::= identifier

	table_name ::= identifier

.. code-block:: postgres

	COPY { [schema_name].table_name [ ( column_name [, ... ] ) ] | query } TO
	[FOREIGN DATA] WRAPPER 
	  snowflake_fdw
	OPTIONS
	 (
	  [ copy_to_option [, ...] ]
	 )

	copy_to_option ::=
	{
	  ACCOUNT_NAME = '<account name>',
	  USER = '<username>',
	  PASSWORD = '<password>',
	  SFWAREHOUSE = '<warehouse_name>',
	  DATABASE = '<database_name>',
	  DBTABLE = '<table_name>',
	  NEW_TABLE = <TRUE | FALSE>,
	  [ SCHEMA = '<schema_name>' ] /* Optional - will use default schema "public" if not specified. */
	}

	column_name ::= identifier
	
	schema_name ::= identifer

	table_name ::= identifier

.. code-block:: postgres

	COPY 
	  [ "<schema_name>". ]"<table_name>" [ (<column_name>) [ ,...] ]
	FROM 
	[FOREIGN DATA] WRAPPER 
	  <fdw_name>
	OPTIONS
	(
	  ACCOUNT_NAME = '<account name>',
	  USERNAME = '<username>',
	  PASSWORD = '<password>',
	  SF_WAREHOUSE = '<warehouse_name>',
	  SCHEMA = '<schema_name>',
	  DATABASE = '<database_name>',
	  DB_TABLE = '<table_name>'
	  );

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the Snowflake schema where the table to be imported is located
   * - ``table_name``
     - The name of the Snowflake table you wish to import
   * - ``account_name``
     - Snowflake account name
   * - ``user``
     - Snowflake username 
   * - ``password``
     - Snowflake password
   * - ``sfWarehouse``
     - The name of the Snowflake warehouse where the table to be imported is located
   * - ``database``
     - The name of the Snowflake database where the table to be imported is located
   * - ``schema``
     - The name of the Snowflake schema where the table to be imported is located
   * - ``dbtable``
     - The name of the Snowflake table to be imported
   * - ``column_name``
     - The name of the columns in the Snowflake table to be imported
   * - ``type_name``
     - The column data type in the Snowflake table to be imported
   * - ``new_table``
     - Specifies whether or not the ``COPY TO`` command creates a new table upon execution. ``TRUE`` = create a new table and ``FALSE`` = copy data into an existing table. The default is ``FALSE``

Usage Notes
===========

.. glossary::

   ``new_table``

      The newly created table will be created within the schema specified under ``option_def``. 

   Communication
   
      Communication with Snowflake web server requires SSL.
	 
Data Types Mapping
==================

The following Snowflake data types are not supported: ``BYTEINT``, ``BINARY``, ``VARBINARY``, ``TIMESTAMP``, ``TIME``, ``TIMESTAMP_LTZ``, ``TIMESTAMP_TZ``, ``VARIANT``, ``OBJECT``, ``GEOGRAPHY``, ``GEOMETRY`` 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - SQream Blue Data Type
     - Snowflake Data Type
   * - ``NUMERIC``
     - ``NUMERIC``, ``NUMBER``, ``DECIMAL`` 
   * - ``INT``, ``INTEGER``
     - ``INT``, ``INTEGER``
   * - ``BIGINT``, ``NUMBER``
     - ``BIGINT``
   * - ``SMALLINT``
     - ``SMALLINT``
   * - ``TINYINT``
     - ``TINYINT``
   * - ``DOUBLE``
     - ``FLOAT``
   * - ``REAL``
     - ``FLOAT4``
   * - ``DOUBLE``
     - ``FLOAT8``
   * - ``TEXT``
     - ``VARCHAR``, ``CHAR``, ``CHARACTER``, ``STRING``, ``TEXT``
   * - ``BOOL``
     - ``BOOLEAN``	
   * - ``DATE``
     - ``DATE``
   * - ``DATETIME``
     - ``DATETIME``
   * - ``DATETIME``
     - ``TIMESTAMP_NTZ``
   * - ``ARRAY``
     - ``ARRAY``		 
	 
Examples
========

Creating a Table
----------------

.. code-block:: postgres

	CREATE OR REPLACE FOREIGN TABLE snowflake_table
	( 
	  id BIGING,
	  address TEXT,
	  purchase DOUBLE
	)
	WRAPPER snowflake_fdw
	OPTIONS 
	 (
	  ACCOUNT_NAME 'my sf account'
	  DBTABLE 'my_customers',
	  USER 'JohnSmith',
	  PASSWORD 'pa$$w0rD',
	  DATABASE 'master',
	  SCHEMA 'public',
	  SFWAREHOUSE 'my_sf_warehouse'
	);
	
Joining Blue and Snowflake Tables
---------------------------------

.. code-block:: postgres

	SELECT
	  *
	FROM
	  snowflake_table sft
	  JOIN table1 t1 ON sft.id = t1.id
	WHERE
	  sft.date >= '2022-01-01'
	  AND t1.status = 'active';
	  
Copying Data Into a Blue Table 
------------------------------

.. code-block:: postgres

	COPY
	  t TO
	WRAPPER
	  snowflake_fdw
	OPTIONS
	 (
	  ACCOUNT_NAME 'my sf account',
	  DBTABLE 'my_customers',
	  USER 'JohnSmith',
	  PASSWORD 'pa$$w0rD',
	  DATABASE 'master',
	  SCHEMA 'public',
	  SFWAREHOUSE 'my_sf_warehouse',
	  NEW_TABLE = TRUE
	 );
	 
	 
	 
.. code-block:: postgres

	COPY
	  customers
	FROM
	WRAPPER
	  snowflake_fdw
	OPTIONS
	(
	  ACCOUNT_NAME = 'my sf account',
	  USERNAME = 'JohnSmith',
	  PASSWORD = 'pa$$w0rD',
	  SF_WAREHOUSE = 'my_sf_warehouse',
	  SCHEMA = 'public',
	  DATABASE = 'master',
	  DB_TABLE = 'my_customers'
	  );