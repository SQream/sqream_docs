.. _grant_usage_on_service_to_all_roles:

***********************************
GRANT_USAGE_ON_SERVICE_TO_ALL_ROLES
***********************************

The ``grant_usage_on_service_to_all_roles`` utility function enables a ``SUPERUSER`` to grant access to services for other system roles.

You may use it to perform one of the following options:

* Granting access to all services for all roles
* Granting access to a specific service for all roles


This utility function is particularly beneficial during the upgrade process from SQreamDB version 4.2 or earlier to version 4.3 or later. In previous versions, service access permissions were not required. In this scenario, you can easily grant access to all services for all roles immediately after the upgrade. If you are already using SQreamDB version 4.3 or later, you can grant or revoke access to services by following the :ref:`access permission guide<access_control_permissions>`. 

.. note::
	
	When you create a new role, it automatically inherits access permissions to all services from the ``PUBLIC`` role. If you prefer to create new roles without automatically granting them access permissions to all services, you will need to follow the :ref:`ALTER DEFAULT PERMISSIONS<alter_default_permissions>` guide to revoke the access permissions of the ``PUBLIC`` role.   

Syntax
======

.. code-block:: psql

   SELECT grant_usage_on_service_to_all_roles (<'single service'>)


Examples
========
Granting access to all services for all roles:

.. code-block:: psql

	SELECT grant_usage_on_service_to_all_roles();
	
Output:

.. code-block::

	role_name |  service_name |  status
	----------+---------------+--------------------
	role1     |  service1     |  Permission Granted
	role1     |  service2     |  Permission Granted
	role1     |  service3     |  Permission Granted
	role2     |  service1     |  Permission Granted
	role2     |  service2     |  Permission Granted
	role2     |  service3     |  Permission Granted
	role3     |  service1     |  Permission Exists
	role3     |  service2     |  Permission Exists
	role3     |  service3     |  Permission Exists

Granting access to one specific service for all roles:

.. code-block:: psql

	SELECT grant_usage_on_service_to_all_roles('service1');
	
Output:

.. code-block::

	role_name |  service_name |  status
	----------+---------------+--------------------
	role1     |  service1     |  Permission Granted
	role2     |  service1     |  Permission Granted
	role3     |  service1     |  Permission Exists
   

Permissions
===========

Using the ``grant_usage_on_service_to_all_roles`` requires ``SUPERUSER`` permission.

