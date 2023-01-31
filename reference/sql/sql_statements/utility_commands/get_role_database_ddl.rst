.. _get_role_database_ddl:

********************
GET_ROLE_DATABASE_DDL
********************
The ``GET_ROLE_DATABASE_DDL`` statement returns the definition of a global role in DDL format.

The ``GET_ROLE_DATABASE_DDL`` page describes the following:

.. contents:: 
   :local:
   :depth: 1   

Syntax
==========
The following is the correct syntax for using the ``GET_ROLE_DATABASE_DDL`` statement:

.. code-block:: postgres

   select get_role_database_ddl(<'role_name'>)

Example
===========
The following is an example of using the ``GET_ROLE_DATABASE_DDL`` statement:

.. code-block:: psql

   select get_role_database_ddl('public');

Parameters
============
The following table shows the ``GET_ROLE_DATABASE_DDL`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The definition of the database role in DDL format.
   
Output
==========
The following is an example of the output of the ``GET_ROLE_DATABASE_DDL`` statement:

.. code-block:: postgres

   grant create, usage on schema "public" to "public" ; alter default schema for "public" to "public"; alter default permissions for "public" for schemas grant superuser to creator_role ; alter default permissions for "public" for tables grant select, insert, delete, ddl to creator_role ;

Permissions
=============
Using the ``GET_ROLE_DATABASE_DDL`` statement requires no special permissions.

For more information, see the following:

* :ref:`get_role_global_ddl`

    ::
	
* :ref:`get_role_permissions`