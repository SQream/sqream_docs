.. _file_types_overview:

**************
Best Practices
**************
  
Foreign Data Wrapper Best Practice
==================================

A recommended approach when working with :ref:`foreign_tables` and Foreign Data Wrapper (FDW) involves storing files belonging to distinct file families in separate folders.

Best Practices for CSV
======================

Text files, such as CSV, rarely conform to `RFC 4180 <https://tools.ietf.org/html/rfc4180>`_ , so you may need to make the following modifications:

* Use ``OFFSET 2`` for files containing header rows.

* You can capture failed rows in a log file for later analysis, or skip them. See :ref:`capturing_rejected_rows` for information on skipping rejected rows.

* You can modify record delimiters (new lines) using the :ref:`RECORD DELIMITER<changing_record_delimiter>` syntax.

* If the date formats deviate from ISO 8601, refer to the :ref:`copy_date_parsers` section for overriding the default parsing.

* *(Optional)* You can quote fields in a CSV using double-quotes (``"``).

.. note:: You must quote any field containing a new line or another double-quote character.

* If a field is quoted, you must double quote any double quote, similar to the **string literals quoting rules**. For example, to encode ``What are "birds"?``, the field should appear as ``"What are ""birds""?"``. For more information, see :ref:`string literals quoting rules<string_literals>`.

* Field delimiters do not have to be a displayable ASCII character. For all supported field delimiters, see :ref:`field_delimiters`.

Best Practices for Parquet
==========================

The following list shows the best practices when ingesting data from Parquet files:

* You must load Parquet files through :ref:`foreign_tables`. Note that the destination table structure must be identical to the number of columns between the source files.

* Parquet files support **predicate pushdown**. When a query is issued over Parquet files, BLUE uses row-group metadata to determine which row-groups in a file must be read for a particular query and the row indexes can narrow the search to a particular set of rows.

Supported Types and Behavior Notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike the ORC format, the column types should match the data types exactly, as shown in the table below:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * -   BLUE type →
   
         Parquet source
     - ``BOOL``
     - ``TINYINT``
     - ``SMALLINT``
     - ``INT``
     - ``BIGINT``
     - ``REAL``
     - ``DOUBLE``
     - ``TEXT``
     - ``DATE``
     - ``DATETIME``
   * - ``BOOLEAN``
     - Supported 
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
     - Supported
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
     - Supported
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
     - Supported
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
     - Supported
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
     - Supported
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
     - Supported
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
     - Supported [#f4]_

If a Parquet file has an unsupported type, such as ``enum``, ``uuid``, ``time``, ``json``, ``bson``, ``lists``, ``maps``, but the table does not reference this data (i.e., the data does not appear in the :ref:`SELECT` query), the statement will succeed. If the table **does** reference a column, an error will be displayed explaining that the type is not supported, but the column may be omitted.

Best Practices for ORC
======================

The following list shows the best practices when ingesting data from ORC files:

* You must load ORC files through :ref:`foreign_tables`. Note that the destination table structure must be identical to the number of columns between the source files.

* ORC files support **predicate pushdown**. When a query is issued over ORC files, BLUE uses ORC metadata to determine which stripes in a file need to be read for a particular query and the row indexes can narrow the search to a particular set of 10,000 rows.

Type Support and Behavior Notes
-------------------------------

You must load ORC files through foreign table. Note that the destination table structure must be identical to the number of columns between the source files.

For more information, see :ref:`foreign_tables`.

The types should match to some extent within the same "class", as shown in the following table:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * -   BLUE Type →
   
         ORC Source
     - ``BOOL``
     - ``TINYINT``
     - ``SMALLINT``
     - ``INT``
     - ``BIGINT``
     - ``REAL``
     - ``DOUBLE``
     - ``TEXT``
     - ``DATE``
     - ``DATETIME``
   * - ``boolean``
     - Supported 
     - Supported [#f5]_
     - Supported [#f5]_
     - Supported [#f5]_
     - Supported [#f5]_
     - 
     - 
     - 
     - 
     - 
   * - ``tinyint``
     - ○ [#f6]_
     - Supported
     - Supported
     - Supported
     - Supported
     - 
     - 
     - 
     - 
     - 
   * - ``smallint``
     - ○ [#f6]_
     - ○ [#f7]_
     - Supported
     - Supported
     - Supported
     - 
     - 
     - 
     - 
     - 
   * - ``int``
     - ○ [#f6]_
     - ○ [#f7]_
     - ○ [#f7]_
     - Supported
     - Supported
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
     - Supported
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
     - Supported
     - Supported
     - 
     - 
     - 
   * - ``double``
     - 
     - 
     - 
     - 
     - 
     - Supported
     - Supported
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
     - Supported
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
     - Supported
     - Supported
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
     - Supported

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

Further Reading and Migration Guides
====================================

For more information, see the following:

* :ref:`copy_from`
* :ref:`insert`
* :ref:`foreign_tables`

.. rubric:: Footnotes

.. [#f2] With UTF8 annotation

.. [#f3] With ``TIMESTAMP_NANOS`` or ``TIMESTAMP_MILLIS`` annotation

.. [#f4] Any microseconds will be rounded down to milliseconds.

.. [#f5] Boolean values are cast to 0, 1

.. [#f6] Will succeed if all values are 0, 1

.. [#f7] Will succeed if all values fit the destination type


Unsupported Data Types
======================

BLUE does not support certain features that are supported by other databases, such as ``BLOB``, ``ENUM``, and ``SET``. You must convert these data types before loading them. For example, you can store ``ENUM`` as ``TEXT``.
