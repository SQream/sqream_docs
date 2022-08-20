.. _drop_role:

*****************
DROP ROLE
*****************

``DROP ROLE`` remove roles.

Learn more about the permission system in the :ref:`access control guide<access_control>`.

See also :ref:`create_role`.

Permissions
=============

To drop a role, the current role must have the ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

   drop_role_statement ::=
      DROP ROLE role_name ;

   role_name ::= identifier  

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role to drop.


Examples
===========

Dropping a role
-----------------------------------------

.. code-block:: postgres

   DROP ROLE new_role;
