.. _apache_iceberg_sqream_integration:

SQream Integration with Apache Iceberg 
------------------------------------------------------

This document outlines SQream's integration with **Apache Iceberg**, a popular open-source table format designed for managing data lakes with transactional and schema evolution capabilities. The initial phases focus on establishing connectivity and enabling efficient read-only querying of existing Iceberg tables, followed by support for querying table metadata and time travel.

Overview of Apache Iceberg Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apache Iceberg acts as a **table format** that manages the relationship between a logical table and its underlying data files (e.g., Parquet, ORC), along with metadata for versioning, statistics, and consistency. This makes it a crucial component in the **Data Lakehouse** concept.

Iceberg Architecture:
=====================

Iceberg uses a multi-layered metadata structure to track table state:

1. **Data Layer:** Contains the actual data in columnar file formats (e.g., **Parquet**) and **Delete Files** (for records that are logically deleted but physically still exist). 

2. **Metadata Layer:** Tracks the table structure and its versions:

  * **Metadata Files (JSON):** Stores the table's schema, partition schemes, and tracks the current and previous **Snapshots**.
  * **Manifest Lists (AVRO):** Defines a Snapshot by listing all the **Manifest Files** that belong to that version.
  * **Manifest Files (AVRO):** Track individual **Data Files** within a subset of the snapshot, including metadata for efficient data pruning (min/max values, null counts).

3. **The Catalog:** An external store (e.g., REST, AWS Glue) that maps a table name to its current **Metadata File** pointer, enabling transactional guarantees and multi-table semantics.

Connectivity and Read-Only Querying
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The initial focus is on connecting SQream to an external Iceberg REST Catalog and querying existing tables.

1. **Create a Catalog Integration**

This step establishes the connection details to the Iceberg Catalog.

**Syntax:**

.. code:: sql

	CREATE [ OR REPLACE ] CATALOG INTEGRATION <catalog_integration_name>
	  OPTIONS (
		CATALOG_SOURCE = 'ICEBERG_REST',
		REST_CONFIG = (
		  CATALOG_URI = '<rest_api_endpoint_url>',
		  prefix = '<prefix to append to all API routes>',
		  endpoint = '<file system endpoint uri>',
		  access_key_id = "<access key>",
		  secret_access_key = "<secret key>",
		  region = "<region>"
		)
	  );
**Key Parameters:**

+--------------------------+--------------------------------------------------------------------------------------------+
| **Parameter**            | **Description**                                                                            |
+--------------------------+--------------------------------------------------------------------------------------------+
| CATALOG_SOURCE           | Must be set to 'ICEBERG_REST' (default).                                                   |
+--------------------------+--------------------------------------------------------------------------------------------+
| CATALOG_URI              | The endpoint URL for the Iceberg REST Catalog API.                                         |
+--------------------------+--------------------------------------------------------------------------------------------+

**Usage Example:**

.. code:: sql

	CREATE OR REPLACE CATALOG INTEGRATION t_iceberg
	  OPTIONS (
		CATALOG_SOURCE = 'ICEBERG_REST',
		REST_CONFIG = (
		  CATALOG_URI = 'http://192.168.5.82:8181',
		  prefix = 's3://warehouse/',
		  endpoint = 'http://192.168.5.82:9000',
		  access_key_id = 'admin',
		  secret_access_key = 'password',
		  region = 'us-east-1'
		));

2. **Create a Foreign Database**

This links the new Catalog Integration to a database object within SQream.

**Syntax:**

.. code:: sql

	CREATE FOREIGN DATABASE <database_name> catalog integration <catalog_integration_name>;
	
**Usage Example:**

.. code:: sql

	CREATE FOREIGN DATABASE t_iceberg_db catalog integration t_iceberg;
	
.. note:: 

   * This can only be performed on an empty database.
   * SQream DB automatically converts Iceberg identifiers (database, namespace, and table names) to lowercase. Therefore, you must use lowercase names, or explicitly quote any identifier that contains uppercase letters or special characters.

**Limitations**

* **File Format:** Only **Parquet** is supported.
* **Operations:** Only **SELECT** queries are supported. DML (**DELETE, INSERT, UPDATE**) and DDL operations will be added in later phases.
* **Advanced Features:** Time travel, schema evolution, and transactional commands **are not supported**.
* **Writability:** ALLOW_WRITES in the external catalog must be set to false.

**Querying an Iceberg Table**

An Iceberg table behaves like a regular SQream table for **SELECT** operations. SQream automatically uses the Iceberg metadata and statistics (like min/max filtering) to prune irrelevant data files, improving performance.

.. code:: sql

	SELECT * FROM t_iceberg_db.namespace.my_iceberg_table WHERE column_a > 100;

Data Type Mapping
=================

SQream supports most standard Iceberg data types:

+---------------------------+----------------+------------------------+
| **Iceberg Type**          | **SQream Type**| **Notes**              |
+---------------------------+----------------+------------------------+
| boolean                   | BOOL           |                        |
+---------------------------+----------------+------------------------+
| int, long                 | INT, BIGINT    |                        |
+---------------------------+----------------+------------------------+
| float, double             | REAL, DOUBLE   |                        |
+---------------------------+----------------+------------------------+
| decimal(P,S)              | NUMERIC(P,S)   | Precision ≤ 38.        |
+---------------------------+----------------+------------------------+
| date, timestamp           | DATE, DATETIME |                        |
+---------------------------+----------------+------------------------+
| timestamp_ns              | DATETIME2      | Nanosecond precision.  |
+---------------------------+----------------+------------------------+
| string                    | TEXT           | Stored as UTF-8.       |
+---------------------------+----------------+------------------------+






