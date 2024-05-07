:orphan:

.. _revoke:

******
REVOKE
******

The ``REVOKE`` statement removes permissions from a role. It allows for removing permissions to specific objects.

Learn more about the permission system in the :ref:`access control guide<access_control>`.

See also :ref:`grant`, :ref:`drop_role`.

Permissions
===========

To revoke permissions, the current role must have the ``SUPERUSER`` permission, or have the ``ADMIN OPTION``.

Syntax
======

.. code-block:: postgres

	-- Revoke permissions from all databases:
	REVOKE {
	SUPERUSER 
	| LOGIN 
	| PASSWORD '<password>' }
	FROM "<role>" [, ...]

	-- Revoke permissions at the database level:
	REVOKE {
	CREATE 
	| CONNECT 
	| DDL 
	| SUPERUSER 
	| CREATE FUNCTION } [, ...] 
	| ALL [PERMISSIONS]
	ON DATABASE <database> [, ...]
	FROM "<role>" [, ...]

	-- Revoke permissions at the schema level: 
	REVOKE { 
	CREATE 
	| DDL 
	| USAGE 
	| SUPERUSER } [, ...] 
	| ALL [PERMISSIONS]
	ON SCHEMA <schema> [, ...]
	FROM "<role>" [, ...]
		   
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
	FROM "<role>" [, ...]

	-- Revoke permissions at the catalog level: 
	REVOKE {
	{SELECT } [, ...] 
	| ALL [PERMISSIONS] }
	ON { CATALOG <catalog_name> [, ...] }
	FROM "<role>" [, ...]

	-- Revoke permissions on the foreign table level:
	
	REVOKE { 
	{SELECT 
	| DDL } [, ...] 
	| ALL [PERMISSIONS] }
	ON { FOREIGN TABLE <table_name> [, ...] 
	| ALL FOREIGN TABLE IN SCHEMA <schema_name> [, ...]}
	FROM "<role>" [, ...]

	-- Revoke function execution permission: 
	REVOKE { 
	ALL 
	| EXECUTE 
	| DDL } 
	ON FUNCTION <function_name>
	FROM "<role>"

	-- Revoke permissions at the column level:
	REVOKE 
	{
	  { SELECT 
	  | DDL } [, ...] 
	  | ALL [PERMISSIONS]}
	ON 
	{ 
	  COLUMN "<column_name>" [,"<column_name2>"] IN TABLE <table_name> [,<table_name2>] | COLUMN "<column_name>" [,"<column_name2>"] IN FOREIGN TABLE <table_name> [,<table_name2>]
	  | ALL COLUMNS IN TABLE <schema_name.table_name> [, ...] 
	  | ALL COLUMNS IN FOREIGN TABLE <schema_name.foreign_table_name> [, ...] 
	}
	FROM "<role>" [, ...]

	-- Revoke permissions on the view level
	REVOKE {
	{SELECT 
	| DDL } [, ...] 
	| ALL [PERMISSIONS] }
	ON { VIEW <view_name> [, ...] 
	| ALL VIEWS IN SCHEMA <schema_name> [, ...]}
	FROM "<role>" [, ...]
		
	-- Removes access to permissions in role1 by role 2
	REVOKE [ADMIN OPTION FOR] "<role1>" [, ...] 
	FROM "<role2>" [, ...] 

	-- Removes permissions to grant role1 to additional roles from role2
	REVOKE [ADMIN OPTION FOR] "<role1>" [, ...] 
	FROM "<role2>" [, ...] 

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role to revoke permissions from
   * - ``table_name``, ``database_name``, ``schema_name``, ``function_name``
     - Object to revoke permissions on.
   * - ``WITH ADMIN OPTION``
     - 
         If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.
         
         Specifying ``WITH ADMIN OPTION`` for revocation will return the role to an ordinary role. An ordinary role cannot grant or revoke membership.
         
         

.. include:: grant.rst
   :start-line: 127
   :end-line: 180


Examples
========

Prevent a role from modifying table contents
----------------------------------------------

If you don't trust user ``shifty``, reokve DDL and INSERT permissions.

.. code-block:: postgres

   REVOKE INSERT ON TABLE important_table FROM shifty;
   REVOKE DDL ON TABLE important_table FROM shifty;

Demoting a user from superuser
-------------------------------------

.. code-block:: postgres
   
   -- On the entire cluster
   REVOKE SUPERUSER FROM new_role;

Revoking admin option
------------------------------

If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.


.. code-block:: postgres
   
   -- dba_user1 has been demoted from team lead, so he should not be able to grant
   -- permissions to other users.
   
   REVOKE r_database_architect FROM dba_user1 WITH ADMIN OPTION;

