.. _access_control_overview:

**************
Overview
**************
Access control refers to SQream's authentication and authorization operations, managed using a **Role-Based Access Control (RBAC)** system, such as ANSI SQL or other SQL products. SQream's default permissions system is similar to Postgres, but is more powerful. SQream's method lets administrators prepare the system to automatically provide objects with their required permissions.

SQream users can log in from any worker, which verify their roles and permissions from the metadata server. Each statement issues commands as the role that you're currently logged into. Roles are defined at the cluster level, and are valid for all databases in the cluster. To bootstrap SQream, new installations require one ``SUPERUSER`` role, typically named ``sqream``. You can only create new roles by connecting as this role.

Access control refers to the following basic concepts:

 * **Role** - A role can be a user, a group, or both. Roles can own database objects (such as tables) and can assign permissions on those objects to other roles. Roles can be members of other roles, meaning a user role can inherit permissions from its parent role.

    ::
   
 * **Authentication** - Verifies the identity of the role. User roles have usernames (or **role names**) and passwords.

    ::
 
 * **Authorization** - Checks that a role has permissions to perform a particular operation, such as the :ref:`grant` command.