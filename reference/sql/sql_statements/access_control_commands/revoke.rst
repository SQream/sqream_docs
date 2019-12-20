.. _revoke:

*****************
REVOKE
*****************

The ``REVOKE`` statement removes permissions from a role. It allows for removing permissions to specific objects.

See also :ref:`grant`, :ref:`drop_role`.

Permissions
=============

To revoke permissions, the current role must have the ``SUPERUSER`` permission, or have the ``ADMIN OPTION``.

Syntax
==========

.. code-block:: postgres

   grant_statement ::=
      { 
      -- revoke permissions at the cluster level:
      REVOKE 
         { SUPERUSER
         | LOGIN 
         | PASSWORD 'password' 
         } 
         FROM role_name [, ...] 
      
      -- Revoke permissions at the database level:
      | REVOKE
         {
            { CREATE
            | CONNECT
            | DDL
            | SUPERUSER
            | CREATE FUNCTION
            } [, ...] 
         | ALL [PERMISSIONS]
         }  
         ON DATABASE database_name [, ...]
         FROM role_name [, ...] 
      
      -- Revoke permissions at the schema level: 
      | REVOKE 
         {
            { CREATE 
            | DDL 
            | USAGE 
            | SUPERUSER 
            } [, ...]
         | ALL [PERMISSIONS ]
         } 
         ON SCHEMA schema_name [, ...] 
         FROM role_name [, ...]
      
      -- Revoke permissions at the object level: 
      | REVOKE 
         {
            { SELECT 
            | INSERT 
            | DELETE 
            | DDL 
            } [, ...]
         | ALL [PERMISSIONS]
         }
         ON { TABLE table_name [, ...] | ALL TABLES IN SCHEMA schema_name [, ...]} 
         FROM role_name [, ...]
      
                  
      -- Revoke execute function permission: 
      | REVOKE 
         { ALL 
         | EXECUTE 
         | DDL
         } 
         ON FUNCTION function_name 
         FROM role_name [, ...]
       
                  
      -- Remove privileges between roles by revoking role membership: 
      | REVOKE role_name [, ...] 
         FROM role_name_2
         [ WITH ADMIN OPTION ]

      ;

   role_name ::= identifier  
   
   role_name2 ::= identifier  
   
   database_name ::= identifier
   
   table_name ::= identifier
   
   schema_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role to revoke permissions from
   * - ``table_name``, ``database_name``, ``schema_name``, ``function_name``
     - Object to revoke permissions on.

Supported permissions
=======================

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
     - Database, Schema
     - For a role to create and manage objects, it needs the ``CREATE`` and ``USAGE`` permissions at the respective level
   * - ``SELECT``
     - Table
     - Allows a user to run :ref:`select` queries on table contents 
   * - ``INSERT``
     - Table
     - Allows a user to run :ref:`copy_from` and :ref:`insert` statements to load data into a table
   * - ``DELETE``
     - Table
     - Allows a user to run :ref:`delete`, :ref:`truncate` statements to delete data from a table
   * - ``DDL``
     - Database, Schema, Table, Function
     - Allows a user to :ref:`alter tables<alter_table>`, rename columns and tables, etc.
   * - ``EXECUTE``
     - Function
     - Allows a user to execute UDFs
   * - ``ALL``
     - Cluster, Database, Schema, Table, Function
     - All of the above permissions at the respective level

Examples
===========

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
