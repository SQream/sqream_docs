.. _security:

************************
Security Best Practices 
************************

Change the default ``SUPERUSER``
--------------------------------

BLUE comes with an out-of-the-box ``SUPERUSER`` role, typically named ``sqream``. 
After creating a second ``SUPERUSER`` role, remove or change the default credentials to the default ``sqream`` user.

No database user should ever use the default ``SUPERUSER`` role in a production environment.

Create distinct user roles
--------------------------

Each user that signs in to a BLUE cluster should have a distinct user role for several reasons:

* For logging and auditing purposes. Each user that logs in to BLUE can be identified.

* For limiting permissions. Use groups and permissions to manage access. See our :ref:`access_control` guide for more information.

Limit ``SUPERUSER`` access
--------------------------

Limit users who have the ``SUPERUSER`` role.

A superuser role bypasses all permissions checks. Only system administrators should have ``SUPERUSER`` roles. See our :ref:`access_control` guide for more information.

Use TLS/SSL when possible
-------------------------

BLUE's protocol implements client/server TLS security (even though it is called SSL).

All BLUE connectors and drivers support transport encryption. Ensure that each connection uses SSL and the correct access port for the BLUE cluster:

* The load balancer (``server_picker``) is often started with the secure port at an offset of 1 from the original port (e.g. port 3108 for the unsecured connection and port 3109 for the secured connection).

* A BLUE worker is often started with the secure port enabled at an offset of 100 from the original port (e.g. port 5000 for the unsecured connection and port 5100 for the secured connection).

Refer to each :ref:`client driver<client_drivers>` for instructions on enabling TLS/SSL.



