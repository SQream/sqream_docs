.. _data_clustering:

***********************
Data Clustering
***********************
The **Data Clustering** page describes the following;

.. contents:: 
   :local:
   :depth: 1   
   
Overview
===========
Data warehouses traditionally use fixed, or static, partitioning on large tables to achieve acceptable performance and improve scaling. A **partition** is unit of data that is manipulated independently using DDL and syntax.

What is Data Clustering?
===========
**Data clustering** refers to dividing table data along required dimensions, such as name, date, or location. Data clustering optimizes table structure to significantly improve query performance, especially on very large tables.

A well-clustered table increases the effectiveness of the metadata collected by focusing on a specific and limited range of rows, called **chunks**. Chunks, sometimes referred to as **micro-partitions**, are a contiguous number of rows in a specific column.

The following figure shows a table rows grouped as chunks:

.. figure:: /_static/images/chunking2.png
   :scale: 75 %
   :align: center
   
The following figure shows the rows from the table above converted into chunks:
   
.. figure:: /_static/images/chunking_metadata2.png
   :scale: 75 %
   :align: center

The following are some scenarios ideal for data clustering:

* Queries containing a ``WHERE`` predicate written as ``column COMPARISON value``, such as ``date_column > '2019-01-01'`` or ``id = 107`` when the columns referenced are clustering keys.

  In such a case SQream reads the portion of data that contain values matching these predicates only.

* Two clustered tables joined by their respective clustering keys.

  In such a case SQream uses metadata to more easily identify matching chunks.

Data Clustering Methods
============
The following data clustering methods can be used in tandem or separately to enhance query performance:

.. contents:: 
   :local:
   :depth: 1
   
Using Time-Based Data Management
----------
Overview
~~~~~~~~~~
**Time-based data management** refers to dividing table data along required dimensions. The most common and naturally occuring sorting mechanism is a **timestamp**, which indicates the point in time at which data was inserted into SQream. Because SQream is a columnar storage system, timestamped metadata facilitates quick and easy query processing.

The following is the correct syntax for timestamping a chunk:

.. code-block:: postgres

   SELECT DATEPART(HOUR, timestamp),
          MIN(transaction_amount),
          MAX(transaction_amount),
          avg(transaction_amount)
   FROM transactions
   WHERE timestamp BETWEEN (CURRENT_TIMESTAMP AND DATEADD(MONTH,-3,CURRENT_TIMESTAMP))
   GROUP BY 1;

Timestamping data includes the following properties:

* Data is loaded in a natural order while being inserted.

   ::
   
* Updates are infrequent or non-existent. Updates occur by inserting new rows, which have their own timestamps. 

   ::
   
* Queries on timestamped data is typically on continuous time range.

   ::
   
* Inserting and reading data are performed independently, not in the operation or transaction.

   ::
  
* Timestamped data has a high data volume and accumulates faster than typical online transactional processing workloads.

The following are some scenarios ideal for timestamping:

* Running analytical queries spanning specific date ranges (such as the sum of transactions during August-July 2020 versus August-July 2019).

   ::
   
* Deleting data older than a specific number of months old.

   ::

* Regulations require you to maintain several years of data that you do not need to query on a regular basis.

Best Practices for Time-Based Management
~~~~~~~~~~
Data inserted in bulks is automatically timestamped with the insertion date and time. Therefore, inserting data through small and frequent bulks has the effect of naturally ordering data according to timestamp. Frequent bulks generally refers to short time frames, such as at 15-minute, hourly, or daily intervals. As you insert new data, SQream chunks and appends it into your existing tables according to its timestamp.

The ``DATE`` and ``DATETIME`` types were created to improve performance, minimze storage size, and maintain data integrity. SQream recommends using them instead of ``VARCHAR``.

Using Clustering Keys
----------
Overview
~~~~~~~~~~
While data clustering occurs relatively naturally within a table, certain practices can be used to actively enhance query performance and runtime. Defining **clustering keys** increases performance by explicitly co-locating your data, enabling SQream to avoid processing irrelevant chunks.

A clustering key is a subset of table columns or expressions and is defined using the ``CLUSTER BY`` statement, as shown below:

.. code-block:: postgres
     
   CREATE TABLE users (
      name VARCHAR(30) NOT NULL,
      start_date datetime not null,
      country VARCHAR(30) DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY country;
   

The ``CLUSTER BY`` statement splits ingested data based on the range of data corresponding to the clustering key. This helps create chunks based on specific or related data, avoiding mixed chunks as much as possible. For example, instead of creating chunks based on a fixed number of rows, the ``CLUSTER_BY`` statement creates them based on common values. This optimizes the ``DELETE`` command as well, which deletes rows based on their location in a table.

For more information, see the following:

* `The CLUSTER_BY statement <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/cluster_by.html>`_
* `The DELETE statement <https://docs.sqream.com/en/latest/reference/sql/sql_statements/dml_commands/delete.html>`_   
* `The Deleting Data guide <https://docs.sqream.com/en/latest/guides/features/delete.html>`_

The ``CLUSTERING_HEALTH`` function returns the average clustering depth of your table relative to the clustering keys. A lower value indicates a well-clustered table.


Clustering keys are useful for restructuring large tables not optimally ordered when inserted or as a result of extensive DML. A table that uses clustering keys is referred to as a **clustered table**. Tables that are not clustered require SQream's query optimizer to scan entire tables while running queries, dramatically increasing runtime. Some queries significantly benefit from clustering, such as filtering or joining extensively on clustered columns.

SQream partially sorts data that you load into a clustered table. Note that while clustering tables increases query performance, clustering during the insertion stage can decrease performance by 75%. Nevertheless, once a table is clustered subsequent queries run more quickly.

.. note:: 

   To determine whether clustering will enhance performance, SQream recommends end-to-end testing your clustering keys on a small subset of your data before committing them to permanent use. This is relevant for testing insert and query performance.   

For more information, see the following:

* **Data Manipulation commands (DML)** - see `Data Manipulation Commands (DML) <https://docs.sqream.com/en/latest/reference/sql/sql_statements/index.html#data-manipulation-commands-dml>`_.

* **Creating tables** - see :ref:`create_table`. When you create a table, all new data is clustered upon insert.
   
* **Modifying tables** - see :ref:`cluster_by`.
   
* **Modifying a table schema** - see :ref:`alter_table`.

Using Metadata
----------
SQream uses an automated and transparent system for collecting metadata describing each chunk. This metadata enables skipping unnecessary chunks and extents during query runtime. The system collects chunk metadata when data is inserted into SQream. This is done by splitting data into chunks and collecting and storing specific parameters to be used later.

Because collecting metadata is not process-heavy and does not contribute significantly to query processing, it occurs continuously as a background process. Most metadata collection is typically performed by the GPU. For example, for a 10TB dataset, the metadata storage overhead is approximately 0.5GB.

When a query includes a filter (such as a ``WHERE`` or ``JOIN`` condition) on a range of values spanning a fraction of the table values, SQream scans only the filtered segment of the table.

Once collected, several metadata parameters are stored for later use, including:
 
* The range of values on each column chunk (minimum, maximum).

   ::
 
* The number of values.

   ::
 
* Additional information for query optimization.

Data is collected automatically and transparently on every column type.

Queries filtering highly granular date and time ranges are the most effective, particularly when data is timestamped, and when tables contain a large amount of historical data.

Using Chunks and Extents
----------
SQream stores data in logical tables made up of rows spanning one or more columns. Internally, data is stored in vertical partitions by column, and horizontally by chunks. The **Using Chunks and Extents** section describes how to leverge chunking to optimize query performance.

A **chunk** is a contiguous number of rows in a specific column. Depending on data type, a chunk's uncompressed size typically ranges between 1MB and a few hundred megabytes. This size range is suitable for filtering and deleting data from large tables, which may contain between hundreds, millions, or billions of chunks.
   
An **extent** is a specific number of contiguous chunks. Extents optimize disk access patterns, at around 20MB uncompressed, on-disk. **Comment** *- sentence unclear.* Extents typically include between one and 25 chunks based on the compressed size of each chunk.

.. note:: 

   SQream compresses all data. In addition, all tables are automatically and transparently chunked.

Unlike node-partitioning (or sharding), chunks are:

* Small enough to be read concurrently by multiple workers.

   ::
   
* Optimized for inserting data quickly.

   ::
  
* Capable of carrying metadata, which narrows down their contents for the query optimizer.
   ::
 
* Ideal for data retension because they can be deleted in bulk.

   ::
 
* Optimized for reading into RAM and the GPU.

   ::
 
* Compressed individually to improve compression and data locality.



Rechunking Data
==========
SQream performs background storage reorganization operations to optimize I/O and read patterns.

For example, when small batches of data are inserted, SQream runs two background processes called **rechunk** and **reextent** to reorganize the data into larger contiguous chunks and extents. This is also what happens when data is deleted.

Instead of overwriting data, SQream writes new optimized chunks and extents to replace old ones. After rewriting all old data, SQream switches to the new optimized chunks and extents and deletes the old data.

Examples
==========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1
   
Creating a Clustered Table
-----------------------------
The following is an example of syntax for creating a clustered table on a table naturally ordered by ``start_date``. An alternative cluster key can be defined on such a table to improve performance on queries already ordered by ``country``:

.. code-block:: postgres

   CREATE TABLE users (
      name VARCHAR(30) NOT NULL,
      start_date datetime not null,
      country VARCHAR(30) DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY country;