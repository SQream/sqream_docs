.. _access_control_password_policy:

**************
Password Policy
**************
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

You can create a password through the Studio graphic interface or through the CLI, as in the following example command:

.. code-block:: console

   CREATE ROLE user_a ;
   GRANT LOGIN to user_a ;
   GRANT PASSWORD 'BBAu47?fqPL' to user_a ;

Creating a password that does not comply with the above requirements generates an error message with a request to modify it.

Unsuccessfully attempting to log in three times displays the following message:

.. code-block:: console

   The user is locked. please contact your system administrator to reset the password and regain access functionality.

For more information, see :ref:`login_max_retries`.
