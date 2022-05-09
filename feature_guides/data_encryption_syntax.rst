.. _data_encryption_syntax:

***********************
Syntax
***********************
The **Syntax** page describes the following:

.. contents::
   :local:
   :depth: 1
   
Encrypting a New Table
----------------
The following is the correct syntax for **encrypting** a new table:

.. code-block:: console
     
   CREATE TABLE client_name  (
        first_name TEXT(128),
        last_name TEXT(128),
        salary INT(6) ENCRYPT);
		
The following is an example of encrypting a new table:

.. code-block:: console
     
   EXAMPLE
   
**Comment** - *Please provide an actual example.*
   
Decrypting a New Table
----------------  
The following is the correct syntax for **decrypting** a table:

.. code-block:: console

   SELECT * FROM TABLE;

The following is an example of decrypting a table:

.. code-block:: console
     
   EXAMPLE
   
**Comment** - *Please provide an actual example.*

Incorrectly Encrypting or Decrypting Your Data
----------------   
Using the incorrect master key or location while encrypting or decrypting generates an error.

**Comment** - *Can I get an example of this error to include in the doc?*

**Comment** - *I thought that the master key was completely hidden from users... The internal doc says, "Master Key-  the key will be generated within the server side, it will reside within a repository which will be hidden from the user."*
   
In logs, master keys are masked to protect user privacy. Users are responsible for maintaining their master keys for the remote repository.

**Comment** - *I'm not sure I fully understand the part about maintaing the master keys on the remote repository.*