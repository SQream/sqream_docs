.. _get_view_ddl:

*****************
GET_VIEW_DDL
*****************

``GET_VIEW_DDL(<view name>)`` is a function that shows the :ref:`CREATE VIEW<create_view>` statement for a view.

.. tip:: 
   * For tables, see :ref:`GET_DDL<get_ddl>`.
   * For the entire database, see :ref:`DUMP_DATABASE_DDL<dump_database_ddl>`.
   * For UDFs, see :ref:`GET_FUNCTION_DDL<get_function_ddl>`.

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.

Syntax
==========

.. code-block:: postgres

   get_view_ddl_statement ::=
       SELECT GET_VIEW_DDL('[schema_name.]view_name')
       ;

   schema_name ::= identifier  

   view_name ::= identifier  

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema.
   * - ``view_name``
     - The name of the view.

Examples
===========

Getting the DDL for a view
-----------------------------

The result of the ``GET_VIEW_DDL`` function is a verbose version of the CREATE VIEW statement, which may include additional information that was added by SQream DB. For example, schemas and column names will be be specified explicitly.

.. code-block:: psql

   farm=> CREATE VIEW angry_animals AS SELECT * FROM cool_animals WHERE is_agressive = false;
   executed
   
   farm=> SELECT GET_VIEW_DDL('angry_animals');
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



Exporting view DDL to a file
-------------------------------

.. code-block:: postgres

   COPY (SELECT GET_VIEW_DDL('angry_animals')) TO '/home/rhendricks/angry_animals.sql';
