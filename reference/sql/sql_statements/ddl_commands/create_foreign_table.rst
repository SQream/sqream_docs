.. _create_foreign_table:

***********************
CREATE FOREIGN TABLE
***********************

Overview
==============

The ``CREATE FOREIGN TABLE`` statement creates a new foreign table in an existing database.


.. note:: 
   
   Starting with SQream DB v2020.2, external tables have been renamed to foreign tables, and use a more flexible foreign data wrapper concept.
   
   Upgrading to a new version of SQream DB converts existing external tables automatically. 




.. tip::

   * Data in a foreign table can change if the sources change, and frequent access to remote files may harm performance.

   * To create a regular table, see :ref:`CREATE TABLE <create_table>`
   
For more information on foreign tables, see :ref:`Foreign tables<external_tables>`.


Permissions
=============

The role must have the ``CREATE`` permission at the database level.

Syntax
==========
The following shows the correct syntax for creating a foreign table:

**Comment - See comment in syntax below:**

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
	   
   -----------------------------------------
   
   -- I replaced what was here with this. Confirm.
   
       [ OPTIONS ( option_name = option_value [, ...  ] ) ]
       ;

   schema_name ::= identifier

   table_name ::= identifier

   option_name ::= identifier
   
   option_value ::= {identifier | literal}
   
   -----------------------------------------
   
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

Creating a Parquet Foreign Table
=================================
Syntax
---------
The following shows the correct syntax for creating a Parquet foreign table:

Example
---------
The following is an example of creating a Parquet foreign table:

Parameters
---------
The following table shows the available options for creating a Parquet table:

+-------------------------+---------------+----------+-----------+--------------------------------------------+
| **Option**              | **Mandatory** | **Read** | **Write** | **Notes**                                  |
+=========================+===============+==========+===========+============================================+
| ``location``            | Yes           | Yes      | Yes       | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``offset``              | No            | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``limit``               | No``          | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``error_log``           | No            | Yes      | No        | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``continue_on_error``   | No            | Yes      | No        |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``error_count``         | No            | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``enforce_single_file`` | No            | No       | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``max_file_size``       | No            | No       | Yes       | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``aws_id``              | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``aws_secret``          | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+




Creating an ORC Foreign Table
=================================
Syntax
---------
The following shows the correct syntax for creating a ORC foreign table:

Example
---------
The following is an example of creating a ORC foreign table:

Parameters
---------
The following table shows the available options for creating a ORC table:

+-------------------------+---------------+----------+-----------+--------------------------------------------+
| **Option**              | **Mandatory** | **Read** | **Write** | **Notes**                                  |
+=========================+===============+==========+===========+============================================+
| ``location``            | Yes           | Yes      | Yes       | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``offset``              | No            | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``limit``               | No``          | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``error_log``           | No            | Yes      | No        | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``continue_on_error``   | No            | Yes      | No        |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``error_count``         | No            | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``enforce_single_file`` | No            | No       | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``max_file_size``       | No            | No       | Yes       | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``aws_id``              | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``aws_secret``          | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+

Creating a CSV Foreign Table
=================================
Syntax
---------
The following shows the correct syntax for creating a CSV foreign table:

Example
---------
The following is an example of creating a CSV foreign table:

Parameters
---------
The following table shows the available options for creating a CSV table:

+-------------------------+---------------+----------+-----------+--------------------------------------------+
| **Option**              | **Mandatory** | **Read** | **Write** | **Notes**                                  |
+=========================+===============+==========+===========+============================================+
| ``location``            | Yes           | Yes      | Yes       | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``offset``              | No            | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``limit``               | No``          | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``error_log``           | No            | Yes      | No        | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``continue_on_error``   | No            | Yes      | No        |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``error_count``         | No            | Yes      | No        | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``enforce_single_file`` | No            | No       | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``max_file_size``       | No            | No       | Yes       | Any positive integer.                      |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``aws_id``              | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``aws_secret``          | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``delimiter``           | No            | Yes      | Yes       |                                            |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``record_delimiter``    | No            | Yes      | Yes       | ``\r``, ``\n`` or ``\r\n``.                |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``rejected_data``       | No            | Yes      | No        | File paths from all supported filesystems. |
+-------------------------+---------------+----------+-----------+--------------------------------------------+
| ``datetime_format``     | No            | Yes      | No        | See supported formats below.               |
+-------------------------+---------------+----------+-----------+--------------------------------------------+

The following list shows the supported ``datetime`` formats:

* DEFAULT
* ISO8601
* ISO8601C
* DMY
* YMD
* MDY
* YYYYMMDD
* YYYY-M-D
* YYYY/M/D
* DD-mon-YYYY
* YYYY-mon-DD



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