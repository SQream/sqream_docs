.. _create_schema:

*************
CREATE SCHEMA
*************

The ``CREATE SCHEMA`` command is used to establish a new schema within an existing database. A schema represents a logical space where tables are organized and stored.

By default, the primary schema in SQream DB is named ``public``.

Schemas are instrumental for organizing and separating different use-cases within a database, for instance, segregating staging and production environments.

See also: :ref:`drop_schema`, :ref:`alter_default_schema`, :ref:`rename_schema`.

Syntax
======

.. code-block:: postgres

	CREATE SCHEMA ["<database_name>".]"<schema_name>"

Parameters
==========

The following table shows the ``schema_name`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema to create
   * - ``database_name``
     - The name of the database within to create the schema

Examples
========

Creating a Schema
-----------------

.. code-block:: postgres

	CREATE SCHEMA staging;
    
	CREATE TABLE staging.users AS
	  SELECT *
	  FROM public.users; 
   
	SELECT * 
	FROM staging.users;

Querying Tables from Different Schemas Without Providing Alias
--------------------------------------------------------------

.. code-block:: postgres

	SELECT 
	  public.users.column1 
	FROM public.users

Altering the Default Schema for a Role
--------------------------------------

.. code-block:: postgres

	SELECT * 
	FROM users; -- Refers to public.users
   
	ALTER DEFAULT SCHEMA FOR bgilfoyle TO staging;
   
	SELECT * 
	FROM users; -- Now refers to staging.users, rather than public.users

Permissions
===========

The role must have the ``CREATE`` permission at the database level.