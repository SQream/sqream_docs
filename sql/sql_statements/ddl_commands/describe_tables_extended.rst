:orphan:

.. _describe_tables_extended:

************************
DESCRIBE TABLES EXTENDED
************************

The ``DESCRIBE TABLES EXTENDED`` command lets you list all the tables in your database, including information about storage and deleted data. You can define the ``DESCRIBE TABLES EXTENDED`` command as either ``EXTERNAL`` or ``INTERNAL``.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] TABLES EXTENDED [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] EXTERNAL | INTERNAL [LIKE 'table_name']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Type
     - Description
   * - ``DATABASE``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - The name of the database to search within
   * - ``SCHEMA``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - The name of the schema to search within
   * - ``EXTERNAL``, ``INTERNAL``
     - 
     - You may define the ``DESCRIBE TABLES`` command to show information related to all tables, external tables, or internal tables. The default value is ``ALL``
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match
   
Output
======

Using ``INTERNAL`` with the ``DESCRIBE_TABLES_EXTENDED`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``database_name``
     - ``TEXT``
     - Displays the name of the database
   * - ``schema_name``
     - ``TEXT``
     - Displays the name of the schema
   * - ``table_name``
     - ``TEXT``
     - Displays the name of the table
   * - ``table_type``
     - ``BOOLEAN``
     - ``Internal`` or ``External``
   * - ``row_count``
     - ``INTEGER``
     - Displays the number of rows in the table
   * - ``created_on``
     - ``DATETIME``
     - Date and time of table creation
   * - ``Additional details``
     - ``TEXT``
     - 
   * - ``number_of_chunks``
     - ``INTEGER``
     - Displays the number of table chunks
   * - ``number_of_chunks_with_deleted_rows``
     - ``INTEGER``
     - Displays the number of table chunks with deleted rows
   * - ``bytes(compressed)``
     - ``INTEGER``
     - 
   * - ``bytes(uncompressed)``
     - ``INTEGER``
     - 


Using ``EXTERNAL`` with the ``DESCRIBE_TABLES_EXTENDED`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``database_name``
     - ``TEXT``
     - Displays the name of the database
   * - ``table_id``
     - ``INTEGER`` 
     - Displays the ID of the table
   * - ``schema_name``
     - ``TEXT``	
     - Displays the name of the schema
   * - ``table_name``
     - ``TEXT`` 
     - Displays the name of the table
   * - ``format``
     - ``BOOLEAN`` 
     - Indicates whether the table is formatted or not
   * - ``created``
     - ``DATE`` 
     - Displays the table's creation date and timestamp


Examples
========

.. code-block:: sql
   
	DESCRIBE TABLES EXTENDED DATABASE master SCHEMA public INTERNAL;

	database_name |schema_name |table_name |table_type |row_count |created_on          |Additional details |number_of_chunks |number_of_chunks_with_deleted_rows |bytes(compressed) |bytes(uncompressed)
	--------------+------------+-----------+-----------+----------+--------------------+-------------------+-----------------+-----------------------------------+------------------+------------------
	master        |public      |alex       |Internal   |1048576   |2023-08-21 10:54:40 |                   |21               |0                                  |294851            |15728640

.. code-block:: sql

	DESCRIBE TABLES EXTENDED DATABASE master SCHEMA public EXTERNAL;

	database_name|schema_name|table_name               |table_type|row_count|created_on         |Additional details                                                                                      |number_of_chunks|number_of_chunks_with_deleted_rows|bytes(compressed)|bytes(uncompressed)|
	-------------+-----------+-------------------------+----------+---------+-------------------+--------------------------------------------------------------------------------------------------------+----------------+----------------------------------+-----------------+-------------------+
	master       |public     |thirdpartydatacleaned    |External  |         |2023-08-22 11:38:53|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/3rdparty_cleaned.parquet     |                |                                  |                 |                   |
	master       |public     |thirdpartydata           |External  |         |2023-08-22 11:39:42|Format: json, Path: gs://product_sqream/blue_demo/DataSources/thirdpartydata.json                       |                |                                  |                 |                   |
	master       |public     |thirdpartydatatransformed|External  |         |2023-08-22 11:41:38|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/3rdparty_transformed.parquet       |                |                                  |                 |                   |
	master       |public     |nba                      |External  |         |2023-08-21 10:58:47|Format: parquet, Path: gs://blue_docs/nba.parquet                                                       |                |                                  |                 |                   |

.. code-block:: sql

	DESCRIBE TABLES EXTENDED DATABASE master SCHEMA public EXTERNAL LIKE '%third%';

	database_name|schema_name|table_name               |table_type|row_count|created_on         |Additional details                                                                                 |number_of_chunks|number_of_chunks_with_deleted_rows|bytes(compressed)|bytes(uncompressed)|
	-------------+-----------+-------------------------+----------+---------+-------------------+---------------------------------------------------------------------------------------------------+----------------+----------------------------------+-----------------+-------------------+
	master       |public     |thirdpartydatacleaned    |External  |         |2023-08-22 11:38:53|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/3rdparty_cleaned.parquet|                |                                  |                 |                   |
	master       |public     |thirdpartydata           |External  |         |2023-08-22 11:39:42|Format: json, Path: gs://product_sqream/blue_demo/DataSources/thirdpartydata.json                  |                |                                  |                 |                   |
	master       |public     |thirdpartydatatransformed|External  |         |2023-08-22 11:41:38|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/3rdparty_transformed.parquet  |                |                                  |                 |                   |

Permissions
===========

This command requires a ``CONNECT`` permission on the database level and a ``USAGE`` permission on the schema level.
