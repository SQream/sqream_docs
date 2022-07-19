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

Permissions
=============

To grant permissions, the current role must have the ``SUPERUSER`` permission, or have the ``ADMIN OPTION``.

Syntax
==========

.. code-block:: postgres

   grant_statement ::=
      { 
      -- Grant permissions at the cluster level:
      GRANT 
         { SUPERUSER
         | LOGIN 
         | PASSWORD 'password' 
         } 
         TO role_name [, ...] 
      
      -- Grant permissions at the database level:
      | GRANT
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
         TO role_name [, ...] 
      
      -- Grant permissions at the schema level: 
      | GRANT 
         {
            { CREATE 
            | DDL 
            | USAGE 
            | SUPERUSER 
            } [, ...]
         | ALL [PERMISSIONS ]
         } 
         ON SCHEMA schema_name [, ...] 
         TO role_name [, ...]
      
      -- Grant permissions at the object level: 
      | GRANT 
         {
            { SELECT 
            | INSERT 
            | DELETE 
            | DDL 
            } [, ...]
         | ALL [PERMISSIONS]
         }
         ON { TABLE table_name [, ...] | ALL TABLES IN SCHEMA schema_name [, ...]} 
         TO role_name [, ...]
      
                  
      -- Grant execute function permission: 
      | GRANT 
         { ALL 
         | EXECUTE 
         | DDL
         } 
         ON FUNCTION function_name 
         TO role_name [, ...]
       
                  
      -- Pass permissions between roles by granting one role to another: 
      | GRANT role_name [, ...] 
         TO role_name_2
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
     - The name of the role to grant permissions to
   * - ``table_name``, ``database_name``, ``schema_name``, ``function_name``
     - Object to grant permissions on.
   * - ``WITH ADMIN OPTION``
     - 
         If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.
         
         Without the admin option, ordinary roles cannot grant or revoke membership.
         
         Roles with ``SUPERUSER`` can grant or revoke membership in any role to anyone.

.. include from here

Supported Permissions
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
     - Schema
     - For a role to see tables in a schema, it needs the ``USAGE`` permissions
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


.. end include


Examples
===========

Creating a user role with login permissions
----------------------------------------------

Convert a role to a user by granting a password and login permissions

.. code-block:: postgres

   CREATE ROLE new_role;
   GRANT LOGIN to new_role;
   GRANT PASSWORD 'Tr0ub4dor&3' to new_role;
   GRANT CONNECT ON DATABASE master to new_role; -- Repeat for other desired databases

Promoting a user to a superuser
-------------------------------------

.. code-block:: postgres
   
   -- On the entire cluster
   GRANT SUPERUSER TO new_role;
   
   -- For a specific database
   GRANT SUPERUSER ON DATABASE my_database TO new_role;


Creating a new role for a group of users
--------------------------------------------

.. code-block:: postgres
   
   -- Create new users (we will grant them passwords and logins later)
   CREATE ROLE dba_user1;
   CREATE ROLE dba_user2;
   CREATE ROLE dba_user3;

   -- Add new users to the existing r_database_architect role
   GRANT r_database_architect TO dba_user1;
   GRANT r_database_architect TO dba_user2;
   GRANT r_database_architect TO dba_user3;

Granting with admin option
------------------------------

If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.

.. code-block:: postgres
   
   -- dba_user1 is our team lead, so he should be able to grant
   -- permissions to other users.
   
   GRANT r_database_architect TO dba_user1 WITH ADMIN OPTION;

Change password for user role
--------------------------------------

To change a user role's password, grant the user a new password.

.. code-block:: postgres

   GRANT  PASSWORD  'new_password'  TO  rhendricks;  

.. note:: Granting a new password overrides any previous password. Changing the password while the role has an active running statement does not affect that statement, but will affect subsequent statements.
