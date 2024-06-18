.. _orc:

***
ORC
***

This guide covers ingesting data from ORC files into SQream DB using :ref:`FOREIGN TABLE<foreign_tables>`. 

.. contents:: 
   :local:
   :depth: 1

Foreign Data Wrapper Prerequisites
===================================

Before proceeding, ensure the following Foreign Data Wrapper (FDW) prerequisites:

* **File Existence:** Verify that the file you are ingesting data from exists at the specified path.

* **Path Accuracy:** Confirm that all path elements are present and correctly spelled. Any inaccuracies may lead to data retrieval issues.
* **Bucket Access Permissions:** Ensure that you have the necessary access permissions to the bucket from which you are ingesting data. Lack of permissions can hinder the data retrieval process.

* **Wildcard Accuracy:** If using wildcards, double-check their spelling and configuration. Misconfigured wildcards may result in unintended data ingestion.

Prepare the files
=================

Prepare the source ORC files, with the following requirements:

.. list-table:: 
   :widths: 5 5 70 70 70 70 5 5 5 5 5
   :header-rows: 1

   
   * -   SQream DB type →
   
         ORC source
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
   * - ``string`` / ``char`` / ``text``
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

* If an ORC file has an unsupported type like ``binary``, ``list``, ``map``, and ``union``, but the data is not referenced in the table (it does not appear in the :ref:`SELECT` query), the statement will succeed. If the column is referenced, an error will be thrown to the user, explaining that the type is not supported, but the column may be ommited. This can be worked around. See more information in the examples.

.. rubric:: Footnotes

.. [#f0] Text values include ``TEXT``

.. [#f5] Boolean values are cast to 0, 1

.. [#f6] Will succeed if all values are 0, 1

.. [#f7] Will succeed if all values fit the destination type

Place ORC files where SQream DB workers can access them
=======================================================

Any worker may try to access files (unless explicitly speficied with the :ref:`workload_manager`).
It is important that every node has the same view of the storage being used - meaning, every SQream DB worker should have access to the files.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream DB servers can access the HDFS name node with the correct user-id. See our :ref:`hdfs` guide for more information.

* For S3, ensure network access to the S3 endpoint. See our :ref:`s3` guide for more information.

Figure out the table structure
==============================

Prior to loading data, you will need to write out the table structure, so that it matches the file structure.

For example, to import the data from ``nba.orc``, we will first look at the source table:

.. csv-table:: nba.orc
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

* The file is stored on S3, at ``s3://sqream-demo-data/nba.orc``.


We will make note of the file structure to create a matching ``CREATE FOREIGN TABLE`` statement.

.. code-block:: postgres
   
	CREATE FOREIGN TABLE ext_nba (
	  Name TEXT(40),
	  Team TEXT(40),
	  Number BIGINT,
	  Position TEXT(2),
	  Age BIGINT,
	  Height TEXT(4),
	  Weight BIGINT,
	  College TEXT(40),
	  Salary FLOAT
	)
	WRAPPER
	  orc_fdw
	OPTIONS
	  (LOCATION = 's3://sqream-docs/nba.orc');

.. tip:: 

   Types in SQream DB must match ORC types according to the table above.
   
   If the column type isn't supported, a possible workaround is to set it to any arbitrary type and then exclude it from subsequent queries.


Verify table contents
=====================

External tables do not verify file integrity or structure, so verify that the table definition matches up and contains the correct data.

.. code-block:: psql
   
	SELECT * FROM ext_nba LIMIT 10;
	
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

If any errors show up at this stage, verify the structure of the ORC files and match them to the external table structure you created.

Copying data into SQream DB
===========================

To load the data into SQream DB, use the :ref:`create_table_as` statement:

.. code-block:: postgres
   
	CREATE TABLE
	  nba AS
	SELECT
	  *
	FROM
	  ext_nba;

Working Around Unsupported Column Types
---------------------------------------

Suppose you only want to load some of the columns - for example, if one of the columns isn't supported.

By ommitting unsupported columns from queries that access the ``EXTERNAL TABLE``, they will never be called, and will not cause a "type mismatch" error.

For this example, assume that the ``Position`` column isn't supported because of its type.

.. code-block:: postgres

	CREATE TABLE
	  nba AS
	SELECT
	  Name,
	  Team,
	  Number,
	  NULL as Position,
	  Age,
	  Height,
	  Weight,
	  College,
	  Salary
	FROM
	  ext_nba;
   
   -- We ommitted the unsupported column `Position` from this query, and replaced it with a default ``NULL`` value, to maintain the same table structure.


Modifying data during the copy process
--------------------------------------

One of the main reasons for staging data with ``EXTERNAL TABLE`` is to examine the contents and modify them before loading them.

Assume we are unhappy with weight being in pounds, because we want to use kilograms instead. We can apply the transformation as part of the :ref:`create_table_as` statement.

Similar to the previous example, we will also set the ``Position`` column as a default ``NULL``.

.. code-block:: postgres
   
	CREATE TABLE
	  nba AS
	SELECT
	  name,
	  team,
	  number,
	  NULL as position,
	  age,
	  height,
	  (weight / 2.205) as weight,
	  college,
	  salary
	FROM
	  ext_nba
	ORDER BY
	  weight;


Further ORC loading examples
============================

:ref:`create_foreign_table` contains several configuration options. See more in :ref:`the CREATE FOREIGN TABLE parameters section<cft_parameters>`.


Loading a table from a directory of ORC files on HDFS
-----------------------------------------------------

.. code-block:: postgres

	CREATE FOREIGN TABLE ext_users (
	  id INT NOT NULL,
	  name TEXT(30) NOT NULL,
	  email TEXT(50) NOT NULL
	)
	WRAPPER
	  orc_fdw
	OPTIONS
	  (
	    LOCATION = 'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.ORC'
	  );
   
	CREATE TABLE
	  users AS
	SELECT
	  *
	FROM
	  ext_users;

Loading a table from a bucket of files on S3
--------------------------------------------

.. code-block:: postgres

	CREATE FOREIGN TABLE ext_users (
	  id INT NOT NULL,
	  name TEXT(30) NOT NULL,
	  email TEXT(50) NOT NULL
	)
	WRAPPER
	  orc_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/users/*.ORC',
	    AWS_ID = 'our_aws_id',
	    AWS_SECRET = 'our_aws_secret'
	  );


	CREATE TABLE
	  users AS
	SELECT
	  *
	FROM
	  ext_users;