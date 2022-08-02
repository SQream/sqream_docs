.. _access_control_password_policy:

**************
Password Policy (New!)
**************

.. |icon-new_gray_2022.1.1| image:: /_static/images/new_gray_2022.1.1.png
   :align: middle
   :width: 110
      
As part of our compliance with GDPR standards |icon-new_gray_2022.1.1| SQream relies on a strong password policy when accessing the CLI or Studio, with the following requirements:

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

Creating a password that does not comply with the above requirements generates the following error message:

.. code-block:: console

   The password you attempt to create does not comply with SQream security requirements. Please follow the requirements below:

   * At least 8 characters long.

   * Must include both upper and lower case letters.

   * Must include at least one numeric character.

   * Must not include your username.

   * Must include at least one “special” character (?, !, $, etc.).
   
.. note:: When a new user created in Studio, a message is displayed to help you determine what the constraints are. 

Unsuccessfully attempting to log in three times displays the following message:

.. code-block:: console

   The user is locked. please contact your system administrator to reset the password and regain access functionality.

For more information, see :ref:`login_max_retries`.