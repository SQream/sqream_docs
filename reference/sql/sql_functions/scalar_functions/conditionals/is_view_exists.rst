.. _is_view_exists:

**************************
IS VIEW EXISTS
**************************

The ``IS VIEW EXISTS`` check whether a view exists in a specified schema within the database.

Syntax
==========

.. code-block:: postgres

   SELECT is_view_exists(<'schema_name'>, <'view_name'>)
   

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema to search for the view within
   * - ``table_name``
     - The name of the view to check for existence

Returns
=======

* ``1`` if view exists
* ``0`` if view does not exist


Example
========

.. code-block:: psql

	SELECT is_view_exists('public', 'my_view');

	-----
	1

	
  

