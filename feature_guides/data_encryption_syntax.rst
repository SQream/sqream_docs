.. _data_encryption_syntax:

***********************
Syntax
***********************

The **Syntax** page describes the following:

.. contents::
   :local:
   :depth: 1

The following is the correct syntax for **encrypting** a new table:

.. code-block:: console
     
   CREATE TABLE client_name  (
        first_name TEXT(128),
        last_name TEXT(128),
        salary INT(6) ENCRYPT);
		
The following is an example of encrypting a new table:

.. code-block:: console
     
   EXAMPLE
  
The following is the correct syntax for **decrypting** a new table:

.. code-block:: console

   SELECT * FROM TABLE;

The following is an example of decrypting a new table:

.. code-block:: console
     
   EXAMPLE
   
Usage notes - this should be included on this page.

When inputting the wrong master key/location in encryption/decryption an error should be raised to the user

The master key needs to be masked in logs to protect user privacy, the responsibility maintaining the master key for the remote repository is on the user side