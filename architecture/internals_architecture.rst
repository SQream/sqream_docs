.. _internals_architecture:

**************************
Internals and Architecture
**************************


SQreamDB internals
==================

Here is a high level architecture diagram of SQreamDB's internals.

.. figure:: /_static/images/sqream_db_internals.png
   :alt: SQreamDB internals

Statement Compiler
------------------

The statement compiler is written in Haskell. This takes SQL text and produces an optimized statement plan.

Concurrency and Concurrency Control
-----------------------------------

The execution engine in SQreamDB is built around thread workers with message passing. It uses threads to overlap different kinds of operations (including IO and GPU operations with CPU operations), and to accelerate CPU intensive operations.

Transactions
------------

SQreamDB has serializable transactions, with these features:

* Serializable, with any kind of statement

* Run multiple :ref:`SELECT queries<select>` concurrently with anything

* Run multiple inserts to the same table at the same time

* Cannot run multiple statements in a single transaction

* Other operations such as :ref:`delete`, :ref:`truncate`, and DDL use :ref:`coarse-grained exclusive locking<concurrency_and_locks>`.

Storage
-------

The storage is split into the :ref:`metadata layer<metadata_system>` and an append-only/ garbage collected bulk data layer.

Metadata Layer
^^^^^^^^^^^^^^

The metadata layer uses RocksDB, and uses RocksDB's snapshot and write atomic features as part of the transaction system.

The metadata layer, together with the append-only bulk data layer help ensure consistency.

Bulk Data Layer 
^^^^^^^^^^^^^^^

The bulk data layer is comprised of extents, which are optimized for IO performance as much as possible. Inside the extents, are chunks, which are optimized for processing in the CPU and GPU. Compression is used in the extents and chunks.

When you run small inserts, you will get less optimized chunks and extents, but the system is designed to both be able to still run efficiently on this, and to be able to reorganize them transactionally in the background, without blocking DML operations. By writing small chunks in small inserts, then reorganizing later, it supports both fast medium sized insert transactions and fast querying.

Building Blocks
---------------

The heavy lifting in SQreamDB is done by single purpose C++/CUDA building blocks.

These are purposely designed to not be smart - they have to be instructed exactly what to do.

Most of the intelligence in piecing things together is in the statement compiler.


Columnar
========

Like many other analytical database management systems, SQreamDB uses a column store for tables.

Column stores offer better I/O and performance with analytic workloads. Columns also compress much better, and lend themselves well to bulk data.

GPU Usage
=========

SQreamDB uses GPUs for accelerating database operations. This acceleration brings additional benefit to columnar data processing.

SQreamDB's GPU acceleration is integral to database operations. It is not an additional feature, but rather core to most data operations, e.g. ``GROUP BY``, scalar functions, ``JOIN``, ``ORDER BY``, and more.

Using a GPU is an extended form of SIMD (Single-instruction, multiple data) intended for high throughput operations. When GPU acceleraiton is used, SQreamDB uses special building blocks to take advantage of the high degree of parallelism of the GPU. This means that GPU operations use a single instruction that runs on multiple values.


