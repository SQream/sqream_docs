.. _internals_architecture:

***************************
Internals and architecture
***************************

SQream DB internals
==============================

.. figure:: /_static/images/sqream_db_internals.png
   :alt: SQream DB internals

SQream DB is built up of several components, which should look familiar when compared to other RDBMSs.

Statement compiler
------------------------

The statement compiler is written in Haskell, in a modern style with lots of micropasses and stages.

Concurrency and concurrency control
----------------------------------------

SQream DB has a lot of concurrency built-in, which is centered around message passing and queues.

SQream DB has worker pools and other techniques to tune the level of concurrency, as well as a :ref:`lock-based concurrency control system<concurrency_and_locks>`.

This mode of concurrency control doesn't affect :ref:`SELECT queries<select>`.
Inserts only interact with the locks when there are things like :ref:`delete` or a :ref:`DDL operation<ddl_commands>` running.

Bulk data is not passed around in messages. Rather, the memory is shared between threads.

Transactions
--------------------

SQream DB has serializable transactions, with some limitations:

* Serializable, with any kind of statement

* Run multiple :ref:`SELECT queries<select>` concurrently with anything

* Run multiple inserts to the same table at the same time

* Can't run multiple statements in a single transaction

* Other operations such as :ref:`delete`, :ref:`truncate`, and DDL use :ref:`coarse-grained exclusive locking<concurrency_and_locks>`.


Storage
----------

The storage is split into the :ref:`metadata layer<metadata_system>` and a light-weight but powerful append-only bulk data layer.

Metadata layer
^^^^^^^^^^^^^^^^^^^^^^

The metadata layer leverages a lot of features from LevelDB, and is split into a metadata database (snapshots, multiple updates, catalog information).

LevelDB also enables some basic database style features such as snapshots and multiple updates.

The metadata layer, together with the append-only bulk data layer help ensure consistency.

Bulk data layer 
^^^^^^^^^^^^^^^^^^^^^^^^

The bulk data layer is a light-weight but powerful append-only bulk data layer, which is heavily focused on raw tablescan performance.

The storage is based around extent files which have compressed chunks representing a single column. 

Chunks are the smallest entity, representing around 1 to 10 million rows.

SQream DB also has a background storage reorganization process,to ensure good performance after the data has been inserted.
The reorganization process allows support for small, fast inserts - while still maintaining the data arranged for maximum query performance. During storage reorganization, the "old data" remains consistent and on-disk. Data is never updated in-place, to ensure consistency.

Building blocks
----------------------

The heavy lifting in SQream DB is done by single purpose C++/CUDA building blocks.

These are purposely designed to not be smart - they have to be instructed exactly what to do.

Most of the intelligence in piecing things together is in the statement compiler.


Columnar
=============

Like many other analytical database management systems, SQream DB uses a column store for tables.

Column stores offer better I/O and performance with analytic workloads. Columns also compress much better, and lend themselves well to bulk data.

GPU usage
=============

SQream DB uses GPUs for accelerating database operations. This acceleration brings additional benefit to columnar data processing.

SQream DB's GPU acceleration is integral to database operations. It is not an additional feature, but rather core to most data operations, e.g. ``GROUP BY``, scalar functions, ``JOIN``, ``ORDER BY``, and more.

Using a GPU is an extended form of SIMD (Single-instruction, multiple data) intended for high throughput operations. When GPU acceleraiton is used, SQream DB uses special building blocks to take advantage of the high degree of parallelism of the GPU. This means that GPU operations use a single instruction that runs on multiple values.



.. describe the concepts behind the storage, transaction, statement
.. engine


.. some of this might be better in another document, if you're reading to
.. understand how sqream performs, this is not the internal architecture
.. but something more directly important to a customer/user


