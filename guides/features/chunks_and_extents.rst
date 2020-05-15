.. _chunks_and_extents:

***********************
Chunks and extents
***********************

All data in SQream DB is stored in logical tables. Each table is made up of rows, spanning one or more columns.

Internally however, SQream DB stores data partitioned vertically by column, and horizontally by **chunks**.

This topic describes the chunk concept, which can be helpful for tuning SQream DB workloads and table structures.

What are chunks? What are extents?
======================================

Chunks
-----------

All data in a table is automatically partitioned into columns, and each column is divided up further into chunks.

A **chunk** is a contiguous number of rows from a specific column. It can be thought of as an automatic partition that spans several millions of records of one column.

.. figure:: /_static/images/chunking.png
   :scale: 80 %
   
   Chunks are collections of rows from a column

A chunk is often between 1MB to a couple hundred megabytes uncompressed, depending on the data type (however, all data in SQream DB is stored compressed).

This chunk size is suitable for filtering and deleting data from large tables, which can contain hundreds of millions or even billions of chunks.

SQream DB adds :ref:`metadata<metadata_system>` to chunks automatically. 

.. note:: Chunking is automatic and transparent for all tables in SQream DB.


Extents
----------

The next step up from the chunk, an **extent** is a specific number of contiguous chunks.

Extents are designed to optimize disk access patterns, at around 20MB compressed, on-disk.

An extent will therefore include between 1 and 25 chunks, based on the actual compressed chunk size.

.. figure:: /_static/images/extents.png
   :scale: 80 %
   
   Extents are a collection of several contiguous chunks


Why was SQream DB built with chunks and extents?
=======================================================

Benefits of chunking
---------------------------

Unlike node-partitioning (or sharding), chunking carries several benefits:

* Chunks are small enough to allow multiple workers to read them concurrently

* Chunks are optimized for fast insertion of data

* Chunks carry metadata, which narrows down their contents for the optimizer

* Chunks are ideal for data retension as they can be deleted en-masse

* Chunks are optimized for reading into RAM and the GPU

* Chunks are compressed individually, which improves compression and data locality

Storage reorganization
--------------------------

SQream DB performs some background storage reorganization to optimize I/O and read patterns.

For example, when data is inserted in small batches, SQream DB will run two background processes called **rechunk** and **reextent** to reorganize the data into larger contiguous chunks and extents.
This is also what happens when :ref:`data is deleted<delete_guide>`.

Data is never overwritten in SQream DB. Instead, new optimized chunks and extents are written to replace the old chunks and extents. Once all data has been rewritten, SQream DB will swap over to the new optimized chunks and extents and remove the old, unoptimized data.


Metadata
------------

The chunk metadata that SQream DB collects enables effective skipping of chunks and extents when queries are executed. When a query specifies a filter (e.g. ``WHERE`` or ``JOIN`` condition) on a range of values that spans a fraction of the table values, SQream DB will optimally scan only that fraction of the table chunks.

Queries that filter on fine-grained date and time ranges will be the most effective, particularly when :ref:`data is timestamped<time_based_data_management>`, and when tables contain a large amount of historical data.

See more in our :ref:`time_based_data_management` guide and our :ref:`metadata_system` guide.