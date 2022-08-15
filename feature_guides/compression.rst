.. _compression:

***********************
Compression
***********************
The **Compression** page describes the following:

.. contents:: 
   :local:
   :depth: 1

.. |icon-new_dark_gray_2022.1.1.png| image:: /_static/images/new_dark_gray_2022.1.1.png
   :align: middle
   :width: 110

SQream uses a variety of compression and encoding methods to optimize query performance and to save disk space.

Encoding
=============
**Encoding** is an automatic operation used to convert data into common formats. For example, certain formats are often used for data stored in columnar format, in contrast with data stored in a CSV file, which stores all data in text format.

Encoding enhances performance and reduces data size by using specific data formats and encoding methods. SQream encodes data in a number of ways in accordance with the data type. For example, a **date** is stored as an **integer**, starting with **March 1st 1CE**, which is significantly more efficient than encoding the date as a string. In addition, it offers a wider range than storing it relative to the Unix Epoch. 

Lossless Compression
==============
**Compression** transforms data into a smaller format without sacrificing accuracy, known as **lossless compression**.

After encoding a set of column values, SQream packs the data and compresses it and decompresses it to make it accessible to users. Depending on the compression scheme used, these operations can be performed on the CPU or the GPU. Some users find that GPU compressions provide better performance.

Automatic Compression
------------------------
By default, SQream automatically compresses every column (see :ref:`Specifying Compression Strategies<specifying_compressions>` below for overriding default compressions). This feature is called **automatic adaptive compression** strategy.

When loading data, SQream DB automatically decides on the compression schemes for specific chunks of data by trying several compression schemes and selecting the one that performs best. SQream DB tries to balance more agressive compressions with the time and CPU/GPU time required to compress and decompress the data.

Compression Methods
------------------------
The following table shows the available compression methods:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Compression Method
     - Supported Data Types
     - Description
     - Location
   * - ``FLAT``
     - All types
     - No compression (forced)
     - NA
   * - ``DEFAULT``
     - All types
     - Automatic scheme selection
     - NA
   * - ``DICT``
     - Integer types, dates and timestamps, short texts
     - 
         Dictionary compression with RLE. For each chunk, SQream DB creates a dictionary of distinct values and stores only their indexes.
         
         Works best for integers and texts shorter than 120 characters, with <10% unique values.
         
         Useful for storing ENUMs or keys, stock tickers, and dimensions.
         
         If the data is optionally sorted, this compression will perform even better.
     - GPU
   * - ``P4D``
     - Integer types, dates and timestamps
     - 
         Patched frame-of-reference + Delta 
         
         Based on the delta between consecutive values.
         Works best for monotonously increasing or decreasing numbers and timestamps
     - GPU
   * - ``LZ4``
     - Text types
     - Lempel-Ziv general purpose compression, used for texts
     - CPU
   * - ``SNAPPY``
     - Text types
     - General purpose compression, used for texts
     - CPU
   * - ``RLE``
     - Integer types, dates and timestamps
     - Run-length encoding. This replaces sequences of values with a single pair. It is best for low cardinality columns that are used to sort data (``ORDER BY``).
     - GPU
   * - ``SEQUENCE``
     - Integer types
     - Optimized RLE + Delta type for built-in :ref:`identity columns<identity>`. 
     - GPU
   * - ``zlib``
     - All types
     - The **basic_zlib_compressor** and **basic_zlib_decompressor** compress and decompress data in the **ZLIB** format, using **DualUseFilters** for input and output. In general, compression filters are for output, and decompression filters for input. 
     - **Comment - GPU, CPU?**
	 
.. note:: Automatic compression does not select the **zlib** compression method.

.. _specifying_compressions:

Specifying Compression Strategies
----------------------------------
When you create a table without defining any compression specifications, SQream defaults to automatic adaptive compression (``"default"``). However, you can prevent this by specifying a compression strategy when creating a table.

This section describes the following compression strategies:

.. contents:: 
   :local:
   :depth: 1

Explicitly Specifying Automatic Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you explicitly specify automatic compression, the following two are equivalent:

.. code-block:: postgres
   
   CREATE TABLE t (
      x INT,
      y TEXT(50)
   );

In this version, the default compression is specified explicitly:

.. code-block:: postgres
   
   CREATE TABLE t (
      x INT CHECK('CS "default"'),
      y TEXT(50) CHECK('CS "default"')
   );

Forcing No Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Forcing no compression** is also known as "flat", and can be used in the event that you want to remove compression entirely on some columns. This may be useful for reducing CPU or GPU resource utilization at the expense of increased I/O.

The following is an example of removing compression:

.. code-block:: postgres
   
   CREATE TABLE t (
      x INT NOT NULL CHECK('CS "flat"'), -- This column won't be compressed
      y TEXT(50) -- This column will still be compressed automatically
   );

Forcing Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In other cases, you may want to force SQream to use a specific compression scheme based on your knowledge of the data, as shown in the following example:

.. code-block:: postgres
   
   CREATE TABLE t (
      id BIGINT NOT NULL CHECK('CS "sequence"'),
      y TEXT(110) CHECK('CS "lz4"'), -- General purpose text compression
      z TEXT(80) CHECK('CS "dict"'), -- Low cardinality column
      
   );

Examining Compression Effectiveness
--------------------------------------
Queries made on the internal metadata catalog can expose how effective the compression is, as well as what compression schemes were selected.

This section describes the following:

.. contents:: 
   :local:
   :depth: 1

Querying the Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following is a sample query that can be used to query the catalog:

.. code-block:: postgres
   
   SELECT c.column_name AS "Column",
          cc.compression_type AS "Actual compression",
          AVG(cc.compressed_size) "Compressed",
          AVG(cc.uncompressed_size) "Uncompressed",
          AVG(cc.uncompressed_size::FLOAT/ cc.compressed_size) -1 AS "Compression effectiveness",
          MIN(c.compression_strategy) AS "Compression strategy"
    FROM sqream_catalog.chunk_columns cc
      INNER JOIN sqream_catalog.columns c
              ON cc.table_id = c.table_id
             AND cc.database_name = c.database_name
             AND cc.column_id = c.column_id

      WHERE c.table_name = 'some_table'  -- This is the table name which we want to inspect

      GROUP BY 1,
               2;

Example Subset from "Ontime" Table			   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following is an example (subset) from the ``ontime`` table:

.. code-block:: psql
   
   stats=> SELECT c.column_name AS "Column",
   .          cc.compression_type AS "Actual compression",
   .          AVG(cc.compressed_size) "Compressed",
   .          AVG(cc.uncompressed_size) "Uncompressed",
   .          AVG(cc.uncompressed_size::FLOAT/ cc.compressed_size) -1 AS "Compression effectiveness",
   .          MIN(c.compression_strategy) AS "Compression strategy"
   .   FROM sqream_catalog.chunk_columns cc
   .     INNER JOIN sqream_catalog.columns c
   .             ON cc.table_id = c.table_id
   .            AND cc.database_name = c.database_name
   .            AND cc.column_id = c.column_id
   .
   .   WHERE c.table_name = 'ontime' 
   .
   .   GROUP BY 1,
   .            2;
   
   Column                    | Actual compression | Compressed | Uncompressed | Compression effectiveness | Compression strategy
   --------------------------+--------------------+------------+--------------+---------------------------+---------------------
   actualelapsedtime@null    | dict               |     129177 |      1032957 |                         7 | default             
   actualelapsedtime@val     | dict               |    1379797 |      4131831 |                         2 | default             
   airlineid                 | dict               |     578150 |      2065915 |                       2.7 | default             
   airtime@null              | dict               |     130011 |      1039625 |                         7 | default             
   airtime@null              | rle                |      93404 |      1019833 |                 116575.61 | default             
   airtime@val               | dict               |    1142045 |      4131831 |                      7.57 | default             
   arrdel15@null             | dict               |     129177 |      1032957 |                         7 | default             
   arrdel15@val              | dict               |     129183 |      4131831 |                     30.98 | default             
   arrdelay@null             | dict               |     129177 |      1032957 |                         7 | default             
   arrdelay@val              | dict               |    1389660 |      4131831 |                         2 | default             
   arrdelayminutes@null      | dict               |     129177 |      1032957 |                         7 | default             
   arrdelayminutes@val       | dict               |    1356034 |      4131831 |                      2.08 | default             
   arrivaldelaygroups@null   | dict               |     129177 |      1032957 |                         7 | default             
   arrivaldelaygroups@val    | p4d                |     516539 |      2065915 |                         3 | default             
   arrtime@null              | dict               |     129177 |      1032957 |                         7 | default             
   arrtime@val               | p4d                |    1652799 |      2065915 |                      0.25 | default             
   arrtimeblk                | dict               |     688870 |      9296621 |                     12.49 | default             
   cancellationcode@null     | dict               |     129516 |      1035666 |                         7 | default             
   cancellationcode@null     | rle                |      54392 |      1031646 |                 131944.62 | default             
   cancellationcode@val      | dict               |     263149 |      1032957 |                      4.12 | default             
   cancelled                 | dict               |     129183 |      4131831 |                     30.98 | default             
   carrier                   | dict               |     578150 |      2065915 |                       2.7 | default             
   carrierdelay@null         | dict               |     129516 |      1035666 |                         7 | default             
   carrierdelay@null         | flat               |    1041250 |      1041250 |                         0 | default             
   carrierdelay@null         | rle                |       4869 |      1026493 |                  202740.2 | default             
   carrierdelay@val          | dict               |     834559 |      4131831 |                     14.57 | default             
   crsarrtime                | p4d                |    1652799 |      2065915 |                      0.25 | default             
   crsdeptime                | p4d                |    1652799 |      2065915 |                      0.25 | default             
   crselapsedtime@null       | dict               |     130449 |      1043140 |                         7 | default             
   crselapsedtime@null       | rle                |       3200 |      1013388 |                 118975.75 | default             
   crselapsedtime@val        | dict               |    1182286 |      4131831 |                       2.5 | default             
   dayofmonth                | dict               |     688730 |      1032957 |                       0.5 | default             
   dayofweek                 | dict               |     393577 |      1032957 |                      1.62 | default             
   departuredelaygroups@null | dict               |     129177 |      1032957 |                         7 | default             
   departuredelaygroups@val  | p4d                |     516539 |      2065915 |                         3 | default             
   depdel15@null             | dict               |     129177 |      1032957 |                         7 | default             
   depdel15@val              | dict               |     129183 |      4131831 |                     30.98 | default             
   depdelay@null             | dict               |     129177 |      1032957 |                         7 | default             
   depdelay@val              | dict               |    1384453 |      4131831 |                      2.01 | default             
   depdelayminutes@null      | dict               |     129177 |      1032957 |                         7 | default             
   depdelayminutes@val       | dict               |    1362893 |      4131831 |                      2.06 | default             
   deptime@null              | dict               |     129177 |      1032957 |                         7 | default             
   deptime@val               | p4d                |    1652799 |      2065915 |                      0.25 | default             
   deptimeblk                | dict               |     688870 |      9296621 |                     12.49 | default             
   month                     | dict               |     247852 |      1035246 |                      3.38 | default             
   month                     | rle                |          5 |       607346 |                  121468.2 | default             
   origin                    | dict               |    1119457 |      3098873 |                      1.78 | default             
   quarter                   | rle                |          8 |      1032957 |                 136498.61 | default             
   securitydelay@null        | dict               |     129516 |      1035666 |                         7 | default             
   securitydelay@null        | flat               |    1041250 |      1041250 |                         0 | default             
   securitydelay@null        | rle                |       4869 |      1026493 |                  202740.2 | default             
   securitydelay@val         | dict               |     581893 |      4131831 |                     15.39 | default             
   tailnum@null              | dict               |     129516 |      1035666 |                         7 | default             
   tailnum@null              | rle                |      38643 |      1031646 |                 121128.68 | default             
   tailnum@val               | dict               |    1659918 |     12395495 |                     22.46 | default             
   taxiin@null               | dict               |     130011 |      1039625 |                         7 | default             
   taxiin@null               | rle                |      93404 |      1019833 |                 116575.61 | default             
   taxiin@val                | dict               |     839917 |      4131831 |                      8.49 | default             
   taxiout@null              | dict               |     130011 |      1039625 |                         7 | default             
   taxiout@null              | rle                |      84327 |      1019833 |                 116575.86 | default             
   taxiout@val               | dict               |     891539 |      4131831 |                      8.28 | default             
   totaladdgtime@null        | dict               |     129516 |      1035666 |                         7 | default             
   totaladdgtime@null        | rle                |       3308 |      1031646 |                 191894.18 | default             
   totaladdgtime@val         | dict               |     465839 |      4131831 |                     20.51 | default             
   uniquecarrier             | dict               |     578221 |      7230705 |                     11.96 | default             
   year                      | rle                |          6 |      2065915 |                 317216.08 | default             

Notes on Reading the "Ontime" Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following are some useful notes on reading the "Ontime" table shown above:

#. Higher numbers in the **Compression effectiveness** column represent better compressions. **0** represents a column that has **not been compressed**.

    ::

#. Column names are an internal representation. Names with ``@null`` and ``@val`` suffixes represent a nullable column's null (boolean) and values respectively, but are treated as one logical column.

    ::
	
#. The query lists all actual compressions for a column, so it may appear several times if the compression has changed mid-way through the loading (as with the ``carrierdelay`` column).

    ::
	
#. When your compression strategy is ``default``, the system automatically selects the best compression, including no compression at all (``flat``).

Best Practices
==============================
This section describes the best compression practices:

.. contents:: 
   :local:
   :depth: 1
   
Letting SQream Determine the Best Compression Strategy
----------------------------------------------------
In general, SQream determines the best compression strategy for most cases. If you decide to override SQream's selected compression strategies, we recommend benchmarking your query and load performance **in addition to** your storage size.

Maximizing the Advantage of Each Compression Scheme
-------------------------------------------------------
Some compression schemes perform better when data is organized in a specific way. For example, to take advantage of RLE, sorting a column may result in better performance and reduced disk-space and I/O usage.
Sorting a column partially may also be beneficial. As a rule of thumb, aim for run-lengths of more than 10 consecutive values.

Choosing Data Types that Fit Your Data
---------------------------------------
Adapting to the narrowest data type improves query performance while reducing disk space usage. However, smaller data types may compress better than larger types.

For example, SQream recommends using the smallest numeric data type that will accommodate your data. Using ``BIGINT`` for data that fits in ``INT`` or ``SMALLINT`` can use more disk space and memory for query execution. Using ``FLOAT`` to store integers will reduce compression's effectiveness significantly.