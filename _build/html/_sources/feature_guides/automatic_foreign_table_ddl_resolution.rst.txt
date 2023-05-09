.. _automatic_foreign_table_ddl_resolution:

***********************
Automatic Foreign Table DDL Resolution
***********************
The **Automatic Foreign Table DDL Resolution** page describes the following:

.. contents:: 
   :local:
   :depth: 1      
   
Overview
----------
SQream must be able to access a schema when reading and mapping external files to a foreign table. To facilitate this, you must specify the correct schema in the statement that creates the foreign table, which must also include the correct list of columns. To avoid human error related to this complex process SQream can now automatically identify the corresponding schema, saving you the time and effort required to build your schema manually. This is especially useful for particular file formats, such as Parquet, which include a built-in schema declaration.

Usage Notes
----------
The automatic foreign table DDL resolution feature supports Parquet, ORC, JSON, and Avro files, while using it with CSV files generates an error. You can activate this feature when you create a foreign table by omitting the column list, described in the **Syntax** section below.

Using this feature the path you specify in the ``LOCATION`` option must point to at least one existing file. If no files exist for the schema to read, an error will be generated. You can specify the schema manually even in the event of the error above.

.. note:: When using this feature, SQream assumes that all files in the path use the same schema.

Syntax
----------
The following is the syntax for using the automatic foreign table DDL resolution feature:

.. code-block:: console
   
   CREATE FOREIGN TABLE table_name
   [FOREIGN DATA] WRAPPER fdw_name
   [OPTIONS (...)];

Example
----------
The following is an example of using the automatic foreign table DDL resolution feature:

.. code-block:: console

   create foreign table parquet_table
   wrapper parquet_fdw
   options (location = '/tmp/file.parquet');
   
Permissions
----------
The automatic foreign table DDL resolution feature requires **Read** permissions.