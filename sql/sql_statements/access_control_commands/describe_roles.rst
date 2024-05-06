:orphan:

.. _describe_roles:

**************
DESCRIBE ROLES
**************

You may use the ``DESCRIBE ROLES`` command to list all roles defined in your system. Since BLUE roles refer to both users and their assigned privileges, you will receive a list of users along with the associated name, privileges, and login if exists.

.. note:: 
	
	``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

	DESC[RIBE] ROLES [LIKE 'pattern']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match


Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``id``
     - ``INT``
     - The ID of a specific role
   * - ``name``
     - ``TEXT``
     - The name of a specific role
   * - ``superuser``
     - ``BOOLEAN``
     - Identifies whether or not a role has ``SUPERUSER`` permissions, with ``1`` indicating ``SUPERUSER`` status and ``0`` indicating regular system user
   * - ``clusteradmin``
     - ``BOOLEAN``
     - Identifies whether or not a role is a ``clusteradmin`` , with ``1`` indicating ``clusteradmin`` status and ``0`` indicating non-clusteradmin user
   * - ``login``
     - ``BOOLEAN``
     - Validates whether or not role has login privileges. Enabled for actual users


Examples
========

Executing ``DESCRIBE ROLES``
----------------------------

.. code-block:: postgres

	DESCRIBE ROLES;

	id|name     |superuser|clusteradmin|login|
	--+---------+---------+------------+-----+
	0 |public   |0        |0           |0    |
	1 |sqream   |1        |0           |1    |
	2 |new_role1|0        |1           |1    |
	3 |new_role2|0        |0           |1    |

Executing ``DESCRIBE ROLES LIKE``
---------------------------------

.. code-block:: sql

	DESCRIBE ROLES LIKE 'ne%';

	id|name     |superuser|clusteradmin|login|
	--+---------+---------+------------+-----+
	2 |new_role1|0        |1           |1    |
	3 |new_role2|0        |0           |1    |


Permissions
===========

This command requires ``SUPERUSER`` permission.
