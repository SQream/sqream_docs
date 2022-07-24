.. _access_control_overview:

**************
Overview
**************
Access control provides authentication and authorization in SQream DB. SQream DB manages authentication and authorization using a role-based access control system (RBAC), like ANSI SQL and other SQL products.

SQream DB has a default permissions system which is inspired by Postgres, but with more power. In most cases, this allows an administrator to set things up so that every object gets permissions set automatically. In SQream DB, users log in from any worker which verifies their roles and permissions from the metadata server. Each statement issues commands as the currently logged in role. 

Roles are defined at the cluster level, meaning they are valid for all databases in the cluster. To bootstrap SQream DB, a new install will always have one ``SUPERUSER`` role, typically named ``sqream``. To create more roles, you should first connect as this role.

The following:

* **Role** - a role can be a user, a group, or both. Roles can own database objects (e.g. tables), and can assign permissions on those objects to other roles. Roles can be members of other roles, meaning a user role can inherit permissions from its parent role.

   ::

* **Authentication** - verifying the identity of the role. User roles have usernames (:term:`role names<role>`) and passwords.

   ::

* **Authorization** - checking the role has permissions to do a particular thing. The :ref:`grant` command is used for this.
