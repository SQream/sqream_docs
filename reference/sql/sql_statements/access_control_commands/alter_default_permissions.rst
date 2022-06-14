.. _alter_default_permissions:

*****************************
ALTER DEFAULT PERMISSIONS
*****************************

``ALTER DEFAULT PERMISSIONS`` allows granting automatic permissions to future objects.

By default, if one user creates a table, another user will not have ``SELECT`` permissions on it.
By modifying the target role's default permissions, a database administrator can ensure that
all objects created by that role will be accessible to others.

Learn more about the permission system in the :ref:`access control guide<access_control>`.

Permissions
=============

To alter default permissions, the current role must have the ``SUPERUSER`` permission.

Syntax
==========

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

Automatic permissions for newly created schemas
-------------------------------------------------

When role ``demo`` creates a new schema, roles u1,u2 will get USAGE and CREATE permissions in the new schema:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR demo FOR SCHEMAS GRANT USAGE, CREATE TO u1,u2;


Automatic permissions for newly created tables in a schema
----------------------------------------------------------------

When role ``demo`` creates a new table in schema ``s1``, roles u1,u2 wil be granted with SELECT on it:

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR demo IN s1 FOR TABLES GRANT SELECT TO u1,u2;

Revoke (``DROP GRANT``) permissions for newly created tables
---------------------------------------------------------------

.. code-block:: postgres

   ALTER DEFAULT PERMISSIONS FOR public FOR TABLES DROP GRANT SELECT,DDL,INSERT,DELETE TO public;
