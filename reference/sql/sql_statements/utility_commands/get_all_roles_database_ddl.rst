.. _get_all_roles_database_ddl:

********************
GET_ALL_ROLES_DATABASE_DDL
********************
The ``GET_ALL_ROLES_DATABASE_DDL`` statement returns the definition of all global roles in DDL format.

.. contents:: 
   :local:
   :depth: 1   

Syntax
==========
The following is the correct syntax for using the ``GET_ALL_ROLES_DATABASE_DDL`` statement:

.. code-block:: postgres

   select get_all_roles_database_ddl()

Example
===========
The following is an example of using the ``GET_ALL_ROLES_DATABASE_DDL`` statement:

.. code-block:: psql

   select get_all_roles_database_ddl();
   
Output
==========
The following is an example of the output of the ``GET_ALL_ROLES_DATABASE_DDL`` statement:

.. code-block:: postgres

   grant create, usage on schema "public" to "public" ; alter default schema for "public" to "public"; alter default permissions for "public" for schemas grant superuser to creator_role ; alter default permissions for "public" for tables grant select, insert, delete, ddl, update to creator_role ; grant select, insert, delete, ddl, update on table "public"."customer" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."d_customer" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."demo_customer" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."demo_lineitem" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."lineitem" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."nation" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."orders" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."part" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."partsupp" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."region" to "sqream" ; grant select, insert, delete, ddl, update on table "public"."supplier" to "sqream" ; alter default schema for "sqream" to "public";

Permissions
=============
Using the ``GET_ALL_ROLES_DATABASE_DDL`` statement requires no special permissions.

For more information, see the following:

* :ref:`get_all_roles_global_ddl`

    ::
	
* :ref:`get_role_permissions`