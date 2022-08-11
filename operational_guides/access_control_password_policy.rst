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

You can grant a password through the Studio graphic interface or through the CLI, as in the following example command:

.. code-block:: console

   CREATE ROLE user_a ;
   GRANT LOGIN to user_a ;
   GRANT PASSWORD 'BBAu47?fqPL' to user_a ;

Granting a password that does not comply with the above requirements generates an error message with a request to modify it;

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
Unsuccessfully attempting to log in three times displays the following message:

.. code-block:: console

   The user is locked. please contact your system administrator to reset the password and regain access functionality.

For more information, see :ref:`login_max_retries`.