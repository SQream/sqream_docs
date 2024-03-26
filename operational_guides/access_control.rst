.. _access_control:

**************
Access Control
**************

Access control refers to BLUE's authentication and authorization operations, managed using a **Role-Based Access Control (RBAC)** system, such as ANSI SQL or other SQL products. BLUE's method lets administrators prepare the system to automatically provide objects with their required permissions.

BLUE users can log in from any worker, which verify their roles and permissions from the metadata server. Each statement issues commands as the role that you're currently logged into. Roles are defined at the cluster level, and are valid for all databases in the cluster. 

Basic Concepts:

* **Role** - A role can be a user, a group, or both. Roles can own database objects (such as tables) and can assign permissions on those objects to other roles. Roles can be members of other roles, meaning a user role can inherit permissions from its parent role.
   
* **Authentication** - Verifies the identity of the role. User roles have usernames (or **role names**) and are granted ``LOGIN`` permission.
 
* **Authorization** - Checks that a role has permissions to perform a particular operation, such as the :ref:`grant` command.

Administrative Roles
====================

In BLUE, there are two types of administrative roles: a pre-defined ``SUPERUSER`` and a custom-configured ``CLUSTERADMIN``.

``SUPERUSER``
-------------

The ``SUPERUSER`` role is granted cluster-level permissions and is responsible for overseeing all query engine operations behind the scenes.

``CLUSTERADMIN``
----------------

The ``CLUSTERADMIN`` role has comprehensive access to BLUE application settings and is responsible for managing the BLUE cluster.



.. toctree::
   :maxdepth: 1
   :titlesonly:

More Under Access Control
-------------------------

:ref:`access_control_managing_roles`

:ref:`access_control_permissions`

:ref:`access_control_departmental_example`