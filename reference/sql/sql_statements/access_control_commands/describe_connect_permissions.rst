.. _describe_connect_permissions:

****************************
DESCRIBE CONNECT PERMISSIONS
****************************

The ``DESCRIBE CONNECT PERMISSIONS`` statement lists all roles and their database connection privileges.

.. note:: 
	
	``DESCRIBE`` commands use CPU to increase usability.
	
Syntax
======

.. code-block:: sql

	DESC[RIBE] CONNECT PERMISSIONS [DATABASE <database_name>] [ROLE ID IN (<role_id 1> [,...])] [PERMISSION ID IN (<permission_id 1> [,...])]

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``DATABASE``
     - ``database_name``
     - Enables filtering results by a specific database
     - ``TEXT``
   * - ``ROLE ID``
     - ``role_id``
     - Enables filtering by one or more role IDs
     - ``INT``
   * - ``PERMISSION ID``
     - ``permission_id``
     - Enables filtering by one or more permission IDs
     - ``INT``


Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``role_id``
     - The ID of a specific role
     - ``INT``
   * - ``role_name``
     - The name of a specific role
     - ``TEXT``
   * - ``database_name``
     - Database name
     - ``TEXT``
   * - ``permission_id``
     - Permission ID
     - ``INT``
   * - ``superuser``
     - Identifies whether or not a role has ``SUPERUSER`` permissions, with ``1`` indicating ``SUPERUSER`` status and ``0`` indicating regular system user
     - ``BOOL``
   * - ``clusteradmin``
     - Identifies whether or not a role is a ``clusteradmin`` , with ``1`` indicating ``clusteradmin`` status and ``0`` indicating non-clusteradmin user
     - ``BOOL``

Examples
========

.. code-block:: sql

	DESCRIBE CONNECT PERMISSIONS;

Output:

.. code-block:: none

	role_id|role_name              |database_name|permission_id|superuser|clusteradmin|
	-------+-----------------------+-------------+-------------+---------+------------+
	1      |sqream                 |master       |1002         |1        |0           |
	1      |sqream                 |master       |1003         |1        |0           |
	2      |someone@blue.com       |master       |1003         |1        |1           |
	4      |anothersomeone@blue.com|master       |1003         |1        |0           |
	6      |triceratop@blue.com    |master       |1003         |1        |1           |
	8      |tyrannosaurus@blue.com |master       |1003         |1        |1           |

Using optional parameters
-------------------------

.. code-block:: sql

	DESCRIBE CONNECT PERMISSIONS DATABASE master ROLE ID in (1,2,3) PERMISSION ID in (1002,1003);

Output:

.. code-block:: none

	role_id|role_name        |database_name|permission_id|superuser|clusteradmin|
	-------+-----------------+-------------+-------------+---------+------------+
	2      |someone@blue.com |master       |1003         |1        |1           |
	
	
Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own permissions.
	
