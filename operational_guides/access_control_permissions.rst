.. _access_control_permissions:

**************
Permissions
**************

The following table displays the access control permissions:

+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Permission**     | **Description**                                                                                                         |
+====================+=========================================================================================================================+
| **Object/Layer: All Databases**                                                                                                              |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``LOGIN``          | Use role to log into the system (the role also needs connect permission on the database it is connecting to)            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``PASSWORD``       | The password used for logging into the system                                                                           |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``      | No permission restrictions on any activity                                                                              |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Database**                                                                                                                   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SUPERUSER``      | No permission restrictions on any activity within that database (this does not include modifying roles or permissions)  |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CONNECT``        | Connect to the database                                                                                                 |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``         | Create schemas in the database                                                                                          |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE FUNCTION``| Create and drop functions                                                                                               |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Schema**                                                                                                                     |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``          | Grants access to schema objects                                                                                         |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``         | Create tables in the schema                                                                                             |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``            | Drop and alter on the schema                                                                                            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Table**                                                                                                                      |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``SELECT``         | :ref:`select` from the table                                                                                            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``INSERT``         | :ref:`insert` into the table                                                                                            |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``UPDATE``         | :ref:`update` the value of certain columns in existing rows                                                             |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DELETE``         | :ref:`delete` and :ref:`truncate` on the table                                                                          |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``            | Drop and alter on the table                                                                                             |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``            | All the table permissions                                                                                               |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Object/Layer: Function**                                                                                                                   |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``        | Use the function                                                                                                        |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``            | Drop and alter on the function                                                                                          |   
+--------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``            | All function permissions                                                                                                |
+--------------------+-------------------------------------------------------------------------------------------------------------------------+




GRANT
-----

:ref:`grant` gives permissions to a role.

.. code-block:: postgres

   -- Grant permissions at the instance/ storage cluster level:
   GRANT 

   { SUPERUSER
   | LOGIN 
   | UPDATE
   | PASSWORD '<password>' 
   } 
   TO <role_name> [, ...] 

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
   GRANT {{SELECT | INSERT | DELETE | DDL | UPDATE } [, ...] | ALL [PERMISSIONS]} 
   ON { TABLE <table_name> [, ...] | ALL TABLES IN SCHEMA <schema_name> [, ...]} 
   TO <role> [, ...] [NO INHERIT | INHERIT]
       
   -- Grant execute function permission: 
   GRANT {ALL | EXECUTE | DDL} ON FUNCTION { function_name [, ...]} 
   TO { role [, ...]}
       
   -- Allows role2 to use permissions granted to role1
   GRANT <role1> [, ...] 
   TO <role2> [, ...] 

    -- Also allows the role2 to grant role1 to other roles:
   GRANT <role1> [, ...] 
   TO <role2> [, ...]
  
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
   | UPDATE
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
   REVOKE { { SELECT | INSERT | DELETE | DDL | UPDATE } [, ...] | ALL }
   ON { [ TABLE ] <table_name> [, ...] | ALL TABLES IN SCHEMA

   -- Revoke execute function permission: 
   REVOKE {ALL | EXECUTE | DDL} ON FUNCTION { function_name [, ...]} FROM role_name [, ...]

         <schema_name> [, ...] }
   FROM <role> [, ...]
            
   -- Removes access to permissions in role1 by role 2
   REVOKE <role1> [, ...] FROM <role2> [, ...]

   -- Removes permissions to grant role1 to additional roles from role2
   REVOKE <role1> [, ...] FROM <role2> [, ...]


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
        | UPDATE
        | EXECUTE
        | ALL
        }