.. _describe_role_permissions:

*************************
DESCRIBE ROLE PERMISSIONS
*************************

You may use the ``DESCRIBE ROLE PERMISSIONS`` command to list all roles defined in your system. Since BLUE roles refer to both users and their assigned privileges, you will receive a list of users along with the associated name, privileges, login, and password if exists.

.. note:: 
	
	``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

	DESCRIBE ROLE PERMISSIONS ROLE NAME <role_name> [PERMISSION ID in (<permission id 1>,...,<permission id N>)];
	DESC ROLE PERMISSIONS ROLE NAME <role name> [PERMISSION ID in (<permission id 1>,...,<permission id N>)];

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``ROLE NAME``
     - ``role_name``
     - A mandatory parameter that specifies the role of which to list privileges
   * - ``PERMISSION ID``
     - ``permission_id``
     - An optional parameter that filters results by specific permission or permissions ID 
  
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``Role ID``
     - Role ID
     - ``INT``, ``SMALLINT``
   * - ``Role Name``
     - Role name
     - ``TEXT``
   * - ``Object/Layer``
     - ``TEXT``
     - Describes role permissions on the Database/Schema/Table/Function level
   * - ``Permission ID``
     - The specific permission's ID
     - ``INT``, ``SMALLINT``
   * - ``Permission Name``
     - The specific permission's name
     - ``TEXT``
   * - ``Superuser``
     - Validates whether or not role is a ``SUPERUSER``
     - ``BOOL``
   * - ``Cluster Admin``
     - Validates whether or not role is a ``clusteradmin``
     - ``BOOL``
   * - ``Login``
     - Validates whether or not the role has login privileges. Enabled for actual users
     - ``BOOL``



Examples
========

.. code-block:: sql

	DESCRIBE ROLE PERMISSIONS ROLE NAME role1;

Output:
  
.. code-block:: none

	role_id|role_name|Object/Layer |permission_id|permission_name|superuser|cluster_admin|login|
	-------+---------+-------------+-------------+---------------+---------+-------------+-----+
	12     |role1    |db1          |1003         |Connect        |0        |0            |0    |
	0      |public   |db1.public   |2000         |Create         |0        |1            |0    |
	0      |public   |db1.public   |2003         |Usage          |0        |1            |0    |
	0      |public   |master.public|2000         |Create         |0        |1            |0    |
	0      |public   |master.public|2003         |Usage          |0        |1            |0    |

.. code-block:: sql

	DESCRIBE ROLE PERMISSIONS ROLE NAME role1 PERMISSION ID in (2003);

Output:
  
.. code-block:: none

	role_id|role_name|Object/Layer |permission_id|permission_name|superuser|cluster_admin|login|
	-------+---------+-------------+-------------+---------------+---------+-------------+-----+
	0      |public   |db1.public   |2003         |Usage          |0        |1            |0    |
	0      |public   |master.public|2003         |Usage          |0        |1            |0    |

Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own permissions.
