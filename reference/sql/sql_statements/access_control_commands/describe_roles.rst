.. _describe_roles:

**************
DESCRIBE ROLES
**************

You may use the ``DESCRIBE ROLES`` command to list all roles defined in your system. Since BLUE roles refer to both users and their assigned privileges, you will receive a list of users along with the associated name, privileges, login, and password if exists.

.. note:: 
	
	``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

	DESCRIBE ROLES [LIKE 'pattern']
	DESC ROLES [LIKE 'pattern']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``LIKE``
     - ``pattern``
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.


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
   * - ``clusteradmin``
     - Validates whether or not role is a ``clusteradmin``
     - BOOL
     - 0
   * - ``login``
     - Validates whether or not role has login privileges. Enabled for actual users
     - BOOL
     - 1
   * - ``has_password``
     - Validates whether or not role has a password.
     - BOOL
     - 0

Examples
========

Executing ``DESCRIBE ROLES``
----------------------------

.. code-block:: postgres

	DESCRIBE ROLES;


Output:


.. code-block:: none

	id|name     |superuser|clusteradmin|login|has_password|
	--+---------+---------+------------+-----+------------+
	0 |public   |0        |0           |0    |0           |
	1 |sqream   |1        |0           |1    |1           |
	2 |new_role1|0        |1           |1    |1           |
	3 |new_role2|0        |0           |1    |1           |

Executing ``DESCRIBE ROLES LIKE``
---------------------------------

.. code-block:: sql

	DESCRIBE ROLES LIKE 'ne%';


Output:


.. code-block:: none

    id|name     |superuser|clusteradmin|login|has_password|
    --+---------+---------+------------+-----+------------+
    2 |new_role1|0        |1           |1    |1           |
    3 |new_role2|0        |0           |1    |1           |


Permissions
===========

This command requires a ``SUPERUSER`` permission.
