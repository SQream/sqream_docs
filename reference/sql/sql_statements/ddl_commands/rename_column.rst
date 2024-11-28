.. _rename_column:

*************
RENAME COLUMN
*************

The ``RENAME COLUMN`` command can be used to rename columns in a table.

Syntax
======

.. code-block:: postgres

	ALTER TABLE [schema_name.]table_name RENAME COLUMN current_name TO new_name

	schema_name ::= identifier
	
	table_name ::= identifier
   
	current_name ::= identifier

	new_name ::= identifier

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified
   * - ``table_name``
     - The table name to apply the change to
   * - ``current_name``
     - The column to rename
   * - ``new_name``
     - The new column name
     
Examples
========

Renaming a Column
-----------------

.. code-block:: postgres

	ALTER TABLE 
	  users RENAME COLUMN weight TO mass;

Renaming a Quoted Name
----------------------

.. code-block:: postgres

	ALTER TABLE 
	  users RENAME COLUMN "mass" TO "Mass" (Kilograms);
   
Permissions
===========

The role must have the ``DDL`` permission at the database or table level.