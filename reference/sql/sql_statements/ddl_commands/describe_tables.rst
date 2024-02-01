.. _describe_tables:

***************
DESCRIBE TABLES
***************

The ``DESCRIBE TABLES`` command lets you list information about tables in your database.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE TABLES`` command:

.. code-block:: postgres

   DESC[RIBE] TABLES [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] [ALL | INTERNAL | EXTERNAL] [LIKE 'table_name']

Parameters
==========

The following parameters can be used with the ``DESCRIBE TABLES`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``DATABASE``
     - ``database_name``
     - The name of the database to search within
   * - ``SCHEMA``
     - ``schema_name``
     - The name of the schema to search within
   * - ``ALL``, ``EXTERNAL``, ``INTERNAL``
     - 
     - You may define the ``DESCRIBE TABLES`` command to show information related to all tables, external tables, or internal tables. The default value is ``ALL``.
   * - ``LIKE``
     - ``pattern``
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.

	 
Output
======

When the set to ``ALL``, the ``DESCRIBE_TABLES`` command returns the following parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``database_name``
     - Displays the name of the database.
     - TEXT
     - master
   * - ``schema_name``
     - Displays the name of the schema.
     - TEXT
     - public
   * - ``table_name``
     - Displays the name of the table.
     - TEXT
     - nba	 
   * - ``table_type``
     - Displays whether the table is internal or external.
     - TEXT
     - Internal	 
   * - ``row_count``
     - Displays the amount of rows in the table.
     - INTEGER
     - 914
   * - ``created_on``
     - Displays the table creation timestamp.
     - DATE
     - 2022-06-14 13:14:45
   * - ``Addtional details``
     - Displays additional table details.
     - TEXT
     - 
	 
Examples
========

.. code-block:: postgres

   DESCRIBE TABLES DATABASE master SCHEMA public EXTERNAL;

.. code-block:: none

	database_name|schema_name|table_name               |table_type|row_count|created_on         |Additional details                                                                                      |
	-------------+-----------+-------------------------+----------+---------+-------------------+--------------------------------------------------------------------------------------------------------+
	master       |public     |AdImpressions            |External  |         |2023-07-05 11:08:48|Format: json, Path: gs://product_sqream/blue_demo/DataSources/ad_impressions.json                       |
	master       |public     |AdImpressionsCleaned     |External  |         |2023-07-06 06:02:32|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/adImpressions_cleaned.parquet|
	master       |public     |applications_gold_ml     |External  |         |2023-08-09 11:15:41|Format: parquet, Path: gs://sqream-blue-fintech-demo/storage/applications_gold_ml/                      |
	master       |public     |AdImpressionsTransformed |External  |         |2023-07-06 06:04:42|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/adImpressions_transformed.parquet  |
	master       |public     |customer                 |External  |         |2023-08-10 12:09:09|Format: parquet, Path: gs://delivery-poc-us/demo/customer-9.parquet                                     |
	master       |public     |applications_bronze      |External  |         |2023-08-10 12:10:57|Format: json, Path: gs://sqream-blue-fintech-demo/loan_dataset/json/application_record.json             |
	master       |public     |credit_records_bronze    |External  |         |2023-08-10 12:13:53|Format: json, Path: gs://sqream-blue-fintech-demo/loan_dataset/json/credit_record.json                  |
	master       |public     |applications_silver      |External  |         |2023-08-10 12:16:38|Format: parquet, Path: gs://sqream-blue-fintech-demo/storage/applications_silver/*                      |
	master       |public     |credit_records_silver    |External  |         |2023-08-10 12:16:41|Format: parquet, Path: gs://sqream-blue-fintech-demo/storage/credit_records_silver/*                    |
	master       |public     |ClickStream              |External  |         |2023-07-06 06:19:26|Format: json, Path: gs://product_sqream/blue_demo/DataSources/clickstream.json                          |
	master       |public     |ClickStreamCleaned       |External  |         |2023-07-06 06:20:51|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/clickstream_cleaned.parquet  |
	master       |public     |ClickStreamTransformed   |External  |         |2023-07-06 06:21:20|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/clickstream_transformed.parquet    |
	master       |public     |ThirdPartyData           |External  |         |2023-07-06 06:22:29|Format: json, Path: gs://product_sqream/blue_demo/DataSources/thirdpartydata.json                       |
	master       |public     |ThirdPartyDataCleaned    |External  |         |2023-07-06 06:23:10|Format: parquet, Path: gs://product_sqream/blue_demo/CleanedNValidatedData/3rdparty_cleaned.parquet     |
	master       |public     |ThirdPartyDataTransformed|External  |         |2023-07-06 06:23:50|Format: parquet, Path: gs://product_sqream/blue_demo/TransformedData/3rdparty_transformed.parquet       |
 

.. code-block:: postgres

  DESCRIBE TABLES DATABASE master SCHEMA public like '%records%';
  
.. code-block:: none

	database_name|schema_name|table_name           |table_type|row_count|created_on         |Additional details                                                                    |
	-------------+-----------+---------------------+----------+---------+-------------------+--------------------------------------------------------------------------------------+
	master       |public     |credit_records_bronze|External  |         |2023-08-10 12:13:53|Format: json, Path: gs://sqream-blue-fintech-demo/loan_dataset/json/credit_record.json|
	master       |public     |credit_records_silver|External  |         |2023-08-10 12:16:41|Format: parquet, Path: gs://sqream-blue-fintech-demo/storage/credit_records_silver/*  |

Permissions
===========

This command requires a ``CONNECT`` permission on the database level and a ``USAGE`` permission on the schema level.
