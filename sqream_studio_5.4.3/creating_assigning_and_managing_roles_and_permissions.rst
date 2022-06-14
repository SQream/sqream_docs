.. _roles_5.4.3:

****************************
Creating, Assigning, and Managing Roles and Permissions
****************************
The **Creating, Assigning, and Managing Roles and Permissions** describes the following:

.. contents:: 
   :local:
   :depth: 1   
   
Overview
---------------
In the **Roles** area you can create and assign roles and manage user permissions. 

The **Type** column displays one of the following assigned role types:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Role Type
     - Description
   * - Groups
     - Roles with no users.
   * - Enabled users
     - Users with log-in permissions and a password.
   * - Disabled users
     - Users with log-in permissions and with a disabled password. An admin may disable a user's password permissions to temporary disable access to the system.

.. note:: If you disable a password, when you enable it you have to create a new one.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.3>`


Viewing Information About a Role
--------------------
Clicking a role in the roles table displays the following information:

 * **Parent Roles** - displays the parent roles of the selected role. Roles inherit all roles assigned to the parent.
 
    ::
   
 * **Members** - displays all members that the role has been assigned to. The arrow indicates the roles that the role has inherited. Hovering over a member displays the roles that the role is inherited from.

    ::
   
 * **Permissions** - displays the role's permissions. The arrow indicates the permissions that the role has inherited. Hovering over a permission displays the roles that the permission is inherited from.
 
:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.3>`


Creating a New Role
--------------------
You can create a new role by clicking **New Role**.
   
An admin creates a **user** by granting login permissions and a password to a role. Each role is defined by a set of permissions. An admin can also group several roles together to form a **group** to manage them simultaneously. For example, permissions can be granted to or revoked on a group level.

Clicking **New Role** lets you do the following:

 * Add and assign a role name (required)
 * Enable or disable log-in permissions for the role.
 * Set a password.
 * Assign or delete parent roles.
 * Add or delete permissions.
 * Grant the selected user with superuser permissions.
 
From the New Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field. From the New Role panel you can also search and scroll through the permissions. In the **Search** field you can use the **and** operator to search for strings that fulfill multiple criteria.

When adding a new role, you must select the **Enable login for this role** and **Has password** check boxes.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.3>`

Editing a Role
--------------------
Once you've created a role, clicking the **Edit Role** button lets you do the following:

 * Edit the role name.
 * Enable or disable log-in permissions.
 * Set a password.
 * Assign or delete parent roles.
 * Assign a role **administrator** permissions.
 * Add or delete permissions.
 * Grant the selected user with superuser permissions.

From the Edit Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field. From the Edit Role panel you can also search and scroll through the permissions. In the **Search** field you can use the **and** operator to search for strings that fulfill multiple criteria.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.3>`

Deleting a Role
-----------------
Clicking the **delete** icon displays a confirmation message with the amount of users and groups that will be impacted by deleting the role.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.3>`