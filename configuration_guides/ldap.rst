.. _ldap:

*************************************
Configuring LDAP authentication
*************************************


Lightweight Directory Access Protocol (LDAP) is an authentication management service. Once LDAP is configured to authenticate SQream users, all existing SQream roles, with the exception of a ``SUPERUSER``, will be required to be authenticated by an LDAP server.

It is recommended that SQream roles be configured before integrating LDAP authentication.

This is ideal for when:
	* SQream DB is being installed within an environment which had already been integrated with LDAP
	* Creating a new SQream role when SQream DB had already been integrated with LDAP

.. contents:: In this topic:
   :local:



Configuring SQream roles
========================



**Procedure**

1. Create a new role:
	
.. code-block:: postgres	
	
	CREATE ROLE <new_role>;

2. Grant new role login permission:

.. code-block:: postgres

	GRANT LOGIN TO <new_role>;

3. Grant the new role ``CONNECT`` permission:

.. code-block:: postgres

	GRANT CONNECT ON DATABASE <my_database> TO <new_role>;


.. note:: If no role exists but LDAP authentication is successful, a role with no login or connection permissions will be added.


Configuring LDAP Authentication
===============================

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
     - Configure the IP address or the Fully Qualified Domain Name (FQDN) of your LDAP server and select a protocol. Out of the ``ldap`` and ``ldaps``, we recommend to use the encrypted ``ldaps`` protocol.
   * - ``ldapConnTimeoutSec``
     - Configure the LDAP connection timeout threshold (seconds). The default is 30 seconds.
.. comment::

Enabling LDAP Authentication
-------------------------------

Only roles with SQream ``SUPERUSER`` privileges or higher may enable LDAP Authentication. 

**Procedure**

1. Set the ``ldapIpAddress`` attribute: 

.. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = 'ldaps://<192.168.10.20>';

2. Set the ``ldapDomain`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET ldapDomain = <'@sqream.loc'>;

3. To set the ``ldapConnTimeoutSec`` attribute (Optional), run:

.. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = <15>;

4. Set the ``authenticationMethod`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';

5. Restart all sqreamd servers. 


Disabling LDAP Authentication
-----------------------------

To disable LDAP authentication and configure sqream authentication: 

1. Execute the following syntax:

.. code-block:: postgres	

	ALTER SYSTEM SET authenticationMethod = 'sqream';

2. Restart all sqreamd servers.  
