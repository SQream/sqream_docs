.. _sql_statements:

***************
SQL Statements
***************

SQream supports commands from ANSI SQL.

.. _ddl_commands_list:

Data Definition Commands (DDL)
================================
The following table shows the DDL commands:

.. list-table:: DDL Commands
   :widths: auto
   :header-rows: 1
   :name: ddl_commands
   
   * - Command
     - Usage
   * - :ref:`ADD COLUMN<add_column>`
     - Adds a new column to a table
   * - :ref:`ALTER DEFAULT SCHEMA<alter_default_schema>`
     - Changes the default schema for a role
   * - :ref:`ALTER TABLE<alter_table>`
     - Changes the schema of a table
   * - :ref:`CREATE DATABASE<create_database>`
     - Creates a new database
   * - :ref:`CREATE EXTERNAL TABLE<create_external_table>`
     - Creates a new external table in the database (deprecated)
   * - :ref:`CREATE FOREIGN TABLE<create_foreign_table>`
     - Creates a new foreign table in the database
   * - :ref:`CREATE FUNCTION <create_function>`
     - Creates a new user defined function in the database
   * - :ref:`CREATE SCHEMA<create_schema>`
     - Creates a new schema in the database
   * - :ref:`CREATE TABLE<create_table>`
     - Creates a new table in the database
   * - :ref:`CREATE TABLE AS<create_table_as>`
     - Creates a new table in the database using results from a select query
   * - :ref:`CREATE VIEW<create_view>`
     - Creates a new view in the database
   * - :ref:`DROP COLUMN<drop_column>`
     - Drops a column from a table
   * - :ref:`DROP DATABASE<drop_database>`
     - Drops a database and all of its objects
   * - :ref:`DROP FUNCTION<drop_function>`
     - Drops a function
   * - :ref:`DROP SCHEMA<drop_schema>`
     - Drops a schema
   * - :ref:`DROP TABLE<drop_table>`
     - Drops a table and its contents from a database
   * - :ref:`DROP VIEW<drop_view>`
     - Drops a view
   * - :ref:`RENAME COLUMN<rename_column>`
     - Rename a column
   * - :ref:`RENAME TABLE<rename_table>`
     - Rename a table

Data Manipulation Commands (DML)
================================
The following table shows the DML commands:

.. list-table:: DML Commands
   :widths: auto
   :header-rows: 1
   :name: dml_commands

   
   * - Command
     - Usage
   * - :ref:`CREATE TABLE AS<create_table_as>`
     - Creates a new table in the database using results from a select query
   * - :ref:`DELETE<delete>`
     - Deletes specific rows from a table
   * - :ref:`COPY FROM<copy_from>`
     - Bulk loads CSV data into an existing table
   * - :ref:`COPY TO<copy_to>`
     - Exports a select query or entire table to CSV files
   * - :ref:`INSERT<insert>`
     - Inserts rows into a table
   * - :ref:`SELECT<select>`
     - Selects rows and column from a table
   * - :ref:`TRUNCATE<truncate>`
     - Deletes all rows from a table
   * - :ref:`VALUES<values>`
     - Returns rows containing literal values

Utility Commands
==================
The following table shows the Utility commands:

.. list-table:: Utility Commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`SELECT GET_DDL<get_ddl>`
     - Views the ``CREATE TABLE`` statement for a table
   * - :ref:`SELECT GET_FUNCTION_DDL<get_function_ddl>`
     - Views the ``CREATE FUNCTION`` statement for a UDF
   * - :ref:`SELECT GET_VIEW_DDL<get_view_ddl>`
     - Views the ``CREATE VIEW`` statement for a view
   * - :ref:`SELECT RECOMPILE_VIEW<recompile_view>`
     - Recreate a view after schema changes
   * - :ref:`SELECT DUMP_DATABASE_DDL<dump_database_ddl>`
     - Views the ``CREATE TABLE`` statement for a current database

Saved Queries
===================
The following table shows the saved query commands:

.. list-table:: Saved Query Commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`SELECT DROP_SAVED_QUERY<drop_saved_query>`
     - Drops a saved query
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

For more information, see See more about :ref:`saved_queries`.

Monitoring
===============
Monitoring statements allow a database administrator to execute actions in the system, such as aborting a query or get information about system processes.

The following table shows the monitoring commands:

.. list-table:: Monitoring
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`explain`
     - Returns a static query plan for a statement
   * - :ref:`show_connections`
     - Returns a list of jobs and statements on the current worker
   * - :ref:`show_locks`
     - Returns any existing locks in the database
   * - :ref:`show_node_info`
     - Returns a query plan for an actively running statement with timing information
   * - :ref:`show_server_status`
     - Shows running statements across the cluster
   * - :ref:`show_version`
     - Returns the version of SQream DB
   * - :ref:`stop_statement`
     - Stops a query (or statement) if it is currently running

Workload Management
======================
The following table shows the workload management commands:

.. list-table:: Workload Management Commands
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`subscribe_service`
     - Adds a SQream DB worker to a service queue 
   * - :ref:`unsubscribe_service`
     - Removes a SQream DB worker to a service queue
   * - :ref:`show_subscribed_instances`
     - Returns a list of service queues and workers

Access Control Commands
================================
The following table shows the access control commands:

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
     - Grants permissions to a role
   * - :ref:`revoke`
     - Revoke permissions from a role
   * - :ref:`rename_role`
     - Renames a role
	 
For more information about Access Control, see :ref:`access_control`.

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:
   :glob:

   ddl_commands/*
   dml_commands/*
   utility_commands/*
   monitoring_commands/*
   wlm_commands/*
   access_control_commands/*