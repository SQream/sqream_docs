.. _add_column:

**********************
ADD COLUMN
**********************

The ``ADD COLUMN`` command is used to add columns to an existing table.



Syntax
==========
The following is the correct syntax for adding a table:

.. code-block:: postgres

   alter_table_add_column_statement ::=
       ALTER TABLE [schema_name.]table_name { ADD COLUMN column_def [, ...] }
       ;

   table_name ::= identifier
   
   schema_name ::= identifier
   
   column_def :: = { column_name type_name [ default ] [ column_constraint ] }

   column_name ::= identifier
   
   column_constraint ::=
       { NOT NULL | NULL }
   
   default ::=
       DEFAULT default_value



Parameters
============
The following parameters can be used for adding a table:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified.
   * - ``table_name``
     - The table name to apply the change to.
   * - ``ADD COLUMN column_def``
     - A comma separated list of ADD COLUMN commands
   * - ``column_def``
     - A column definition. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.

.. note::
   * When adding a new column to an existing table, a default (or null constraint) has to be specified, even if the table is empty.
   * A new column added to the table can not contain an IDENTITY or be of the TEXT type.
   

Permissions
=============
The role must have the ``DDL`` permission at the database or table level.

Examples
===========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1
   
Adding a Simple Column with a Default Value
-----------------------------------------
This example shows how to add a simple column with a default value:

.. code-block:: postgres

   ALTER TABLE cool_animals 
     ADD COLUMN number_of_eyes INT DEFAULT 2 NOT NULL;
     

Adding Several Columns in One Command
-------------------------------------------
This example shows how to add several columns in one command:

.. code-block:: postgres

   ALTER TABLE cool_animals
     ADD COLUMN number_of_eyes INT DEFAULT 2 NOT NULL,
     ADD COLUMN date_seen DATE DEFAULT '2019-08-01'; 
