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

	DESC[RIBE] CONNECT PERMISSIONS [DATABASE <database_name>] [ROLE ID IN (<role_id> [,...])] [PERMISSION ID IN (<permission_id> [,...])]

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``DATABASE``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - Filters by a specific database
   * - ``ROLE ID``
     - :ref:`NUMBER<sql_data_types_numeric>` 
     - Filters by one or more role IDs
   * - ``PERMISSION ID``
     - :ref:`NUMBER<sql_data_types_numeric>` 
     - Filters by one or more permission IDs
	 
	 
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``role_id``
     - ``INT``
     - The ID of a specific role
   * - ``role_name``
     - ``TEXT``
     - The name of a specific role
   * - ``database_name``
     - ``TEXT``
     - Database name
   * - ``permission_id``
     - ``INT``
     - The specific permission's ID
   * - ``superuser``
     - ``BOOLEAN``
     - Identifies whether or not a role has ``SUPERUSER`` permissions, with ``1`` indicating ``SUPERUSER`` status and ``0`` indicating regular system user
   * - ``clusteradmin``
     - ``BOOLEAN``
     - Identifies whether or not a role is a ``clusteradmin`` , with ``1`` indicating ``clusteradmin`` status and ``0`` indicating non-clusteradmin user

Examples
========

.. code-block:: sql

	DESCRIBE CONNECT PERMISSIONS;

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

	DESCRIBE CONNECT PERMISSIONS DATABASE products ROLE ID in (1,2,3) PERMISSION ID in (1002,1003);

	role_id|role_name        |database_name|permission_id|superuser|clusteradmin|
	-------+-----------------+-------------+-------------+---------+------------+
	2      |someone@blue.com |products     |1003         |1        |1           |
	
	
Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own permissions.
	
