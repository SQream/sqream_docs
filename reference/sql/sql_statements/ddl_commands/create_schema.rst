.. _create_schema:

*****************
CREATE SCHEMA
*****************
The ``CREATE SCHEMA`` command creates a new schema in an existing database. A schema is a virtual space for storing tables. The default schema in SQream is ``public``.

.. tip:: You can use schemas to separate between use-cases, such as staging and production.

For more information, see the following:

* :ref:`drop_schema`
* :ref:`alter_default_schema`.

Overview
---------
The **CREATE SCHEMA** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Syntax
==========
The following is the correct syntax for CREATE_SCHEMA:

.. code-block:: postgres

   create_schema_statement ::=
       CREATE SCHEMA schema_name
       ;

   schema_name ::= identifier  


Parameters
============
The following table shows the CREATE_SCHEMA parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema to create.

Examples
===========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1
   
Creating a Schema
--------------------
The following example shows how to create a schema:

.. code-block:: postgres

   CREATE SCHEMA staging;
    
   CREATE TABLE staging.users AS SELECT * FROM public.users;
   
   SELECT * FROM staging.users;

Altering the Default Schema for a Role
-----------------------------------------
The following example shows how to alter the default schema for a role:

.. code-block:: postgres

   SELECT * FROM users; -- Refers to public.users
   
   ALTER DEFAULT SCHEMA FOR bgilfoyle TO staging;
   
   SELECT * FROM users; -- Now refers to staging.users, rather than public.users

Permissions
=============
The role must have the ``CREATE`` permission at the database level.