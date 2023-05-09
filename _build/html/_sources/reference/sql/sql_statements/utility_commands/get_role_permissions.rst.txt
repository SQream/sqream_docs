.. _get_role_permissions:

********************
GET_ROLE_PERMISSIONS
********************
The ``GET_ROLE_PERMISSIONS`` statement returns all permissions granted to a role in table format.

The ``GET_ROLE_PERMISSIONS`` page describes the following:

.. contents:: 
   :local:
   :depth: 1 

Syntax
==========
The following is the correct syntax for using the ``GET_ROLE_PERMISSIONS`` statement:

.. code-block:: postgres

   select get_role_permissions()
      
Example
===========
The following is an example of using the ``GET_ROLE_PERMISSIONS`` statement:

.. code-block:: psql

   select get_role_permissions();

Parameters
============
The following table shows the ``GET_ROLE_PERMISSIONS`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``()``
     - The permissions belonging to the role.

Output
==========
The following is an example of the output of the ``GET_ROLE_PERMISSIONS`` statement:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Example
   * - ``permission_type``
     - The permission type granted to the role.
     - SUPERUSER
   * - ``object_type``
     - The data object type.
     - table
   * - ``object_name``
     - The name of the object.
     - master.public.nba

Permissions
=============
Using the ``GET_ROLE_PERMISSIONS`` statement requires no special permissions.

For more information, see the following:

* :ref:`get_role_database_ddl`

    ::
	
* :ref:`get_role_global_ddl`