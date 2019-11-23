.. _drop_column:

**********************
DROP COLUMN
**********************

``DROP COLUMN`` can be used to remove columns from a table.

Privileges
=============

The role must have the ``DDL`` permission at the database or table level.

Synopsis
==========

.. code-block:: postgres

   alter_table_drop_column_statement ::=
       ALTER TABLE [schema_name.]table_name DROP COLUMN column_name
       ;

   table_name ::= identifier
   
   schema_name ::= identifier
   
   column_name ::= identifier



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
   * - ``column_name``
     - The column to remove.

Examples
===========

Removing a column
-----------------------------------------

.. code-block:: postgres

   -- Remove the 'weight' column
   ALTER TABLE users DROP COLUMN weight;

Removing a column with a quoted identifier name
----------------------------------------------------

.. code-block:: postgres

   ALTER TABLE users DROP COLUMN "Weight in kilograms";