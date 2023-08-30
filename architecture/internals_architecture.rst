.. _internals_architecture:

**************************
Internals and Architecture
**************************

Get to know the SQreamDB key functions and system architecture components and the best practices and customization possibilities.     

.. figure:: /_static/images/sqream_db_internals.png
   :align: left
   :width: 75%
   :alt: SQreamDB internals

Key Functions and Components
============================

Statement Compiler
------------------

The Statement Compiler, developed using Haskell, accepts SQL text and generates optimized statement plans.

Building Blocks
---------------

In SQreamDB, the main workload is carried out by specialized C++/CUDA building blocks intentionally kept devoid of inherent intelligence; they require precise instructions for operation. The task of effectively assembling these components relies largely on the capabilities of the statement compiler.

Storage Layer
-------------

The storage is split into the metadata layer and an append-only / garbage-collected bulk data layer.

Metadata Layer
^^^^^^^^^^^^^^

Utilizing RocksDB, the metadata layer incorporates features such as snapshots and atomic writes within the transaction system, while working in conjunction with the append-only bulk data layer to maintain overall data consistency.

Bulk Data Layer 
^^^^^^^^^^^^^^^

The bulk data layer consists of IO-optimized extents, containing CPU and GPU-efficient chunks, both of which incorporate compression. During small insert operations, less optimized chunks and extents might result, yet the system is intentionally designed to maintain operational efficiency in such scenarios. It achieves this by facilitating background transactional reorganization without disrupting DML operations. By initially writing small chunks via small inserts and subsequently reorganizing them, the system accommodates swift medium-sized insert transactions while enabling rapid querying capabilities.

Columnar Storage
^^^^^^^^^^^^^^^^

Similar to numerous other analytical database management systems, SQreamDB employs a column store structure for its tables, leveraging the advantages it provides. This approach enhances I/O efficiency and overall performance when dealing with analytic workloads. Furthermore, columns exhibit superior compression properties and are particularly suited for handling bulk data operations.

Concurrency and Admission Control
---------------------------------

The SQreamDB execution engine employs thread workers and message passing for its foundation. This threading approach enables the concurrent execution of diverse operations, seamlessly integrating IO and GPU tasks with CPU operations while boosting the performance of CPU-intensive tasks.

Learn more about :ref:`concurrency_and_scaling_in_sqream`.

Transactions
------------

SQreamDB has serializable transactions, with these features:

* Serializable, with any kind of statement

* Run multiple :ref:`SELECT queries<select>` concurrently with anything

* Run multiple inserts to the same table at the same time

* Cannot run multiple statements in a single transaction

* Other operations such as :ref:`delete`, :ref:`truncate`, and DDL use :ref:`coarse-grained exclusive locking<concurrency_and_locks>`.

GPU Usage
=========

SQreamDB uses GPUs for accelerating database operations. This acceleration brings additional benefits to columnar data processing.

SQreamDB's GPU acceleration is integral to database operations. It is not an additional feature, but rather core to most data operations, e.g. ``GROUP BY``, scalar functions, ``JOIN``, ``ORDER BY``, and more.

Using a GPU is an extended form of SIMD (Single-Instruction, Multiple Data) intended for high throughput operations. When GPU acceleration is used, SQreamDB uses special building blocks to take advantage of the high degree of parallelism of the GPU. This means that GPU operations use a single instruction that runs on multiple values.


