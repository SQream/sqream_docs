.. _alter_default_permissions:

*****************************
ALTER DEFAULT PERMISSIONS
*****************************
The **ALTER DEFAULT PERMISSIONS** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
=============
The ``ALTER DEFAULT PERMISSIONS`` command lets you grant automatic permissions to future objects.

By default, users do not have ``SELECT`` permissions on tables created by other users. Database administrators can grant access to other users by modifying the target role default permissions.

For more information about access control, see :ref:`Access Control<access_control>`.

Permissions
=============
The ``SUPERUSER`` permission is required to alter default permissions.

Syntax
==========
The following is the syntax for altering default permissions:

.. code-block:: postgres

   alter_default_permissions_statement ::=
         ALTER DEFAULT PERMISSIONS FOR target_role_name
         [IN schema_name, ...] 
         FOR { TABLES | SCHEMAS }
         { grant_clause | DROP grant_clause} 
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
         | EXECUTE
         | ALL
         }

   target_role_name ::= identifier 
   
   role_name ::= identifier 
   
   schema_name ::= identifier
   

.. include:: grant.rst
   :start-line: 127
   :end-line: 180

Examples
============
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1
   
Granting Default Table Permissions
-------------------------------------------------
This example is based on the roles **r1** and **r2**, created as follows:

.. code-block:: postgres

   create role r1;
   create role r2;
   alter default permissions for r1 for tables grant select to r2;

Once created, you can build and run the following query based on the above:

.. code-block:: postgres

   select
     tdp.database_name as "database_name",
     ss.schema_name as "schema_name",
     rs1.name as "table_creator",
     rs2.name as "grant_to",
     pts.name  as "permission_type"
   from sqream_catalog.table_default_permissions tdp
   inner join sqream_catalog.roles rs1 on tdp.modifier_role_id = rs1.role_id
   inner join sqream_catalog.roles rs2 on tdp.getter_role_id = rs2.role_id
   left join sqream_catalog.schemas ss on tdp.schema_id = ss.schema_id
   inner join sqream_catalog.permission_types pts on pts.permission_type_id=tdp.permission_type
   ;   
   
The following is an example of the output generated from the above queries:

+-----------------------+----------------------+-------------------+--------------+------------------------------+
| **database_name**     | **schema_name**      | **table_creator** | **grant_to** | **permission_type**          |
+-----------------------+----------------------+-------------------+--------------+------------------------------+
| master                |   NULL               | public            | public       | select                       | 
+-----------------------+----------------------+-------------------+--------------+------------------------------+

For more information about default permissions, see `Default Permissions <https://docs.sqream.com/en/v2022.1/reference/catalog_reference_catalog_tables.html#default-permissions.html>`_.  
   
Granting Automatic Permissions for Newly Created Schemas
-------------------------------------------------
When the role ``demo`` creates a new schema, roles **u1,u2** are granted ``USAGE`` and ``CREATE`` permissions in the new schema, as shown below:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR demo FOR SCHEMAS GRANT USAGE, CREATE TO u1,u2;

Granting Automatic Permissions for Newly Created Tables in a Schema
----------------------------------------------------------------
When the role ``demo`` creates a new table in schema ``s1``, roles **u1,u2** are granted ``SELECT`` permissions, as shown below:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR demo IN s1 FOR TABLES GRANT SELECT TO u1,u2;

Revoking Permissions from Newly Created Tables
---------------------------------------------------------------
Revoking permissions refers to using the ``DROP GRANT`` command, as shown below:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR public FOR TABLES DROP GRANT SELECT,DDL,INSERT,DELETE TO public;