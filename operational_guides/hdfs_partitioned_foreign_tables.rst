.. _hdfs_partitioned_foreign_tables:

*******************************
HDFS Partitioned Foreign Tables
*******************************

.. contents::
   :local:
   :depth: 1

Overview
========

Scailium has introduced optimized support for partitioned foreign tables stored on HDFS-compatible systems. This native integration allows Scailium to interpret directory structures as physical partitions. During query execution, the engine ‘prunes’ irrelevant data by scanning only the specific folders that match your predicates. This ensures high-performance analytics on massive datasets without the cost of unnecessary data ingestion.

New SQL Syntax
==============

Use the new ``PARTITIONED BY`` clause to declare the partition keys and their SQL data types. The key order must match the physical directory nesting order on HDFS.

.. code-block:: postgres

   CREATE FOREIGN TABLE <table_name>
   (
       <column_1> <data_type>,
       ...
   )
   PARTITIONED BY (
       <partition_key_1> <data_type>,
       <partition_key_2> <data_type>
   )
   WRAPPER <wrapper_name>
   OPTIONS (
       LOCATION = 'hdfs://<namenode_host>:<port>/<base_path>'
   );

.. note:: The ``PARTITIONED BY`` clause is optional. Existing foreign tables without it continue to perform a full table scan as before. No migration is required. Partitions are supported for parquet files only. 

What's New
==========

* **Partition Pruning on Filter Predicates:** Scailium evaluates ``WHERE`` clause predicates against the declared partition keys and restricts HDFS reads to matching directories. Supported predicate types include equality, range, date arithmetic, and NULL checks.
* **Dynamic Spool Join Filter Pushdown:** When a partitioned foreign table is joined with an internal Scailium table or another foreign table, join filters are pushed down to the HDFS side before any data is transferred.
* **Null Partition Handling:** Scailium follows the Hive standard for null partition values. Querying ``WHERE country IS NULL`` resolves to the ``HIVE_DEFAULT_PARTITION`` directory.
* **Graceful Handling of Missing and Empty Partitions:** Non-existent or empty partitions return zero rows without throwing an error.

Usage Examples
==============

Example 1 — Basic Partition Pruning
-----------------------------------

.. code-block:: psql

   CREATE FOREIGN TABLE sales (
       sale_id INT,
       amount FLOAT,
       product_id INT
   )
   PARTITIONED BY (country TEXT, year INT)
   WRAPPER parquet_fdw
   OPTIONS (
       LOCATION = 'hdfs://namenode:9000/data/sales'
   );

   -- Reads only .../sales/country=USA/year=2024/
   
   SELECT * FROM sales
   WHERE year = 2024 AND country = 'USA';

Example 2 — Dynamic Spool Join Filter
-------------------------------------

.. code-block:: psql

   SELECT a.*, b.product_name
   FROM sales_data a
   JOIN internal_products b
       ON a.product_id = b.product_id
       AND a.year = b.year
   WHERE a.year = 2024;
   -- 'year=2024' is pushed to HDFS, pruning all other year partitions.

Expected HDFS Directory Structure
=================================

Directories must follow ``key=value`` naming, nested in the same order as the ``PARTITIONED BY`` clause:

.. code-block:: text

   /data/sales/
       country=USA/
           year=2023/
           year=2024/
       country=UK/
           year=2024/
       country=HIVE_DEFAULT_PARTITION/ <- NULL values
           year=2024/

Verifying Partition Pruning in the Query Plan
=============================================

When partition pruning is active, the compiler report will include an explicit "Partition Pruning" step. Run ``SELECT compiler_report(...)`` on your query and confirm the node is present. If absent, verify that your ``WHERE`` predicate references a declared partition key.

When Partition Pruning Does Not Apply
-------------------------------------

If the "Partition Pruning" step is missing from the compiler report, check whether any of these conditions apply:

* **Predicate does not reference a partition key:** (e.g., ``WHERE sale_amount > 1000``)[cite: 53].
* **Function cannot be evaluated at planning time:** (e.g., ``WHERE UPPER(country) = 'USA'``)[cite: 54].
* **Implicit cast prevents type alignment:** (e.g., partition key declared as INT but compared to a TEXT literal)[cite: 55].
* **Non-deterministic expression:** (e.g., ``WHERE year = EXTRACT(YEAR FROM GETDATE())``)[cite: 56].

.. tip:: Use ``SELECT compiler_report(...)`` and confirm the "Partition Pruning" node is present. As a baseline test, try a direct literal comparison using the exact declared data type of the partition key.

Limitations
===========

Supported Partition Key Data Types
----------------------------------
Only the following types are supported in the ``PARTITIONED BY`` clause:

.. code-block:: text

   BOOLEAN, TINYINT, SMALLINT, INT, BIGINT, DATE, DATETIME, TEXT

Unsupported Hive Partition Values
---------------------------------
Hive partition directory values containing a colon (``:``) or whitespace are not supported in HDFS storage. Partitions with such values will be skipped and a warning will be logged.

Backward Compatibility
======================

This feature is fully backward compatible. No existing tables or queries are affected.

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - Scenario
     - Behavior
   * - No ``PARTITIONED BY`` clause
     - Full table scan as before 
   * - ``PARTITIONED BY``, no matching filter
     - All partitions scanned 
   * - ``PARTITIONED BY``, matching filter
     - Only matching partitions read 
   * - Filter on non-existent partition
     - Zero rows returned, no error 

Security
========

The feature relies on the existing HDFS connectivity layer. HDFS permissions are enforced by HDFS itself; Scailium respects the permissions of the connecting user.