.. _ldap:

********************
LDAP
********************


Lightweight Directory Access Protocol (LDAP) is an authentication management service used with Microsoft Active Directory and other directory services. Once LDAP authentication has been configured for SQream, authorization for all existing and newly added roles must be handled by the LDAP server, except for the initial system deployment ``sqream`` role, which was immediately given full control permissions when SQream was initially deployed. 

Before integrating SQream with LDAP consider the following:

* If SQream DB is being installed within an environment where LDAP is already configured, it is best practice to ensure that the newly created SQream role names are consistent with existing LDAP user names.

* If SQream DB has been installed and LDAP has not yet been integrated with SQream, it is best practice to ensure that the newly created LDAP user names are consistent with existing SQream role names. Previously existing SQream roles that were mistakenly not configured in LDAP or that have names which are different than in LDAP, will be recreated in SQream as roles that cannot log in, have no permissions, and have no default schema.

.. contents::
   :local:
   :depth: 1

Configuring SQream roles
========================

Follow this procedure if you already have LDAP configured for your environment.

1. Create a new role:
	
.. code-block:: postgres	
	
	CREATE ROLE <new_role>;

2. Grant the new role login permission:

.. code-block:: postgres

	GRANT LOGIN TO <new_role>;

3. Grant the new role ``CONNECT`` permission:

.. code-block:: postgres

	GRANT CONNECT ON DATABASE <my_database> TO <new_role>;

You may also wish to :ref:`rename SQream roles<rename_role>` so that they are consistent with existing LDAP user names.


Configuring LDAP Authentication
===============================

.. contents::
   :local:
   :depth: 1

Configuration Methods
---------------------

To configure LDAP authentication for SQream, you may choose one of the following configuration methods:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Method 
     - Description
   * - Basic method
     - A traditional approach to authentication in which the user provides a username and password combination to authenticate with the LDAP server. In this approach, all users are given access to SQream.
   * - Advanced method
     - This approach allows for compartmentalization, which means that users can be grouped into categories, and each category can be assigned or denied access to SQream. This allows administrators to control access to SQream.


   
Basic Method
------------

Flag Attributes
~~~~~~~~~~~~~~~

To enable basic LDAP authentication, configure the following cluster flag attributes using the ``ALTER SYSTEM SET`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Attribute
     - Description
   * - ``authenticationMethod``
     - Configure an authentication method: ``sqream`` or ``ldap``. To configure LDAP authentication, choose ``ldap``
   * - ``ldapIpAddress``
     - Configure the IP address or the Fully Qualified Domain Name (FQDN) of your LDAP server and select a protocol: ``ldap`` or ``ldaps``. Sqream recommends using the encrypted ``ldaps`` protocol
   * - ``ldapConnTimeoutSec``
     - Configure the LDAP connection timeout threshold (seconds). Default = 30 seconds
   * - ``ldapPort``
     - LDAP server port number.
   * - ``ldapAdvancedMode``
     - Configure either basic or advanced authentication method. Default = ``false``
   * - ``ldapPrefix``
     - String to prefix to the user name when forming the DN to bind as, when doing simple bind authentication
   * - ``ldapSuffix``
     - String to append to the user name when forming the DN to bind as, when doing simple bind authentication


Basic Method Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Only roles with admin privileges or higher may enable LDAP Authentication. 

**Procedure**

1. Set the ``authenticationMethod`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';
	
2. Set the ``ldapIpAddress`` attribute: 

.. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = '<ldaps://...>';
	
3. Set the ``ldapPrefix`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET ldapPrefix = '<DN_binding_string_prefix>=';
	
4. Set the ``ldapSuffix`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET ldapSuffix  = '<DN_binding_string_suffix>';

5.  To set the ``ldapPort`` attribute (Optional), run:

.. code-block:: postgres

	ALTER SYSTEM SET ldapPort = <port_number>
	
6. To set the ``ldapConnTimeoutSec`` attribute (Optional), run:

.. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = <15>;

7. Restart all sqreamd servers. 

Example
~~~~~~~

After completing the setup above, we can try to bind to a user by a distinguished name. For example, if the DN of the user is:

.. code-block:: postgres

	CN=ElonMusk,OU=Sqream Users,DC=sqream,DC=loc

We could set the ldapPrefix and ldapSuffix to 

.. code-block:: postgres

	ALTER SYSTEM SET ldapPrefix = 'CN=';

	ALTER SYSTEM SET ldapSuffix  = ',OU=Sqream Users,DC=sqream,DC=loc';

Logging in will be possible using the username ElonMusk using sqream client  

.. code-block:: postgres

	./sqream sql --username=ElonMusk --password=sqream123 --databasename=master --port=5000

Advanced Method
---------------

Flag Attributes
~~~~~~~~~~~~~~~

To enable advanced LDAP authentication, configure the following cluster flag attributes using the ``ALTER SYSTEM SET`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Attribute
     - Description
   * - ``authenticationMethod``
     - Configure an authentication method: ``sqream`` or ``ldap``. To configure LDAP authentication, choose ``ldap``
   * - ``ldapIpAddress``
     - Configure the IP address or the Fully Qualified Domain Name (FQDN) of your LDAP server and select a protocol: ``ldap`` or ``ldaps``. Sqream recommends using the encrypted ``ldaps`` protocol
   * - ``ldapConnTimeoutSec``
     - Configure the LDAP connection timeout threshold (seconds). Default = 30 seconds
   * - ``ldapPort``
     - LDAP server port number
   * - ``ldapAdvancedMode``
     - Set ``ldapAdvancedMode`` = ``true``
   * - ``ldapBaseDn``
     - Root DN to begin the search for the user in, when doing advanced authentication
   * - ``ldapBindDn``
     - DN of user with which to bind to the directory to perform the search when doing search + bind authentication
   * - ``ldapBindDnPassword``
     - Password for user with which to bind to the directory to perform the search when doing search + bind authentication
   * - ``ldapSearchAttribute``
     - Attribute to match against the user name in the search when doing search + bind authentication. If no attribute is specified, ``the uid`` attribute will be used
   * - ``ldapSearchFilter``
     - Filters ``ldapAdvancedMode`` authentication. ``ALTER SYSTEM SET ldapSearchFilter = '(<attribute>=<value>)(<attribute2>=<value2>)(…)';``

Advanced Method Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only roles with admin privileges and higher may enable LDAP Authentication. 

**Procedure**

1. Set the ``authenticationMethod`` attribute:

.. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';

2. Set the ``ldapAdvancedMode`` attribute:

.. code-block:: postgres
	
	ALTER SYSTEM SET ldapAdvancedMode = true;

3. Set the ``ldapIpAddress`` attribute: 

.. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = '<ldaps://<IpAddress>';

4. Set the ``ldapBindDn`` attribute: 

.. code-block:: postgres

	ALTER SYSTEM SET ldapBindDn = <binding_user_DN>;

5. Set the ``ldapBindDnPassword`` attribute: 

.. code-block:: postgres

	ALTER SYSTEM SET ldapBindDnPassword = '<binding_user_password>';
	
6. Set the ``ldapBaseDn`` attribute: 

.. code-block:: postgres	

	ALTER SYSTEM SET ldapBaseDn = '<search_root_DN>';
	
7. Set the ``ldapSearchAttribute`` attribute: 

.. code-block:: postgres	

	ALTER SYSTEM SET ldapSearchAttribute = '<search_attribute>';
	
8. To set the ``ldapSearchFilter`` attribute (Optional), run: 

.. code-block:: postgres	

	ALTER SYSTEM SET ldapSearchFilter = '(<attribute>=<value>)(<attribute2>=<value2>)(…)';

9. To set the ``ldapPort`` attribute (Optional), run:

.. code-block:: postgres

	ALTER SYSTEM SET ldapPort = <port_number>
	
10. To set the ``ldapConnTimeoutSec`` attribute (Optional), run:

.. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = <15>;

11. Restart all sqreamd servers. 

Example
~~~~~~~

After completing the setup above we can try to bind to a user by locating it by one of its unique attributes. 

User DN = 

.. code-block:: postgres

	CN=ElonMusk,OU=Sqream Users,DC=sqream,DC=loc

User has value of elonm for attribute ``sAMAccountName``.


.. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';
	
	ALTER SYSTEM SET ldapAdvancedMode = true;

	ALTER SYSTEM SET ldapIpAddress = 'ldaps://192.168.10.20';
	
	ALTER SYSTEM SET ldapPort = 5000

	ALTER SYSTEM SET ldapBindDn = 'CN=LDAP admin,OU=network admin,DC=sqream,DC=loc';

	ALTER SYSTEM SET ldapBindDnPassword = 'sqream123';

	ALTER SYSTEM SET ldapBaseDn = 'OU=Sqream Users,DC=sqream,DC=loc';
	
	ALTER SYSTEM SET ldapSearchAttribute = 'sAMAccountName';
	
	ALTER SYSTEM SET ldapConnTimeoutSec = 30;
	
	ALTER SYSTEM SET ldapSearchFilter =  "(memberOf=CN=SqreamGroup,CN=Builtin,DC=sqream,DC=loc)(memberOf=CN=Admins,CN=Builtin,DC=sqream,DC=loc)";
	
	
Logging in will be possible using the username elonm using sqream client  

.. code-block:: postgres

	./sqream sql --username=elonm --password=<elonm_password> --databasename=master --port=5000
	

Disabling LDAP Authentication
-----------------------------

To disable LDAP authentication and configure sqream authentication: 

1. Execute the following syntax:

.. code-block:: postgres	

	ALTER SYSTEM SET authenticationMethod = 'sqream';

2. Restart all sqreamd servers.  
