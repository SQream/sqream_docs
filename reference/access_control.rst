
.. _access_control:

**************
Access control
**************

.. toctree::
   :maxdepth: 2
   :caption: In this section:
   :glob:

The system which provides basic authentication and authorization for
users in SQream DB.

Authentication: this is how the system checks that you are who you say
you are. This is done using the familiar usernames and passwords.

Authorization: this is how the system checks that you are allowed to
do the action that you are trying to do.

Compared to ANSI SQL and other SQL products:

* we use roles as users and as groups, just like ANSI SQL and other
  SQL products you're familiar with

* we have a default permissions system based on the system in
  Postgres, but with more power. In most cases, this allows you to set
  things up so that every object you create gets permissions set
  automatically.

* we don't have row based permissions

* we don't have object ownership

.. http://docs.sqream.com/latest/manual/Content/Guides/Quick_Guides/Quick_guide_to_roles_and_permissions/Quick_guide_to_roles_and_permissions.htm

.. http://docs.sqream.com/latest/manual/Content/Concepts/12_1.10_Catalog_(information_schema).htm?tocpath=Concepts%7CCatalog%20(information%20schema)%7C_____0#Catalog_(information_schema)_..198

.. http://docs.sqream.com/latest/manual/Content/SQL_Reference_Guide/16_2.1_Data_Definition_Language.htm?tocpath=SQream%20DB%20%20SQL%20Reference%20Guide%7CData%20Definition%20Language%7C_____0#Database_Roles_and_Permissions_..322



Introductory examples
=====================

go through some basic permissions

show a user trying to do something without permission

then add the permission

then show it succeeding

show adding a new login user

show adding a user to another role

show adding a superuser


Reference for all permissions
=============================

attributes for a role: name and optional password

permissions:

* superuser
* login
* connect to database <database>
* create, ddl, superuser, create function <database>
* create, ddl, usage, superuser <schema>
* select, insert, delete, ddl <table>
* *  <all tables for a schema>
* execute | ddl <specific function>

what happens when e.g. a database doesn't exist

what if you drop it then recreate it

what are the options for default permissions

Permissions catalog
===================

show the permissions as data structures

make sure all this appears in the catalog

do the catalog reference/guide here for now

establish a better catalog: write create tables statements too
do full examples of querying the catalog

sqream_catalog.roles                  

sqream_catalog.role_memberships       

sqream_catalog.table_permissions      

sqream_catalog.database_permissions   

sqream_catalog.schema_permissions     

sqream_catalog.permission_types


How the permissions work
========================


How to work out if a user has permission to execute a statement?
-> go through all the options

the two parts are

1. work out what permissions are needed from a statement

2. work out what permissions a user has by role membership

how do default permissions work
-------------------------------

when you create an object:

the system looks for default permissions statements which match the
current role or a group the current role is in, and the object being
created

each match will behave as if a grant permissions statement was also
run, on the created object, granted to the target role in the default
permissions match, with the permissions in the default permissions
match

utility functions
=================

what utility functions are relevant for permissions

how do they interact with permissions

Syntax reference
================

Roles
-----

.. code-block:: sql

  create | alter |drop role
  grant
  alter default permissions

  CREATE ROLE role_name ;
  GRANT PASSWORD 'new_password' to role_name ;

  DROP ROLE role_name ;

  alter - rename only:

  ALTER ROLE role_name RENAME TO new_role_name ;

granting permissions
--------------------

to create a database installation wide superuser:

.. code-block:: sql

  GRANT SUPERUSER to <role>

  does a super user have login + connect to all databases?

to allow a user to login, and to connect to a database

.. code-block:: sql
                
  GRANT LOGIN to role_name ;
  GRANT CONNECT ON DATABASE database_name to role_name ;
  
can a user have one and not the other?

when should a user have a password

.. code-block:: sql

  GRANT 

	{ SUPERUSER
	| LOGIN 
	| PASSWORD '<password>' 
	} 
	TO <role> [, ...] 

  GRANT <role1> [, ...] 
	TO <role2> 
	[WITH ADMIN OPTION]


from the current docs, it's not that clear what all these mean

granting permissions to objects
-------------------------------

.. code-block:: sql

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


alter default permissions
-------------------------

.. code-block:: sql
                
  ALTER DEFAULT PERMISSIONS FOR <role_name>
       IN <schema_name> FOR TABLES
       GRANT { SELECT | INSERT | DELETE [,...] } TO <role_name>;

I think you can also do it for schemas?
       
how do you undo a default permissions - use revoke? something isn't
quite right about that

revoking permissions
--------------------

.. code-block:: sql
                
  -- Revoke permissions at the cluster level:
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
				
  -- Revoke privileges from other roles by granting one role to another:
	REVOKE <role1> [, ...] FROM <role2> [, ...] WITH ADMIN OPTION


Behaviour reference
===================

show examples of every permission? Or just a subset

example will have the permission fail

then the add permission statement

then the permission succeed

can also go through something similar for default permissions

Usage guides
============

minimal permission system use
-----------------------------

Trivial use of permissions system in sqream: use super user

how to add a new superuser role

what this means

adding a guest user

simple user, with limited read only ability


Basic use
---------

how to set up a group with permissions database wide for the following:

* security officer
* database architect
* updater
* reader
* udf author

how to maintain this


Advanced use
------------

permissions/group per schema

show a list of roles for a schema, how you set it up

then show how to maintain this system

variation: roles which cover multiple schemas

* what does a superuser need to do
* what can a division 'owner' do

maintain - how to add something missing or modify:

* a new schema
* a new division
* a new user
* remove access
* fix an existing schema to add permissions
* * maybe a mistake
* * maybe a division gets new access to an existing schema

key secure things:

* what can only superusers do
* what are normal users restricted from doing
* who else can do stuff with the permissions system
* how are divisions protected from other divisions
