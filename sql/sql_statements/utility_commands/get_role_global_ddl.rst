:orphan:

.. _get_role_global_ddl:

*********************
GET ROLE GLOBAL DDL
*********************

The ``GET_ROLE_GLOBAL_DDL`` statement returns the definition of a role's database in DDL format.

Syntax
======

.. code-block:: postgres

	SELECT GET_ROLE_GLOBAL_DDL("<role_name>")

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

   SELECT GET_ROLE_GLOBAL_DDL("public");

Output:

.. code-block:: console

	ddl                                                          |
	-------------------------------------------------------------+
	create role "sqream";  grant superuser, login to "sqream" ;  |

Permissions
===========

Using the ``GET_ROLE_GLOBAL_DDL`` statement requires no special permissions.
