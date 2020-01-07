.. _access_control:

**************
Access control
**************

.. contents:: In this topic:
   :local:

Overview
=========


Access control provides authentication and authorization in SQream DB.

Authentication: this is how the system checks that you are who you say you are. This is done using the familiar usernames and passwords. The role object is used for both users and groups (which can be used to manage permissions for multiple users together).

Authorization: this is how the system checks that you are allowed to do the action that you are trying to do. This is implemented using grant and revoke (a.k.a. permissions).

Compared to ANSI SQL and other SQL products:

* SQream DB has roles as users and as groups, like ANSI SQL and other SQL products a user may be familiar with

* SQream DB has a default permissions system based on the system in Postgres, but with more power.
  In most cases, this allows an administrator to set things up so that every object gets permissions set automatically.

* SQream DB does not have row based permissions

* SQream DB does not have object ownership


Roles
-----

SQream has the standard ROLE object. Roles are used for users and for groups.

To use a ROLE a USER, it should have a password, and login and connect permissions to the relevant databases.

CREATE ROLE
^^^^^^^^^^^

Adds a new user/role to the instance/ storage cluster.

.. code-block:: postgres
                
  create_role_statement ::=

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

DROP ROLE
^^^^^^^^^

Deletes a role/user.

.. code-block:: postgres

  drop_role_statement ::=

      DROP ROLE role_name ;

Examples:

.. code-block:: postgres

  DROP  ROLE  admin_role;

ALTER ROLE
^^^^^^^^^^

Renames an existing role.

.. code-block:: postgres

  alter_role_statement ::=

      ALTER ROLE role_name RENAME TO new_role_name ;

Examples:

.. code-block:: postgres

  ALTER  ROLE  admin_role  RENAME  TO  copy_role;

Superusers
^^^^^^^^^^

There are two kinds of superusers - one for the entire instance/storage cluster, and a superuser for a given database or schema.

PUBLIC Role
^^^^^^^^^^^

There is a public role which always exists. Each role is granted to the PUBLIC role, and this cannot be revoked. You can alter the permissions granted to the public role.

The PUBLIC role has USAGE and CREATE permissions on PUBLIC schema by default, therefore, new users can create and manage their own objects in the PUBLIC schema.


Permissions
-----------

Each role can be granted permissions.

Roles are global across all databases in the instance/ storage cluster.

For a role to function as a user in a database, it must have USAGE permission on the specific database.

Roles are granted permissions and access to specific objects. The specified object can be any defined object such as a database or table.
    
Roles can be granted permissions to other roles, thus creating a hierarchy of role with increasingly specific or limited permissions for lower-level users.

For a role to create and manage (read/write/alter) objects, it has to have the CREATE and USAGE permissions.

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Object/layer
     - Permission
     - Description

   * - all databases
     - Login
     - Allows a role to be used to log into the system

   * - all databases
     - password
     - the password used for logging into the system

   * - all databases
     - create function
     - permission to create and drop functions

   * - all databases
     - superuser
     - no permission restrictions on any activity

       
   * - database
     - superuser
     -

   * - database
     - connect
     -

   * - database
     - create
     -

   * - database
     - usage 
     -

   * - schema
     - usage
     - has all permissions on existing and new objects in the schema

   * - schema
     - create
     -

   * - table
     - select
     -

   * - table
     - insert
     - allows inserting into the table

   * - table
     - delete
     - allows delete and truncate on the table

   * - table
     - ddl
     - allows drop and alter on the table

   * - table
     - all
     - all the table permissions

   * - function
     - execute
     - allows using the function

   * - function
     - ddl
     - allows drop and alter on the function

   * - function
     - all
     - all function permissions

GRANT
^^^^^

Grant is used to give permissions to roles.

CURRENT_ROLE refers to the current login role, and can be used as the <role> in permissions statements.

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
  	[WITH ADMIN OPTION]

    -- Also allows the role2 to grant role1 to other roles:
  	GRANT <role1> [, ...] 
  	TO <role2> 
  	WITH ADMIN OPTION
  
Examples:

.. code-block:: postgres

  GRANT  LOGIN,superuser  TO  admin;
  
  GRANT  CREATE  FUNCTION  TO  admin;
  
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
^^^^^^

Removes permissions from one or more roles.

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
below for how it can be used.

A default permissions rule looks for a schema being created, or a
table (possibly by schema), and is table to grant any permission to
that object to any role. This happens when the create table or create
schema statement is run.

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
  

Departmental Example
====================

This is an example of how to manage permissions in a database shared by multiple departments, where each department has different roles for the tables by schema. It shows how to set the permissions up for existing objects and how to set up default permissions rules to cover newly created objects.

.. todo: what are the activities that only a superuser can do

Here are the roles that can be assigned per department/schema:

* superuser - sets up the system and permissions
* security officer – change group membership
* database architect – create/modify table structure DDL
* updater - modify tables data (DML)
* reader - read data, execute functions, use views, etc.
* function author - create functions

The example assumes the following:

    database is my_database
    schema is my_schema

The superuser connects to any database.

Create the role r_security_officer and give it the ability to login and use database MYDB.

CREATE ROLE r_security_officer;

GRANT LOGIN to r_security_officer;

GRANT PASSWORD 'pass' to r_security_officer;

GRANT CONNECT ON DATABASE mydb to r_security_officer;

    Create the role r_database_architect and give it the needed permissions in schema dwh_schema:

Permissions: USAGE, CREATE and DDL

CREATE ROLE r_database_architect;

GRANT connect ON DATABASE mydb TO r_database_architect;

GRANT usage,create,ddl ON SCHEMA dwh_schema TO r_database_architect;

    Create the role r_updater and give it the needed permissions in schema dwh_schema on tables created by the r_database_architect  role group:

Permissions:SELECT/INSERT/DELETE on ALL tables

Run ALTER DEFAULT PERMISSION so that the permission will be granted for new tables in that schema as well.

CREATE ROLE r_updater;

GRANT connect ON DATABASE mydb TO r_updater;

GRANT usage ON SCHEMA dwh_schema TO r_updater;

GRANT SELECT,INSERT,DELETE ON ALL TABLES IN SCHEMA dwh_schema TO r_updater;

ALTER DEFAULT PERMISSIONS FOR r_database_architect IN dwh_schema FOR TABLES GRANT SELECT,INSERT,DELETE TO r_updater;

    Create the role r_udf_author and give it the needed permissions.

Permissions:

    SELECT on all the tables in schema dwh_schema
    CREATE FUNCTIONS (UDF)

Run ALTER DEFAULT PERMISSION so that the permission will be granted for new tables in that schema as well. 

CREATE ROLE r_udf_author;

GRANT connect ON DATABASE mydb TO r_udf_author;

GRANT usage ON SCHEMA dwh_schema TO r_udf_author;

GRANT CREATE FUNCTION ON DATABASE mydb TO r_udf_author;

GRANT SELECT ON ALL TABLES IN SCHEMA dwh_schema TO r_udf_author;

ALTER DEFAULT PERMISSIONS FOR r_database_architect IN dwh_schema FOR TABLES GRANT SELECT TO r_udf_author;

    Create the role r_reader and give it the needed permissions in schema dwh_schema on tables created by the r_database_architect  role group:

Permissions:

    SELECT on all the tables in schema dwh_schema
    EXECUTE ALL FUNCTIONS (UDFs)

Run ALTER DEFAULT PERMISSION so that the permission will be granted for new tables in that schema as well. 

CREATE ROLE r_reader;

GRANT connect ON DATABASE mydb TO r_reader;

GRANT usage ON SCHEMA dwh_schema TO r_reader;

GRANT SELECT ON ALL TABLES IN SCHEMA dwh_schema TO r_reader;

ALTER DEFAULT PERMISSIONS FOR r_database_architect IN dwh_schema FOR TABLES GRANT SELECT TO r_reader;

GRANT EXECUTE ON ALL FUNCTIONS TO r_reader;

GRANT EXECUTE FUCTION affects only existing functions.

    Give the role r_security_officer the ability to grant all the new roles to others:

GRANT r_database_architect TO r_security_officer WITH ADMIN OPTION;

GRANT r_updater TO r_security_officer WITH ADMIN OPTION;

GRANT r_reader TO r_security_officer WITH ADMIN OPTION;

GRANT r_udf_author TO r_security_officer WITH ADMIN OPTION;

At this point, the security officer (who is not a superuser) can grant any of the roles they were defined as admin of to any new users created by the superuser (role with login/password).
As a superuser:

    Create the roles user1, user2, user3 etc.

CREATE ROLE user1;

GRANT LOGIN to user1;

GRANT PASSWORD 'pass1' to user1;

CREATE ROLE user2;

GRANT LOGIN to user2;

GRANT PASSWORD 'pass2' to user2;

CREATE ROLE user3;

GRANT LOGIN to user3;

GRANT PASSWORD 'pass3' to user3;

CREATE ROLE user4;

GRANT LOGIN to user4;

GRANT PASSWORD 'pass4' to user4;
As the security officer:

GRANT r_database_architect TO user1;

GRANT r_reader TO user2;

GRANT r_udf_author TO user3;

GRANT r_updater TO user4;

Note that the ‘with admin option’ can be used in hierarchy. For example, if each department wishes to have its own dept_admin role, the superuser can create this role and grant it the required permissions with admin option so they can then assign the roles to users in their department.

Hierarchy example:

    As superuser:

CREATE ROLE dept1_admin;

GRANT LOGIN TO dept1_admin;

GRANT PASSWORD 'password' TO dept1_admin;

GRANT CONNECT ON DATABASE mydb TO dept1_admin;

    As the security officer or superuser:

GRANT r_reader TO dept1_admin WITH ADMIN OPTION;

    As the dept1_admin:

GRANT r_reader TO user2;
