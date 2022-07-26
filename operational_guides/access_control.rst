.. _access_control:

**************
Access Control
**************
The **Access Control** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
==========
Access control refers to SQream's authentication and authorization operations, managed using a **Role-Based Access Control (RBAC)** system, such as ANSI SQL or other SQL products. SQream's default permissions system is similar to Postgres, but is more powerful. SQream's method lets administrators prepare the system to automatically provide objects with their required permissions.

SQream users can log in from any worker, which verify their roles and permissions from the metadata server. Each statement issues commands as the role that you're currently logged into. Roles are defined at the cluster level, and are valid for all databases in the cluster. To bootstrap SQream, new installations require one ``SUPERUSER`` role, typically named ``sqream``. You can only create new roles by connecting as this role.

Access control refers to the following basic concepts:

 * **Role** - A role can be a user, a group, or both. Roles can own database objects (such as tables) and can assign permissions on those objects to other roles. Roles can be members of other roles, meaning a user role can inherit permissions from its parent role.

    ::
   
 * **Authentication** - Verifies the identity of the role. User roles have usernames (or **role names**) and passwords.

    ::
 
 * **Authorization** - Checks that a role has permissions to perform a particular operation, such as the :ref:`grant` command.

Managing Roles
================
Roles are used for both users and groups, and are global across all databases in the SQream cluster. For a ``ROLE`` to be used as a user, it requires a password and log-in and connect permissionss to the relevant databases.

The Managing Roles section describes the following role-related operations:

.. contents:: 
   :local:
   :depth: 1

Creating New Roles (Users)
------------------------------
A user role logging in to the database requires ``LOGIN`` permissions and as a password.

The following is the syntax for creating a new role:

.. code-block:: postgres
                
   CREATE ROLE <role_name> ;
   GRANT LOGIN to <role_name> ;
   GRANT PASSWORD <'new_password'> to <role_name> ;
   GRANT CONNECT ON DATABASE <database_name> to <role_name> ;

The following is an example of creating a new role:

.. code-block:: postgres

   CREATE  ROLE  new_role_name  ;  
   GRANT  LOGIN  TO  new_role_name;  
   GRANT  PASSWORD  'my_password' to new_role_name;  
   GRANT  CONNECT  ON  DATABASE  master to new_role_name;

A database role may have a number of permissions that define what tasks it can perform, which are  assigned using the :ref:`grant` command.

Dropping a User
------------------------------
The following is the syntax for dropping a user:

.. code-block:: postgres

   DROP ROLE <role_name> ;

The following is an example of dropping a user:

.. code-block:: postgres

   DROP ROLE  admin_role ;

Altering a User Name
------------------------------
The following is the syntax for altering a user name:

.. code-block:: postgres

   ALTER ROLE <role_name> RENAME TO <new_role_name> ;

The following is an example of altering a user name:

.. code-block:: postgres

   ALTER ROLE admin_role RENAME TO copy_role ;

Changing a User Password
------------------------------
You can change a user role's password by granting the user a new password.

The following is an example of changing a user password:

.. code-block:: postgres

   GRANT  PASSWORD  <'new_password'>  TO  rhendricks;  

.. note:: Granting a new password overrides any previous password. Changing the password while the role has an active running statement does not affect that statement, but will affect subsequent statements.

Altering Public Role Permissions
------------------------------

There is a public role which always exists. Each role is granted to the ``PUBLIC`` role (i.e. is a member of the public group), and this cannot be revoked. You can alter the permissions granted to the public role.

The ``PUBLIC`` role has ``USAGE`` and ``CREATE`` permissions on ``PUBLIC`` schema by default, therefore, new users can create, :ref:`insert`, :ref:`delete`, and :ref:`select` from objects in the ``PUBLIC`` schema.


Altering Role Membership (Groups)
------------------------------

Many database administrators find it useful to group user roles together. By grouping users, permissions can be granted to, or revoked from a group with one command. In SQream DB, this is done by creating a group role, granting permissions to it, and then assigning users to that group role.

To use a role purely as a group, omit granting it ``LOGIN`` and ``PASSWORD`` permissions.

The ``CONNECT`` permission can be given directly to user roles, and/or to the groups they are part of.

.. code-block:: postgres

   CREATE ROLE my_group;

Once the group role exists, you can add user roles (members) using the ``GRANT`` command. For example:

.. code-block:: postgres

   -- Add my_user to this group
   GRANT my_group TO my_user;


To manage object permissions like databases and tables, you would then grant permissions to the group-level role (see :ref:`the permissions table<permissions_table>` below.

All member roles then inherit the permissions from the group. For example:

.. code-block:: postgres

   -- Grant all group users connect permissions
   GRANT  CONNECT  ON  DATABASE  a_database  TO  my_group;
   
   -- Grant all permissions on tables in public schema
   GRANT  ALL  ON  all  tables  IN  schema  public  TO  my_group;

Removing users and permissions can be done with the ``REVOKE`` command:

.. code-block:: postgres

   -- remove my_other_user from this group
   REVOKE my_group FROM my_other_user;

Permissions
===========
The following table displays the access control permissions:



+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Permission**     | **Description**                                                                                                         |
+====================+=========================================================================================================================+
| **Object/Layer: All Databases**                                                                                                              |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``LOGIN``          | use role to log into the system (the role also needs connect permission on the database it is connecting to)            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``PASSWORD``       | the password used for logging into the system                                                                           |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``      | no permission restrictions on any activity                                                                              |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Database**                                                                                                                   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``      | no permission restrictions on any activity within that database (this does not include modifying roles or permissions)  |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CONNECT``        | connect to the database                                                                                                 |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``         | create schemas in the database                                                                                          |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE FUNCTION``| create and drop functions                                                                                               |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Schema**                                                                                                                     |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``          | allows additional permissions within the schema                                                                         |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``         | create tables in the schema                                                                                             |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Table**                                                                                                                      |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``         | :ref:`select` from the table                                                                                            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``INSERT``         | :ref:`insert` into the table                                                                                            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``UPDATE``         | UPDATE the value of certain columns in existing rows without creating a table                                           |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DELETE``         | :ref:`delete` and :ref:`truncate` on the table                                                                          |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``            | drop and alter on the table                                                                                             |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``            | all the table permissions                                                                                               |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Function**                                                                                                                   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``        | use the function                                                                                                        |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``            | drop and alter on the function                                                                                          |   
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``            | all function permissions                                                                                                |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+




GRANT
-----

:ref:`grant` gives permissions to a role.

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
  
``GRANT`` examples:

.. code-block:: postgres

   GRANT  LOGIN,superuser  TO  admin;

   GRANT  CREATE  FUNCTION  ON  database  master  TO  admin;

   GRANT  SELECT  ON  TABLE  admin.table1  TO  userA;

   GRANT  EXECUTE  ON  FUNCTION  my_function  TO  userA;

   GRANT  ALL  ON  FUNCTION  my_function  TO  userA;

   GRANT  DDL  ON  admin.main_table  TO  userB;

   GRANT  ALL  ON  all  tables  IN  schema  public  TO  userB;

   GRANT  admin  TO  userC;

   GRANT  superuser  ON  schema  demo  TO  userA

   GRANT  admin_role  TO  userB;

REVOKE
------

:ref:`revoke` removes permissions from a role.

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
=======================

You work in a company with several departments.

The example below shows you how to manage permissions in a database shared by multiple departments, where each department has different roles for the tables by schema. It walks you through how to set the permissions up for existing objects and how to set up default permissions rules to cover newly created objects.

The concept is that you set up roles for each new schema with the correct permissions, then the existing users can use these roles. 

A superuser must do new setup for each new schema which is a limitation, but superuser permissions are not needed at any other time, and neither are explicit grant statements or object ownership changes.

In the example, the database is called ``my_database``, and the new or existing schema being set up to be managed in this way is called ``my_schema``.

Our departmental example has four user group roles and seven users roles

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

Setting up the department permissions
------------------------------------------

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

   -- For every table created by my_schema_database_designers, give access to my_schema_readers:
   
   ALTER DEFAULT PERMISSIONS FOR my_schema_database_designers IN my_schema
    FOR TABLES GRANT SELECT TO my_schema_readers;

.. note::
   * This process needs to be repeated by a user with ``SUPERUSER`` permissions each time a new schema is brought into this permissions management approach.
   
   * 
      By default, any new object created will not be accessible by our new ``my_schema_readers`` group.
      Running a ``GRANT SELECT ...`` only affects objects that already exist in the schema or database.
   
      If you're getting a ``Missing the following permissions: SELECT on table 'database.public.tablename'`` error, make sure that
      you've altered the default permissions with the ``ALTER DEFAULT PERMISSIONS`` statement.

Creating new users in the departments
-----------------------------------------

After the group roles have been created, you can now create user roles for each of your users.

.. code-block:: postgres

   -- create the new database designer users
   
   CREATE  ROLE  ecodd;
   GRANT  LOGIN  TO  ecodd;
   GRANT  PASSWORD  'ecodds_secret_password'  TO ecodd;
   GRANT  CONNECT  ON  DATABASE  my_database  TO  ecodd;
   GRANT my_schema_database_designers TO ecodd;

   CREATE  ROLE  ebachmann;
   GRANT  LOGIN  TO  ebachmann;
   GRANT  PASSWORD  'another_secret_password'  TO ebachmann;
   GRANT  CONNECT  ON  DATABASE  my_database  TO  ebachmann;
   GRANT my_database_designers TO ebachmann;

   -- If a user already exists, we can assign that user directly to the group
   
   GRANT my_schema_updaters TO rhendricks;
   
   -- Create users in the readers group
   
   CREATE  ROLE  jbarker;
   GRANT  LOGIN  TO  jbarker;
   GRANT  PASSWORD  'action_jack'  TO jbarker;
   GRANT  CONNECT  ON  DATABASE  my_database  TO  jbarker;
   GRANT my_schema_readers TO jbarker;
   
   CREATE  ROLE  lbream;
   GRANT  LOGIN  TO  lbream;
   GRANT  PASSWORD  'artichoke123'  TO lbream;
   GRANT  CONNECT  ON  DATABASE  my_database  TO  lbream;
   GRANT my_schema_readers TO lbream;
   
   CREATE  ROLE  pgregory;
   GRANT  LOGIN  TO  pgregory;
   GRANT  PASSWORD  'c1ca6a'  TO pgregory;
   GRANT  CONNECT  ON  DATABASE  my_database  TO  pgregory;
   GRANT my_schema_readers TO pgregory;

   -- Create users in the security officers group

   CREATE  ROLE  hoover;
   GRANT  LOGIN  TO  hoover;
   GRANT  PASSWORD  'mintchip'  TO hoover;
   GRANT  CONNECT  ON  DATABASE  my_database  TO  hoover;
   GRANT my_schema_security_officers TO hoover;


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

All this will happen without having to run any more ``GRANT`` statements.

Any security officer will be able to add and remove users from these
groups. Creating and dropping login users themselves must be done by a
superuser.