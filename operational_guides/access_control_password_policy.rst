.. _access_control_password_policy:

**************
Password Policy
**************
The **Password Policy** describes the following:

.. contents:: 
   :local:
   :depth: 1

Password Strength Requirements
==============================
As part of our compliance with GDPR standards SQream relies on a strong password policy when accessing the CLI or Studio, with the following requirements:

* At least eight characters long.

   ::

* Mandatory upper and lowercase letters.

   ::

* At least one numeric character.

   ::

* May not include a username.

   ::

* Must include at least one special character, such as **?**, **!**, **$**, etc.

You can create a password by using the Studio graphic interface or using the CLI, as in the following example command:

.. code-block:: console

   CREATE ROLE user_a ;
   GRANT LOGIN to user_a ;
   GRANT PASSWORD 'BBAu47?fqPL' to user_a ;

Creating a password which does not comply with the password policy generates an error message with a request to include any of the missing above requirements:

.. code-block:: console

   The password you attempted to create does not comply with SQream's security requirements.

   Your password must:

   * Be at least eight characters long.

   * Contain upper and lowercase letters.

   * Contain at least one numeric character.

   * Not include a username.

   * Include at least one special character, such as **?**, **!**, **$**, etc.

Brute Force Prevention
==============================
Unsuccessfully attempting to log in five times displays the following message:

.. code-block:: console

   The user is locked. Please contact your system administrator to reset the password and regain access functionality.

You must have superuser permissions to release a locked user to grant a new password:

.. code-block:: console

   GRANT PASSWORD '<password>' to <blocked_user>;

For more information, see :ref:`login_max_retries`.

.. warning:: Because superusers can also be blocked, **you must have** at least two superusers per cluster.