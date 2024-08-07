.. _parquet:

*******
Parquet
*******

Ingesting Parquet files into SQreamDB is generally useful when you want to store the data permanently and perform frequent queries on it. Ingesting the data can also make it easier to join with other tables in your database. However, if you wish to retain your data on external Parquet files instead of ingesting it into SQreamDB due to it being an open-source column-oriented data storage format, you may also execute :ref:`FOREIGN TABLE<foreign_tables>` queries.

.. contents:: 
   :local:
   :depth: 1
   
Preparing Your Parquet Files
============================

Prepare your source Parquet files according to the requirements described in the following table:

.. list-table:: 
   :widths: 40 5 20 20 20 20 5 5 5 5 10
   :header-rows: 1
   
   * -   SQreamDB Type →
         Parquet Source ↓
     - ``BOOL``
     - ``TINYINT``
     - ``SMALLINT``
     - ``INT``
     - ``BIGINT``
     - ``REAL``
     - ``DOUBLE``
     - ``TEXT`` [#f0]_
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

Your statements will succeed even if your Parquet file contains unsupported types, such as ``enum``, ``uuid``, ``time``, ``json``, ``bson``, ``lists``, ``maps``, but the data is not referenced in the table (it does not appear in the :ref:`SELECT` query). If the column containing the unsupported type is referenced, an error message is displayed explaining that the type is not supported and that the column may be ommitted. For solutions to this error message, see more information in **Managing Unsupported Column Types** example in the **Example** section.

.. rubric:: Footnotes

.. [#f0] Text values include ``TEXT``

.. [#f2] With UTF8 annotation

.. [#f3] With ``TIMESTAMP_NANOS`` or ``TIMESTAMP_MILLIS`` annotation

.. [#f4] Any microseconds will be rounded down to milliseconds.

Making Parquet Files Accessible to Workers
==========================================

To give workers access to files, every node must have the same view of the storage being used.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQreamDB servers have access to the HDFS name node with the correct user-id. For more information, see :ref:`hdfs` guide.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3` guide.

Creating a Table
================

Before loading data, you must create a table that corresponds to the file structure of the table you wish to insert.

The example in this section is based on the source nba.parquet table shown below:

.. csv-table:: nba.parquet
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used for creating a :ref:`FOREIGN TABLE<foreign_tables>` based on the nba.parquet table:

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

.. tip:: An exact match must exist between the SQreamDB and Parquet types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.parquet** file is stored on S3 at ``s3://sqream-demo-data/nba.parquet``.

Ingesting Data into SQreamDB
============================
   
Syntax
------

You can use the :ref:`create_table_as` statement to load the data into SQreamDB, as shown below:

.. code-block:: postgres
   
   CREATE TABLE nba AS
      SELECT * FROM ext_nba;

Examples
--------


.. contents:: 
   :local:
   :depth: 1

Omitting Unsupported Column Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When loading data, you can omit columns using the NULL as argument. You can use this argument to omit unsupported columns from queries that access external tables. By omitting them, these columns will not be called and will avoid generating a “type mismatch” error.

In the example below, the ``Position column`` is not supported due its type.

.. code-block:: postgres
   
   CREATE TABLE nba AS
      SELECT Name, Team, Number, NULL as Position, Age, Height, Weight, College, Salary FROM ext_nba;

Modifying Data Before Loading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the main reasons for staging data using the ``EXTERNAL TABLE`` argument is to examine and modify table contents before loading it into SQreamDB.

For example, we can replace **pounds** with **kilograms** using the ``CREATE TABLE AS`` statement.

In the example below, the ``Position column`` is set to the default ``NULL``.

.. code-block:: postgres
   
   CREATE TABLE nba AS 
      SELECT name, team, number, NULL as position, age, height, (weight / 2.205) as weight, college, salary 
              FROM ext_nba
              ORDER BY weight;

Loading a Table from a Directory of Parquet Files on HDFS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is an example of loading a table from a directory of Parquet files on HDFS:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name TEXT(30) NOT NULL, email TEXT(50) NOT NULL)  
   WRAPPER parquet_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );
   
   CREATE TABLE users AS SELECT * FROM ext_users;

Loading a Table from a Directory of Parquet Files on S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is an example of loading a table from a directory of Parquet files on S3:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name TEXT(30) NOT NULL, email TEXT(50) NOT NULL)  
   WRAPPER parquet_fdw
   OPTIONS
     ( LOCATION = 's3://pp-secret-bucket/users/*.parquet',
       AWS_ID = 'our_aws_id',
       AWS_SECRET = 'our_aws_secret'
      );
   
   CREATE TABLE users AS SELECT * FROM ext_users;

For more configuration option examples, navigate to the :ref:`create_foreign_table` page and see the **Parameters** table.

Best Practices
==============

Because external tables do not automatically verify the file integrity or structure, SQreamDB recommends manually verifying your table output when ingesting Parquet files into SQreamDB. This lets you determine if your table output is identical to your originally inserted table.

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

.. note:: If your table output has errors, verify that the structure of the Parquet files correctly corresponds to the external table structure that you created.