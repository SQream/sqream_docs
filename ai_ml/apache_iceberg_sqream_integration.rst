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
	
.. note:: This can only be performed on an empty database.

**Limitations (Private Preview)**

* **File Format:** Only **Parquet** is supported.
* **Operations:** Only **SELECT** queries are supported. DML (**DELETE, INSERT, UPDATE**) and DDL operations will be added in later phases.
* **Advanced Features:** Time travel, schema evolution, and transactional commands **are not supported**.
* **Writability:** ALLOW_WRITES in the external catalog must be set to false.

**Querying an Iceberg Table**

An Iceberg table behaves like a regular SQream table for **SELECT** operations. SQream automatically uses the Iceberg metadata and statistics (like min/max filtering) to prune irrelevant data files, improving performance.

.. code:: sql

	SELECT * FROM t_iceberg_db.namespace.my_iceberg_table WHERE column_a > 100;

**Data Type Mapping**

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
| decimal(P,S)              | NUMERIC(P,S)   | Precision $\le 38$.    |
+---------------------------+----------------+------------------------+
| date, timestamp           | DATE, DATETIME | Microsecond precision. |
+---------------------------+----------------+------------------------+
| timestamp_ns              | DATETIME       | Nanosecond precision.  |
+---------------------------+----------------+------------------------+
| string                    | TEXT           | Stored as UTF-8.       |
+---------------------------+----------------+------------------------+
| timestamp_nz			    | DATETIME2      |                        |
+---------------------------+----------------+------------------------+


**Querying Data Files (.files)**

This queries the list of data files that belong to the current snapshot.

**Syntax:**

.. code:: sql

	SELECT * FROM <sqream_db_name>.<iceberg_namespace>.<table_name>.files;
	
+--------------------+---------------+----------------------------------------------------------------------+
| **Column**         | **Data Type** | **Description**                                                      |
+--------------------+---------------+----------------------------------------------------------------------+
| file_path          | Text          | Full file path and name.                                             |
+--------------------+---------------+----------------------------------------------------------------------+
| file_format        | Text          | Format, e.g. PARQUET.                                                |
+--------------------+---------------+----------------------------------------------------------------------+
| record_count       | BIGINT        | Number of rows in the file.                                          |
+--------------------+---------------+----------------------------------------------------------------------+
| file_size_in_bytes | BIGINT        | Size of file.                                                        |
+--------------------+---------------+----------------------------------------------------------------------+
| content            | INT           | Type of content (0: Data, 1: Position Deletes, 2: Equality Deletes). |
+--------------------+---------------+----------------------------------------------------------------------+

**Querying Manifests (.manifests)**

This queries the manifest files that make up the current snapshot.

**Syntax:**

.. code:: sql

	SELECT * FROM <sqream_db_name>.<iceberg_namespace>.<table_name>.manifests;
	
+--------------------------+------------+--------------------------------------------------+
| Column                   | Data Type  | Description                                      |
+--------------------------+------------+--------------------------------------------------+
| path                     | Text       | Full path and name of manifest file.             |
+--------------------------+------------+--------------------------------------------------+
| length                   | BIGINT     | Size in bytes.                                   |
+--------------------------+------------+--------------------------------------------------+
| added_snapshot_id        | BIGINT     | ID of the snapshot in which it was added.        |
+--------------------------+------------+--------------------------------------------------+
| added_data_files_count   | BIGINT     | Number of new data files added in this manifest. |
+--------------------------+------------+--------------------------------------------------+
| deleted_data_files_count | BIGINT     | Number of files removed in this manifest.        |
+--------------------------+------------+--------------------------------------------------+

Time Travel and Extended Metadata Queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Phase 2 introduces time travel and expanded metadata query capabilities.

**Time Travel**

Users can query the table state as it existed at a specific timestamp or snapshot ID.

**Syntax:**

.. code:: sql

	SELECT <select_list> FROM <database>.<iceberg_table>
	  [[ TIMESTAMP | VERSION ] AS OF [ timestamp | snapshot-id ]]
	  
Usage Examples:

+----------------------------+---------------------------------------------------------------------------+
| **Feature**                | **Example Query**                                                         |
+----------------------------+---------------------------------------------------------------------------+
| Time Travel to Timestamp   | SELECT * FROM db1.table1 TIMESTAMP AS OF '2023-04-11T18:06:36.289+00:00'; |
+----------------------------+---------------------------------------------------------------------------+
| Time Travel to Snapshot ID | SELECT * FROM db1.table1 VERSION AS OF 2583872980615177898;               |
+----------------------------+---------------------------------------------------------------------------+

**Querying History (.history)**

Shows the changes and lineage of snapshots for a table.

**Syntax:**

.. code:: sql

	SELECT * FROM <sqream_db_name>.<iceberg_namespace>.<table_name>.history;
	
+---------------------+----------------+-----------------------------------------------------------------------+
| **Column**          | **Data Type**  | **Description**                                                       |
+---------------------+----------------+-----------------------------------------------------------------------+
| made_current_at     | Datetime       | Timestamp of when the snapshot became current.                        |
+---------------------+----------------+-----------------------------------------------------------------------+
| snapshot_id         | BIGINT         | Unique identifier for the snapshot.                                   |
+---------------------+----------------+-----------------------------------------------------------------------+
| is_current_ancestor | BOOLEAN        | Indicates if this snapshot is an ancestor of the current table state. |
+---------------------+----------------+-----------------------------------------------------------------------+

Querying Snapshots (.snapshots)

Shows all valid snapshots for a table, including the operation that created them.

**Syntax:**

.. code:: sql

	SELECT * FROM <sqream_db_name>.<iceberg_namespace>.<table_name>.snapshots;
	
+--------------+---------------+-------------------------------------------------------------+
| **Column**   | **Data Type** | **Description**                                             |
+--------------+---------------+-------------------------------------------------------------+
| committed_at | Datetime      | Timestamp of committed snapshot.                            |
+--------------+---------------+-------------------------------------------------------------+
| operation    | TEXT          | Type of operation that created the snapshot (e.g., append). |
+--------------+---------------+-------------------------------------------------------------+
| summary      | TEXT          | Brief description/metrics of the operation.                 |
+--------------+---------------+-------------------------------------------------------------+













