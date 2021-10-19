.. _foreign_data_wrapper:

:download:`Download this page <C:/Users/Yaniv/Desktop/Yaniv/Local Work/New_Documentation/Q4/V2_Documentation/Foreign_Data_Wrapper/PDFs/Foreign Data Wrapper_A4.pdf>`

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
   
The following is an example of creating a **CSV** foreign data wrapper:

.. code-block:: postgres

   CREATE OR REPLACE EXTERNAL TABLE cool_animals
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, weight FLOAT NOT NULL)  
   USING FORMAT csv 
   WITH  PATH  '/home/rhendricks/cool_animals.csv'
         FIELD DELIMITER '\t';
		 
		 
The following is an example of creating a **Parquet** foreign data wrapper:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)
   WRAPPER parquet_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );
   
The following is an example of creating an **ORC** foreign data wrapper:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)
   WRAPPER orc_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );

Parameters
-----------
The following table shows the available parameters for **CSV** foreign data wrappers:

**Comment - We need the missing descriptions in all three of the following tables.**

**Comment - Do we want the parameters in alphabetical order?**

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\csv_foreign_data_wrappers.csv
   
.. _supported_datetime_formats:


CSV supports the following ``datetime`` formats:

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
   
The following table shows the available parameters for **Parquet** foreign data wrappers:

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\parquet_foreign_data_wrappers.csv

The following table shows the available parameters for **ORC** foreign data wrappers:

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\orc_foreign_data_wrappers.csv
