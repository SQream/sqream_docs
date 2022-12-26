.. _ldap:

*************************
LDAP Authentication
*************************

.. contents:: In this topic:
   :local:


Overview
========

Lightweight Directory Access Protocol (LDAP) is an authentication management service. Once LDAP is configured to authenticate SQream users, all existing roles, with the exception of a ``SUPERUSER``, are required to be authenticated by an LDAP server.


Flag Attributes
---------------
To enable LDAP Authentication, configure the following **cluster** flag attributes using the ``ALERT SYSTEM SET`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Attribute
     - Description
   * - ``authenticationMethod``
     - Configure an authentication method. Attribute may be set to either ``sqream`` or ``ldap``. To configure LDAP authentication, choose ``ldap``. 	 
   * - ``ldapDomain``
     - Configure users` domain.
   * - ``ldapIpAddress``
     - Configure the IP address of your LDAP server and select a protocol. Out of the ``ldap`` and ``ldaps``, we recommend to use the encrypted ``ldaps`` protocol.
   * - ``ldapConnTimeoutSec``
     - Configure the LDAP connection timeout threshold (seconds). The default is 30 seconds.

	 
LDAP Configuration
==================

Configuring system roles
------------------------
When using external authentication such as LDAP, it is recommend that roles be configured in advance.

To configure roles, follow these steps:

1. Create a new role.
	
.. code-block:: postgres	
	
	CREATE ROLE my_new_role;

2. Grant new role login permissions.

.. code-block:: postgres

	GRANT LOGIN TO my_new_role;

Grant the new role ``CONNECT`` permissions.

.. code-block:: postgres

	GRANT CONNECT ON DATABASE my_database TO my_new_role;

Note - in the case that no role exists but LDAP authentication is successful, a role with no login or connection permissions will be added.


Enabling LDAP Authentication
----------------------------

Only roles with admin privileges or higher may enable LDAP Authentication. 

To enable LDAP Authentication, follow these steps. The provided syntax for each of the steps is an example.

1. Set the ``ldapIpAddress`` attribute. 

.. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = 'ldaps://192.168.10.20';

2. Set the ``ldapDomain`` attribute.

.. code-block:: postgres

	ALTER SYSTEM SET ldapDomain = '@sqream.loc';

3. Set the ``ldapConnTimeoutSec`` attribute (Optional).

.. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = 15;

4. Set the ``authenticationMethod`` attribute.

.. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';

5. **Reset all ``sqreamd`` servers.** 


Disabling LDAP Authentication
-----------------------------

To disable LDAB authentication and configure sqream authentication, execute the following syntax:

.. code-block:: postgres	

	ALTER SYSTEM SET authenticationMethod = 'sqream';


