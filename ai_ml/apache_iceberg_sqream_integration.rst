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

Connectivity to Iceberg
~~~~~~~~~~~~~~~~~~~~~~~

Connecting SQream to an external Iceberg REST Catalog.

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

**Limitations:**

* **File Format:** Only **Parquet** is supported.
* **Operations:** Only **SELECT** queries are supported. DML (**DELETE, INSERT, UPDATE**) and DDL operations will be added in later phases.
* **Advanced Features:** schema evolution, and transactional commands **are not supported**.
* **Writability:** ALLOW_WRITES in the external catalog must be set to false.

DDL Operations on an Iceberg Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An Iceberg table can be created in Sqream with DDL support for the data types listed below. ALTER operations are currently not supported.

**Syntax:**

.. code:: sql

	CREATE [OR REPLACE] ICEBERG TABLE <FOREIGN_DATABASE>.<NAMESPACE/S>.table_name
    -- Column Definitions
    (
      col_name1 col_type1 [NULL / NOT NULL],
      col_name2 col_type2 [NULL / NOT NULL]],
      ...
    )
    [OPTIONS (
       [PARTITIONED BY ([<COLUMN>|<TRANSFORMED_COLUMN*>, ..])]
       [TBLPROPERTIES* = [...]
       [COMMENT*='table_comment']
    )]
    -- Creation from Query
    [AS select_statement];
	
	DROP [TABLE] [IF EXISTS] <FOREIGN_DATABASE>.<NAMESPACE>.table_name;

	TRUNCATE [TABLE] <FOREIGN_DATABASE>.<NAMESPACE>.table_name;

Usage Examples:

.. code:: sql

	--create table
	CREATE OR REPLACE ICEBERG TABLE t_iceberg_db.test_namespace.t (
		id BIGINT,
		event_time TIMESTAMP,
		data TEXT,
		category TEXT
	);
	
	--create as select
	CREATE OR REPLACE ICEBERG TABLE t_iceberg_db.test_namespace.t1 AS select * from x;
	
	--drop
	DROP TABLE IF EXISTS t_iceberg_db.test_namespace.t;
	
	--truncate
	TRUNCATE TABLE t_iceberg_db.test_namespace.t;
	
.. note:: 

   * Namespace creation is currently not supported in Sqream and must be performed externally.
   * Partitions are not supported at this stage.
	

Querying an Iceberg Table
~~~~~~~~~~~~~~~~~~~~~~~~~

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

Time Travel
===========

Apache Iceberg’s Time Travel capability allows users to query a table as it existed at a specific point in time or at a specific version. This is achieved through Iceberg’s snapshot-based architecture, which captures the full state of the table following every write operation.

**Time Travel Core Concepts:**

* **Snapshots:** A snapshot represents the state of a table at a point in time. Every commit (insert, update, delete, or overwrite) generates a new snapshot.

* **Snapshot IDs:** Each snapshot is assigned a unique 64-bit integer ID, providing a definitive reference for auditing or rollbacks.

* **Immutability:** Once a snapshot is created, the underlying data files associated with it are immutable. This ensures that historical queries remain consistent even as the "live" table continues to evolve.


**Syntax:**

.. code:: sql

	SELECT <select_list> FROM <database>.<namespace>.<iceberg_table>
		[[ TIMESTAMP | VERSION ] AS OF [ timestamp| unix_timestamp | snapshot-id ]];
	 
.. list-table::
   :header-rows: 1

   * - Parameter
     - Description
   * - ``TIMESTAMP``
     - The ``TIMESTAMP AS OF`` clause allows for temporal lookups by resolving the most recent snapshot that was successfully committed at or before the specified point in time.
   * - ``VERSION``
     - The ``VERSION AS OF`` clause allows for deterministic query execution by pinning the query plan to a specific, unique Snapshot ID.
	 	  
Usage Examples:

.. code:: sql

	SELECT * FROM t_iceberg_db.namespace.my_iceberg_table TIMESTAMP AS OF '2023-04-11T18:06:36.289' WHERE column_a > 100;
	
	SELECT * FROM t_iceberg_db.namespace.my_iceberg_table VERSION AS OF 1231234;
	
	SELECT * FROM t_iceberg_db.namespace.my_iceberg_table VERSION AS OF 2583872980615177898;
	

Extended Metadata Queries
=========================

**Querying Snapshots (.snapshots)**

Shows all valid snapshots for a table, including the operation that created them.

**Syntax:**

.. code:: sql

	SELECT * FROM <database>.<namespace>.<iceberg_table>.snapshots;
	
+--------------+---------------+-------------------------------------------------------------+
| **Column**   | **Data Type** | **Description**                                             |
+--------------+---------------+-------------------------------------------------------------+
| committed_at | DATETIME2     | Timestamp of committed snapshot.                            |
+--------------+---------------+-------------------------------------------------------------+
| snapshot_id  | BIGINT        | The unique identifier for the snapshot.                     |
+--------------+---------------+-------------------------------------------------------------+
| parent_id    | BIGINT        | The ID of the previous snapshot.                            |
+--------------+---------------+-------------------------------------------------------------+
| operation    | TEXT          | Type of operation that created the snapshot (e.g., append). |
+--------------+---------------+-------------------------------------------------------------+
| manifest_list| TEXT          | The full path to the manifest list file.                    |
+--------------+---------------+-------------------------------------------------------------+

**Querying History (.history)**

Shows the changes and lineage of snapshots for a table.

**Syntax:**

.. code:: sql

	SELECT * FROM <database>.<namespace>.<iceberg_table>.history;
	
+---------------------+----------------+-----------------------------------------------------------------------+
| **Column**          | **Data Type**  | **Description**                                                       |
+---------------------+----------------+-----------------------------------------------------------------------+
| made_current_at     | DATETIME2      | Timestamp of when the snapshot became current.                        |
+---------------------+----------------+-----------------------------------------------------------------------+
| snapshot_id         | BIGINT         | Unique identifier for the snapshot.                                   |
+---------------------+----------------+-----------------------------------------------------------------------+
| parent_id           | BIGINT         | The ID of the snapshot that preceded this one.                        |
+---------------------+----------------+-----------------------------------------------------------------------+
| is_current_ancestor | BOOL           | Indicates if this snapshot is an ancestor of the current table state. |
+---------------------+----------------+-----------------------------------------------------------------------+

**Querying Manifests (.manifests)**

The manifests table returns a list of all manifest files that make up the current table state.

**Syntax:**

.. code:: sql

	SELECT * FROM <database>.<namespace>.<iceberg_table>.manifests;

+------------------------------+---------------+------------------------------------------------------------------------------------------+
| **Column**                   | **Data Type** | **Description**                                                                          |
+==============================+===============+==========================================================================================+
| content                      | INT           | Type of manifest: 0 (Data) or 1 (Deletes).                                               |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| path                         | TEXT          | The full URI/path to the specific manifest file stored in your storage layer             |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| length                       | BIGINT        | The size of the manifest file in bytes.                                                  |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| added_snapshot_id            | BIGINT        | The ID of the snapshot that first introduced this manifest file to the table.            |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| added_data_files_count       | INT           | The number of new data files that were added within this specific manifest.              |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| existing_data_files_count    | INT           | The number of data files that already existed and were carried over into this manifest.  |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| deleted_data_files_count     | INT           | The number of data files marked as deleted in this manifest.                             |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| added_delete_files_count     | INT           | The number of new delete files (position or equality deletes) added to the table in the  |
|                              |               | snapshot that created this manifest.                                                     |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| existing_delete_files_count  | INT           | The number of previously existing delete files that are still active and were carried    |
|                              |               | over into this manifest from earlier snapshots.                                          |
+------------------------------+---------------+------------------------------------------------------------------------------------------+
| deleted_delete_files_count   | INT           | The number of delete files marked as removed in this manifest                            |
+------------------------------+---------------+------------------------------------------------------------------------------------------+

**Querying Files (.files)**

The files table (often called the files metadata view) returns a granular list of every individual data file (e.g., Parquet, Avro, or ORC) currently tracked by the table.

**Syntax:**

.. code:: sql
   
   SELECT * FROM <database>.<namespace>.<iceberg_table>.files;

+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| **Column**          | **Data Type**  | **Description**                                                                                       |
+=====================+================+=======================================================================================================+
| content             | INT            | Refers to type of content stored by the data file: 0 (Data), 1 (Position Deletes), 2 (Equality).      |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| file_path           | TEXT           | Full file path and name                                                                               |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| file_format         | TEXT           | Format, e.g. PARQUET.                                                                                 |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| spec_id             | INT            | Refers to the partition specification that a particular data file adheres to.                         |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| record_count        | BIGINT         | Number of rows.                                                                                       |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| file_size_in_bytes  | BIGINT         | Size of file.                                                                                         |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| split_offsets       | ARRAY[BIGINT]  | A list of byte offsets within the file where it can be safely split for parallel reading.             |
|                     |                | For example, in a large Parquet file, these offsets point to the start of row groups.                 |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| equality_ids        | ARRAY[INT]     | Used specifically for Equality Delete files.                                                          |
|                     |                | Field IDs of the columns used to determine if a row is deleted.                                       |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+
| sort_order_id       | INT            | The identifier for the specific Sort Order applied to the data within this file.                      |
|                     |                | Maps back to metadata to optimize join and aggregation performance.                                   |
+---------------------+----------------+-------------------------------------------------------------------------------------------------------+

Usefull Example: 

In addition to querying Iceberg metadata tables, you can also join them with each other.

.. code:: sql

	SELECT * FROM t_iceberg_db.namespace.my_iceberg_table1.manifests a 
		JOIN t_iceberg_db.namespace.my_iceberg_table2.snapshots b 
		ON a.added_snapshot_id = b.snapshot_id;