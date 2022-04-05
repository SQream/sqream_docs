.. _dump_database_ddl:

*****************
DUMP_DATABASE_DDL
*****************

``DUMP_DATABASE_DDL()`` is a function that shows the ``CREATE`` statements for database objects including views and tables. Begining with 2020.3.1, DUMP_DATABASE_DDL includes foreign tables in the output.

.. warning:: 
   This function does not currently show UDFs. To list available UDFs, use the catalog:
   
   .. code-block:: psql

      farm=> SELECT * FROM sqream_catalog.user_defined_functions;
      farm,1,my_distance
   
   Then, export UDFs one-by-one using :ref:`GET_FUNCTION_DDL<get_function_ddl>`.

.. tip:: 
   * For just tables, see :ref:`GET_DDL<get_ddl>`.
   * For just views, see :ref:`GET_VIEW_DDL<get_view_ddl>`.
   * For UDFs, see :ref:`GET_FUNCTION_DDL<get_function_ddl>`.

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.

Syntax
==========

.. code-block:: postgres

   dump_database_ddl_statement ::=
       SELECT DUMP_DATABASE_DDL()
       ;

Parameters
============

This function accepts no parameters.

Examples
===========

Getting the DDL for a database
---------------------------------

.. code-block:: psql

   farm=> SELECT DUMP_DATABASE_DDL();
   create table "public"."cool_animals" (
     "id" int not null,
     "name" text(30) not null,
     "weight" double null,
     "is_agressive" bool default false not null
   )
   ;

   create view "public".angry_animals as
     select
         "cool_animals"."id" as "id",
         "cool_animals"."name" as "name",
         "cool_animals"."weight" as "weight",
         "cool_animals"."is_agressive" as "is_agressive"
       from
         "public".cool_animals as cool_animals
       where
         "cool_animals"."is_agressive" = false;



Exporting database DDL to a file
------------------------------------

.. code-block:: postgres

   COPY (SELECT DUMP_DATABASE_DDL()) TO '/home/rhendricks/database.ddl';
