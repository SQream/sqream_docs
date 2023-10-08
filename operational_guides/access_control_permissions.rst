.. _access_control_permissions:

**************
Permissions
**************

SQreamDB’s primary permission object is a role. The role operates in a dual capacity as both a user and a group. In its user role, it may execute operations like creating tables, querying data, and administering the database, depending on its permissions. The role’s group attribute allows it to extend its permissions to roles defined as its group members. Information about permissions for all roles is stored in the metadata.

There are two main types of permissions: global and object-level. Global permissions belong to ``SUPERUSER`` roles, allowing unrestricted access to all system and database activities. Object-level permissions apply to non-``SUPERUSER`` roles and can be assigned to databases, schemas, tables, functions, views, foreign tables, columns, catalogs, and services.

The following tables describe the required permissions for performing and executing operations on various SQreamDB objects.
 
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
| ``CREATE FUNCTION``  | Create and drop functions                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Schema**                                                                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``            | Grants access to schema objects                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``           | Create tables in the schema                                                                                             |
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
| ``ALL``              | All the table permissions                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Function**                                                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``          | Use the function                                                                                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Drop and alter on the function                                                                                          |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | All function permissions                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **View**                                                                                                                                       |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from view                                                                                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | DDL operations of view results                                                                                          |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Foreign Table**                                                                                                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from foreign table                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Foreign table DDL operations                                                                                            |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Column**                                                                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from catalog                                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Column DDL operations                                                                                                   |   
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Catalog**                                                                                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``           | Select from catalog                                                                                                     | 
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Services**                                                                                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``            | Using a specific service                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+


GRANT Syntax
============

:ref:`grant` gives permissions to a role.

.. code-block:: postgres

	-- Grant permissions at the instance/ storage cluster level:
	GRANT 
	{ 
	  SUPERUSER
	  | LOGIN 
	  | PASSWORD '<password>' 
	} 
	TO <role> [, ...] 

	-- Grant permissions at the database level:
	GRANT
	{
	  { CREATE 
	  | CONNECT
	  | DDL 
	  | SUPERUSER 
	  | CREATE FUNCTION } [, ...] 
	  | ALL [PERMISSIONS]
	}
	ON DATABASE <database> [, ...]
	TO <role> [, ...] 

	-- Grant permissions at the schema level: 
	GRANT 
	{
	  { CREATE 
	  | DDL 
	  | USAGE 
	  | SUPERUSER } [, ...] 
	  | ALL [PERMISSIONS]
	} 
	ON SCHEMA <schema> [, ...] 
	TO <role> [, ...] 
		   
	-- Grant permissions at the object level: 
	GRANT
	{
	  { SELECT 
	  | INSERT 
	  | DELETE 
	  | DDL 
	  | UPDATE } [, ...] 
	  | ALL [PERMISSIONS]
	}
	ON 
	{ 
	  TABLE <table_name> [, ...] 
	  | ALL TABLES IN SCHEMA <schema_name> [, ...] 
	  | VIEW <schema_name.view_name> [, ...] 
	  | ALL VIEWS IN SCHEMA <schema_name> [, ...] 
	  | FOREIGN TABLE <table_name> [, ...] 
	  | ALL FOREIGN TABLES IN SCHEMA <schema_name> [, ...] 
	}
	TO <role> [, ...];

	GRANT
	{
	  { SELECT 
	  | INSERT 
	  | DELETE 
	  | UPDATE } [, ...] 
	  | ALL [PERMISSIONS]
	}
	ON 
	{ 
	  | CATALOG <catalog_name> [, ...]
	}
	TO <role> [, ...];

	-- Grant execute function permission: 
	GRANT 
	{ 
	  ALL 
	  | EXECUTE 
	  | DDL
	} 
	ON FUNCTION function_name 
	TO role; 
	   
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
	TO <role> [, ...];

	-- Grant permissions at the Service level:
	GRANT 
	{
	{ USAGE } [PERMISSIONS]
	}
	ON { SERVICE <service_name> }
	TO <role> [, ...]

	-- Allows role2 to use permissions granted to role1
	GRANT <role1> [, ...] 
	TO <role2> 

	-- Also allows the role2 to grant role1 to other roles:
	GRANT <role1> [, ...] 
	TO <role2> [,...] [WITH ADMIN OPTION]
	

REVOKE Syntax
=============

:ref:`revoke` removes permissions from a role.

.. code-block:: postgres

	-- Revoke permissions at the instance/ storage cluster level:
	REVOKE
	{ 
	  SUPERUSER
	  | LOGIN
	  | PASSWORD
	}
	FROM <role> [, ...]
				
	-- Revoke permissions at the database level:
	REVOKE 
	{
	  { CREATE 
	  | CONNECT 
	  | DDL 
	  | SUPERUSER 
	  | CREATE FUNCTION }[, ...] 
	  | ALL [PERMISSIONS]
	}
	ON DATABASE <database> [, ...]
	FROM <role> [, ...]

	-- Revoke permissions at the schema level:
	REVOKE 
	{ 
	  { CREATE 
	  | DDL 
	  | USAGE 
	  | SUPERUSER } [, ...] 
	  | ALL [PERMISSIONS]
	}
	ON SCHEMA <schema> [, ...]
	FROM <role> [, ...]
				
	-- Revoke permissions at the object level:
	REVOKE 
	{ 
	  { SELECT 
	  | INSERT 
	  | DELETE 
	  | DDL 
	  | UPDATE } [, ...] 
	  | ALL 
	}
	ON 
	{ 
	  [ TABLE ] <table_name> [, ...] 
	  | ALL TABLES IN SCHEMA <schema_name> [, ...] 
	  | VIEW <schema_name.view_name> [, ...] 
	  | ALL VIEWS IN SCHEMA <schema_name> [, ...] 
	  | FOREIGN TABLE <table_name> [, ...] 
	  | ALL FOREIGN TABLES IN SCHEMA <schema_name> [, ...] 
	}
	FROM <role> [, ...];

	REVOKE 
	{ 
	  { SELECT 
	  | INSERT 
	  | DELETE 
	  | UPDATE } [, ...] 
	  | ALL 
	}
	ON 
	{ 
	  | CATALOG <catalog_name> [, ...] 
	}
	FROM <role> [, ...];
				
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
	FROM <role> [, ...];

		
	-- Revoke permissions at the service level:
	REVOKE 
	{
	  { USAGE } [, ...] 
	  | ALL [PERMISSIONS] 
	}
	ON { SERVICE <service_name> }
	FROM <role> [, ...]
		
	-- Removes access to permissions in role1 by role 2
	REVOKE [ADMIN OPTION FOR] <role1> [, ...] 
	FROM <role2> [, ...] 

	-- Removes permissions to grant role1 to additional roles from role2
	REVOKE [ADMIN OPTION FOR] <role1> [, ...] 
	FROM <role2> [, ...] 

Altering Default Permissions
============================

The default permissions system (See :ref:`alter_default_permissions`) 
can be used to automatically grant permissions to newly 
created objects (See the departmental example below for one way it can be used).

A default permissions rule looks for a schema being created, or a
table (possibly by schema), and is table to grant any permission to
that object to any role. This happens when the create table or create
schema statement is run.


.. code-block:: postgres

     ALTER DEFAULT PERMISSIONS FOR target_role_name
     [IN schema_name, ...]
     FOR { 
          SCHEMAS 
          | TABLES 
          | FOREIGN TABLE 
          | VIEWS 
          | COLUMNS 
          | SAVED_QUERIES
         }
          { grant_clause 
          | DROP grant_clause }
          TO ROLE { role_name | public };

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

GRANT Examples
--------------

Grant superuser privileges and login capability to a role:

.. code-block:: postgres

	GRANT SUPERUSER, LOGIN TO role_name;
	
Grant specific permissions on a database to a role:

.. code-block:: postgres

	GRANT CREATE, CONNECT, DDL, SUPERUSER, CREATE FUNCTION ON DATABASE database_name TO role_name;
	
Grant various permissions on a schema to a role:

.. code-block:: postgres

	GRANT CREATE, DDL, USAGE, SUPERUSER ON SCHEMA schema_name TO role_name;
	
Grant permissions on specific objects (table, view, foreign table, or catalog) to a role:

.. code-block:: postgres

	GRANT SELECT, INSERT, DELETE, DDL, UPDATE ON TABLE schema_name.table_name TO role_name;

Grant execute function permission to a role:

.. code-block:: postgres

	GRANT EXECUTE ON FUNCTION function_name TO role_name;

Grant column-level permissions to a role:

.. code-block:: postgres

	GRANT SELECT, DDL ON COLUMN column_name IN TABLE schema_name.table_name TO role_name;

Grant usage permissions on a service to a role:

.. code-block:: postgres

	GRANT USAGE ON SERVICE service_name TO role_name;

Grant role2 the ability to use permissions granted to role1:

.. code-block:: postgres

	GRANT role1 TO role2;

Grant role2 the ability to grant role1 to other roles:

.. code-block:: postgres

	GRANT role1 TO role2 WITH ADMIN OPTION;


REVOKE Examples
---------------

Revoke superuser privileges or login capability from a role:

.. code-block:: postgres

	REVOKE SUPERUSER, LOGIN FROM role_name;

Revoke specific permissions on a database from a role:

.. code-block:: postgres

	REVOKE CREATE, CONNECT, DDL, SUPERUSER, CREATE FUNCTION ON DATABASE database_name FROM role_name;

Revoke permissions on a schema from a role:

.. code-block:: postgres

	REVOKE CREATE, DDL, USAGE, SUPERUSER ON SCHEMA schema_name FROM role_name;

Revoke permissions on specific objects (table, view, foreign table, or catalog) from a role:

.. code-block:: postgres

	REVOKE SELECT, INSERT, DELETE, DDL, UPDATE ON TABLE schema_name.table_name FROM role_name;

Revoke column-level permissions from a role:

.. code-block:: postgres

	REVOKE SELECT, DDL FROM COLUMN column_name IN TABLE schema_name.table_name FROM role_name;

Revoke usage permissions on a service from a role:

.. code-block:: postgres

	REVOKE USAGE ON SERVICE service_name FROM role_name;

Remove access to permissions in role1 by role2:

.. code-block:: postgres

	REVOKE role1 FROM role2 ;

Remove permissions to grant role1 to additional roles from role2:

.. code-block:: postgres

	REVOKE ADMIN OPTION FOR role1 FROM role2 ;


