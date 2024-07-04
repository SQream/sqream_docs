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
	
Permissions
===========

This utility function requires a ``SUPERUSER`` permission.