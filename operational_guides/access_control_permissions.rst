.. _access_control_permissions:

***********
Permissions
***********

SQreamDB’s primary permission object is a role. The role operates in a dual capacity as both a user and a group. As a user, a role may have permissions to execute operations like creating tables, querying data, and administering the database. The group attribute may be thought of as a membership. As a group, a role may extend its permissions to other roles defined as its group members. This becomes handy when privileged roles wish to extend their permissions and grant multiple permissions to multiple roles. The information about all system role permissions is stored in the metadata.

There are two types of permissions: global and object-level. Global permissions belong to ``SUPERUSER`` roles, allowing unrestricted access to all system and database activities. Object-level permissions apply to non-``SUPERUSER`` roles and can be assigned to databases, schemas, tables, functions, views, foreign tables, catalogs, and services.

The following table describe the required permissions for performing and executing operations on various SQreamDB objects.
 
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Permission**       | **Description**                                                                                                         |
+======================+=========================================================================================================================+
|**All Databases**                                                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``LOGIN``            | Use role to log into the system (the role also needs connect permission on the database it is connecting to)            |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``PASSWORD``         | The password used for logging into the system                                                                           |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``        | No permission restrictions on any activity                                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Database**                                                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``        | No permission restrictions on any activity within that database (this does not include modifying roles or permissions)  |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CONNECT``          | Connect to the database                                                                                                 |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``           | Create schemas in the database                                                                                          |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATEFUNCTION``   | Create and drop functions                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Drop and alter tables within the database                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All database permissions except for a SUPERUSER permission                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Schema**                                                                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``            | Grants access to schema objects                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``           | Create tables in the schema                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``        | No permission restrictions on any activity within the schema (this does not include modifying roles or permissions)     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Drop and alter tables within the schema                                                                                 |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All schema permissions                                                                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Table**                                                                                                                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | :ref:`select` from the table                                                                                            |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``INSERT``           | :ref:`insert` into the table                                                                                            |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``UPDATE``           | :ref:`update` the value of certain columns in existing rows                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DELETE``           | :ref:`delete` and :ref:`truncate` on the table                                                                          |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Drop and alter on the table                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All table permissions                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Function**                                                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``          | Use the function                                                                                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Drop and alter on the function                                                                                          |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All function permissions                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Column**                                                                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from column                                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Column DDL operations                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **View**                                                                                                                                       |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from view                                                                                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | DDL operations of view results                                                                                          |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All views permissions                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Foreign Table**                                                                                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from foreign table                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Foreign table DDL operations                                                                                            |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All foreign table permissions                                                                                           |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Catalog**                                                                                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from catalog                                                                                                     | 
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All catalog permissions                                                                                                 |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Services**                                                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``            | Using a specific service                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All services permissions                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Saved Query**                                                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Executing saved query statements and utility functions                                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Saved query DDL operations                                                                                              |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``            | Grants access to saved query objects                                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All saved query permissions                                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+

Syntax
======

Permissions may be granted or revoked using the following syntax.

GRANT
------

.. code-block:: postgres

	-- Grant permissions to all databases:
	GRANT {
	SUPERUSER 
	| LOGIN 
	| PASSWORD '<password>' }
	TO <role> [, ...]

	-- Grant permissions at the database level:
	GRANT {
	CREATE 
	| CONNECT 
	| DDL 
	| SUPERUSER 
	| CREATE FUNCTION } [, ...] 
	| ALL [PERMISSIONS]
	ON DATABASE <database> [, ...]
	TO <role> [, ...]

	-- Grant permissions at the schema level: 
	GRANT { 
	CREATE 
	| DDL 
	| USAGE 
	| SUPERUSER } [, ...] 
	| ALL [PERMISSIONS]
	ON SCHEMA <schema> [, ...]
	TO <role> [, ...]
		   
	-- Grant permissions at the object level: 
	GRANT { 
	SELECT 
	| INSERT 
	| DELETE 
	| DDL 
	| UPDATE } [, ...] 
	| ALL [PERMISSIONS]
	ON {TABLE <table_name> [, ...] 
	| ALL TABLES IN SCHEMA <schema_name> [, ...]}
	TO <role> [, ...]

	-- Grant permissions at the catalog level: 
	GRANT {
	{SELECT } [, ...] 
	| ALL [PERMISSIONS] }
	ON { CATALOG <catalog_name> [, ...] }
	TO <role> [, ...]

	-- Grant permissions on the foreign table level:
	
	GRANT { 
	{SELECT 
	| DDL } [, ...] 
	| ALL [PERMISSIONS] }
	ON { FOREIGN TABLE <table_name> [, ...] 
	| ALL FOREIGN TABLE IN SCHEMA <schema_name> [, ...]}
	TO <role> [, ...]

	-- Grant function execution permission: 
	GRANT { 
	ALL 
	| EXECUTE 
	| DDL } 
	ON FUNCTION <function_name>
	TO <role>

	-- Grant permissions at the column level:
	GRANT 
	{
	  { SELECT 
	  | DDL } [, ...] 
	  | ALL [PERMISSIONS]
	}
	ON 
	{ 
	  COLUMN <column_name> [,<column_name_2>] IN TABLE <table_name> [,<table_name2>] 
	  | COLUMN <column_name> [,<column_name_2>] IN FOREIGN TABLE <table_name> [,<table_name2>]
	  | ALL COLUMNS IN TABLE <schema_name.table_name> [, ...] 
	  | ALL COLUMNS IN FOREIGN TABLE <foreign_table_name> [, ...] 
	}
	TO <role> [, ...]

	-- Grant permissions on the view level
	GRANT {
	{SELECT 
	| DDL } [, ...] 
	| ALL [PERMISSIONS] }
	ON { VIEW <view_name> [, ...] 
	| ALL VIEWS IN SCHEMA <schema_name> [, ...]}
	TO <role> [, ...]

	-- Grant permissions at the Service level:
	GRANT {
	{USAGE} [, ...] 
	| ALL [PERMISSIONS] }
	ON { SERVICE <service_name> [, ...] 
	| ALL SERVICES IN SYSTEM }
	TO <role> [, ...]
	
	-- Grant saved query permissions
	GRANT
	SELECT 
	| DDL
	| USAGE
	| ALL
	ON SAVED QUERY <saved_query> [,...]
	TO <role> [,...]

	-- Allows role2 to use permissions granted to role1
	GRANT <role1> [, ...] 
	TO <role2> 

	-- Also allows the role2 to grant role1 to other roles:
	GRANT <role1> [, ...] 
	TO <role2> [,...] [WITH ADMIN OPTION]
	

REVOKE
-------

.. code-block:: postgres

	-- Revoke permissions from all databases:
	REVOKE {
	SUPERUSER 
	| LOGIN 
	| PASSWORD '<password>' }
	FROM <role> [, ...]

	-- Revoke permissions at the database level:
	REVOKE {
	CREATE 
	| CONNECT 
	| DDL 
	| SUPERUSER 
	| CREATE FUNCTION } [, ...] 
	| ALL [PERMISSIONS]
	ON DATABASE <database> [, ...]
	FROM <role> [, ...]

	-- Revoke permissions at the schema level: 
	REVOKE { 
	CREATE 
	| DDL 
	| USAGE 
	| SUPERUSER } [, ...] 
	| ALL [PERMISSIONS]
	ON SCHEMA <schema> [, ...]
	FROM <role> [, ...]
		   
	-- Revoke permissions at the object level: 
	REVOKE { 
	SELECT 
	| INSERT 
	| DELETE 
	| DDL 
	| UPDATE } [, ...] 
	| ALL [PERMISSIONS]
	ON {TABLE <table_name> [, ...] 
	| ALL TABLES IN SCHEMA <schema_name> [, ...]}
	FROM <role> [, ...]

	-- Revoke permissions at the catalog level: 
	REVOKE {
	{SELECT } [, ...] 
	| ALL [PERMISSIONS] }
	ON { CATALOG <catalog_name> [, ...] }
	FROM <role> [, ...]

	-- Revoke permissions on the foreign table level:
	
	REVOKE { 
	{SELECT 
	| DDL } [, ...] 
	| ALL [PERMISSIONS] }
	ON { FOREIGN TABLE <table_name> [, ...] 
	| ALL FOREIGN TABLE IN SCHEMA <schema_name> [, ...]}
	FROM <role> [, ...]

	-- Revoke function execution permission: 
	REVOKE { 
	ALL 
	| EXECUTE 
	| DDL } 
	ON FUNCTION <function_name>
	FROM <role>

	-- Revoke permissions at the column level:
	REVOKE 
	{
	  { SELECT 
	  | DDL } [, ...] 
	  | ALL [PERMISSIONS]}
	ON 
	{ 
	  COLUMN <column_name> [,<column_name_2>] IN TABLE <table_name> [,<table_name2>] | COLUMN <column_name> [,<column_name_2>] IN FOREIGN TABLE <table_name> [,<table_name2>]
	  | ALL COLUMNS IN TABLE <schema_name.table_name> [, ...] 
	  | ALL COLUMNS IN FOREIGN TABLE <schema_name.foreign_table_name> [, ...] 
	}
	FROM <role> [, ...]

	-- Revoke permissions on the view level
	REVOKE {
	{SELECT 
	| DDL } [, ...] 
	| ALL [PERMISSIONS] }
	ON { VIEW <view_name> [, ...] 
	| ALL VIEWS IN SCHEMA <schema_name> [, ...]}
	FROM <role> [, ...]

	-- Revoke permissions at the Service level:
	REVOKE {
	{USAGE} [, ...] 
	| ALL [PERMISSIONS] }
	ON { SERVICE <service_name> [, ...] 
	| ALL SERVICES IN SYSTEM }
	FROM <role> [, ...]
		
	-- Revoke saved query permissions
	REVOKE
	SELECT 
	| DDL
	| USAGE
	| ALL
	ON SAVED QUERY <saved_query> [,...]
	FROM <role> [,...]
		
	-- Removes access to permissions in role1 by role 2
	REVOKE [ADMIN OPTION FOR] <role1> [, ...] 
	FROM <role2> [, ...] 

	-- Removes permissions to grant role1 to additional roles from role2
	REVOKE [ADMIN OPTION FOR] <role1> [, ...] 
	FROM <role2> [, ...] 

Altering Default Permissions
-----------------------------

The default permissions system (See :ref:`alter_default_permissions`) 
can be used to automatically grant permissions to newly 
created objects (See the departmental example below for one way it can be used).

A default permissions rule looks for a schema being created, or a
table (possibly by schema), and is table to grant any permission to
that object to any role. This happens when the create table or create
schema statement is run.


.. code-block:: postgres

     ALTER DEFAULT PERMISSIONS FOR modifying_role
     [IN <schema_name> [, ...]
     FOR { 
          SCHEMAS 
          | TABLES 
          | FOREIGN TABLES 
          | VIEWS
          | COLUMNS   
          | CATALOGS
          | SERVICES
          | SAVED_QUERIES
         }
          { grant_clause 
          | DROP grant_clause }
          TO ROLE { role_name | public 
		 }

     grant_clause ::=
     GRANT
        { CREATE FUNCTION
         | SUPERUSER
         | CONNECT
         | CREATE
         | USAGE
         | SELECT
         | INSERT
         | DELETE
         | DDL
         | UPDATE
         | EXECUTE
         | ALL
        }
		
Examples
========

GRANT
--------------

Grant superuser privileges and login capability to a role:

.. code-block:: sql

	GRANT SUPERUSER, LOGIN TO role_name;
	
Grant specific permissions on a database to a role:

.. code-block:: postgres

	GRANT CREATE, CONNECT, DDL, SUPERUSER, CREATE FUNCTION ON DATABASE database_name TO role_name;
	
Grant various permissions on a schema to a role:

.. code-block:: postgres

	GRANT CREATE, USAGE, SUPERUSER ON SCHEMA schema_name TO role_name;
	
Grant permissions on specific objects (table, view, foreign table, or catalog) to a role:

.. code-block:: postgres

	GRANT SELECT, INSERT, DELETE, DDL, UPDATE ON TABLE schema_name.table_name TO role_name;

Grant execute function permission to a role:

.. code-block:: postgres

	GRANT EXECUTE ON FUNCTION function_name TO role_name;

Grant column-level permissions to a role:

.. code-block:: postgres

	GRANT SELECT, DDL ON COLUMN column_name IN TABLE schema_name.table_name TO role_name;

Grant view-level permissions to a role:

.. code-block:: postgres

	GRANT ALL PERMISSIONS ON VIEW "view_name" IN SCHEMA "schema_name" TO role_name;

Grant usage permissions on a service to a role:

.. code-block:: postgres

	GRANT USAGE ON SERVICE service_name TO role_name;

Grant role2 the ability to use permissions granted to role1:

.. code-block:: postgres

	GRANT role1 TO role2;

Grant role2 the ability to grant role1 to other roles:

.. code-block:: postgres

	GRANT role1 TO role2 WITH ADMIN OPTION;


REVOKE
---------------

Revoke superuser privileges or login capability from a role:

.. code-block:: postgres

	REVOKE SUPERUSER, LOGIN FROM role_name;

Revoke specific permissions on a database from a role:

.. code-block:: postgres

	REVOKE CREATE, CONNECT, DDL, SUPERUSER, CREATE FUNCTION ON DATABASE database_name FROM role_name;

Revoke permissions on a schema from a role:

.. code-block:: postgres

	REVOKE CREATE, USAGE, SUPERUSER ON SCHEMA schema_name FROM role_name;

Revoke permissions on specific objects (table, view, foreign table, or catalog) from a role:

.. code-block:: postgres

	REVOKE SELECT, INSERT, DELETE, DDL, UPDATE ON TABLE schema_name.table_name FROM role_name;
	
Revoke execute function permission from a role:

.. code-block:: postgres

	REVOKE EXECUTE ON FUNCTION function_name FROM role_name;

Revoke column-level permissions from a role:

.. code-block:: postgres

	REVOKE SELECT, DDL FROM COLUMN column_name IN TABLE schema_name.table_name FROM role_name;

Revoke view-level permissions from a role:

.. code-block:: postgres

	REVOKE ALL PERMISSIONS ON VIEW "view_name" IN SCHEMA "schema_name" FROM role_name;

Revoke usage permissions on a service from a role:

.. code-block:: postgres

	REVOKE USAGE ON SERVICE service_name FROM role_name;

Remove access to permissions in role1 by role2:

.. code-block:: postgres

	REVOKE role1 FROM role2 ;

Remove permissions to grant role1 to additional roles from role2:

.. code-block:: postgres

	REVOKE ADMIN OPTION FOR role1 FROM role2 ;


