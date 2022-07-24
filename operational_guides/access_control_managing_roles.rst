.. _access_control_managing_roles:

**************
Managing Roles
**************
Roles are used for both users and groups. Roles are global across all databases in the SQream DB cluster. To use a ``ROLE`` as a user, it should have a password, the login permission, and connect permissions to the relevant databases.

The Roles section describes the following role-related operations: 

.. contents:: 
   :local:
   :depth: 1

Creating New Roles (Users)
------------------------------
A user role can log in to the database, so it should have ``LOGIN`` permissions, as well as a password.

For example:

.. code-block:: postgres
                
   CREATE ROLE role_name ;
   GRANT LOGIN to role_name ;
   GRANT PASSWORD 'new_password' to role_name ;
   GRANT CONNECT ON DATABASE database_name to role_name ;

Examples:

.. code-block:: postgres

   CREATE  ROLE  new_role_name  ;  
   GRANT  LOGIN  TO  new_role_name;  
   GRANT  PASSWORD  'my_password'  TO  new_role_name;  
   GRANT  CONNECT  ON  DATABASE  master  TO  new_role_name;

A database role may have a number of permissions that define what tasks it can perform. These are assigned using the :ref:`grant` command.

Dropping Users
---------------

.. code-block:: postgres

   DROP ROLE role_name ;

Examples:

.. code-block:: postgres

   DROP ROLE  admin_role ;

Altering a User Name
------------------------

Renaming a user's role:

.. code-block:: postgres

   ALTER ROLE role_name RENAME TO new_role_name ;

Examples:

.. code-block:: postgres

   ALTER ROLE  admin_role  RENAME  TO  copy_role ;

.. _change_password:

Changing User Passwords
--------------------------

To change a user role's password, grant the user a new password.

.. code-block:: postgres

   GRANT  PASSWORD  'new_password'  TO  rhendricks;  

.. note:: Granting a new password overrides any previous password. Changing the password while the role has an active running statement does not affect that statement, but will affect subsequent statements.

Altering Public Role Permissions
-----------

There is a public role which always exists. Each role is granted to the ``PUBLIC`` role (i.e. is a member of the public group), and this cannot be revoked. You can alter the permissions granted to the public role.

The ``PUBLIC`` role has ``USAGE`` and ``CREATE`` permissions on ``PUBLIC`` schema by default, therefore, new users can create, :ref:`insert`, :ref:`delete`, and :ref:`select` from objects in the ``PUBLIC`` schema.


Altering Role Membership (Groups)
-------------------------

Many database administrators find it useful to group user roles together. By grouping users, permissions can be granted to, or revoked from a group with one command. In SQream DB, this is done by creating a group role, granting permissions to it, and then assigning users to that group role.

To use a role purely as a group, omit granting it ``LOGIN`` and ``PASSWORD`` permissions.

The ``CONNECT`` permission can be given directly to user roles, and/or to the groups they are part of.

.. code-block:: postgres

   CREATE ROLE my_group;

Once the group role exists, you can add user roles (members) using the ``GRANT`` command. For example:

.. code-block:: postgres

   -- Add my_user to this group
   GRANT my_group TO my_user;


To manage object permissions like databases and tables, you would then grant permissions to the group-level role (see :ref:`the permissions table<permissions_table>` below.

All member roles then inherit the permissions from the group. For example:

.. code-block:: postgres

   -- Grant all group users connect permissions
   GRANT  CONNECT  ON  DATABASE  a_database  TO  my_group;
   
   -- Grant all permissions on tables in public schema
   GRANT  ALL  ON  all  tables  IN  schema  public  TO  my_group;

Removing users and permissions can be done with the ``REVOKE`` command:

.. code-block:: postgres

   -- remove my_other_user from this group
   REVOKE my_group FROM my_other_user;
