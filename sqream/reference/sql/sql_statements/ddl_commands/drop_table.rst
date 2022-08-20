.. _drop_table:

**********************
DROP TABLE
**********************

``DROP TABLE`` can be used to remove a table and all of its contents.

Permissions
=============

The role must have the ``DDL`` permission at the database or table level.

Syntax
==========

.. code-block:: postgres

   drop_table_statement ::=
       DROP TABLE [ IF EXISTS ] [schema_name.]table_name
       ;

   table_name ::= identifier
   
   schema_name ::= identifier



Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``IF EXISTS``
     - Drop the table if it exists. Does not error if the table does not exist.
   * - ``schema_name``
     - The name of the schema from which to drop the table.
   * - ``table_name``
     - The name of the table to drop.

Examples
===========

Dropping a table
---------------------------------------------

.. code-block:: postgres

   DROP TABLE cool_animals;


Dropping a table (always succeeds)
-------------------------------------

.. code-block:: psql

   farm=> DROP TABLE cool_animals;
   executed
   
   farm=> DROP TABLE cool_animals;
   Table 'public.cool_animals' not found
   
   -- This will succeed, even though the table does not exist
   farm=> DROP TABLE IF EXISTS cool_animals;
   executed
   
