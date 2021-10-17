.. _create_external_table:

***********************
CREATE EXTERNAL TABLE
***********************
The ``CREATE TABLE`` command creates a new external table in an existing database.

In Release `2020.2 <https://docs.sqream.com/en/latest/releases/2020.2.html>`_ external tables were renamed **foreign tables** and use a more flexible foreign data wrapper. When creating a new external tables, use the new foreign table syntax.

Note that upgrading to a new version of SQream DB converts existing tables automatically. 

.. tip::

   Data in an external table can change if the sources change, and frequent access to remote files may harm performance. Creating a regular table may avoid issues related to external tables that change. For more information, see :ref:`CREATE TABLE <create_table>`.
   
For related information, see the following:

* Foreign data wrappers - :ref:`foreign_data_wrapper`

* Creating foreign tables - :ref:`create_foreign_table`
  
* Creating foreign tables - :ref:`Foreign Tables<external_tables>`

**Comment - The content on the Foreign Tables page has to be reviewed in light of Foreign Data Wrappers. There may be duplicate content.**

Permissions
=============

The role must have the ``CREATE`` permission at the database level.

Syntax
==========
The following is the correct syntax for creating a new table:

**Comment - See comment in syntax code below:**

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
   
   -------------------------------------------
   
   -- Comment - should this section be removed?
   
   external_table_option ::= {
      PATH '{ path_spec }' 
      | FIELD DELIMITER '{ field_delimiter }'
      | RECORD DELIMITER '{ record_delimiter }'
      | AWS_ID '{ AWS ID }'
      | AWS_SECRET '{ AWS SECRET }'
	  
   -------------------------------------------

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
**Comment - This section should be removed because we want to document the three format types on the CREATE FOREIGN TABLES page, but not this page. Confirm.**

The following parameters apply to creating a new table:

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


   
* :ref:`Creating a simple table from a tab-delimited file <create_simple_table_from_tab_delimited_file>`
* :ref:`Creating a table from a directory of Parquet files on HDFS <create_table_from_directory_of_parquet_files>`
* :ref:`Creating a table from a bucket of files on S3 <create_table_from_bucket_of_files_on_s3>`
* :ref:`Creating an external table to a regular table <create_external_table_to_regular_table>`




.. _create_simple_table_from_tab_delimited_file:

Creating a Simple Table from a Tab-Delimited File
----------------------------------------------
The following is an example of creating a simple table from a tab-delimited file (TSV):

.. code-block:: postgres

   CREATE OR REPLACE EXTERNAL TABLE cool_animals
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, weight FLOAT NOT NULL)  
   USING FORMAT csv 
   WITH  PATH  '/home/rhendricks/cool_animals.csv'
         FIELD DELIMITER '\t';

.. _create_table_from_directory_of_parquet_files:

Creating a Table from a Directory of Parquet Files on HDFS
-----------------------------------------------------
The following is an example of creating a table from a directory of Parquet files on HDFS:

.. code-block:: postgres

   CREATE EXTERNAL TABLE users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)  
   USING FORMAT Parquet
   WITH  PATH  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet';

.. _create_table_from_bucket_of_files_on_s3:

Creating a Table from a Bucket of Files on S3
--------------------------------------
The following is an example of creating a table from a bucket of files on S3:

.. code-block:: postgres

   CREATE EXTERNAL TABLE users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)  
   USING FORMAT Parquet
   WITH  PATH  's3://pp-secret-bucket/users/*.parquet'
         AWS_ID 'our_aws_id'
         AWS_SECRET 'our_aws_secret';

.. _create_external_table_to_regular_table:

Changing an External Table to a Regular Table
------------------------------------------------
**Comment: "Changing" = "Converting"?**

Materializes an external table into a regular table.

**Comment - This is very strange wording. What is the exact meaning here?**

.. tip: Using an external table allows you to perform ETL-like operations in SQream DB by applying SQL functions and operations to raw files

.. code-block:: postgres

   CREATE TABLE real_table
    AS SELECT * FROM external_table;