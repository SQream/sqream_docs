.. _get_open_snapshots:

******************
GET_OPEN_SNAPSHOTS
******************
 
The ``GET_OPEN_SNAPSHOTS`` utility function lists information about all currently open snapshots.

Syntax
======

.. code-block:: postgres

	SELECT GET_OPEN_SNAPSHOTS()

Output
======

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description  
   * - ``database_name``
     - 	 
   * - ``reason``
     - 	 
   * - ``open_time``
     - 	 
   * - ``database_version``
     - 	 
   * - ``snapshot_id``
     - 	 
   * - ``statement_id``
     - 	 
   * - ``current_time``
     - 	 
   * - ``is_statement_active``
     - 	 
	 
Example
=======

.. code-block:: postgres

	SELECT GET_OPEN_SNAPSHOTS();
	
Output:

.. code-block:: console

	database_name |reason          |open_time          |database_version |snapshot_id |statement_id |current_time       |is_statement_active 
	--------------+----------------+-------------------+-----------------+------------+-------------+-------------------+-------------------
	master        |on_new_statement|2024-07-04 17:16:56|1                |30898       |0            |2024-07-04 17:16:57|1

	
Permissions
===========

This utility function requires a ``SUPERUSER`` permission.