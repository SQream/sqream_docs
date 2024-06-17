:orphan:

.. _drop_column:

***********
DROP COLUMN
***********
 
``DROP COLUMN`` can be used to remove columns from a table.

Syntax
======

.. code-block:: postgres

	ALTER TABLE [schema_name.]table_name DROP COLUMN column_name

	schema_name ::= identifier
	
	table_name ::= identifier

	column_name ::= identifier

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
   * - ``column_name``
     - The column to remove

Examples
========

Removing a Column
-----------------

.. code-block:: postgres

	ALTER TABLE 
	  users DROP COLUMN weight;

Removing a Column with a Quoted Identifier Name
-----------------------------------------------

.. code-block:: postgres

	ALTER TABLE 
	  users DROP COLUMN "Weight in kilograms";
   
Permissions
===========

The role must have the ``DDL`` permission at the database or table level.
