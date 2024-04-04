.. _ldap:

****
LDAP
****

Lightweight Directory Access Protocol (LDAP) is an authentication management service used with Microsoft Active Directory and other directory services. 

Once LDAP has been configured as an authentication service for SQreamDB, authentication for all existing and newly added roles is handled by an LDAP server. The exception for this rule is the out-of-the-box administrative ``sqream`` role, which will always use the conventional SQreamDB authentication instead LDAP authentication.

.. contents::
   :local:
   :depth: 1

Before You Begin
================

* If SQreamDB is being installed within an environment where LDAP is already configured, it is best practice to ensure that the newly created SQreamDB role names are consistent with existing LDAP user names.

* When setting up LDAP for an existing SQreamDB installation, it's recommended to ensure that newly created LDAP usernames match existing SQreamDB role names. If SQreamDB roles were not configured in LDAP or have different names, they'll be recreated in SQreamDB as roles without login capabilities, permissions, or default schemas.

Setting LDAP Authentication Management
======================================

To set LDAP authentication for SQreamDB, choose one of the following configuration methods:

.. contents::
   :local:
   :depth: 1

Basic Method
------------

A traditional approach to authentication in which the user provides a username and password combination to authenticate with the LDAP server. In this approach, all users are given access to SQream.

Flags
^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag
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
^^^^^^^^^^^^^^^^^^^^^^^^^^

Only roles with admin privileges or higher may enable LDAP Authentication. 

1. Set the ``authenticationMethod`` flag:

   .. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';
	
2. Set the ``ldapIpAddress`` flag: 

   .. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = '<ldaps://...>';
	
3. Set the ``ldapPrefix`` flag:

   .. code-block:: postgres

	ALTER SYSTEM SET ldapPrefix = '<DN_binding_string_prefix>=';
	
4. Set the ``ldapSuffix`` flag:

   .. code-block:: postgres

	ALTER SYSTEM SET ldapSuffix  = '<DN_binding_string_suffix>';

5.  To set the ``ldapPort`` flag (optional), run:

    .. code-block:: postgres

	ALTER SYSTEM SET ldapPort = <port_number>
	
6. To set the ``ldapConnTimeoutSec`` flag (optional), run:

   .. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = <15>;

7. Restart all sqreamd servers. 

Example
^^^^^^^

After completing the setup above, we can bind to a user by a distinguished name. For example, if the DN of the user is:

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

This method lets users be grouped into categories. Each category can then be given or denied access to SQreamDB, giving administrators control over access.

Flags
^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag
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
   * - ``ldapSearchAttribute``
     - Attribute to match against the user name in the search when doing search + bind authentication. If no attribute is specified, ``the uid`` attribute will be used
   * - ``ldapSearchFilter``
     - Filters ``ldapAdvancedMode`` authentication. ``ALTER SYSTEM SET ldapSearchFilter = '(<attribute>=<value>)(<attribute2>=<value2>)(…)';``
   * - ``ldapGetAttributeList``
     - Enables you to include LDAP user attributes, as they appear in LDAP, in your SQreamDB metadata. After having set this flag, you may execute the :ref:`ldap_get_attr` utility function which will show you the attribute values associated with each SQreamDB role.


Preparing LDAP Users
^^^^^^^^^^^^^^^^^^^^

If installing SQreamDB in an environment with LDAP already set up, it's best to ensure the new SQreamDB role names match the existing LDAP user names.

It is also recommended to:

* Group Active Directory users so that they may be filtered during setup, using the ``ldapSearchFilter`` flag.

* Provide a unique attribute to each user name, such as an employee ID, to be easily searched for when using the ``ldapSearchAttribute`` flag.

Preparing SQreamDB Roles
^^^^^^^^^^^^^^^^^^^^^^^^

For a SQreamDB admin to be able to manage role permissions, for every Active Directory user connecting to SQreamDB, there must be an existing SQreamDb role name that is consistent with existing LDAP user names.

You may either :ref:`rename SQream roles<rename_role>` or create new roles, such as in the following example: 

1. Create a new role:
	
   .. code-block:: postgres	
	
	CREATE ROLE role12345;

2. Grant the new role login permission:

   .. code-block:: postgres

	GRANT LOGIN TO role12345;

3. Grant the new role ``CONNECT`` permission:

   .. code-block:: postgres

	GRANT CONNECT ON DATABASE master TO role12345;

Advanced Method Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only roles with admin privileges and higher may enable LDAP Authentication. 

1. Set your LDAP password 

Configure an LDAP admin password (a kind of out-of-the-box LDAP admin user, no REVOKE or GRANT, etc'..) :

   .. code-block:: postgres
   
	GRANT PASSWORD <'binding_user_password'> TO ldap_bind_dn_admin_password;
	
  This password is your LDAP server password.
  
  This password is encrypted in your SQreamDB metadata. 

2. Set the ``authenticationMethod`` flag:

   .. code-block:: postgres

	ALTER SYSTEM SET authenticationMethod = 'ldap';

3. Set the ``ldapAdvancedMode`` flag:

   .. code-block:: postgres
	
	ALTER SYSTEM SET ldapAdvancedMode = true;

4. Set the ``ldapIpAddress`` flag: 

   .. code-block:: postgres

	ALTER SYSTEM SET ldapIpAddress = '<ldaps://<IpAddress>';

5. Set the ``ldapBindDn`` flag: 

   .. code-block:: postgres

	ALTER SYSTEM SET ldapBindDn = <binding_user_DN>;
	
6. Set the ``ldapBaseDn`` flag: 

   .. code-block:: postgres	

	ALTER SYSTEM SET ldapBaseDn = '<search_root_DN>';
	
7. Set the ``ldapSearchAttribute`` flag: 

   .. code-block:: postgres	

	ALTER SYSTEM SET ldapSearchAttribute = '<search_attribute>';
	
8. To set the ``ldapSearchFilter`` flag (optional), run: 

   .. code-block:: postgres	

	ALTER SYSTEM SET ldapSearchFilter = '(<attribute>=<value>)(<attribute2>=<value2>)[...]';

9. To set the ``ldapPort`` flag (optional), run:

   .. code-block:: postgres

	ALTER SYSTEM SET ldapPort = <port_number>
	
10. To set the ``ldapConnTimeoutSec`` flag (optional), run:

   .. code-block:: postgres

	ALTER SYSTEM SET ldapConnTimeoutSec = <15>;
	
11. To set the ``ldapGetAttributeList`` flag (optional), run:

   .. code-block:: postgres

	ALTER SYSTEM SET ldapGetAttributeList = <'ldap_attribute1'>,<'ldap_attribute2'>,<'ldap_attribute3'>,[,...];
	
   a. To see the LDAP user attributes associated with SQreamDB roles in your metadata, execute the :ref:`ldap_get_attr` utility function.

12. Restart all sqreamd servers. 

Example
^^^^^^^

After completing the setup above we can try to bind to a user by locating it by one of its unique attributes. 

User DN = 

.. code-block:: postgres

	CN=ElonMusk,OU=Sqream Users,DC=sqream,DC=loc

User has value of elonm for attribute ``sAMAccountName``.


.. code-block:: postgres

	GRANT PASSWORD 'LdapPassword12#4%' TO ldap_bind_dn_admin_password;

	ALTER SYSTEM SET authenticationMethod = 'ldap';
	
	ALTER SYSTEM SET ldapAdvancedMode = true;

	ALTER SYSTEM SET ldapIpAddress = 'ldaps://192.168.10.20';
	
	ALTER SYSTEM SET ldapPort = 5000

	ALTER SYSTEM SET ldapBindDn = 'CN=LDAP admin,OU=network admin,DC=sqream,DC=loc';

	ALTER SYSTEM SET ldapBaseDn = 'OU=Sqream Users,DC=sqream,DC=loc';
	
	ALTER SYSTEM SET ldapSearchAttribute = 'sAMAccountName';
	
	ALTER SYSTEM SET ldapConnTimeoutSec = 30;
	
	ALTER SYSTEM SET ldapSearchFilter =  "(memberOf=CN=SqreamGroup,CN=Builtin,DC=sqream,DC=loc)(memberOf=CN=Admins,CN=Builtin,DC=sqream,DC=loc)";
	
	
Logging in will be possible using the username elonm using sqream client  

.. code-block:: postgres

	./sqream sql --username=elonm --password=<elonm_password> --databasename=master --port=5000
	

Disabling LDAP Authentication
=============================

To disable LDAP authentication and configure sqream authentication: 

1. Execute the following syntax:

   .. code-block:: postgres	

	ALTER SYSTEM SET authenticationMethod = 'sqream';

2. Restart all sqreamd servers.  
