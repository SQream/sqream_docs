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

:ref:`EXTERNAL TABLE<external_tables>` can be used to load text files, Parquet, and ORC files, and can also transform the data prior to materialization as a full table.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * - Method / File type
     - Text (CSV)
     - Parquet
     - ORC
     - Streaming data
   * - :ref:`copy_from`
     - ✓
     - ✗
     - ✗
     - ✗
   * - :ref:`external_tables`
     - ✓
     - ✓
     - ✓
     - ✗
   * - :ref:`insert`
     - ✗
     - ✗
     - ✗
     - ✓ (Python, JDBC, Node.JS)

Unsupported data types
-----------------------------

SQream DB doesn't support the entire set of features that some other database systems may have, such as ``ARRAY``, ``BLOB``, ``ENUM``, ``SET``, etc.

These data types will have to be converted before load. For example, ``ENUM`` can often be stored as a ``VARCHAR``.

Extended error handling
----------------------------

While :ref:`external tables<external_tables>` can be used to load CSVs, the ``COPY FROM`` statement provides more fine-grained error handling options, as well as extended support for non-standard CSVs with multi-character delimiters, alternate timestamp formats, and more.

Best practices for CSV
------------------------------

Best practices for Parquet
--------------------------------

* Parquet files are loaded through :ref:`external_tables`. The destination table structure has to match in number of columns between the source files.

* Parquet files support predicate pushdown. When a query is issued over Parquet files, SQream DB uses row-group metadata to determine which row-groups in a file need to be read for a particular query and the row indexes can narrow the search to a particular set of rows.

Type support and behavior notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Unlike ORC, the column types should match the data types exactly (see table below).

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * -   SQream DB type →
   
         Parquet source
     - ``BOOL``
     - ``TINYINT``
     - ``SMALLINT``
     - ``INT``
     - ``BIGINT``
     - ``REAL``
     - ``DOUBLE``
     - Text [#f0]_
     - ``DATE``
     - ``DATETIME``
   * - ``BOOLEAN``
     - ✓ 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - ``INT16``
     - 
     - 
     - ✓
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - ``INT32``
     - 
     - 
     - 
     - ✓
     - 
     - 
     - 
     - 
     - 
     - 
   * - ``INT64``
     - 
     - 
     - 
     - 
     - ✓
     - 
     - 
     - 
     - 
     - 
   * - ``FLOAT``
     - 
     - 
     - 
     - 
     - 
     - ✓
     - 
     - 
     - 
     - 
   * - ``DOUBLE``
     - 
     - 
     - 
     - 
     - 
     - 
     - ✓
     - 
     - 
     - 
   * - ``BYTE_ARRAY`` [#f2]_
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - ✓
     - 
     - 
   * - ``INT96`` [#f3]_
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - ✓ [#f4]_

* If a Parquet file has an unsupported type like ``enum``, ``uuid``, ``time``, ``json``, ``bson``, ``lists``, ``maps``, but the data is not referenced in the table (it does not appear in the :ref:`SELECT` query), the statement will succeed. If the column is referenced, an error will be thrown to the user, explaining that the type is not supported, but the column may be ommited.

Best practices for ORC
--------------------------------

* ORC files are loaded through :ref:`external_tables`. The destination table structure has to match in number of columns between the source files.

* ORC files support predicate pushdown. When a query is issued over ORC files, SQream DB uses ORC metadata to determine which stripes in a file need to be read for a particular query and the row indexes can narrow the search to a particular set of 10,000 rows.

Type support and behavior notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ORC files are loaded through :ref:`external_tables`. The destination table structure has to match in number of columns between the source files.

* The types should match to some extent within the same "class" (see table below).

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * -   SQream DB type →
   
         ORC source
     - ``BOOL``
     - ``TINYINT``
     - ``SMALLINT``
     - ``INT``
     - ``BIGINT``
     - ``REAL``
     - ``DOUBLE``
     - Text [#f0]_
     - ``DATE``
     - ``DATETIME``
   * - ``boolean``
     - ✓ 
     - ✓ [#f5]_
     - ✓ [#f5]_
     - ✓ [#f5]_
     - ✓ [#f5]_
     - 
     - 
     - 
     - 
     - 
   * - ``tinyint``
     - ○ [#f6]_
     - ✓
     - ✓
     - ✓
     - ✓
     - 
     - 
     - 
     - 
     - 
   * - ``smallint``
     - ○ [#f6]_
     - ○ [#f7]_
     - ✓
     - ✓
     - ✓
     - 
     - 
     - 
     - 
     - 
   * - ``int``
     - ○ [#f6]_
     - ○ [#f7]_
     - ○ [#f7]_
     - ✓
     - ✓
     - 
     - 
     - 
     - 
     - 
   * - ``bigint``
     - ○ [#f6]_
     - ○ [#f7]_
     - ○ [#f7]_
     - ○ [#f7]_
     - ✓
     - 
     - 
     - 
     - 
     - 
   * - ``float``
     - 
     - 
     - 
     - 
     - 
     - ✓
     - ✓
     - 
     - 
     - 
   * - ``double``
     - 
     - 
     - 
     - 
     - 
     - ✓
     - ✓
     - 
     - 
     - 
   * - ``string`` / ``char`` / ``varchar``
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - ✓
     - 
     - 
   * - ``date``
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - ✓
     - ✓
   * - ``timestamp``, ``timestamp`` with timezone
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - ✓

* If an ORC file has an unsupported type like ``binary``, ``list``, ``map``, and ``union``, but the data is not referenced in the table (it does not appear in the :ref:`SELECT` query), the statement will succeed. If the column is referenced, an error will be thrown to the user, explaining that the type is not supported, but the column may be ommited.



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

.. rubric:: Footnotes

.. [#f0] Text values include ``TEXT``, ``VARCHAR``, and ``NVARCHAR``

.. [#f2] With UTF8 annotation

.. [#f3] With ``TIMESTAMP_NANOS `` or ``TIMESTAMP_MILLIS`` annotation

.. [#f4] Any microseconds will be rounded down to milliseconds.

.. [#f5] Boolean values are cast to 0, 1

.. [#f6] Will succeed if all values are 0, 1

.. [#f7] Will succeed if all values fit the destination type