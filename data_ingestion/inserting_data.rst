.. _inserting_data:

***************************
Inserting Data Overview
***************************
The **Inserting Data Overview** page provides basic information useful when ingesting data into SQream from a variety of sources and locations, and describes the following:

.. contents::
   :local:
   :depth: 1
   
Getting Started
================================
SQream supports ingesting data using the following methods:

* Executing the ``INSERT`` statement using a client driver.

   ::
   
* Executing the ``COPY FROM`` statement or ingesting data from foreign tables:

  * Local filesystem and locally mounted network filesystems
  * Inserting Data using the Amazon S3 object storage service
  * Inserting Data using an HDFS data storage system

SQream supports loading files from the following formats:

* Text - CSV, TSV, and PSV
* Parquet
* ORC

For more information, see the following:

* Using the ``INSERT`` statement - :ref:`insert`

* Using client drivers - :ref:`Client drivers<client_drivers>`

* Using the ``COPY FROM`` statement - :ref:`copy_from`

* Using the Amazon S3 object storage service - :ref:`s3`

* Using the HDFS data storage system - :ref:`hdfs`

* Loading data from foreign tables - :ref:`foreign_tables`

Data Loading Considerations
================================
The **Data Loading Considerations** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Verifying Data and Performance after Loading
-----------------------------------------
Like many RDBMSs, SQream recommends its own set of best practices for table design and query optimization. When using SQream, verify the following:

* That your data is structured as you expect (row counts, data types, formatting, content).

* That your query performance is adequate.

* That you followed the table design best practices (:ref:`Optimization and Best Practices<sql_best_practices>`).

* That you've tested and verified that your applications work (such as :ref:`Tableau<connect_to_tableau>`).

* That your data types have not been not over-provisioned.

File Soure Location when Loading
--------------------------------
While you are loading data, you can use the ``COPY FROM`` command to let statements run on any worker. If you are running multiple nodes, verify that all nodes can see the source the same. Loading data from a local file that is only on one node and not on shared storage may cause it to fail. If required, you can also control which node a statement runs on using the Workload Manager).

For more information, see the following:

* :ref:`copy_from`

* :ref:`workload_manager`

Supported Load Methods
-------------------------------
You can use the ``COPY FROM`` syntax to load CSV files.

.. note:: The ``COPY FROM`` cannot be used for loading data from Parquet and ORC files.

You can use foreign tables to load text files, Parquet, and ORC files, and to transform your data before generating a full table, as described in the following table:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * - Method/File Type
     - Text (CSV)
     - Parquet
     - ORC
     - Streaming Data
   * - COPY FROM
     - Supported
     - Not supported
     - Not supported
     - Not supported
   * - Foreign tables
     - Supported
     - Supported
     - Supported
     - Not supported
   * - INSERT
     - Not supported
     - Not supported
     - Not supported
     - Supported (Python, JDBC, Node.JS)
	 
For more information, see the following:

* :ref:`COPY FROM<copy_from>`

* :ref:`Foreign tables<foreign_tables>`

* :ref:`INSERT<insert>`

Unsupported Data Types
-----------------------------
SQream does not support certain features that are supported by other databases, such as ``ARRAY``, ``BLOB``, ``ENUM``, and ``SET``. You must convert these data types before loading them. For example, you can store ``ENUM`` as ``TEXT``.

Handing Extended Errors
----------------------------
While you can use foreign tables to load CSVs, the ``COPY FROM`` statement provides more fine-grained error handling options and extended support for non-standard CSVs with multi-character delimiters, alternate timestamp formats, and more.

For more information, see :ref:`foreign tables<foreign_tables>`.

Best Practices for CSV
------------------------------
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
--------------------------------
The following list shows the best practices when inserting data from Parquet files:

* You must load Parquet files through :ref:`foreign_tables`. Note that the destination table structure must be identical to the number of columns between the source files.

* Parquet files support **predicate pushdown**. When a query is issued over Parquet files, SQream uses row-group metadata to determine which row-groups in a file must be read for a particular query and the row indexes can narrow the search to a particular set of rows.

Supported Types and Behavior Notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Unlike the ORC format, the column types should match the data types exactly, as shown in the table below:

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
--------------------------------
The following list shows the best practices when inserting data from ORC files:

* You must load ORC files through :ref:`foreign_tables`. Note that the destination table structure must be identical to the number of columns between the source files.

* ORC files support **predicate pushdown**. When a query is issued over ORC files, SQream uses ORC metadata to determine which stripes in a file need to be read for a particular query and the row indexes can narrow the search to a particular set of 10,000 rows.

Type Support and Behavior Notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You must load ORC files through foreign table. Note that the destination table structure must be identical to the number of columns between the source files.

For more information, see :ref:`foreign_tables`.

The types should match to some extent within the same "class", as shown in the following table:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * -   SQream DB Type →
   
         ORC Source
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
=======================================
For more information, see the following:

* :ref:`copy_from`
* :ref:`insert`
* :ref:`foreign_tables`

.. rubric:: Footnotes

.. [#f0] Text values include ``TEXT``, ``VARCHAR``, and ``NVARCHAR``

.. [#f2] With UTF8 annotation

.. [#f3] With ``TIMESTAMP_NANOS`` or ``TIMESTAMP_MILLIS`` annotation

.. [#f4] Any microseconds will be rounded down to milliseconds.

.. [#f5] Boolean values are cast to 0, 1

.. [#f6] Will succeed if all values are 0, 1

.. [#f7] Will succeed if all values fit the destination type