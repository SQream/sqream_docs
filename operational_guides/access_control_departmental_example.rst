.. _access_control_departmental_example:

**************
Departmental Example
**************
You work in a company with several departments.

The example below shows you how to manage permissions in a database shared by multiple departments, where each department has different roles for the tables by schema. It walks you through how to set the permissions up for existing objects and how to set up default permissions rules to cover newly created objects.

The concept is that you set up roles for each new schema with the correct permissions, then the existing users can use these roles. 

A superuser must do new setup for each new schema which is a limitation, but superuser permissions are not needed at any other time, and neither are explicit grant statements or object ownership changes.

In the example, the database is called ``my_database``, and the new or existing schema being set up to be managed in this way is called ``my_schema``.

.. figure:: /_static/images/access_control_department_example.png
   :scale: 60 %
   
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

