.. _data_encryption_syntax:

***********************
Syntax
***********************
The **Syntax** page describes the syntax for the following:

.. contents::
   :local:
   :depth: 1
   
Encrypting a New Table
----------------
The following is the correct syntax for encrypting a new table:

.. code-block:: console
     
   CREATE TABLE <name of table>  (
        <column_name> <data type> <(maximum string length)>,
        <column_name> <data type>
	last_name <data type> <(maximum string length)>,
        salary <data type>(<(maximum string length)>) ENCRYPT);
		
The following is an example of encrypting a new table:

.. code-block:: console
     
   CREATE TABLE client_name  (
        first_name TEXT(128),
        last_name TEXT(128),
        salary INT(6) ENCRYPT);
		   
.. note::  Encrypting a column in a table prevents users from viewing the entire table without a decryption key.
   
Decrypting a Table
----------------  
The following is the correct syntax for decrypting a table:

.. code-block:: console

   SELECT * FROM <name of encrypted table>;

The following is an example of decrypting a table:

.. code-block:: console
     
   SELECT * FROM TABLE;