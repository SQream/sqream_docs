.. _get_all_roles_global_ddl:

********************
GET_ALL_ROLES_GLOBAL_DDL
********************
The ``GET_ALL_ROLES_GLOBAL_DDL`` statement returns the definition of all global roles in DDL format.

.. contents:: 
   :local:
   :depth: 1   

Syntax
==========
The following is the correct syntax for using the ``GET_ALL_ROLES_GLOBAL_DDL`` statement:

.. code-block:: postgres

   select get_all_roles_global_ddl()
   
Example
===========
The following is an example of using the ``GET_ALL_ROLES_GLOBAL_DDL`` statement:

.. code-block:: psql

   select get_all_roles_global_ddl();


Output
==========
The following is an example of the output of the ``GET_ALL_ROLES_GLOBAL_DDL`` statement:

.. code-block:: postgres

   create role "public"; create role "sqream"; grant superuser, login to "sqream" ;

Permissions
=============
Using the ``GET_ALL_ROLES_GLOBAL_DDL`` statement requires no special permissions.

For more information, see the following:

* :ref:`get_all_roles_database_ddl`

    ::
	
* :ref:`get_role_permissions`