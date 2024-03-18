.. _security:

************************
Security Best Practices 
************************

Administrative Roles
====================

``SUPERUSER``
-------------

BLUE comes with an out-of-the-box ``SUPERUSER`` role, typically named ``sqream``. 
After creating a second ``SUPERUSER`` role, remove or change the default credentials to the default ``sqream`` user.

No database user should ever use the default ``SUPERUSER`` role in a production environment.

``CLUSTERADMIN``
----------------

Since there's no out-of-the-box ``CLUSTERADMIN``, it is advisable that during the initial deployment of BLUE, you assign ``CLUSTERADMIN`` permissions to at least one role. With that said, it is best practice to restrict ``CLUSTERADMIN`` permissions to a specific set of roles.

Create Distinct User Roles
==========================

Each user that signs in to a BLUE cluster should have a distinct user role for several reasons:

* For logging and auditing purposes. Each user that logs in to BLUE can be identified.

* For limiting permissions. Use groups and permissions to manage access.

Limit ``SUPERUSER`` Access
==========================

Limit users who have the ``SUPERUSER`` role.

A superuser role bypasses all permission checks. Only system administrators should have ``SUPERUSER`` roles. See our

----------------------------------------

Learn more about :ref:`roles and permissions<access_control>`



