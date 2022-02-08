.. _viewing_system_objects_as_ddl:

********************************
Seeing System Objects as DDL
********************************

Dump specific objects
===========================

Tables
----------

See :ref:`get_ddl` for more information. 

.. rubric:: Examples

Getting the DDL for a table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   farm=> SELECT GET_DDL('cool_animals');
   create table "public"."cool_animals" (
     "id" int not null,
     "name" varchar(30) not null,
     "weight" double null,
     "is_agressive" bool default false not null )
     ;

Exporting table DDL to a file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: postgres

   COPY (SELECT GET_DDL('cool_animals')) TO '/home/rhendricks/animals.ddl';

Views
----------

See :ref:`get_view_ddl` for more information.

.. rubric:: Examples

Listing all views
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   farm=> SELECT view_name FROM sqream_catalog.views;
   view_name             
   ----------------------
   angry_animals         
   only_agressive_animals


Getting the DDL for a view
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: postgres

   COPY (SELECT GET_VIEW_DDL('angry_animals')) TO '/home/rhendricks/angry_animals.sql';

User defined functions
-------------------------

See :ref:`get_function_ddl` for more information.

.. rubric:: Examples

Listing all UDFs
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql
   
   master=> SELECT * FROM sqream_catalog.user_defined_functions;
   database_name | function_id | function_name
   --------------+-------------+--------------
   master        |           1 | my_distance  

Getting the DDL for a function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   master=> SELECT GET_FUNCTION_DDL('my_distance');
   create function "my_distance" (x1 float,
                               y1 float,
                               x2 float,
                               y2 float) returns float as
      $$  
      import  math  
      if  y1  <  x1:  
          return  0.0  
      else:  
          return  math.sqrt((y2  -  y1)  **  2  +  (x2  -  x1)  **  2)  
      $$
      language python volatile;

Exporting function DDL to a file
------------------------------------

.. code-block:: postgres

   COPY (SELECT GET_FUNCTION_DDL('my_distance')) TO '/home/rhendricks/my_distance.sql';

Saved queries
-----------------

See :ref:`list_saved_queries`, :ref:`show_saved_query` for more information.

Dump entire database DDLs
==================================

Dumping the database DDL includes tables and views, but not UDFs and saved queries.

See :ref:`dump_database_ddl` for more information.

.. rubric:: Examples

Exporting database DDL to a client
---------------------------------------

.. code-block:: psql

   farm=> SELECT DUMP_DATABASE_DDL();
   create table "public"."cool_animals" (
     "id" int not null,
     "name" varchar(30) not null,
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
---------------------------------------

.. code-block:: postgres

   COPY (SELECT DUMP_DATABASE_DDL()) TO '/home/rhendricks/database.ddl';



.. note:: To export data in tables, see :ref:`copy_to`.
