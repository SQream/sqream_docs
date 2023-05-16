.. _sql_statements:

***************
SQL Statements
***************

SQream supports commands from ANSI SQL.


Data Definition Commands (DDL)
==============================

.. list-table::
   :widths: 10 100
   :header-rows: 1
   :name: ddl_commands
   
   * - Command
     - Usage
   * - :ref:`ADD_COLUMN<add_column>`
     - Add a new column to a table
   * - :ref:`ALTER_DEFAULT_SCHEMA<alter_default_schema>`
     - Change the default schema for a role
   * - :ref:`ALTER_TABLE<alter_table>`
     - Change the schema of a table
   * - :ref:`CLUSTER_BY<cluster_by>`
     - Change clustering keys in a table
   * - :ref:`CREATE_DATABASE<create_database>`
     - Create a new database
   * - :ref:`CREATE_FOREIGN_TABLE<create_foreign_table>`
     - Create a new foreign table in the database
   * - :ref:`CREATE_FUNCTION<create_function>`
     - Create a new user defined function in the database
   * - :ref:`CREATE_SCHEMA<create_schema>`
     - Create a new schema in the database
   * - :ref:`CREATE_TABLE<create_table>`
     - Create a new table in the database
   * - :ref:`CREATE_TABLE_AS<create_table_as>`
     - Create a new table in the database using results from a select query
   * - :ref:`CREATE_VIEW<create_view>`
     - Create a new view in the database
   * - :ref:`DESCRIBE_TABLE<describe_tables>`
     - List information about tables in your database
   * - :ref:`DROP_CLUSTERING_KEY<drop_clustering_key>`
     - Drops all clustering keys in a table
   * - :ref:`DROP_COLUMN<drop_column>`
     - Drop a column from a table
   * - :ref:`DROP_DATABASE<drop_database>`
     - Drop a database and all of its objects
   * - :ref:`DROP_FUNCTION<drop_function>`
     - Drop a function
   * - :ref:`DROP_SCHEMA<drop_schema>`
     - Drop a schema
   * - :ref:`DROP_TABLE<drop_table>`
     - Drop a table and its contents from a database
   * - :ref:`DROP_VIEW<drop_view>`
     - Drop a view
   * - :ref:`RENAME_COLUMN<rename_column>`
     - Rename a column
   * - :ref:`RENAME_TABLE<rename_table>`
     - Rename a table


Data Manipulation Commands (DML)
================================

.. list-table::
   :widths: 10 100
   :header-rows: 1
   :name: dml_commands
   
   * - Command
     - Usage
   * - :ref:`CREATE_TABLE_AS<create_table_as>`
     - Create a new table in the database using results from a select query
   * - :ref:`DELETE<delete>`
     - Delete specific rows from a table
   * - :ref:`COPY_TO<copy_to>`
     - Export a select query or entire table to CSV files
   * - :ref:`SELECT<select>`
     - Select rows and column from a table
   * - :ref:`TRUNCATE<truncate>`
     - Delete all rows from a table
   * - :ref:`UPDATE<update>`
     - Modify the value of certain columns in existing rows without creating a table
   * - :ref:`VALUES<values>`
     - Return rows containing literal values

Utility Commands
================

.. list-table::
   :widths: 10 100
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`DROP SAVED QUERY<drop_saved_query>`
     - Drops a saved query
   * - :ref:`EXECUTE SAVED QUERY<execute_saved_query>`
     - Executes a previously saved query
   * - :ref:`EXPLAIN<explain>`
     - Returns a static query plan, which can be used to debug query plans
   * - :ref:`LIST SAVED QUERIES<list_saved_queries>`
     - Lists previously saved query names, one per row.
   * - :ref:`RECOMPILE SAVED QUERY<recompile_saved_query>`
     - Recompiles a saved query that has been invalidated due to a schema change
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
   * - :ref:`SHOW LOCKS<show_locks>`
     - Returns a list of locks from across the cluster
   * - :ref:`SHOW SAVED QUERY<show_saved_query>`
     - Returns a single row result containing the saved query string
   * - :ref:`SHUTDOWN_SERVER<shutdown_server_command>`
     - Sets your server to finish compiling all active queries before shutting down according to a user-defined time value
   * - :ref:`STOP STATEMENT<stop_statement>`
     - Stops or aborts an active statement

Access Control Commands
=======================
The following table shows the Access Control commands:

.. list-table::
   :widths: 10 100
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
   * - :ref:`get_role_permissions`
     - Returns all permissions granted to a role in table format
   * - :ref:`get_role_global_ddl`
     - Returns the definition of a global role in DDL format
   * - :ref:`get_all_roles_global_ddl`
     - Returns the definition of all global roles in DDL format
   * - :ref:`get_role_database_ddl`
     - Returns the definition of a role's database in DDL format
   * - :ref:`get_all_roles_database_ddl`
     - Returns the definition of all role databases in DDL format
   * - :ref:`get_statement_permissions`
     - Returns a list of permissions required to run a statement or query
   * - :ref:`grant`
     - Grant permissions to a role
   * - :ref:`revoke`
     - Revoke permissions from a role
   * - :ref:`rename_role`
     - Rename a role