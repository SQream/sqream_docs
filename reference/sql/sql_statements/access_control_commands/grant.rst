.. _grant:

*****************
GRANT
*****************

The ``GRANT`` statement adds permissions for a role. It allows for setting permissions to databases, schemas, and tables.

It also allows adding a role as a memeber to another role.

When granting permissions to a role, the permission is added for existing objects only.
To automatically add permissions to newly created objects, see :ref:`alter_default_permissions`.

Learn more about the permission system in the :ref:`access control guide<access_control>`.

See also :ref:`revoke`, :ref:`create_role`.

Syntax
==========

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
	TO <role> [, ...]

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
	TO <role> [, ...]

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
	TO <role> [, ...]

	-- Grant permissions at the Service level:
	GRANT 
	{
	{ USAGE } [PERMISSIONS]
	}
	ON { SERVICE <service_name> }
	TO <role> [, ...]
	
	-- Grant permissions at the Saved Query level:
	GRANT {
	{ SELECT 
	| DDL 
	| USAGE } [, ...] 
	| ALL [PERMISSIONS] }
	ON SAVED QUERY <saved_query_name> [, ...]
	TO <role> [, ...]

	-- Allows role2 to use permissions granted to role1
	GRANT <role1> [, ...] 
	TO <role2> 

	-- Also allows the role2 to grant role1 to other roles:
	GRANT <role1> [, ...] 
	TO <role2> [,...] [WITH ADMIN OPTION]


Parameters
============

The following table describes the ``GRANT`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role to grant permissions to
   * - ``table_name``, ``database_name``, ``schema_name``, ``function_name``, ``catalog_name``, ``column_name``, ``service_name``, ``saved_query_name``
     - Object to grant permissions on.
   * - ``WITH ADMIN OPTION``
     - 
         If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.
         
         Without the admin option, ordinary roles cannot grant or revoke membership.
         
         Roles with ``SUPERUSER`` can grant or revoke membership in any role to anyone.

.. include from here

Supported Permissions
=======================

The following table describes the supported permissions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Permission
     - Object
     - Description
   * - ``LOGIN``
     - Cluster
     - Login permissions (with a password) allows a role to be a user and login to a database
   * - ``PASSWORD``
     - Cluster
     - Sets the password for a user role
   * - ``CREATE FUNCTION``
     - Database
     - Allows a user to :ref:`create a Python UDF<create_function>`
   * - ``SUPERUSER``
     - Cluster, Database, Schema
     - The most privileged role, with full control over a cluster, database, or schema
   * - ``CONNECT``
     - Database
     - Allows a user to connect and use a database
   * - ``CREATE``
     - Database, Schema, Table
     - For a role to create and manage objects, it needs the ``CREATE`` and ``USAGE`` permissions at the respective level
   * - ``USAGE``
     - Schema, Saved Query, Services
     - For a role to see tables in a schema, it needs the ``USAGE`` permissions
   * - ``SELECT``
     - Table, Saved Query, View, Catalog, Foreign Table
     - Allows a user to run :ref:`select` queries on table contents
   * - ``INSERT``
     - Table
     - Allows a user to run :ref:`copy_from` and :ref:`insert` statements to load data into a table
   * - ``UPDATE``
     - Table
     - Allows a user to modify the value of certain columns in existing rows without creating a table
   * - ``DELETE``
     - Table
     - Allows a user to run :ref:`delete`, :ref:`truncate` statements to delete data from a table
   * - ``DDL``
     - Database, Schema, Table, Function, Saved Query, View, Foreign Table
     - Allows a user to :ref:`alter tables<alter_table>`, rename columns and tables, etc.
   * - ``EXECUTE``
     - Function
     - Allows a user to execute UDFs
   * - ``ALL``
     - Cluster, Database, Schema, Table, Function, Saved Query, Services, Catalog, Foreign Table
     - All of the above permissions at the respective level

.. end include


Examples
===========

This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1

Creating a User Role with Log-in Permissions
----------------------------------------------

The following example shows how to convert a role to a user by granting password and log-in permissions:

.. code-block:: postgres

   CREATE ROLE new_role;
   GRANT LOGIN to new_role;
   GRANT PASSWORD 'Tr0ub4dor&3' to new_role;
   GRANT CONNECT ON DATABASE master to new_role; -- Repeat for other desired databases

Promoting a User to a Superuser
-------------------------------------

The following is the syntax for promoting a user to a superuser:

.. code-block:: postgres
   
   -- On the entire cluster
   GRANT SUPERUSER TO new_role;
   
   -- For a specific database
   GRANT SUPERUSER ON DATABASE my_database TO new_role;

Creating a New Role for a Group of Users
--------------------------------------------

The following example shows how to create a new role for a group of users:

.. code-block:: postgres
   
   -- Create new users (we will grant them passwords and logins later)
   CREATE ROLE dba_user1;
   CREATE ROLE dba_user2;
   CREATE ROLE dba_user3;

   -- Add new users to the existing r_database_architect role
   GRANT r_database_architect TO dba_user1;
   GRANT r_database_architect TO dba_user2;
   GRANT r_database_architect TO dba_user3;

Granting with Admin Option
------------------------------

If ``WITH ADMIN OPTION`` is specified, the role with the **admin** option can grant membership in the role to others and revoke membership, as shown below:

.. code-block:: postgres
   
   -- dba_user1 is our team lead, so he should be able to grant
   -- permissions to other users.
   
   GRANT r_database_architect TO dba_user1 WITH ADMIN OPTION;

Changing Password for User Role
--------------------------------------

The following is an example of changing a password for a user role. This is done by granting the user a new password:

.. code-block:: postgres

   GRANT  PASSWORD  'new_password'  TO  rhendricks;  

.. note:: Granting a new password overrides any previous password. Changing the password while the role has an active running statement does not affect that statement, but will affect subsequent statements.

Permissions
=============

To grant permissions, the current role must have the ``SUPERUSER`` permission, or have the ``ADMIN OPTION``.