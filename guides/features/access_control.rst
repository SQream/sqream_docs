.. _access_control:

**************
Access control
**************

.. contents:: In this topic:
   :local:

Overview
========

Access control provides authentication and authorization in SQream DB.

:term:`Authentication` : verifying the identity of the user. Users have usernames (:term:`role names<role>`) and passwords.

:term:`Authorization` : checking the user has permissions to do a particular thing. The :ref:`grant` command is used for this.

* SQream DB uses roles as users and groups, like ANSI SQL and other SQL products

* SQream DB has a default permissions system based on the system in Postgres, but with more power.
  In most cases, this allows an administrator to set things up so that every object gets permissions set automatically.

Roles
=====

Roles are used for users and for groups.

Roles are global across all databases in the instance / storage cluster.

To use a ``ROLE`` as USER, it should have a password, the login permission, and connect permissions to the relevant databases.

Creating a user
---------------

.. code-block:: postgres
                
   CREATE ROLE role_name ;
   GRANT LOGIN to role_name ;
   GRANT PASSWORD 'new_password' to role_name ;
   GRANT CONNECT ON DATABASE database_name to role_name ;

Examples:

.. code-block:: postgres

   CREATE  ROLE  new_role_name  ;  
   GRANT  LOGIN  TO  new_role_name;  
   GRANT  PASSWORD  'my_password'  TO  new_role_name;  
   GRANT  CONNECT  ON  DATABASE  master  TO  new_role_name;

Dropping a user
---------------

.. code-block:: postgres

   DROP ROLE role_name ;

Examples:

.. code-block:: postgres

   DROP  ROLE  admin_role ;

Altering a user
---------------

.. code-block:: postgres

   ALTER ROLE role_name RENAME TO new_role_name ;

Examples:

.. code-block:: postgres

   ALTER  ROLE  admin_role  RENAME  TO  copy_role ;

Public Role
-----------

There is a public role which always exists. Each role is granted to the ``PUBLIC`` role (i.e. is a member of the public group), and this cannot be revoked. You can alter the permissions granted to the public role.

The ``PUBLIC`` role has ``USAGE`` and ``CREATE`` permissions on ``PUBLIC`` schema by default, therefore, new users can create, :ref:`insert`, :ref:`delete`, and :ref:`select` from objects in the ``PUBLIC`` schema.

Groups
------

A group can be created, altered, and dropped the same way as a user.

To use a role purely as a group, omit granting it ``LOGIN`` and ``PASSWORD`` permissions. The ``CONNECT`` permission can be given directly to users, and/or to the groups they are part of.

.. code-block:: postgres

   CREATE ROLE my_group;
   GRANT  CONNECT  ON  DATABASE  a_database  TO  my_group;
   -- add my_user to this group
   GRANT my_group TO my_user;

   -- remove my_other_user from this group

   REVOKE my_group FROM my_other_user;

.. _permissions_table:

Permissions
===========

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Object/layer
     - Permission
     - Description

   * - all databases
     - ``LOGIN``
     - use role to log into the system (the role also needs connect permission on the database it is connecting to)

   * - all databases
     - ``PASSWORD``
     - the password used for logging into the system

   * - all databases
     - ``SUPERUSER``
     - no permission restrictions on any activity

       
   * - database
     - ``SUPERUSER``
     - no permission restrictions on any activity within that database (this does not include modifying roles or permissions)

   * - database
     - ``CONNECT``
     - connect to the database

   * - database
     - ``CREATE``
     - create schemas in the database

   * - database
     - ``CREATE FUNCTION``
     - create and drop functions
     
   * - schema
     - ``USAGE``
     - allows additional permissions within the schema

   * - schema
     - ``CREATE``
     - create tables in the schema

   * - table
     - ``SELECT``
     - :ref:`select` from the table

   * - table
     - ``INSERT``
     - :ref:`insert` into the table

   * - table
     - ``DELETE``
     - :ref:`delete` and :ref:`truncate` on the table

   * - table
     - ``DDL``
     - drop and alter on the table

   * - table
     - ``ALL``
     - all the table permissions

   * - function
     - ``EXECUTE``
     - use the function

   * - function
     - ``DDL``
     - drop and alter on the function

   * - function
     - ``ALL``
     - all function permissions

GRANT
-----

Grant gives permissions to a role.

.. code-block:: postgres

   -- Grant permissions at the instance/ storage cluster level:
   GRANT 

   { SUPERUSER
   | LOGIN 
   | PASSWORD '<password>' 
   } 
   TO <role> [, ...] 

   -- Grant permissions at the database level:
        GRANT {{CREATE | CONNECT| DDL | SUPERUSER | CREATE FUNCTION} [, ...] | ALL [PERMISSIONS]}

   ON DATABASE <database> [, ...]
   TO <role> [, ...] 

   -- Grant permissions at the schema level: 
   GRANT {{ CREATE | DDL | USAGE | SUPERUSER } [, ...] | ALL [ 
   PERMISSIONS ]} 
   ON SCHEMA <schema> [, ...] 
   TO <role> [, ...] 
       
   -- Grant permissions at the object level: 
   GRANT {{SELECT | INSERT | DELETE | DDL } [, ...] | ALL [PERMISSIONS]} 
   ON { TABLE <table_name> [, ...] | ALL TABLES IN SCHEMA <schema_name> [, ...]} 
   TO <role> [, ...]
       
   -- Grant execute function permission: 
   GRANT {ALL | EXECUTE | DDL} ON FUNCTION function_name 
   TO role; 
       
   -- Allows role2 to use permissions granted to role1
   GRANT <role1> [, ...] 
   TO <role2> 

    -- Also allows the role2 to grant role1 to other roles:
   GRANT <role1> [, ...] 
   TO <role2> 
   WITH ADMIN OPTION
  
Examples:

.. code-block:: postgres

   GRANT  LOGIN,superuser  TO  admin;

   GRANT  CREATE  FUNCTION  ON  database  master  TO  admin;

   GRANT  SELECT  ON  TABLE  admin.table1  TO  userA;

   GRANT  EXECUTE  ON  FUNCTION  my_function  TO  userA;

   GRANT  ALL  ON  FUNCTION  my_function  TO  userA;

   GRANT  DDL  ON  admin.main_table  TO  userB;

   GRANT  ALL  ON  all  tables  IN  schema  public  TO  userB;

   GRANT  SELECT  ON  all  views  IN  schema  admin  TO  userA;

   GRANT  admin  TO  userC;

   GRANT  superuser  ON  schema  demo  TO  userA

   GRANT  admin_role  TO  userB;

REVOKE
------

Revoke removes permissions from a role.

.. code-block:: postgres

   -- Revoke permissions at the instance/ storage cluster level:
   REVOKE
   { SUPERUSER
   | LOGIN
   | PASSWORD
   }
   FROM <role> [, ...]
            
   -- Revoke permissions at the database level:
   REVOKE {{CREATE | CONNECT | DDL | SUPERUSER | CREATE FUNCTION}[, ...] |ALL [PERMISSIONS]}
   ON DATABASE <database> [, ...]
   FROM <role> [, ...]

   -- Revoke permissions at the schema level:
   REVOKE { { CREATE | DDL | USAGE | SUPERUSER } [, ...] | ALL [PERMISSIONS]}
   ON SCHEMA <schema> [, ...]
   FROM <role> [, ...]
            
   -- Revoke permissions at the object level:
   REVOKE { { SELECT | INSERT | DELETE | DDL } [, ...] | ALL }
   ON { [ TABLE ] <table_name> [, ...] | ALL TABLES IN SCHEMA

         <schema_name> [, ...] }
   FROM <role> [, ...]
            
   -- Removes access to permissions in role1 by role 2
   REVOKE <role1> [, ...] FROM <role2> [, ...] WITH ADMIN OPTION

   -- Removes permissions to grant role1 to additional roles from role2
   REVOKE <role1> [, ...] FROM <role2> [, ...] WITH ADMIN OPTION


Examples:

.. code-block:: postgres

   REVOKE  superuser  on  schema  demo  from  userA;

   REVOKE  delete  on  admin.table1  from  userB;

   REVOKE  login  from  role_test;

   REVOKE  CREATE  FUNCTION  FROM  admin;

Default permissions
-------------------

The default permissions system can be used to automatically grant
permissions to newly created objects. See the departmental example
below for one way it can be used.

A default permissions rule looks for a schema being created, or a
table (possibly by schema), and is table to grant any permission to
that object to any role. This happens when the create table or create
schema statement is run.

.. code-block:: postgres


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
  

Departmental Example
====================

You work in a company with several departments.

The example below shows you how to manage permissions in a database shared by multiple departments, where each department has different roles for the tables by schema. It walks you through how to set the permissions up for existing objects and how to set up default permissions rules to cover newly created objects.

The concept is that you set up roles for each new schema with the correct permissions, then the existing users can use these roles. 

A superuser must do new setup for each new schema which is a limitation, but superuser permissions are not needed at any other time, and neither are explicit grant statements or object ownership changes.

In the example, the database is called ``my_database``, and the new or existing schema being set up to be managed in this way is called ``my_schema``.

There will be a group for this schema for each of the following:


.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Group
     - Activities

   * - database designers
     - create, alter and drop tables

   * - updaters
     - insert and delete data

   * - readers
     - read data

   * - security officers
     - add and remove users from these groups

As a superuser, you connect to the system and run the following:

.. code-block:: postgres

   -- create the groups

   CREATE ROLE my_schema_security_officers;
   CREATE ROLE my_schema_database_designers;
   CREATE ROLE my_schema_updaters;
   CREATE ROLE my_schema_readers;

   -- grant permissions for each role
   -- we grant permissions for existing objects here too, 
   -- so you don't have to start with an empty schema

   -- security officers

   GRANT connect ON DATABASE my_database TO my_schema_security_officers;
   GRANT usage ON SCHEMA my_schema TO my_schema_security_officers;

   GRANT my_schema_database_designers TO my_schema_security_officers WITH ADMIN OPTION;
   GRANT my_schema_updaters TO my_schema_security_officers WITH ADMIN OPTION;
   GRANT my_schema_readers TO my_schema_security_officers WITH ADMIN OPTION;

   -- database designers

   GRANT connect ON DATABASE my_database TO my_schema_database_designers;
   GRANT usage ON SCHEMA my_schema TO my_schema_database_designers;

   GRANT create,ddl ON SCHEMA my_schema TO my_schema_database_designers;

   -- updaters

   GRANT connect ON DATABASE my_database TO my_schema_updaters;
   GRANT usage ON SCHEMA my_schema TO my_schema_updaters;

   GRANT SELECT,INSERT,DELETE ON ALL TABLES IN SCHEMA my_schema TO my_schema_updaters;

   -- readers

   GRANT connect ON DATABASE my_database TO my_schema_readers;
   GRANT usage ON SCHEMA my_schema TO my_schema_readers;

   GRANT SELECT ON ALL TABLES IN SCHEMA my_schema TO my_schema_readers;
   GRANT EXECUTE ON ALL FUNCTIONS TO my_schema_readers;


   -- create the default permissions for new objects

   ALTER DEFAULT PERMISSIONS FOR my_schema_database_designers IN my_schema
    FOR TABLES GRANT SELECT,INSERT,DELETE TO my_schema_updaters;

   ALTER DEFAULT PERMISSIONS FOR my_schema_database_designers IN my_schema
    FOR TABLES GRANT SELECT TO my_schema_readers;


This process needs to be repeated by a superuser each time a new
schema is brought into this permissions management approach.

.. todo:
   create some example users
   show that they have the right permission
   try out the with admin option. we can't really do a security officer because
   only superusers can create users and logins. see what can be done
   need 1-2 users in each group, for at least 2 schemas/departments
   this example will be very big just to show what this setup can do ...
   example: a security officer for a department which will only have
     read only access to a schema can only get that with admin option
     access granted to them

After this setup:

* Database designers will be able to run any ddl on objects in the schema and create new objects, including ones created by other database designers
* Updaters will be able to insert and delete to existing and new tables
* Readers will be able to read from existing and new tables

All this will happen without having to run any more grant statements.

Any security officer will be able to add and remove users from these
groups. Creating and dropping login users themselves must be done by a
superuser.
