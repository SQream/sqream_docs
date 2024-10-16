.. _data_encryption_syntax:

***********************
Syntax
***********************
Encrypting columns in a new table

.. code-block:: psql
     
   CREATE TABLE <table name>  (
        <column_name> <data_type> ENCRYPT,
        <column_name> <data_type> NULL ENCRYPT,
		<column_name> <data_type> NOT NULL ENCRYPT
		);

Adding an encrypted column to an existing table

.. code-block:: psql

	ALTER TABLE <table_name> ADD COLUMN <column_name> <data_type> ENCRYPT;
		
		
Encryption methods

.. code-block:: psql

	ENCRYPT ( <column name to encrypt> , <Secret Key of exactly 256-bit (32-byte) length> )


Decryption method

.. code-block:: psql

	DECRYPT ( <column name to decrypt> , <Secret Key of exactly 256-bit (32-byte) length> )

***********************
Examples
***********************

Encrypting a new table

.. code-block:: psql
     
   CREATE TABLE client_name  (
        id BIGINT NOT NULL ENCRYPT,
        first_name TEXT ENCRYPT,
        last_name TEXT,
        salary INT ENCRYPT);

Inserting encrypt player salary (``INT`` data type)

.. code-block:: psql

	INSERT INTO NBA (player_name, team_name, jersey_number, position, age, height, weight, college, salary)
	VALUES ('Jayson Christopher Tatum', 'Boston Celtics', 0, 'SF', 25, '6-8', 210 , 'Duke', ENCRYPT ( 32600060 , '6a8431f6e9c2777ee356c0b8aa3c12c0c63bdf366ac3342c4c9184b51697b47f');

Similar example using ``COPY FROM''

.. code-block:: psql

	COPY NBA
	(
	player_name, team_name, jersey_number, position, age, height, weight, college, 
	ENCRYPT (salary, '6a8431f6e9c2777ee356c0b8aa3c12c0c63bdf366ac3342c4c9184b51697b47f')
	)
	FROM WRAPPER csv_fdw 
	OPTIONS
	(location = '/tmp/source_file.csv', quote='@');

Query the encrypted data

.. code-block:: psql

	SELECT player_name, salary FROM NBA
	WHERE player_name ='Jayson Christopher Tatum';

	player_name             |salary    |
	------------------------+----------+
	Jayson Christopher Tatum|-561885196|

Query the encrypted data using ``WHERE`` clause on an encrypted column

.. code-block:: psql

	SELECT player_name, DECRYPT( salary, '6a8431f6e9c2777ee356c0b8aa3c12c0c63bdf366ac3342c4c9184b51697b47f')
	FROM NBA
	WHERE DECRYPT( salary, '6a8431f6e9c2777ee356c0b8aa3c12c0c63bdf366ac3342c4c9184b51697b47f') > 1000000;

Example of ``COPY TO`` using ``DECRYPT``

.. code-block:: psql

	COPY 
	  (SELECT player_name, DECRYPT( salary, '6a8431f6e9c2777ee356c0b8aa3c12c0c63bdf366ac3342c4c9184b51697b47f')
	  FROM NBA
	  WHERE player_name ='Jayson Christopher Tatum') 
	TO WRAPPER parquet_fdw 
	OPTIONS (LOCATION = '/tmp/file.parquet');


***********************
Limitations
***********************
* The following functionality is not supported by the encryption feature: ``Catalog queries``, ``Utility commands``, ``Foreign Tables``, ``Create AS SELECT``.
* A single encryption key must be used per column - using a different key would result in an error.
* Compression of encrypted columns is limited to the following types: ``Flat``,	``LZ4``, ``PD4``, ``DICT``, ``RLE``.
* This feature is not backward compatible with previous versions of SQreamDB.
* The encryption feature affect performance and compression.



***********************
Permissions
***********************
The Data Encryption feature does not require a specific permission, users with **Read** or **Insert** may utilize encryption.