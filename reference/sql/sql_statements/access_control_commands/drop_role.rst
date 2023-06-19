.. _drop_role:

*****************
DROP ROLE
*****************

The ``DROP ROLE`` command is used for removing roles.

See also :ref:`create_role`.

Syntax
======

.. code-block:: postgres

   drop_role_statement ::=
      DROP ROLE <role_name>

   role_name ::= identifier  
   
Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - Role name to be removed

Examples
========

.. code-block:: postgres

   DROP ROLE new_role;

Permissions
===========

To drop a role, the current role must have a ``SUPERUSER`` permission.

You can learn more about system permissions in the :ref:`access control guide<access_control>`.