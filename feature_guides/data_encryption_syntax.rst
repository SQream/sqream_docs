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
		   
.. note:: Because encryption is not associated with any role, users with **Read** or **Insert** permissions can read tables containing encrypted data.

.. warning:: Your performance degradation increases in correlation with the amount of added columns.

You cannot encrypt more than three columns. Attempting to encrypt more than three columns displays the following error message:

.. code-block:: console

   Error preparing statement: Cannot create a table with more than three encrypted columns.