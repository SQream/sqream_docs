:orphan:

.. _create_role:

*****************
CREATE ROLE
*****************

``CREATE ROLE`` creates roles which can be assigned permissions.

A ``ROLE`` can be used as a ``USER`` if it has been granted login permissions.

Learn more about the permission system in the :ref:`access control guide<access_control>`.

See also :ref:`drop_role`, :ref:`alter_role`, :ref:`grant`.

Permissions
=============

To create a role, the current role must have the ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

   create_role_statement ::=
      CREATE ROLE role_name ;

   role_name ::= identifier  

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role to create, which must be unique across the cluster

Notes
==========

BLUE recommend that role names should follow these rules:

* Are case-insensitive

* Start with either a letter or underscore

* Contain only ASCII letters, numbers, or underscores

* Follow rules for :ref:`keywords_and_identifiers`

* A role has no permissions by default. Follow the examples below to see how to grant permissions to databases and tables.

* Roles can be members of other roles.

* Roles must be unique across the cluster.

* Roles cannot log in by default. They do not have login permissions until granted.

Examples
===========

Creating a role with no permissions
-----------------------------------------

.. code-block:: postgres

   CREATE ROLE new_role;


Creating a user role
-------------------------

A user role has permissions to login.

.. code-block:: postgres

   CREATE ROLE new_role;
   GRANT LOGIN to new_role;
   GRANT CONNECT ON DATABASE master to new_role; -- Repeat for all desired databases
   GRANT ALL ON SCHEMA public; -- It is advisable to grant permissions on at least one schema


