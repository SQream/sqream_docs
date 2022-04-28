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
   * - :ref:`DESCRIBE CLUSTER STATUS<describe_cluster_status>`
     - Displays the currently running cluster resources, state, and total line
   * - :ref:`DESCRIBE DATABASES<describe_databases>`
     - Show all databases in your cluster
   * - :ref:`DESCRIBE LOCKS<describe_locks>`
     - Returns a list of locks from across the cluster.
   * - :ref:`DESCRIBE QUERY<describe_query>`
     - Display information about query execution for monitoring and troubleshooting purposes
   * - :ref:`DESCRIBE SCHEMAS<describe_schemas>`
     - Show all schemas in your cluster
   * - :ref:`DESCRIBE SESSIONS<describe_sessions>`
     - Show a list of sessions
   * - :ref:`DESCRIBE TABLES<describe_tables>`
     - List all tables in your database
   * - :ref:`DESCRIBE TABLES EXTENDED<describe_tables_extended>`
     - List all tables in your database, including information about storage and deleted data.
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

Saved Queries
===================

.. list-table:: Saved Queries
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`SELECT DROP_SAVED_QUERY<drop_saved_query>`
     - Drop a saved query
   * - :ref:`SELECT EXECUTE_SAVED_QUERY<execute_saved_query>`
     - Executes a saved query
   * - :ref:`SELECT LIST_SAVED_QUERIES<list_saved_queries>`
     - Returns a list of saved queries
   * - :ref:`SELECT RECOMPILE_SAVED_QUERY<recompile_saved_query>`
     - Recompiles a query that has been invalidated by a schema change
   * - :ref:`SELECT SAVE_QUERY<save_query>`
     - Compiles and saves a query for re-use and sharing
   * - :ref:`SELECT SHOW_SAVED_QUERY<show_saved_query>`
     - Shows query text for a saved query

Monitoring
===============

Monitoring statements allow a database administrator to execute actions in the system, such as aborting a query or get information about system processes.

.. list-table:: Monitoring
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`explain`
     - Returns a static query plan for a statement
   * - :ref:`show_connections`
     - Returns a list of jobs and statements on the current worker
   * - :ref:`DESCRIBE LOCKS<describe_locks>`
     - Returns a list of locks from across the cluster.
   * - :ref:`DESCRIBE QUERY<describe_query>`
     - Display information about query execution for monitoring and troubleshooting purposes
   * - :ref:`DESCRIBE SESSIONS<describe_sessions>`
     - Show a list of sessions
   * - :ref:`show_version`
     - Returns the version of SQream DB
   * - :ref:`stop_statement`
     - Stops a query (or statement) if it is currently running

Workload Management
======================

.. list-table:: Workload Management
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`subscribe_service`
     - Add a SQream DB worker to a service queue 
   * - :ref:`unsubscribe_service`
     - Remove a SQream DB worker to a service queue
   * - :ref:`show_subscribed_instances`
     - Return a list of service queues and workers

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