.. _rename_column:

**********************
RENAME COLUMN
**********************
 
``RENAME COLUMN`` can be used to rename columns in a table.

Permissions
=============

The role must have the ``DDL`` permission at the database or table level.

Syntax
==========

.. code-block:: postgres

   alter_table_rename_column_statement ::=
       ALTER TABLE [schema_name.]table_name RENAME COLUMN current_name TO new_name
       ;

   table_name ::= identifier
   
   schema_name ::= identifier
   
   current_name ::= identifier

   new_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified.
   * - ``table_name``
     - The table name to apply the change to.
   * - ``current_name``
     - The column to rename.
   * - ``new_name``
     - The new column name.
     
Examples
===========

Renaming a column
-----------------------------------------

.. code-block:: postgres

   -- Remove the 'weight' column
   ALTER TABLE users RENAME COLUMN weight TO mass;

Renaming a quoted name
--------------------------

.. code-block:: postgres

   ALTER TABLE users RENAME COLUMN "mass" TO "Mass (Kilograms);