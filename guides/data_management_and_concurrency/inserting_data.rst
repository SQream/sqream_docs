.. _inserting_data:

***************************
Data loading and migration
***************************

This guide covers inserting data into SQream DB via the :ref:`insert` statement and the :ref:`copy_from` statements.

It contains subguides to help with migration from a variety of sources and data locations.

Data loading overview
================================

SQream DB supports importing data from the following sources:

* Local filesystem and Network filesystems (NFS)
* S3
* HDFS
* Over the network, using :ref:`a client driver<client_drivers>`

SQream DB supports loading files in the following formats:

* Text - CSV, TSV, PSV
* Parquet
* ORC

Data loading considerations
================================

Verify data and performance after load
-----------------------------------------

Like other RDBMSs, SQream DB has its own set of best practcies for table design and query optimization.

SQream therefore recommends:

* Verify that the data is as you expect it (e.g. row counts, data types, formatting, content)
* The performance of your queries is adequate
* :ref:`Best practices<sql_best_practices>` were followed for table design
* Applications such as :ref:`Tableau<connect_to_tableau>` and others have been tested, and work
* Data types were not over-provisioned (e.g. don't use VARCHAR(2000) to store a short string)

File storage during load
-------------------------------

During data load, the :ref:`copy_from` command can run on any worker (unless explicitly speficied with the :ref:`workload_manager`).
It is important that every node has the same view of the storage being used - meaning, every SQream DB worker should have access to the files.

Use a supported load method
-------------------------------

SQream DB's :ref:`COPY FROM<copy_from>` syntax can be used to load text files (e.g. CSV), but can't be used for Parquet and ORC.

:ref:`EXTERNAL TABLE<external_tables>` can be used to load test files, Parquet, and ORC files, and can also transform the data prior to materialization as a full table.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * - Method / File type
     - Text (CSV)
     - Parquet
     - ORC
   * - :ref:`copy_from`
     - ✓
     - ✗
     - ✗
   * - :ref:`external_tables`
     - ✓
     - ✓
     - ✓

Unsupported data types
-----------------------------

SQream DB doesn't support the entire set of features that some RDBMSs have, such as ``ARRAY``, ``BLOB``, ``ENUM``, ``SET``, etc..

Some data types will have to be converted. For example, ``ENUM`` can often be stored as a ``VARCHAR``.


..
   insert

   example

   are there some variations to highlight?:

   create table as

   sequences, default values

   insert select

   make distinction between an insert command, and a parameterized/bulk
   insert "over the network"


   copy


   best practices for insert

   chunks and extents, and storage reorganisation

   copy:

   give an example

   supports csv and parquet

   what else do we have right now? any other formats? have the s3 and
   hdfs url support also

   error handling

   best practices

   try to combine sensibly with the external table stuff

Further reading and migration guides
=======================================

.. toctree::
   :maxdepth: 1
   :caption: Migration guides
   :titlesonly:
   
   migration/csv
   migration/parquet
   migration/orc

.. seealso::

   * :ref:`copy_from`
   * :ref:`insert`
   * :ref:`external_tables`
