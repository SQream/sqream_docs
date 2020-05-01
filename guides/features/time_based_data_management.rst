.. _time_based_data_management:

***************************
Time based data management
***************************

SQream DB's columnar-storage system is well adapted to timestamped data.

When loading data with natural ordering (sorted by a timestamp), SQream DB organizes and collects metadata in chunks of time.
Natural ordering allows for fast retrieval when performing range queries.

.. contents:: In this topic:
   :local:


Timestamped data
===========================

Timestamped data usually has some interesting attributes:

* Data is loaded in a natural order, as it is created

* Updates are infrequent or non-existent. Any updates are done by inserting a new row relating to a new timestamp

* Queries on timestamped data is typically on continuous time ranges

* Inserting and reading data are performed in independently, not in the operation or transaction

* Timestamped data has a high data volume and accumulates faster than typical OLTP workloads

Chunking
=================

Core to handling timestamped data is SQream DB's chunking and metadata system.

When data is inserted, data is automatically partitioned vertically by column, and horizontally by chunk.

A chunk can be thought of as an automatic partition that spans several millions of records of one column.
Unlike node-partitioning (or sharding), chunking carries several benefits:

* Chunks are small enough to allow multiple workers to read them concurrently

* Chunks are optimized for fast insertion of data

* Chunks carry metadata, which narrows down their contents for the optimizer

* CHunks are ideal for data retension as they can be deleted en-masse

* Chunks are optimized for reading into RAM and the GPU

* Chunks are compressed individually, which improves compression and data locality

Use cases
============

Consider a set of data with a timestamp column.

The timestamp order matches the order of data insertion (i.e. newer data is loaded after older data).
This is common when you insert data in small bulks - every 15 minutes, every hour, every day, etc.

SQream DB's storage works by appending new data, partitioned into chunks containing millions of values.
As new data is loaded, it is chunked and appended to a table.

This is particularly useful in many scenarios:

* You run analytical queries spanning specific date ranges (e.g. the sum of transactions during the summer in 2020 vs. the summer in 2019)

* You :ref:`delete data<delete_guide>` when it is older than X months old

* Regulations instruct you to keep several years' worth of data, but you're not interested in querying this data all the time

Best practices for time-based data
=========================================

Use date and datetime types for columns
-----------------------------------------

When creating tables with dates or timestamps, using the purpose-built ``DATE`` and ``DATETIME`` types over integer types or ``VARCHAR`` will bring performance and storage footprint improvements, and in many cases huge performance improvements (as well as data integrity benefits). SQream DB stores dates and datetimes very efficiently and can strongly optimize queries using these specific types.

Ordering
-----------

Data ordering is an important factor in minimizing storage size and improving query performance.

Prioritize inserting data based on timestamps. This will likely reduces the number of chunks that SQream DB reads during query execution.

Limit workload by timestamp
------------------------------

Grouping by and filtering data based on timestamps will improve performance.

For example,

.. code-block:: postgres
   
   SELECT DATEPART(HOUR, timestamp),
          MIN(transaction_amount),
          MAX(transaction_amount),
          avg(transaction_amount)
   FROM transactions
   WHERE timestamp BETWEEN (CURRENT_TIMESTAMP AND DATEADD(MONTH,-3,CURRENT_TIMESTAMP))
   GROUP BY 1;
