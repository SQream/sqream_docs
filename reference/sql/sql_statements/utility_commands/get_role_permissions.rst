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

Output
==========
The following is an example of the output of the ``GET_ROLE_PERMISSIONS`` statement:

.. code-block:: postgres

permission_type
object_type
object_name


   
   


Parameters
============
The following table shows the ``GET_ROLE_PERMISSIONS`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The permissions belonging to the role.

Permissions
=============
Using the ``GET_ROLE_PERMISSIONS`` statement requires no special permissions.

**Comment** - *Confirm.*

For more information, see the following:

* :ref:`get_role_database_ddl`

    ::
	
* :ref:`get_role_global_ddl`