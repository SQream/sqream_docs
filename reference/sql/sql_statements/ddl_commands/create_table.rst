.. _create_table:

*****************
CREATE TABLE
*****************

``CREATE TABLE`` creates a new table in an existing database.

.. tip:: 
   * To create a table based on the result of a select query, see :ref:`CREATE TABLE AS <create_table_as>`.
   * To create a table based on files like Parquet and ORC, see :ref:`CREATE EXTERNAL TABLE <create_external_table>`

Permissions
=============

The role must have the ``CREATE`` permission at the schema level.

Synopsis
==========

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] TABLE [schema_name.]table_name (
           { column_def [, ...] }
       )
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

   column_def :: = { column_name type_name [ default ] [ column_constraint ] }

   column_name ::= identifier
   
   column_constraint ::=
       { NOT NULL | NULL }
   
   default ::=
   
       DEFAULT default_value
       | IDENTITY [ ( start_with [ , increment_by ] ) ]

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

Examples
===========

A simple table
-----------------

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name varchar(30) NOT NULL,
      weight FLOAT,
      is_agressive BOOL DEFAULT false NOT NULL
   );

A table with an identity (autoincrement) column
---------------------------------------------------

.. code-block:: postgres

   CREATE TABLE users (
      id BIGINT NOT NULL IDENTITY(0,1), -- Start with 0, increment by 1
      name VARCHAR(30) NOT NULL,
      country VARCHAR(30) NOT NULL,
   );

.. note:: 
   * Identity columns are supported on BIGINT columns.
   * Identity does not enforce the uniqueness of values. The identity value can be bypassed by specifying it in an INSERT command.

Creating a table from a SELECT query
-----------------------------------------

You can use a :ref:`CREATE TABLE AS <create_table_as>` statement to create a new table from the results of a SELECT query.

.. code-block:: postgres
   
   CREATE TABLE users_uk AS SELECT * FROM users WHERE country = 'United Kingdom';