:orphan:

.. _alter_default_permissions:

*************************
ALTER DEFAULT PERMISSIONS
*************************

The ``ALTER DEFAULT PERMISSIONS`` command lets you grant automatic permissions to future objects.

By default, users do not have ``SELECT`` permissions on tables created by other users. Database administrators can grant access to other users by modifying the target role default permissions.

For more information about access control, see :ref:`Access Control<access_control>`.

Permissions
===========

The ``SUPERUSER`` permission is required to alter default permissions.

Syntax
======

The following is the syntax for altering default permissions:

.. code-block:: postgres

         ALTER DEFAULT PERMISSIONS FOR { "<modifying_role>" | ALL ROLES }
         [ IN "<schema_name>", ...] 
         FOR { TABLES | SCHEMAS }
         { <grant_clause> [, ...] | DROP <grant_clause> [, ...] } 
         TO { "<role_name>" [, ...] | public };
   
   grant_clause ::= 
      GRANT 
         { SUPERUSER
         | CREATE
         | USAGE
         | SELECT
         | UPDATE
         | DDL
         | ALL
         } [, ...]

Supported Permissions
=====================

The following table describes the supported permissions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Permission
     - Object
     - Description
   * - ``SUPERUSER``
     - Schema
     - The most privileged role, with full control over a cluster, database, or schema
   * - ``CREATE``
     - Schema
     - For a role to create and manage objects, it needs the ``CREATE`` and ``USAGE`` permissions at the respective level
   * - ``USAGE``
     - Schema
     - For a role to see tables in a schema, it needs the ``USAGE`` permissions
   * - ``SELECT``
     - Table
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
     - Schema, Table
     - Allows a user to :ref:`alter tables<alter_table>`, rename columns and tables, etc.


Examples
========
   
Granting Default Table Permissions
----------------------------------

This example is based on the roles **r1** and **r2**, created as follows:

.. code-block:: postgres

   CREATE ROLE r1;
   CREATE ROLE r2;
   ALTER DEFAULT PERMISSIONS FOR r1 FOR TABLES GRANT SELECT to r2;

Once created, you can build and run the following query based on the above:

.. code-block:: postgres

   SELECT
     tdp.database_name AS "database_name",
     ss.schema_name AS "schema_name",
     rs1.name AS "table_creator",
     rs2.name AS "grant_to",
     pts.name  AS "permission_type"
   FROM sqream_catalog.table_default_permissions tdp
   INNER JOIN sqream_catalog.roles rs1 ON tdp.modifier_role_id = rs1.role_id
   INNER JOIN sqream_catalog.roles rs2 ON tdp.getter_role_id = rs2.role_id
   LEFT JOIN sqream_catalog.schemas ss ON tdp.schema_id = ss.schema_id
   INNER JOIN sqream_catalog.permission_types pts ON pts.permission_type_id=tdp.permission_type
   ;   

Output:

.. code-block:: none

	database_name | schema_name | table_creator | grant_to | permission_type          
	--------------+-------------+---------------+----------+----------------
	master        |   NULL      | public        | public   | select                        
   
Granting Automatic Permissions for Newly Created Schemas
--------------------------------------------------------

When the role ``demo`` creates a new schema, roles **u1,u2** are granted ``USAGE`` and ``CREATE`` permissions in the new schema, as shown below:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR demo FOR SCHEMAS GRANT USAGE, CREATE TO u1,u2;

Granting Automatic Permissions for Newly Created Tables in a Schema
-------------------------------------------------------------------

When the role ``demo`` creates a new table in schema ``s1``, roles **u1,u2** are granted ``SELECT`` permissions, as shown below:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR demo IN s1 FOR TABLES GRANT SELECT TO u1,u2;

Revoking Permissions from Newly Created Tables
----------------------------------------------

Revoking permissions refers to using the ``DROP GRANT`` command, as shown below:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR public FOR TABLES DROP GRANT SELECT,DDL TO public;