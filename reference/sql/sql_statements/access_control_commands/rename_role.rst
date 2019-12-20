.. _rename_role:

**********************
RENAME ROLE
**********************

``RENAME ROLE`` can be used to rename a role.

Permissions
=============

The role must have the ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

   alter_role_rename_role_statement ::=
       ALTER ROLE role_name RENAME TO new_name
       ;

   role_name ::= identifier

   new_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The role name to apply the change to
   * - ``new_name``
     - The new role name

Notes
========

* Role names are unique across the cluster.

* SQream recommend that role names should follow these rules:

   * Are case-insensitive

   * Start with either a letter or underscore

   * Contain only ASCII letters, numbers, or underscores

   * Follow rules for :ref:`identifiers`



Examples
===========

Renaming a role
-----------------------------------------

.. code-block:: postgres

   ALTER ROLE rhendricks RENAME TO patches;
