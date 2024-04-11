.. _get_ddl:

*******
GET DDL
*******

The result of the ``GET_DDL`` function is a verbose version of the :ref:`create_table` syntax, which may include additional information that was added by SQream DB. For example, a ``NULL`` constraint may be specified explicitly.

See also: :ref:`GET_VIEW_DDL<get_view_ddl>`, :ref:`DUMP_DATABASE_DDL<dump_database_ddl>`, :ref:`GET_FUNCTION_DDL<get_function_ddl>`

Syntax
======

.. code-block:: postgres

   SELECT 
     GET_DDL(["<schema_name>".]"<table_name>")

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema.
   * - ``table_name``
     - The name of the table.

Examples
========

.. code-block:: psql

   -- Create a table:
   CREATE TABLE
     cool_animals (
       id INT NOT NULL,
       name TEXT(30) NOT NULL,
       weight FLOAT,
       is_agressive BOOL DEFAULT false NOT NULL
     );

   -- Get table ddl:
   SELECT
     GET_DDL("cool_animals");
     
   -- Result:
   create table
     "public"."cool_animals" (
       "id" INT NOT NULL,
       "name" TEXT(30) NOT NULL,
       "weight" DOUBLE NULL,
       "is_agressive" BOOL DEFAULT FALSE NOT NULL
     );

Exporting table DDL to a file
-------------------------------

.. code-block:: postgres

   COPY
     (
       SELECT
         GET_DDL("cool_animals")
     ) TO
   WRAPPER
     csv_fdw
   OPTIONS
     (LOCATION = 's3://sqream-docs/cool_animals_ddl.csv');

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.
