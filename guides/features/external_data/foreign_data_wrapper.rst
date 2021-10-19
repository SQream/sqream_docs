.. _foreign_data_wrapper:

Foreign Data Wrapper
=======================================
The **Foreign Data Wrapper** page includes the following sections:

.. contents:: 
   :local:
   :depth: 1
   
Overview
----------
Foreign data is accessed using a **foreign data wrapper**. A foreign data wrapper is a library that lets you access a table or schema in one database from another. It does this by converting data from an external source, such as a Parquet file, to a format readable by SQream.

SQream supports foreign data wrappers for the following file formats:

* CSV files
* Parquet files
* ORC files

While foreign data wrappers are designed for converting data from external sources, they can also be used for importing other foreign information, such as data from external Oracle servers.

Syntax
-----------
The following is the correct syntax for creating a foreign data wrapper:

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] FOREIGN TABLE [schema_name].table_name (
           { column_def [, ...] }
       )
       [ FOREIGN DATA ] WRAPPER fdw_name
       [ OPTIONS ( option_name = option_value [, ...  ] ) ]
       ;

   schema_name ::= identifier

   table_name ::= identifier

   option_name ::= identifier
   
   option_value ::= {identifier | literal}
   



Examples
-----------
The following is an example of creating a **Parquet** foreign data wrapper:

**Comment - This is probably not the example that we want, but rather something similar to the CSV example below.**

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)
   WRAPPER parquet_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

   CREATE TABLE users AS SELECT * FROM ext_users;
   
The following is an example of creating an **ORC** foreign data wrapper:

**Comment - This is probably not the example that we want, but rather something similar to the CSV example below.**

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)
   WRAPPER orc_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

   CREATE TABLE users AS SELECT * FROM ext_users;
   
The following is an example of creating a **CSV** foreign data wrapper:

.. code-block:: postgres

 COPY [schema name.]table_name
   FROM WRAPPER fdw_name
   OPTIONS
   (
     [ copy_from_option [, ...] ]
   )
 ;

 schema_name ::= identifer

 table_name ::= identifier

 copy_from_option ::=

    LOCATION = { filename | S3 URI | HDFS URI }

    | QUOTE = {'C' | E'\ooo')

    | OFFSET = { offset }

    | LIMIT = { limit }

    | DELIMITER = '{ delimiter }'

    | RECORD_DELIMITER = '{ record delimiter }'

    | ERROR_LOG = '{ local filepath }'

    | REJECTED_DATA = '{ local filepath }'

    | CONTINUE_ON_ERROR = { true | false }

    | ERROR_COUNT = '{ error count }'

    | DATETIME_FORMAT = '{ parser format }'

    | AWS_ID = '{ AWS ID }'

    | AWS_SECRET = '{ AWS Secret }'

 offset ::= positive integer

 limit ::= positive integer

 delimiter ::= string

 record delimiter ::= string

 error count ::= integer

 parser_format ::= see supported parser table below

 AWS ID ::= string

 AWS Secret ::= string



Parameters
-----------
This section describes the available parameters for Parquet, CSV, and ORC files.

The following table shows the available options for **Parquet** foreign data wrappers:

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

	 
The following table shows the available options for **CSV** foreign data wrappers:

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

**Comment - Merge the tables above and below to include the Description column. Incorporate that column into the other two tables on this page.**

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **CSV**                                                                                                                                                                                                                                          |
+============================+=====================================================================================================================================================================================================================+
| **Parameter**              | **Description**                                                                                                                                                                                                     |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``OR REPLACE``             | Create a new table, and overwrite any existing table by the same name. Does not return an error if the table already exists. CREATE OR REPLACE does not check the table contents or structure, only the table name. |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``schema_name``            | The name of the schema in which to create the table.                                                                                                                                                                |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``table_name``             | The name of the table to create, which must be unique inside the schema.                                                                                                                                            |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``column_def``             | A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.                           |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``WRAPPER ...``            | Specifies the format of the source files, such as parquet_fdw, orc_fdw, or csv_fdw.                                                                                                                                 |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``LOCATION = ...``         | Specifies a path or URI of the source files, such as /path/to/*.parquet.                                                                                                                                            |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``DELIMITER = ...``        | Specifies the field delimiter for CSV files. Defaults to ,.                                                                                                                                                         |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``RECORD_DELIMITER = ...`` | Specifies the record delimiter for CSV files. Defaults to a newline, \n                                                                                                                                             |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``AWS_ID, AWS_SECRET``     | Credentials for authenticated S3 access                                                                                                                                                                             |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following table shows the available options for **ORC** foreign data wrappers:

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
