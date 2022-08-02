.. _data_encryption_syntax:

***********************
Syntax
***********************
The following is the syntax for encrypting a new table:

.. code-block:: console
     
   CREATE TABLE <table name>  (
        <column_name> NOT NULL ENCRYPT,
        <column_name> <type_name> ENCRYPT,
        <column_name> <type_name>,
        <column_name> <type_name> ENCRYPT);
		
The following is an example of encrypting a new table:

.. code-block:: console
     
   CREATE TABLE client_name  (
        id BIGINT NOT NULL ENCRYPT,
        first_name TEXT ENCRYPT,
        last_name TEXT,
        salary INT ENCRYPT);
		   
.. note::  Users without permissions cannot view the entire table as long as at least one column is encrypted. The (unique) encryption/decryption key is relevant only at the system level and is not held by users.