.. _drop_role:

*****************
DROP ROLE
*****************

The ``DROP ROLE`` command is used for removing roles from the database. The optional ``IF EXISTS`` clause can be included to prevent an error if the specified role does not exist. If the ``IF EXISTS`` clause is omitted and the role does not exist, an error will be raised.

See also :ref:`create_role`.

Syntax
======

.. code-block:: postgres

   drop_role_statement ::=
      DROP ROLE [IF EXISTS] <role_name>

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