.. _copy_to:

**********************
COPY TO
**********************

``COPY ... TO`` is a statement that can be used to export data from a SQream database table or query to a file on the filesystem.

In general, ``COPY`` moves data between filesystem files and SQream DB tables.

.. note:: To copy data from a file to a table, see :ref:`COPY FROM<copy_from>`.

Permissions
=============

The role must have the ``SELECT`` permission on every table or schema that is referenced by the statement.

Syntax
==========

.. code-block:: postgres

   COPY { [schema_name].table_name [ ( column_name [, ... ] ) ] | query } 
     TO [FOREIGN DATA] WRAPPER fdw_name
      
       OPTIONS
       (
          [ copy_to_option [, ...] ]
       )
       ;
       
   fdw_name ::= csw_fdw | parquet_fdw | orc_fdw
   
   schema_name ::= identifer
  
   table_name ::= identifier

   copy_to_option ::= 

      LOCATION = { filename | S3 URI | HDFS URI }   
      
      | DELIMITER = '{ delimiter }'
      
      | RECORD_DELIMITER = '{ record delimiter }'
      
      | HEADER = { true | false }
      
      | AWS_ID = '{ AWS ID }'
      
      | AWS_SECRET = '{ AWS Secret }'

  delimiter ::= string

  record delimiter ::= string

  AWS ID ::= string

  AWS Secret ::= string

Elements
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``[schema_name].table_name``
     - Name of the table to be exported
   * - ``query``
     - An SQL query that returns a table result, or a table name
   * - ``fdw_name``
     - The name of the Foreign Data Wrapper to use. Supported FDWs are ``csv_fdw``, ``orc_fdw``, or ``parquet_fdw``.
   * - ``LOCATION``
     - A path on the local filesystem, S3, or HDFS URI. For example, ``/tmp/foo.csv``, ``s3://my-bucket/foo.csv``, or ``hdfs://my-namenode:8020/foo.csv``. The local path must be an absolute path that SQream DB can access.
   * - ``HEADER``
     - The CSV file will contain a header line with the names of each column in the file. This option is allowed only when using CSV format.
   * - ``DELIMITER``
     - Specifies the character that separates fields (columns) within each row of the file. The default is a comma character (``,``).
   * - ``AWS_ID``, ``AWS_SECRET``
     - Specifies the authentication details for secured S3 buckets

Usage notes
===============

Supported field delimiters
------------------------------

Printable characters
^^^^^^^^^^^^^^^^^^^^^

Any printable ASCII character can be used as a delimiter without special syntax. The default CSV field delimiter is a comma (``,``).

A printable character is any ASCII character in the range 32 - 126.

Non-printable characters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A non-printable character (1 - 31, 127) can be used in its octal form. 

A tab can be specified by escaping it, for example ``\t``. Other non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.


Date format
---------------

The date format in the output CSV is formatted as ISO 8601 (``2019-12-31 20:30:55.123``), regardless of how it was parsed initially with :ref:`COPY FROM date parsers<copy_date_parsers>`.


Examples
===========

Export table to a CSV without HEADER
------------------------------------

.. code-block:: psql
   
   COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = ',', HEADER = false);

.. code-block:: console
   
   $ head -n6 nba.csv
   Avery Bradley,Boston Celtics,0,PG,25,6-2,180,Texas,7730337
   Jae Crowder,Boston Celtics,99,SF,25,6-6,235,Marquette,6796117
   John Holland,Boston Celtics,30,SG,27,6-5,205,Boston University,\N
   R.J. Hunter,Boston Celtics,28,SG,22,6-5,185,Georgia State,1148640
   Jonas Jerebko,Boston Celtics,8,PF,29,6-10,231,\N,5000000
   Amir Johnson,Boston Celtics,90,PF,29,6-9,240,\N,12000000

Export table to a CSV with a HEADER row
-----------------------------------------

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = ',', HEADER = true);

.. code-block:: console
   
   $ head -n6 nba_h.csv
   Name,Team,Number,Position,Age,Height,Weight,College,Salary
   Avery Bradley,Boston Celtics,0,PG,25,6-2,180,Texas,7730337
   Jae Crowder,Boston Celtics,99,SF,25,6-6,235,Marquette,6796117
   John Holland,Boston Celtics,30,SG,27,6-5,205,Boston University,\N
   R.J. Hunter,Boston Celtics,28,SG,22,6-5,185,Georgia State,1148640
   Jonas Jerebko,Boston Celtics,8,PF,29,6-10,231,\N,5000000

Export table to a TSV with a header row
-----------------------------------------

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = '|', HEADER = true);

.. code-block:: console
   
   $ head -n6 nba_h.tsv
   Name    Team    Number  Position        Age     Height  Weight  College Salary
   Avery Bradley   Boston Celtics  0       PG      25      6-2     180     Texas  7730337
   Jae Crowder     Boston Celtics  99      SF      25      6-6     235     Marquette       6796117
   John Holland    Boston Celtics  30      SG      27      6-5     205     Boston University       \N
   R.J. Hunter     Boston Celtics  28      SG      22      6-5     185     Georgia State   1148640
   Jonas Jerebko   Boston Celtics  8       PF      29      6-10    231     \N     5000000

Use non-printable ASCII characters as delimiter
-------------------------------------------------------

Non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = E'\017');   

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = E'\011'); -- 011 is a tab character

Exporting the result of a query to a CSV
--------------------------------------------

.. code-block:: psql
   
	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv');

.. code-block:: console
   
   $ head -n5 nba_salaries.csv
   Atlanta Hawks,4860196
   Boston Celtics,4181504
   Brooklyn Nets,3501898
   Charlotte Hornets,5222728
   Chicago Bulls,5785558

Saving files to an authenticated S3 bucket
--------------------------------------------

.. code-block:: psql
   
	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = 's3://my_bucket/salaries/nba_export.csv', AWS_ID = 'my_aws_id', AWS_SECRET = 'my_aws_secret');

Saving files to an HDFS path
--------------------------------------------

.. code-block:: psql
   
   	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = 'hdfs://pp_namenode:8020/nba_export.csv');


Export table to a parquet file
------------------------------

.. code-block:: psql
   
	COPY nba TO WRAPPER parquet_fdw OPTIONS (LOCATION = '/tmp/nba_export.parquet');


Export a query to a parquet file
--------------------------------

.. code-block:: psql

	COPY (select x,y from t where z=0) TO WRAPPER parquet_fdw OPTIONS (LOCATION = '/tmp/file.parquet');


Export table to a ORC file
------------------------------

.. code-block:: psql
   
	COPY nba TO WRAPPER orc_fdw OPTIONS (LOCATION = '/tmp/nba_export.orc');
