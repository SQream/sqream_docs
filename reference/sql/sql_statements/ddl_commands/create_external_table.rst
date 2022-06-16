.. _create_external_table:

***********************
CREATE EXTERNAL TABLE
***********************

.. warning:: 
   
   The ``CREATE EXTERNAL TABLE`` syntax is deprecated, and will be removed in future versions.
   
   Starting with SQream DB v2020.2, external tables have been renamed to :ref:`foreign tables<create_foreign_table>`, and use a more flexible foreign data wrapper concept. See :ref:`create_foreign_table` instead.
   
   Upgrading to a new version of SQream DB converts existing tables automatically. When creating a new external tables, use the new foreign table syntax.


The ``CREATE TABLE`` command creates a new external table in an existing database.

.. tip::

   * Data in an external table can change if the sources change, and frequent access to remote files may harm performance.

   * To create a regular table, see :ref:`CREATE TABLE <create_table>`
   
For more information, see :ref:`External tables guide<external_tables>`.

The **CREATE EXTERNAL TABLE** page describes the following:

Syntax
==========
The following is the correct syntax for CREATE_EXTERNAL_TABLE:

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] EXTERNAL TABLE [schema_name].table_name (
           { column_def [, ...] }
       )
       USING FORMAT format_def
       WITH { external_table_option [ ...] }
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

   format_def ::= { PARQUET | ORC | CSV }
   
   external_table_option ::= {
      PATH '{ path_spec }' 
      | FIELD DELIMITER '{ field_delimiter }'
      | RECORD DELIMITER '{ record_delimiter }'
      | AWS_ID '{ AWS ID }'
      | AWS_SECRET '{ AWS SECRET }'
   }
   
   path_spec ::= { local filepath | S3 URI | HDFS URI }
   
   field_delimiter ::= delimiter_character
   
   record_delimiter ::= delimiter_character
      
   column_def ::= { column_name type_name [ default ] [ column_constraint ] }

   column_name ::= identifier
   
   column_constraint ::=
       { NOT NULL | NULL }
   
   default ::=
   
       DEFAULT default_value
       | IDENTITY [ ( start_with [ , increment_by ] ) ]

.. _cet_parameters:

Parameters
============
The following table shows the CREATE_EXTERNAL_TABLE parameters:

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
   * - ``USING FORMAT ...``
     - Specifies the format of the source files, such as ``PARQUET``, ``ORC``, or ``CSV``.
   * - ``WITH PATH ...``
     - Specifies a path or URI of the source files, such as ``/path/to/*.parquet``.
   * - ``FIELD DELIMITER``
     - Specifies the field delimiter for CSV files. Defaults to ``,``.
   * - ``RECORD DELIMITER``
     - Specifies the record delimiter for CSV files. Defaults to a newline, ``\n``
   * - ``AWS_ID``, ``AWS_SECRET``
     - Credentials for authenticated S3 access


Examples
===========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1
   
Creating a Simple Table from a Tab-Delimited File
----------------------------------------------
The following example shows how to create a simple table from a **tab-delimited file (TSV)**:

.. code-block:: postgres

   CREATE OR REPLACE EXTERNAL TABLE cool_animals
     (id INT NOT NULL, name TEXT NOT NULL, weight FLOAT NOT NULL)  
   USING FORMAT csv 
   WITH  PATH  '/home/rhendricks/cool_animals.csv'
         FIELD DELIMITER '\t';


Creating a Table from a Directory of Parquet Files on HDFS
-----------------------------------------------------
The following example shows how to create a table from a directory of Parquet files on HDFS:

.. code-block:: postgres

   CREATE EXTERNAL TABLE users
     (id INT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL)  
   USING FORMAT Parquet
   WITH  PATH  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet';

Creating a Table from a Bucket of Files on S3
--------------------------------------
The following example shows how to create a table from a bucket of files on S3:

.. code-block:: postgres

   CREATE EXTERNAL TABLE users
     (id INT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL)  
   USING FORMAT Parquet
   WITH  PATH  's3://pp-secret-bucket/users/*.parquet'
         AWS_ID 'our_aws_id'
         AWS_SECRET 'our_aws_secret';

Changing an External Table into a Regular Table
------------------------------------------------
The following example shows how to change an external table into a regular table:

.. code-block:: postgres

   CREATE TABLE real_table
    AS SELECT * FROM external_table;

.. tip: Using an external table allows you to perform ETL-like operations in SQream DB by applying SQL functions and operations to raw files.

Permissions
=============
The role must have the ``CREATE`` permission at the database level.