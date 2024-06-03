.. _get_role_database_ddl:

*********************
GET ROLE DATABASE DDL
*********************

The ``GET_ROLE_DATABASE_DDL`` statement returns the definition of a role's database in DDL format.

Syntax
======

.. code-block:: postgres

	SELECT GET_ROLE_DATABASE_DDL('<role_name>')

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The role for which to get database definition 

Example
=======

.. code-block:: postgres

   SELECT GET_ROLE_DATABASE_DDL('public');

Output:

.. code-block:: console

	Name|Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
	----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	ddl |grant create, usage on schema 'master'.'public' to 'public' ;alter default schema for 'public' to 'master'.'public';alter default permissions for 'public' for schemas grant superuser to creator_role ;alter default permissions for 'public' for tables grant select, insert, delete, update, ddl to creator_role ;alter default permissions for 'public' for external tables grant select, ddl to creator_role ;alter default permissions for 'public' for views grant select, ddl to creator_role ;|

Permissions
===========

Using the ``GET_ROLE_DATABASE_DDL`` statement requires no special permissions.
