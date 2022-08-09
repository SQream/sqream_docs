.. _access_control_password_policy:

**************
Password Security Compliance (New!)
**************

.. |icon-new_gray_2022.1.1| image:: /_static/images/new_gray_2022.1.1.png
   :align: middle
   :width: 110
      
As part of our compliance with GDPR standards SQream relies on a strong password policy when accessing the CLI or Studio.

The following requirements apply when creating a password:

* At least eight characters long.

   ::

* At least one numeric character.

   ::

* Should not include a username.

   ::

* Must include at least one special character, such as **?**, **!**, **$**, etc.

   ::

* Mandatory upper and lowercase letters.

The following is the syntax for creating a password:

.. code-block:: console

   CREATE ROLE <name of role> ;
   GRANT LOGIN <permisson type> ;
   GRANT PASSWORD <'password'> to <name of user> ;

The following is an example of creating a password:

.. code-block:: console

   CREATE ROLE user_a ;
   GRANT LOGIN to user_a ;
   GRANT PASSWORD 'BBAu47?fqPL' to user_a ;

Creating a password that does not comply with the above requirements generates the following error message:

.. code-block:: console

   The password you attempt to create does not comply with SQream security requirements. Please follow the requirements below:

   * At least 8 characters long.

   * Must include both upper and lower case letters.

   * Must include at least one numeric character.

   * Must not include your username.

   * Must include at least one “special” character (?, !, $, etc.).
   
.. note:: When a new user is created in Studio, a message is displayed to help you determine what the constraints are. 

Unsuccessfully attempting to log in three times displays the following message:

.. code-block:: console

   The user is locked. please contact your system administrator to reset the password and regain access functionality.

For more information, see :ref:`login_max_retries`.