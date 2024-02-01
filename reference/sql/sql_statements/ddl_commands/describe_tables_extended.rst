.. _describe_tables_extended:

************************
DESCRIBE TABLES EXTENDED
************************

The ``DESCRIBE TABLES EXTENDED`` command lets you list all the tables in your database, including information about storage and deleted data. You can define the ``DESCRIBE TABLES EXTENDED`` command as either ``EXTERNAL`` or ``INTERNAL``.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.
.. note::  The **DESCRIBE TABLES EXTENDED** command is not relevant to Alpha, and will be implemented in Beta.


Syntax
======

The following is the syntax for the ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres

   DESC[RIBE] TABLES EXTENDED [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] EXTERNAL | INTERNAL

Parameters
==========

The following parameters can be used with the ``DESCRIBE TABLES EXTENDED`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``database_name``
     - The name of the database.
     - Text
   * - ``schema_name``
     - The name of the table.
     - Text	
   * - ``LIKE``
     - ``pattern``
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.
   
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``database_name``
     - Displays the name of the database
     - Text
     - master
   * - ``schema_name``
     - Displays the name of the schema
     - Text
     - public
   * - ``table_name``
     - Displays the name of the table
     - Text
     - t5
   * - ``table_type``
     - ``Internal`` or ``External``
     - Boolean
     - ``Internal``
   * - ``table_id``
     - Displays the ID of the table
     - Integer
     - 0	 
   * - ``row_count``
     - Displays the number of rows in the table
     - Integer
     - 0
   * - ``created_on``
     - Date and time of table creation
     - Datetime
     - ``2023-08-21 10:54:40``
   * - ``Additional details``
     - 
     - 
     - 
   * - ``number_of_chunks``
     - Displays the number of table chunks
     - Integer
     - ``21``
   * - ``number_of_chunks_with_deleted_rows bytes(compressed)``
     - 
     - Integer
     - ``0``
   * - ``bytes(uncompressed)``
     - 
     - Integer
     - ``15728640``


Using the **external** ``DESCRIBE_TABLES_EXTENDED`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``database_name``
     - Displays the name of the database.
     - Text
     - master
   * - ``table_id``
     - Displays the ID of the table.
     - Integer
     - 3	 
   * - ``schema_name``
     - Displays the name of the schema.
     - Text	
     - public
   * - ``table_name``
     - Displays the name of the table.
     - Text
     - t4	 
   * - ``format``
     - Indicates whether the table is formatted or not.
     - Boolean
     - 0	 
   * - ``created``
     - Displays the table's creation date and timestamp.
     - Date
     - 2022-05-02 15:25:57	 

Examples
========
   
The following is an example of an **internal** ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres
   
   DESCRIBE TABLES EXTENDED DATABASE master SCHEMA public INTERNAL;

.. code-block:: none

   database_name |schema_name |table_name |table_type |row_count |created_on          |Additional details |number_of_chunks |number_of_chunks_with_deleted_rows |bytes(compressed) |bytes(uncompressed)
   --------------+------------+-----------+-----------+----------+--------------------+-------------------+-----------------+-----------------------------------+------------------+------------------
   master        |public      |alex       |Internal   |1048576   |2023-08-21 10:54:40 |                   |21               |0                                  |294851            |15728640

The following is an example of an **external** ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres

   DESCRIBE TABLES EXTENDED DATABASE master SCHEMA public EXTERNAL;

.. code-block:: none

	database_name|schema_name|table_name               |table_type|row_count|created_on         |Additional details                                                                                      |number_of_chunks|number_of_chunks_with_deleted_rows|bytes(compressed)|bytes(uncompressed)|
	-------------+-----------+-------------------------+----------+---------+-------------------+--------------------------------------------------------------------------------------------------------+----------------+----------------------------------+-----------------+-------------------+
	master       |public     |thirdpartydatacleaned    |External  |         |2023-08-22 11:38:53|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/3rdparty_cleaned.parquet     |                |                                  |                 |                   |
	master       |public     |thirdpartydata           |External  |         |2023-08-22 11:39:42|Format: json, Path: gs://product_sqream/blue_demo/DataSources/thirdpartydata.json                       |                |                                  |                 |                   |
	master       |public     |thirdpartydatatransformed|External  |         |2023-08-22 11:41:38|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/3rdparty_transformed.parquet       |                |                                  |                 |                   |
	master       |public     |nba                      |External  |         |2023-08-21 10:58:47|Format: parquet, Path: gs://blue_docs/nba.parquet                                                       |                |                                  |                 |                   |

Using the ``LIKE`` parameter:

.. code-block:: postgres

	DESCRIBE TABLES EXTENDED DATABASE master SCHEMA public EXTERNAL LIKE '%third%';
	
.. code-block:: none

	database_name|schema_name|table_name               |table_type|row_count|created_on         |Additional details                                                                                 |number_of_chunks|number_of_chunks_with_deleted_rows|bytes(compressed)|bytes(uncompressed)|
	-------------+-----------+-------------------------+----------+---------+-------------------+---------------------------------------------------------------------------------------------------+----------------+----------------------------------+-----------------+-------------------+
	master       |public     |thirdpartydatacleaned    |External  |         |2023-08-22 11:38:53|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/3rdparty_cleaned.parquet|                |                                  |                 |                   |
	master       |public     |thirdpartydata           |External  |         |2023-08-22 11:39:42|Format: json, Path: gs://product_sqream/blue_demo/DataSources/thirdpartydata.json                  |                |                                  |                 |                   |
	master       |public     |thirdpartydatatransformed|External  |         |2023-08-22 11:41:38|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/3rdparty_transformed.parquet  |                |                                  |                 |                   |

Permissions
===========

This command requires a ``CONNECT`` permission on the database level and a ``USAGE`` permission on the schema level.
