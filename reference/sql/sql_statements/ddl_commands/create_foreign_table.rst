.. _create_foreign_table:

***********************
CREATE FOREIGN TABLE
***********************

``CREATE FOREIGN TABLE`` creates a new foreign table in an existing database.

Changes in the source data can result in corresponding modifications to the content of a foreign table. Consistent access to remote files might impact performance.

Permissions
=============

The role must have the ``CREATE`` permission at the database level.

Syntax
==========

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] FOREIGN TABLE [schema_name].table_name (
           { column_def [, ...] }
       )
       [ FOREIGN DATA ] WRAPPER fdw_name
       [ OPTIONS ( option_def [, ...  ] ) ]
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

   fdw_name ::= 
       { csv_fdw | orc_fdw | parquet_fdw | json_fdw | avro_fdw }
   
   option_def ::= 
   {
      LOCATION = '{ path_spec }',
      | DELIMITER = '{ field_delimiter }' -- for CSV only,
      | RECORD_DELIMITER = '{ record_delimiter }', -- for CSV only
      | AWS_ID '{ AWS ID }',
      | CONTINUE_ON_ERROR = { true | false }
      | ERROR_COUNT = '{ error count }'
      | AWS_SECRET '{ AWS SECRET }',
      | OFFSET -- for CSV and JSON only
   }
   
   path_spec ::= { local filepath | S3 URI | HDFS URI }
   
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
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally
   * - ``WRAPPER ...``
     - Specifies the format of the source files, such as ``parquet_fdw``, ``orc_fdw``, or ``csv_fdw``
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
     - Specifies if errors should be ignored or skipped. When set to ``true``, the transaction will continue despite rejected data. This parameter should be set together with ``ERROR_COUNT`` When reading multiple files, if an entire file can’t be opened it will be skipped. Default value: ``false``. Value range: ``true`` or ``false``.
   * - ``ERROR_COUNT``
     - Specifies the threshold for the maximum number of faulty records that will be ignored. This setting must be used in conjunction with ``CONTINUE_ON_ERROR``. Default value: ``unlimited``. Value range: 1 to 2147483647.
	 


Examples
===========

A simple table from Tab-delimited file (TSV)
----------------------------------------------

.. code-block:: postgres

   CREATE OR REPLACE FOREIGN TABLE cool_animals
     (id INT NOT NULL, name text(30) NOT NULL, weight FLOAT NOT NULL)  
   WRAPPER csv_fdw
   OPTIONS
     ( LOCATION = '/home/rhendricks/cool_animals.csv',
       DELIMITER = '\t'
     )
    ;


A table from a directory of Parquet files on HDFS
-----------------------------------------------------

.. code-block:: postgres

   CREATE FOREIGN TABLE users
     (id INT NOT NULL, name text(30) NOT NULL, email text(50) NOT NULL)  
   WRAPPER parquet_fdw
   OPTIONS
     (
       LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

A table from a bucket of ORC files on S3
------------------------------------------

.. code-block:: postgres

   CREATE FOREIGN TABLE users
     (id INT NOT NULL, name text(30) NOT NULL, email text(50) NOT NULL)  
   WRAPPER orc_fdw
   OPTIONS
     (
         LOCATION = 's3://pp-secret-bucket/users/*.orc',
         AWS_ID = 'our_aws_id',
         AWS_SECRET = 'our_aws_secret'
      );


Changing a foreign table to a regular table
------------------------------------------------

Materializes a foreign table into a regular table.

.. tip: Using a foreign table allows you to perform ETL-like operations in SQream DB by applying SQL functions and operations to raw files

.. code-block:: postgres

   CREATE TABLE real_table
    AS SELECT * FROM some_foreign_table;
	
Using the ``OFFSET`` Parameter
--------------------------------

The ``OFFSET`` parameter may be used with Parquet and CSV textual formats. 

.. code-block::

	CREATE FOREIGN TABLE users7
	  (id INT NOT NULL, name text(30) NOT NULL, email text(50) NOT NULL)
	WRAPPER parquet_fdw
	OPTIONS
	  (
	    LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet',
	    OFFSET = 2
	  );

Using the ``CONTINUE_ON_ERROR`` and ``ERROR_COUNT`` Parameters
----------------------------------------------------------------

.. code-block::

	CREATE OR REPLACE FOREIGN TABLE cool_animalz
	  (id INT NOT NULL, name text(30) NOT NULL, weight FLOAT NOT NULL)
	WRAPPER csv_fdw
	OPTIONS
	  ( LOCATION = '/home/rhendricks/cool_animals.csv',
		DELIMITER = '\t',
		continue_on_error = true,
		ERROR_COUNT = 3
	  )
	 ;