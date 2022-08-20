.. _get_role_global_ddl:

********************
GET_ROLE_GLOBAL_DDL
********************
The ``GET_ROLE_GLOBAL_DDL`` statement returns the definition of a global role in DDL format.

The ``GET_ROLE_GLOBAL_DDL`` page describes the following:

.. contents:: 
   :local:
   :depth: 1   

Syntax
==========
The following is the correct syntax for using the ``GET_ROLE_GLOBAL_DDL`` statement:

.. code-block:: postgres

   select get_role_global_ddl(<'role_name'>)
   
Example
===========
The following is an example of using the ``GET_ROLE_GLOBAL_DDL`` statement:

.. code-block:: psql

   select get_role_global_ddl('public');

Parameters
============
The following table shows the ``GET_ROLE_GLOBAL_DDL`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The definition of the global role in DDL format.

Output
==========
The following is an example of the output of the ``GET_ROLE_GLOBAL_DDL`` statement:

.. code-block:: postgres

   create role "public";

Permissions
=============
Using the ``GET_ROLE_GLOBAL_DDL`` statement requires no special permissions.

For more information, see the following:

* :ref:`get_role_database_ddl`

    ::
	
* :ref:`get_role_permissions`