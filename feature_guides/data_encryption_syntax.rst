.. _data_encryption_syntax:

***********************
Syntax
***********************
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
		   
.. note::  Users without permissions cannot view the entire table as long as at least one column is encrypted. The decryption key is relevant only at the system level and is not held by users.