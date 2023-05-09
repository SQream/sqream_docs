.. _parquet:

**********************
Parquet
**********************

.. contents:: 
   :local:
   :depth: 1

Overview
===================
BLUE supports ingesting data into BLUE from Parquet files. However, because it is an open-source column-oriented data storage format, you may want to retain your data on foreign Parquet files instead of ingesting it into BLUE. BLUE supports executing queries on foreign Parquet files.

Preparing Your Parquet Files
=====================
Prepare your source Parquet files according to the requirements described in the following table:

.. list-table:: 
   :widths: 40 5 20 20 20 20 5 5 5 5 10
   :header-rows: 1
   
   * -   BLUE Type →
   
          ::

         Parquet Source ↓
     - ``BOOL``

          ::

     - ``TINYINT``

          ::

     - ``SMALLINT``

          ::

     - ``INT``

          ::

     - ``BIGINT``

          ::

     - ``REAL``

          ::

     - ``DOUBLE``

          ::

     - ``TEXT`` [#f0]_

          ::

     - ``DATE``

          ::

     - ``DATETIME``

          ::

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
   * - ``BYTE_ARRAY`` / ``FIXED_LEN_BYTE_ARRAY`` [#f2]_
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

* Your statements will succeed even if your Parquet file contains an unsupported type, such as ``enum``, ``uuid``, ``time``, ``json``, ``bson``, ``lists``, ``maps``, but the data is not referenced in the table (it does not appear in the :ref:`SELECT` query). If the column containing the unsupported type is referenced, an error message is displayed explaining that the type is not supported and that the column may be ommitted. For solutions to this error message, see more information in **Managing Unsupported Column Types** example in the **Example** section.

.. rubric:: Footnotes

.. [#f0] Text values include ``TEXT``

.. [#f2] With UTF8 annotation

.. [#f3] With ``TIMESTAMP_NANOS`` or ``TIMESTAMP_MILLIS`` annotation

.. [#f4] Any microseconds will be rounded down to milliseconds.



Creating a Table
===============================================
Before loading data, you must build the CREATE TABLE to correspond with the file structure of the inserted table.

The example in this section is based on the source nba.parquet table shown below:

.. csv-table:: nba.parquet
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to create the ``CREATE FOREIGN TABLE`` statement based on the nba.parquet table:

.. code-block:: postgres
   
   CREATE FOREIGN TABLE ext_nba
   (
        Name       TEXT(40),
        Team       TEXT(40),
        Number     BIGINT,
        Position   TEXT(2),
        Age        BIGINT,
        Height     TEXT(4),
        Weight     BIGINT,
        College    TEXT(40),
        Salary     FLOAT
    )
    WRAPPER parquet_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.parquet'
    );

.. tip:: An exact match must exist between the BLUE and Parquet types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.parquet** file is stored on S3 at ``s3://sqream-demo-data/nba.parquet``.


Best Practices
============
Because foreign tables do not automatically verify the file integrity or structure, BLUE recommends manually verifying your table output when ingesting Parquet files into BLUE. This lets you determine if your table output is identical to your originally inserted table.

The following is an example of the output based on the **nba.parquet** table:

.. code-block:: psql
   
   t=> SELECT * FROM ext_nba LIMIT 10;
   Name          | Team           | Number | Position | Age | Height | Weight | College           | Salary  
   --------------+----------------+--------+----------+-----+--------+--------+-------------------+---------
   Avery Bradley | Boston Celtics |      0 | PG       |  25 | 6-2    |    180 | Texas             |  7730337
   Jae Crowder   | Boston Celtics |     99 | SF       |  25 | 6-6    |    235 | Marquette         |  6796117
   John Holland  | Boston Celtics |     30 | SG       |  27 | 6-5    |    205 | Boston University |         
   R.J. Hunter   | Boston Celtics |     28 | SG       |  22 | 6-5    |    185 | Georgia State     |  1148640
   Jonas Jerebko | Boston Celtics |      8 | PF       |  29 | 6-10   |    231 |                   |  5000000
   Amir Johnson  | Boston Celtics |     90 | PF       |  29 | 6-9    |    240 |                   | 12000000
   Jordan Mickey | Boston Celtics |     55 | PF       |  21 | 6-8    |    235 | LSU               |  1170960
   Kelly Olynyk  | Boston Celtics |     41 | C        |  25 | 7-0    |    238 | Gonzaga           |  2165160
   Terry Rozier  | Boston Celtics |     12 | PG       |  22 | 6-2    |    190 | Louisville        |  1824360
   Marcus Smart  | Boston Celtics |     36 | PG       |  22 | 6-4    |    220 | Oklahoma State    |  3431040

.. note:: If your table output has errors, verify that the structure of the Parquet files correctly corresponds to the foreign table structure that you created.