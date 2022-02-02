.. _security:

*************************
Security
*************************

SQream DB has some security features that you should be aware of to increase the security of your data.

.. contents:: In this topic:
   :local:


Overview
============

An **initial, unsecured** installation of SQream DB can carry some risks:

* Your data open to any client that can access an open node through an IP and port combination.
* The initial administrator username and password, when unchanged, can let anyone log in.
* Network connections to SQream DB aren't encrypted.

To avoid these security risks, SQream DB provides authentication, authorizaiton, logging, and network encryption. 

Read through the best practices guide to understand more.

Security best practices for SQream DB
==============================================

Secure OS access
-------------------------

SQream DB often runs as a dedicated user on the host OS. This user is the file system owner of SQream DB data files. 

Any user who logs in to the OS with this user can read or delete data from outside of SQream DB.

This user can also read any logs which may contain user login attempts. 

Therefore, it is very important to secure the host OS and prevent unauthorized access.

System administrators should only log in to the host OS to perform maintenance tasks like upgrades. A database user should not log in using the same username in production environments.

Change the default ``SUPERUSER``
-----------------------------------

To bootstrap SQream DB, a new install will always have one ``SUPERUSER`` role, typically named ``sqream``. 
After creating a second ``SUPERUSER`` role, remove or change the default credentials to the default ``sqream`` user.

No database user should ever use the default ``SUPERUSER`` role in a production environment.

If you don't change the user role itself, change the password of the default ``SUPERUSER``. See the :ref:`change password<change_password>` section of our :ref:`access control<access_control>` guide.

Create distinct user roles
--------------------------------

Each user that signs in to a SQream DB cluster should have a distinct user role for several reasons:

* For logging and auditing purposes. Each user that logs in to SQream DB can be identified.

* For limiting permissions. Use groups and permissions to manage access. See our :ref:`access_control` guide for more information.

Limit ``SUPERUSER`` access
-------------------------------

Limit users who have the ``SUPERUSER`` role.

A superuser role bypasses all permissions checks. Only system administrators should have ``SUPERUSER`` roles. See our :ref:`access_control` guide for more information.

Password strength guidelines
--------------------------------

System administrators should verify the passwords used are strong ones.

SQream DB stores passwords as salted SHA1 hashes in the system catalog so they are obscured and can't be recovered. However, passwords may appear in server logs. Prevent access to server logs by securing OS access as described above.

Follow these recommendations to strengthen passwords:

* Pick a password that's easy to remember
* At least 8 characters
* Mix upper and lower case letters
* Mix letters and numbers
* Include non-alphanumeric characters (except ``"`` and ``'``)






Use TLS/SSL when possible
----------------------------

SQream DB's protocol implements client/server TLS security (even though it is called SSL).

All SQream DB connectors and drivers support transport encryption. Ensure that each connection uses SSL and the correct access port for the SQream DB cluster:

* The load balancer (``server_picker``) is often started with the secure port at an offset of 1 from the original port (e.g. port 3108 for the unsecured connection and port 3109 for the secured connection).

* A SQream DB worker is often started with the secure port enabled at an offset of 100 from the original port (e.g. port 5000 for the unsecured connection and port 5100 for the secured connection).

Refer to each :ref:`client driver<client_drivers>` for instructions on enabling TLS/SSL.



