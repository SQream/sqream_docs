.. _get_ddl:

*****************
GET_DDL
*****************

``GET_DDL(<table name>)`` is a function that shows the :ref:`CREATE TABLE<create_table>` statement for a table.

.. tip:: 
   * For views, see :ref:`GET_VIEW_DDL<get_view_ddl>`.
   * For the entire database, see :ref:`DUMP_DATABASE_DDL<dump_database_ddl>`.
   * For UDFs, see :ref:`GET_FUNCTION_DDL<get_function_ddl>`.

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.

Synopsis
==========

.. code-block:: postgres

   get_ddl_statement ::=
       SELECT GET_DDL('[schema_name.]table_name')
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

Parameters
============

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
===========

Getting the DDL for a table
-----------------------------

The result of the ``GET_DDL`` function is a verbose version of the CREATE TABLE Syntax, which may include additional information that was added by SQream DB. For example, a ``NULL`` constraint may be specified explicitly.

.. code-block:: psql

   farm=> CREATE TABLE cool_animals (
      id INT NOT NULL,
      name varchar(30) NOT NULL,
      weight FLOAT,
      is_agressive BOOL DEFAULT false NOT NULL
   );
   executed
   
   farm=> SELECT GET_DDL('cool_animals');
   create table "public"."cool_animals" (
     "id" int not null,
     "name" varchar(30) not null,
     "weight" double null,
     "is_agressive" bool default false not null )
     ;

Exporting table DDL to a file
-------------------------------

.. code-block:: postgres

   COPY (SELECT GET_DDL('cool_animals')) TO '/home/rhendricks/animals.ddl';
