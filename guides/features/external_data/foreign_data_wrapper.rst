.. _foreign_data_wrapper:

:download:`Download a PDF of this page <C:/Users/Yaniv/Desktop/Yaniv/Local Work/New_Documentation/Q4/V2_Documentation/Foreign_Data_Wrapper/PDFs/Foreign Data Wrapper.pdf>`



Foreign Data Wrapper
=======================================
The **Foreign Data Wrapper** page includes the following sections:

.. contents:: 
   :local:
   :depth: 1
   
Overview
----------

Foreign data is accessed using a **foreign data wrapper**. A foreign data wrapper is a library that lets you access a table or schema in one database from another. It does this by converting data from an external source, such as a CSV file, to a format readable by SQream.

SQream currently supports foreign data wrappers for the following file formats:

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

.. _fdw_page_csv:

The following is an example of creating a **CSV** foreign data wrapper:

.. code-block:: postgres

   CREATE OR REPLACE EXTERNAL TABLE cool_animals
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, weight FLOAT NOT NULL)  
   USING FORMAT csv 
   WITH  PATH  '/home/rhendricks/cool_animals.csv'
         FIELD DELIMITER '\t';
		 
.. _fdw_page_parquet:
 
The following is an example of creating a **Parquet** foreign data wrapper:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)
   WRAPPER parquet_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

.. _fdw_page_orc:
	 
The following is an example of creating an **ORC** foreign data wrapper:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)
   WRAPPER orc_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

