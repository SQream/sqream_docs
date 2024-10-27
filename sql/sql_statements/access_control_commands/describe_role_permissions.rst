:orphan:

.. _describe_role_permissions:

*************************
DESCRIBE ROLE PERMISSIONS
*************************

You may use the ``DESCRIBE ROLE PERMISSIONS`` command to list all roles defined in your system. Since BLUE roles refer to both users and their assigned privileges, you will receive a list of users along with the associated name, privileges, and login if exists.

.. note:: 
	
	``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

	DESC[RIBE] ROLE PERMISSIONS ROLE NAME <role_name> [PERMISSION ID in (<permission id 1> [,...])]

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``ROLE NAME``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - A mandatory parameter that specifies the role of which to list privileges
   * - ``PERMISSION ID``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - An optional parameter that filters results by specific permission or permissions ID 
  
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Type
     - Description
   * - ``Role ID``
     - ``INT``, ``SMALLINT``
     - The ID of a specific role
   * - ``Role Name``
     - ``TEXT``
     - The name of a specific role
   * - ``Object/Layer``
     - ``TEXT``
     - Describes role permissions on the Database/Schema/Table/Function level
   * - ``Permission ID``
     - ``INT``, ``SMALLINT``
     - The specific permission's ID
   * - ``Permission Name``
     - ``TEXT``
     - The specific permission's name
   * - ``Superuser``
     - ``BOOLEAN``
     - Validates whether or not role is a ``SUPERUSER``
   * - ``Cluster Admin``
     - ``BOOLEAN``
     - Validates whether or not role is a ``clusteradmin``
   * - ``Login``
     - ``BOOLEAN``
     - Validates whether or not the role has login privileges. Enabled for actual users



Examples
========

.. code-block:: sql

	DESCRIBE ROLE PERMISSIONS ROLE NAME "user1@someorg.com";

	role_id|role_name        |Object/Layer |permission_id|permission_name|superuser|cluster_admin|login|
	-------+-----------------+-------------+-------------+---------------+---------+-------------+-----+
	12     |user1@someorg.com|db1          |1003         |Connect        |0        |0            |0    |
	0      |public           |db1.public   |2000         |Create         |0        |1            |0    |
	0      |public           |db1.public   |2003         |Usage          |0        |1            |0    |
	0      |public           |master.public|2000         |Create         |0        |1            |0    |
	0      |public           |master.public|2003         |Usage          |0        |1            |0    |

.. code-block:: sql

	DESCRIBE ROLE PERMISSIONS ROLE NAME "user1@someorg.com" PERMISSION ID in (2003);

	role_id|role_name|Object/Layer |permission_id|permission_name|superuser|cluster_admin|login|
	-------+---------+-------------+-------------+---------------+---------+-------------+-----+
	0      |public   |db1.public   |2003         |Usage          |0        |1            |0    |
	0      |public   |master.public|2003         |Usage          |0        |1            |0    |

Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own permissions.
