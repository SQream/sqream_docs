.. _describe_roles:

*****************
DESCRIBE ROLES
*****************


The ``DESCRIBE ROLES`` command lists all roles defined in your system along with the associated role name, role privileges, login, and password. Since SQream roles refer to both users and their assigned roles, when you execute the ``DESCRIBE ROLES`` command, you will receive a list of all SQream users.

.. comment:: Clarification required for "login" and "password". 



Permissions
===========

This command requires a ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

	DESCRIBE ROLES [LIKE 'pattern'];

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``LIKE``
     - ``pattern``
     - Optional parameter for filtering by view name using wildcards.
     - TEXT


Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``id``
     - Role id
     - INT
     - 1
   * - ``name``
     - Role name
     - TEXT
     - new_role1
   * - ``superuser``
     - Validates whether or not role is a ``SUPERUSER``
     - BOOL
     - 0
   * - ``login``
     - Validates whether or not role has login privileges
     - BOOL
     - 1
   * - ``has_password``
     - Validates whether or not role has a password.
     - BOOL
     - 0

Examples
========

The following is the syntax for the ``DESCRIBE ROLES LIKE`` command:

.. code-block:: postgres

	DESCRIBE ROLES LIKE 'ne%';


The following is the output for the ``DESCRIBE ROLES LIKE`` command:


.. code-block:: console

	id|name     |superuser|login|has_password|
	--+---------+---------+-----+------------+
	2 |new_role1|0        |1    |0           |
	3 |new_role2|0        |1    |0           |