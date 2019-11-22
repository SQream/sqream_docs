.. _sql_statements:

***************
SQL Statements
***************

SQream DB supports commands from ANSI SQL.

Data Definition commands (DDL)
================================

.. list-table:: DDL commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - ``ALTER DEFAULT SCHEMA``
     - Change the default schema for a role
   * - ``ALTER TABLE``
     - Change the schema of a table
   * - :ref:`CREATE DATABASE <create_database>`
     - Create a new database
   * - ``CREATE EXTERNAL TABLE``
     - Create a new external table in the database
   * - ``CREATE FUNCTION``
     - Create a new user defined function in the database
   * - ``CREATE SCHEMA``
     - Create a new schema in the database
   * - :ref:`CREATE TABLE <create_table>`
     - Create a new table in the database
   * - ``CREATE TABLE AS``
     - Create a new table in the database using results from a select query
   * - :ref:`CREATE VIEW <create_view>`
     - Create a new view in the database
   * - ``DROP COLUMN``
     - Drop a column from a table
   * - ``DROP DATABASE``
     - Drop a database and all of its objects
   * - ``DROP FUNCTION``
     - Drop a function
   * - ``DROP TABLE``
     - Drop a table and its contents from a database
   * - ``DROP VIEW``
     - Drop a view
   * - ``RENAME COLUMN``
     - Rename a column
   * - ``RENAME TABLE``
     - Rename a table
   * - ``SELECT GET_DDL(<table name>)``
     - View the ``CREATE TABLE`` statement for a table
   * - ``SELECT GET_FUNCTION_DDL(<function name>)``
     - View the ``CREATE FUNCTION`` statement for a UDF
   * - ``SELECT GET_VIEW_DDL(<view name>)``
     - View the ``CREATE VIEW`` statement for a view
   * - ``SELECT DUMP_DATABASE_DDL(<database name>)``
     - View the ``CREATE TABLE`` statement for an entire database


.. list-table:: Access control DDL commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - ``ALTER DEFAULT PERMISSIONS``
     - Applies a change to defaults in the current schema
   * - ``ALTER ROLE``
     - Applies a change to an existing role
   * - ``CREATE ROLE``
     - Creates a roles, which lets you control permissions on tables and databases
   * - ``DROP ROLE``
     - Removes roles
   * - ``GRANT``
     - Grant permissions to a role
   * - ``REVOKE``
     - Revoke permissions from a role
   * - ``RENAME ROLE``
     - Rename a role

Data manipulation commands (DML)
================================

.. list-table:: DML commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - ``CREATE TABLE AS``
     - Create a new table in the database using results from a select query
   * - ``DELETE``
     - Delete specific rows from a table
   * - ``COPY FROM``
     - Bulk load CSV data into an existing table
   * - ``COPY TO``
     - Export a select query or entire table to CSV files
   * - ``INSERT``
     - Insert rows into a table
   * - ``SELECT``
     - Select rows and column from a table
   * - ``TRUNCATE``
     - Delete all rows from a table
   * - ``VALUES``
     - Return rows containing literal values

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:
   :glob:

   ddl_commands/*
   dml_commands/*
   query_syntax/*
   query_operators/*