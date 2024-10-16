.. _data_encryption_syntax:

***********************
Syntax
***********************
The following is the syntax for encrypting a new table:

.. code-block:: psql
     
   CREATE TABLE <table name>  (
        <column_name> NOT NULL ENCRYPT,
        <column_name> <type_name> ENCRYPT,
        <column_name> <type_name>,
        <column_name> <type_name> ENCRYPT);
		
The following is an example of encrypting a new table:

.. code-block:: psql
     
   CREATE TABLE client_name  (
        id BIGINT NOT NULL ENCRYPT,
        first_name TEXT ENCRYPT,
        last_name TEXT,
        salary INT ENCRYPT);
		   
.. note:: xxxxxxxxxxxx.



***********************
Permissions
***********************
Because the Data Encryption feature does not require a role, users with **Read** and **Insert** permissions can read tables containing encrypted data.