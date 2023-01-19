.. _ldap:

*************************************
Configuring LDAP authentication
*************************************


Lightweight Directory Access Protocol (LDAP) is an authentication management service widely use with Microsoft Active Directory. Once it has been configured to authenticate SQream roles, all existing and newly added roles will be required to be authenticated by an LDAP server, with the exception of the initial system deployment ``sqream`` role, which is granted full control permissions upon deployment.

Prior to integrating SQream with LDAP, two preconditions must be considered:

	* If SQream DB is being installed within an LDAP-integrated environment, it is best practice to ensure that the newly created SQream role names are consistent with existing LDAP user names.
	
	* If LDAP is being integrated with a SQream environment, it is best practice to ensure that the newly created LDAP user names are consistent with existing SQream role names. Note that after LDAP has been successfully integrated, SQream roles that were mistakenly not configured or have conflicting names with LDAP will be recreated in SQream as roles without the ability to log in, without permissions, and without a default schema.

.. contents:: In this topic:
   :local:

Before You Begin
================

Enable self-signed certificates for OpenLDAP by adding the following line to the ``ldap.conf`` configuration file:

.. code-block:: postgres	

	``TLS_REQCERT allow``

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


You may also wish to :ref:`rename SQream roles<rename_role>`.


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

Roles with admin privileges or higher may enable LDAP Authentication. 

**Procedure**

1. Set the ``ldapIpAddress`` attribute: 

.. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = '<ldaps://...>';

2. Set the ``ldapDomain`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET ldapDomain = '<domain>';

3. To set the ``ldapConnTimeoutSec`` attribute (Optional), run:

.. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = <...>;

4. Set the ``authenticationMethod`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';

5. Restart all sqreamd servers. 

Example
-------

.. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = '<ldaps://192.168.10.20>';
	ALTER SYSTEM SET ldapDomain = '<@sqream.loc>';
	ALTER SYSTEM SET ldapConnTimeoutSec = <15>;
	ALTER SYSTEM SET authenticationMethod = 'ldap';
		
		
Disabling LDAP Authentication
-----------------------------

To disable LDAP authentication and configure sqream authentication: 

1. Execute the following syntax:

.. code-block:: postgres	

	ALTER SYSTEM SET authenticationMethod = 'sqream';

2. Restart all sqreamd servers.  
