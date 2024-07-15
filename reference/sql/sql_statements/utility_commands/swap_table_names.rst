.. _swap_table_names:

****************
SWAP TABLE NAMES
****************

The ``SWAP_TABLE_NAMES`` command enables you to swap the names of two tables within a schema. 

Syntax
======

.. code-block:: postgres

	SELECT SWAP_TABLE_NAMES ('<schema_name>', '<table1_name>', '<table2_name>')	

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema both tables are contained within
   * - ``table_name``
     - The table name you wish to swap names for

Notes
=====

When setting views or performing any operation that points to a table whose name has been swapped, the view will address the same table name. If no columns are specified, the operation will succeed. However, if the operation references specific columns, it will fail because the view points to a table containing different columns.

Examples
========

.. code-block:: postgres

	SELECT SWAP_TABLE_NAMES ('public', 'table1', 'table2');	

Permissions
===========

This utility command requires a permission to execute utility functions.