:orphan:

.. _snowflake:

*********
Snowflake
*********


Syntax
======

.. code-block:: postgres

	create_table_statement ::=
	    CREATE [ OR REPLACE ] FOREIGN TABLE [schema_name].table_name (
	        { column_def [, ...] }
	    )
	    [ FOREIGN DATA ] WRAPPER snowflake_fdw
	    [ OPTIONS ( option_def [, ...  ] ) ]

	schema_name ::= identifier

	table_name ::= identifier

	option_def ::=
	{
	  account_name = '{account name}'
	  user = '{ username }',
	  password = '{ password }',
	  sfWarehouse = '{ warehouse_name }'
	  database = '{ database_name }',
	  [ schema = '{ schema_name }' ], /* Optional - will use default schema "public" if not specified. */
	  dbtable = '{ table_name }'
	}

	column_def ::=
	    { column_name type_name [ default ] [ column_constraint ] }

	column_name ::= identifier

	column_constraint ::=
	    { NOT NULL | NULL }

	default ::=
	    DEFAULT default_value
	    | IDENTITY [ ( start_with [ , increment_by ] ) ]
		
	drop_table_statement ::=
	    DROP TABLE [ IF EXISTS ] [schema_name.]table_name

	table_name ::= identifier

	schema_name ::= identifier

	 COPY { [schema_name].table_name [ ( column_name [, ... ] ) ] | query }
	   TO [FOREIGN DATA] WRAPPER snowflake_fdw
	     OPTIONS
	     (
	        [ copy_to_option [, ...] ]
	     )

	 schema_name ::= identifer

	 table_name ::= identifier

	 copy_to_option ::=

	{
	  account_name = '{account name}'
	  user = '{ username }',
	  password = '{ password }',
	  sfWarehouse = '{ warehouse_name }'
	  database = '{ database_name }',
	  [ schema = '{ schema_name }' ], /* Optional - will use default schema "public" if not specified. */
	  dbtable = '{ table_name }'
	  new_table = {TRUE | FALSE}
	}

	schema_name ::= identifier

	table_name ::= identifier

	column_name ::= identifier

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - 
   * - ``table_name``
     - 
   * - ``account_name``
     - 
   * - ``user``
     - 
   * - ``password``
     - 
   * - ``sfWarehouse``
     - 
   * - ``database``
     - 
   * - ``schema``
     - 
   * - ``dbtable``
     - 
   * - ``column_name``
     - 
   * - ``type_name``
     - 
   * - ``new_table``
     - 

Usage Notes
===========

* Export, copying into an existing table or a new one will be supported, when the new_table option is set, a validation that this table doesn’t exist will take place. please note that the schema will be identical to the FDW’s schema, if it doesn’t exist in snowflake then an error will be thrown.

* If the new_table option is unset, validation that the table exist will take place, and the data will be appended.

* Please note, that the default of new_table will be set to false.

* Snowflake communication must always use SSL
	 
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
	  id biging,
	  address text,
	  purchase double
	)
	WRAPPER snowflake_fdw
	OPTIONS 
	 (
	  account_name '<account name>'
	  dbtable '<table_name>',
	  user '<username>',
	  password '<password>',
	  database '<database_name>',
	  schema '<schema_name>',
	  sfWarehouse '<warehouse_name>'
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
	  
Export Data to a New Snowflake Table
------------------------------------

.. code-block:: postgres

	COPY
	  t TO FOREIGN DATA
	WRAPPER
	  snowflake_fdw
	OPTIONS
	 (
	  account_name '{account name}' dbtable '<table_name>',
	  user '<username>',
	  password '<password>',
	  database '<database_name>',
	  schema '<schema_name>',
	  sfWarehouse '<warehouse_name>'
	 );