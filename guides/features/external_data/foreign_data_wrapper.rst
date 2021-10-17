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

