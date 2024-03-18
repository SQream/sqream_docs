.. _security:

************************
Security Best Practices 
************************

Change the default ``SUPERUSER``
--------------------------------

BLUE comes with an out-of-the-box ``SUPERUSER`` role, typically named ``sqream``. 
After creating a second ``SUPERUSER`` role, remove or change the default credentials to the default ``sqream`` user.

No database user should ever use the default ``SUPERUSER`` role in a production environment.

Creating a ``CLUSTERADMIN``
---------------------------

Since there's no out-of-the-box ``CLUSTERADMIN``, it is recommended that upon deployment you grant ``CLUSTERADMIN`` permissions to at least one role. With that said, it is best practice to limit ``CLUSTERADMIN`` permissions to a selected number of roles.  

Create distinct user roles
--------------------------

Each user that signs in to a BLUE cluster should have a distinct user role for several reasons:

* For logging and auditing purposes. Each user that logs in to BLUE can be identified.

* For limiting permissions. Use groups and permissions to manage access. See our :ref:`access_control` guide for more information.

Limit ``SUPERUSER`` access
--------------------------

Limit users who have the ``SUPERUSER`` role.

A superuser role bypasses all permission checks. Only system administrators should have ``SUPERUSER`` roles. See our :ref:`access_control` guide for more information.





