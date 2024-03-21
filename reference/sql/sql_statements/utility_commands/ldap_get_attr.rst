.. _ldap_get_attr:

*************
LDAP GET ATTR
*************

The ``ldap_get_attr()`` utility function may be used only after having set :ref:`ldap` as your authentication service. This function enables you to specify LDAP attributes you want your SQreamDB role catalog table to include when executing ``SELECT`` on the ``sqream_catalog.roles`` metadata object.

Syntax
==========

.. code-block:: postgres

   SELECT ldap_get_attr()

Example
=======

Assume the following LDAP attributes are set to be associated with SQreamDB roles:

* distinguishedName
* primaryGroupID
* userprincipalname 

.. code-block:: psql

   SELECT ldap_get_attr();

Output

.. code-block:: console

   role_name         | distinguishedName                         | primaryGroupID| userprincipalname    
   ------------------+-------------------------------------------+---------------+---------------------
   public            |                                           |               | 
   sqream            | CN=sqream,OU=Sqream Users,DC=sqream,DC=loc| 513           | sqream@sqream.loc
   test_user         | CN=test_user,OU=test,DC=sqream,DC=loc     | 513           | test_user@sqream.loc

Permissions
===========

Using the ``ldap_get_attr`` command requires no special permissions.