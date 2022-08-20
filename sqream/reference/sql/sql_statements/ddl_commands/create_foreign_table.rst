.. _create_foreign_table:

***********************
CREATE FOREIGN TABLE
***********************

.. note:: 
   
   Starting with SQream DB v2020.2, external tables have been renamed to foreign tables, and use a more flexible foreign data wrapper concept.
   
   Upgrading to a new version of SQream DB converts existing external tables automatically. 


``CREATE FOREIGN TABLE`` creates a new foreign table in an existing database.

See more in the :ref:`Foreign tables guide<external_tables>`.

.. tip::

   * Data in a foreign table can change if the sources change, and frequent access to remote files may harm performance.

   * To create a regular table, see :ref:`CREATE TABLE <create_table>`

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
       { csv_fdw | orc_fdw | parquet_fdw }
   
   option_def ::= 
   {
      LOCATION = '{ path_spec }'
      | DELIMITER = '{ field_delimiter }' -- for CSV only
      | RECORD_DELIMITER = '{ record_delimiter }' -- for CSV only
      | AWS_ID '{ AWS ID }'
      | AWS_SECRET '{ AWS SECRET }'
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
     - Create a new table, and overwrite any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check the table contents or structure, only the table name.
   * - ``schema_name``
     - The name of the schema in which to create the table.
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema.
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.
   * - ``WRAPPER ...``
     - Specifies the format of the source files, such as ``parquet_fdw``, ``orc_fdw``, or ``csv_fdw``.
   * - ``LOCATION = ...``
     - Specifies a path or URI of the source files, such as ``/path/to/*.parquet``.
   * - ``DELIMITER = ...``
     - Specifies the field delimiter for CSV files. Defaults to ``,``.
   * - ``RECORD_DELIMITER = ...``
     - Specifies the record delimiter for CSV files. Defaults to a newline, ``\n``
   * - ``AWS_ID``, ``AWS_SECRET``
     - Credentials for authenticated S3 access


Examples
===========

A simple table from Tab-delimited file (TSV)
----------------------------------------------

.. code-block:: postgres

   CREATE OR REPLACE FOREIGN TABLE cool_animals
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, weight FLOAT NOT NULL)  
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
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)  
   WRAPPER parquet_fdw
   OPTIONS
     (
       LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

A table from a bucket of ORC files on S3
------------------------------------------

.. code-block:: postgres

   CREATE FOREIGN TABLE users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)  
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

