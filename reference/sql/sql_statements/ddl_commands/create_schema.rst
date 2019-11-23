.. _create_schema:

*****************
CREATE SCHEMA
*****************

``CREATE SCHEMA`` creates a new schema in an existing database. A schema is a virtual space for storing tables.

The default schema in SQream DB is ``public``.

.. tip:: Use schemas to separate between use-cases, such as staging and production.


Privileges
=============
The role must have the ``CREATE`` permission at the database level.

Synopsis
==========

.. code-block:: postgres

   create_schema_statement ::=
       CREATE SCHEMA schema_name
       ;

   schema_name ::= identifier  


Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema to create.

Examples
===========

Creating a schema
--------------------

.. code-block:: postgres

   CREATE SCHEMA staging;
    
   CREATE TABLE staging.users AS SELECT * FROM public.users;
   
   SELECT * FROM staging.users;

Altering the default schema for a role
-----------------------------------------

.. code-block:: postgres

   SELECT * FROM users; -- Refers to public.users
   
   ALTER DEFAULT SCHEMA FOR bgilfoyle TO staging;
   
   SELECT * FROM users; -- Now refers to staging.users, rather than public.users
