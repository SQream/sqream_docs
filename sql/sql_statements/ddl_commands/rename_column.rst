.. _rename_column:

**********************
RENAME COLUMN
**********************
The ``RENAME COLUMN`` command can be used to rename columns in a table.

Syntax
==========
The following is the correct syntax for the ``RENAME_COLUMN`` command:

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
The following table describes the `RENAME_COLUMN`` parameters:

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
The **Examples** section includes the following examples:

.. contents::
   :local:
   :depth: 1

Renaming a Column
-----------------------------------------
The following is an example of renaming a column:

.. code-block:: postgres

   -- Remove the 'weight' column
   ALTER TABLE users RENAME COLUMN weight TO mass;

Renaming a Quoted Name
--------------------------
The following is an example of renaming a quoted name:

.. code-block:: postgres

   ALTER TABLE users RENAME COLUMN "mass" TO "Mass (Kilograms);
   
Permissions
=============
The role must have the ``DDL`` permission at the database or table level.