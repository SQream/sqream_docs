.. _is_table_exists:

**************************
IS TABLE EXISTS
**************************

The ``IS TABLE EXISTS`` check whether a table exists in a specified schema within the database.

Syntax
==========

.. code-block:: postgres

   SELECT is_table_exists(<'schema_name'>, <'table_name'>)
   

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema to search for the table within
   * - ``table_name``
     - The name of the table to check for existence

Returns
=======

* ``1`` if table exists
* ``0`` if table does not exist


Example
========

.. code-block:: psql

	SELECT is_table_exists('public', 'my_table');

	-----
	1

	
  

