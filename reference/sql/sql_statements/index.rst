.. _sql_statements:

***************
SQL Statements
***************
The **SQL Statements** page describes the following commands:

.. contents::
   :local:
   :depth: 1

SQream DB supports commands from ANSI SQL.

.. _ddl_commands_list:

Data Definition Commands (DDL)
================================

.. list-table:: DDL Commands
   :widths: auto
   :header-rows: 1
   :name: ddl_commands
   
   * - Command
     - Usage
   * - :ref:`ADD COLUMN<add_column>`
     - Add a new column to a table
   * - :ref:`ALTER TABLE<alter_table>`
     - Change the schema of a table
   * - :ref:`CLUSTER BY<cluster_by>`
     - Changes the clustering keys in a table
   * - :ref:`CREATE DATABASE<create_database>`
     - Create a new database
   * - :ref:`CREATE EXTERNAL TABLE<create_external_table>`
     - Create a new external table in the database (deprecated)
   * - :ref:`CREATE FOREIGN TABLE<create_foreign_table>`
     - Create a new foreign table in the database
   * - :ref:`CREATE FUNCTION <create_function>`
     - Create a new user defined function in the database
   * - :ref:`CREATE SCHEMA<create_schema>`
     - Create a new schema in the database
   * - :ref:`CREATE TABLE<create_table>`
     - Create a new table in the database
   * - :ref:`CREATE TABLE AS<create_table_as>`
     - Create a new table in the database using results from a select query
   * - :ref:`CREATE VIEW<create_view>`
     - Create a new view in the database
   * - :ref:`DESCRIBE COLUMNS<describe_columns>`
     - List all columns in your internal or external table
   * - :ref:`DESCRIBE DATABASES<describe_databases>`
     - Show all databases in your cluster
   * - :ref:`DESCRIBE QUERY<describe_query>`
     - Display information about query execution for monitoring and troubleshooting purposes
   * - :ref:`DESCRIBE SCHEMAS<describe_schemas>`
     - Show all schemas in your cluster
   * - :ref:`DESCRIBE SESSIONS<describe_sessions>`
     - Show a list of sessions
   * - :ref:`DESCRIBE SESSION QUERIES<describe_session_queries>`
     - Show a list of queries per session
   * - :ref:`DESCRIBE TABLES<describe_tables>`
     - List all tables in your database
   * - :ref:`DESCRIBE USER FUNCTIONS<describe_user_functions>`
     - List all user-defined functions
   * - :ref:`DROP COLUMN<drop_column>`
     - Drop a column from a table
   * - :ref:`DROP DATABASE<drop_database>`
     - Drop a database and all of its objects
   * - :ref:`DROP FUNCTION<drop_function>`
     - Drop a function
   * - :ref:`DROP SCHEMA<drop_schema>`
     - Drop a schema
   * - :ref:`DROP TABLE<drop_table>`
     - Drop a table and its contents from a database
   * - :ref:`DROP VIEW<drop_view>`
     - Drop a view
   * - :ref:`RENAME COLUMN<rename_column>`
     - Rename a column
   * - :ref:`RENAME TABLE<rename_table>`
     - Rename a table
   * - :ref:`USE DATABASE<use_database>`
     - Switch between databases on an existing connection and session
   * - :ref:`USE SCHEMA<use_schema>`
     - Switch between schemas	 

Data Manipulation Commands (DML)
================================

.. list-table:: DML Commands
   :widths: auto
   :header-rows: 1
   :name: dml_commands

   
   * - Command
     - Usage
   * - :ref:`CREATE TABLE AS<create_table_as>`
     - Create a new table in the database using results from a select query
   * - :ref:`DELETE<delete>`
     - Delete specific rows from a table
   * - :ref:`COPY FROM<copy_from>`
     - Bulk load CSV data into an existing table
   * - :ref:`COPY TO<copy_to>`
     - Export a select query or entire table to CSV files
   * - :ref:`INSERT<insert>`
     - Insert rows into a table
   * - :ref:`SELECT<select>`
     - Select rows and column from a table
   * - :ref:`TRUNCATE<truncate>`
     - Delete all rows from a table
   * - :ref:`UPDATE<update>`
     - Modify the value of certain columns in existing rows without creating a table
   * - :ref:`VALUES<values>`
     - Return rows containing literal values
	 
.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   :width: 110

Utility Commands
==================

.. list-table:: Utility Commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`EXPLAIN<explain>`
     - Returns a static query plan, which can be used to debug query plans
   * - :ref:`SELECT GET_LICENSE_INFO<get_license_info>`
     - View a user's license information
   * - :ref:`SELECT GET_DDL<get_ddl>`
     - View the ``CREATE TABLE`` statement for a table
   * - :ref:`SELECT GET_FUNCTION_DDL<get_function_ddl>`
     - View the ``CREATE FUNCTION`` statement for a UDF
   * - :ref:`SELECT GET_VIEW_DDL<get_view_ddl>`
     - View the ``CREATE VIEW`` statement for a view
   * - :ref:`SELECT RECOMPILE_VIEW<recompile_view>`
     - Recreate a view after schema changes
   * - :ref:`SELECT DUMP_DATABASE_DDL<dump_database_ddl>`
     - View the ``CREATE TABLE`` statement for an current database
   * - :ref:`SHOW CONNECTIONS<show_connections>`
     - Returns a list of active sessions on the current worker
   * - :ref:`SHOW VERSION<show_version>`
     - Returns the system version for SQream DB
   * - :ref:`STOP STATEMENT<stop_statement>`
     - Stops or aborts an active statement


Access Control Commands
================================

.. list-table:: Access Control Commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`alter_default_permissions`
     - Applies a change to defaults in the current schema
   * - :ref:`alter_role`
     - Applies a change to an existing role
   * - :ref:`create_role`
     - Creates a roles, which lets a database administrator control permissions on tables and databases
   * - :ref:`drop_role`
     - Removes roles
   * - :ref:`get_statement_permissions`
     - Returns a list of permissions required to run a statement or query
   * - :ref:`grant`
     - Grant permissions to a role
   * - :ref:`revoke`
     - Revoke permissions from a role
   * - :ref:`rename_role`
     - Rename a role