.. _create_schema:

*****************
CREATE SCHEMA
*****************
The **CREATE SCHEMA** page describes the following:


.. contents:: 
   :local:
   :depth: 2
   
Overview
============

``CREATE SCHEMA`` creates a new schema in an existing database. A schema is a virtual space for storing tables.

The default schema in SQream DB is ``public``.

.. tip:: Use schemas to separate between use-cases, such as staging and production.

The **CREATE SCHEMA** statement can be used to query tables from different schemas without providing an alias, as in the following example:

.. code-block:: postgres

   select schema1.table1.column from schema1.table1 join schema2.table1 on schema1.table1.column1=schema2.table1.column1

See also: :ref:`drop_schema`, :ref:`alter_default_schema`.

Permissions
=============

The role must have the ``CREATE`` permission at the database level.

Syntax
==========
The following example shows the correct syntax for creating a schema:

.. code-block:: postgres

   create_schema_statement ::=
       CREATE SCHEMA schema_name
       ;

   schema_name ::= identifier  


Parameters
============
The following table shows the ``schema_name`` parameters:

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
The following example shows an example of the syntax for creating a schema:

.. code-block:: postgres

   CREATE SCHEMA staging;
    
   CREATE TABLE staging.users AS SELECT * FROM public.users;
   
   SELECT * FROM staging.users;

Altering the Default Schema for a Role
-----------------------------------------
The following example shows an example of the syntax for altering the default schema for a role:

.. code-block:: postgres

   SELECT * FROM users; -- Refers to public.users
   
   ALTER DEFAULT SCHEMA FOR bgilfoyle TO staging;
   
   SELECT * FROM users; -- Now refers to staging.users, rather than public.users