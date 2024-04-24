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
   * - :ref:`add_column`
     - Add a new column to a table
   * - :ref:`alter_default_schema`
     - Change the default schema for a role
   * - :ref:`alter_table`
     - Change the schema of a table
   * - :ref:`cluster_by`
     - Change clustering keys in a table
   * - :ref:`create_database`
     - Create a new database
   * - :ref:`create_foreign_table`
     - Create a new foreign table in the database
   * - :ref:`create_function`
     - Create a new user-defined function in the database
   * - :ref:`create_schema`
     - Create a new schema in the database
   * - :ref:`create_table`
     - Create a new table in the database
   * - :ref:`create_table_as`
     - Create a new table in the database using results from a select query
   * - :ref:`create_view`
     - Create a new view in the database
   * - :ref:`describe_columns`
     - Lists information about columns in an internal or external table
   * - :ref:`describe_configuration`
     - Shows all configurations set on the session level
   * - :ref:`describe_databases`
     - Lists information about the databases in your cluster
   * - :ref:`describe_pools`
     - List all of your pools
   * - :ref:`describe_schemas`
     - Lists information about schemas in your cluster
   * - :ref:`describe_tables`
     - List information about tables in your database
   * - :ref:`describe_tables_extended`
     - Lists all the tables in your database
   * - :ref:`describe_user_functions`
     - Lists all user-defined functions in your database
   * - :ref:`describe_views`
     - Creates a list of database views
   * - :ref:`drop_clustering_key`
     - Drops all clustering keys in a table
   * - :ref:`drop_column`
     - Drop a column from a table
   * - :ref:`drop_database`
     - Drop a database and all of its objects
   * - :ref:`drop_function`
     - Drop a function
   * - :ref:`drop_schema`
     - Drop a schema
   * - :ref:`drop_table`
     - Drop a table and its contents from a database
   * - :ref:`drop_view`
     - Drop a view
   * - :ref:`rename_column`
     - Rename a column
   * - :ref:`rename_table`
     - Rename a table
   * - :ref:`use_database`
     - Lets you shift between databases within an existing session
   * - :ref:`use_pool`
     - Lets you shift between pools within a session
   * - :ref:`use_schema`
     - Lets you shift between schemes within an existing session
   * - :ref:`rename_schema`
     - Rename a schema


Data Manipulation Commands (DML)
================================

.. list-table::
   :widths: 10 100
   :header-rows: 1
   :name: dml_commands
   
   * - Command
     - Usage
   * - :ref:`copy_from`
     - Bulk load data into an existing table from different file formats
   * - :ref:`copy_to`
     - Export a select query or entire table to CSV files
   * - :ref:`delete`
     - Delete specific rows from a table
   * - :ref:`insert`
     - Inserts rows into a table
   * - :ref:`select`
     - Select rows and column from a table
   * - :ref:`truncate`
     - Delete all rows from a table
   * - :ref:`update`
     - Modify the value of certain columns in existing rows without creating a table
   * - :ref:`values`
     - Return rows containing literal values

Utility Commands
================

.. list-table::
   :widths: 10 100
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`abort`
     - Performs a graceful stop, known as an abort, on an active statement
   * - :ref:`audit_log`
     - Returns system user activity
   * - :ref:`describe_locks`
     - Returns a list of locks from across your cluster
   * - :ref:`describe_saved_queries_list`
     - Lists of all of your saved queries		 
   * - :ref:`describe_saved_query`
     - Returns the SQL syntax of a specific saved query
   * - :ref:`describe_session_queries`
     - Lists queries per session, including queued queries
   * - :ref:`describe_sessions`
     - Outputs information about your current session
   * - :ref:`describe_query`
     - Displays information about query execution
   * - :ref:`drop_saved_query`
     - Drops a saved query
   * - :ref:`execute_saved_query`
     - Executes a previously saved query
   * - :ref:`explain`
     - Returns a static query plan, which can be used to debug query plans
   * - :ref:`recompile_saved_query`
     - Recompiles a saved query that has been invalidated due to a schema change
   * - :ref:`get_ddl`
     - View the ``CREATE TABLE`` statement for a table
   * - :ref:`get_function_ddl`
     - View the ``CREATE FUNCTION`` statement for a UDF
   * - :ref:`get_view_ddl`
     - View the ``CREATE VIEW`` statement for a view
   * - :ref:`recompile_view`
     - Recreate a view after schema changes
   * - :ref:`dump_database_ddl`
     - View the ``CREATE TABLE`` statement for a current database
   * - :ref:`shutdown_server_command`
     - Sets your server to finish compiling all active queries before shutting down according to a user-defined time value
   * - :ref:`save_query`
     - Saves query execution plan

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
     - Creates a role, which lets a database administrator control permissions on tables and databases
   * - :ref:`describe_connect_permissions`
     - Lists all roles and their database connection privileges
   * - :ref:`describe_roles`
     - Lists all roles defined in your system
   * - :ref:`describe_role_permissions`
     - Lists all role privileges
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
