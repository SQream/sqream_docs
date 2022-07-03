.. _copy_to:

**********************
COPY TO
**********************
The **COPY TO** page includes the following sections:

.. contents:: 
   :local:
   :depth: 1

Overview
==========
``COPY ... TO`` is a statement that can be used to export data from a SQream database table or query to a file on the filesystem.

In general, ``COPY`` moves data between filesystem files and SQream DB tables.

.. note:: To copy data from a file to a table, see :ref:`COPY FROM<copy_from>`.

Syntax
==========
The following is the correct syntax for using the **COPY TO** statement:

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
	  
      | MAX_FILE_SIZE = '{ size_in_bytes }'
	  
      | ENFORCE_SINGLE_FILE = { true | false }


  delimiter ::= string

  record delimiter ::= string

  AWS ID ::= string

  AWS Secret ::= string

.. note:: The DELIMITER is applicable to the CSV format only.
  
.. note:: In Studio, you must write the parameters using lower case letters. Using upper case letters generates an error.

Elements
============
The following table shows the ``COPY_TO`` elements:

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
   * - ``MAX_FILE_SIZE``
     - Sets the maximum file size (bytes). Default value: 16*2^20 (16MB).
   * - ``ENFORCE_SINGLE_FILE``
     - Enforces the maximum file size (bytes). Permitted values: ``true`` - creates one file of unlimited size, ``false`` - permits creating several files together limited by the ``MAX_FILE_SIZE``. When set to ``true``, the single file size is not limited by the ``MAX_FILE_SIZE`` setting. When set to ``false``, the combined file sizes cannot exceed the ``MAX_FILE_SIZE``. Default value: ``FALSE``.

Usage Notes
===============
The **Usage Notes** describes the following:

.. contents:: 
   :local:
   :depth: 1

Supported Field Delimiters
------------------------------

Printable ASCII Characters
^^^^^^^^^^^^^^^^^^^^^
Any printable ASCII character can be used as a delimiter without special syntax. The default CSV field delimiter is a comma (``,``).

The following table shows the supported printable ASCII characters:

.. list-table:: Printable ASCII Characters
   :widths: 25
   :header-rows: 1
   
   * - Octal Notation
   * - 32-33
   * - 35-38
   * - 40-43
   * - 59-64
   * - 91-96
   * - 123-126 (ASCII)

Non-Printable ASCII Characters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following table shows the supported non-printable ASCII characters:

.. list-table:: Non-Printable ASCII Characters
   :widths: 25
   :header-rows: 1

   * - Octal Notation
   * - 1-9, 11, 12
   * - 14-31
   * - 127 (ASCII)
   
A tab can be specified by escaping it, for example ``\t``. Other non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. note:: Delimiters are only applicable to the CSV file format.

Date Format
---------------
The date format in the output CSV is formatted as ISO 8601 (``2019-12-31 20:30:55.123``), regardless of how it was parsed initially with :ref:`COPY FROM date parsers<copy_date_parsers>`.

Unsupported ASCII Field Delimiters
------------------------------
The following table shows the unsupported ASCII field delimiters:

.. list-table:: Unsupported ASCII Field Delimiters
   :widths: 25 25
   :header-rows: 1

   * - Character
     - Octal Notation
   * - ``"``
     - 42
   * - ``-``
     - 55
   * - ``.``
     - 56
   * - ``:``
     - 72
   * - ``\``
     - 134
   * - Digits ``0`` - ``9``
     - 060-070
   * - Letters ``a`` - ``z``
     - 141-172
   * - Letter ``N``
     - 116
   * - ASCII character ``10`` and ``13``
     - 012 and 015

Examples
===========

Exporting a Table to a CSV File without a HEADER Row
------------------------------------
The following is an example of exporting a table to a CSV file without a HEADER row:

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

Exporting a Table to a CSV with a HEADER Row
-----------------------------------------
The following is an example of exporting a table to a CSV file with a HEADER row:

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

Exporting a Table to TSV with a HEADER Row
-----------------------------------------
The following is an example of exporting a table to a TSV file with a HEADER row:

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

Using Non-Printable ASCII Characters as Delimiters
-------------------------------------------------------
The following is an example of using non-printable ASCII characters as delimiters:

Non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = E'\017');   

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = E'\011'); -- 011 is a tab character

Exporting the Result of a Query to CSV File
--------------------------------------------
The following is an example of exporting the result of a query to a CSV file:

.. code-block:: psql
   
	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv');

.. code-block:: console
   
   $ head -n5 nba_salaries.csv
   Atlanta Hawks,4860196
   Boston Celtics,4181504
   Brooklyn Nets,3501898
   Charlotte Hornets,5222728
   Chicago Bulls,5785558

Saving Files to an Authenticated S3 Bucket
--------------------------------------------
The following is an example of saving files to an authenticated S3 bucket:

.. code-block:: psql
   
	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = 's3://my_bucket/salaries/nba_export.csv', AWS_ID = 'my_aws_id', AWS_SECRET = 'my_aws_secret');

Saving Files to an HDFS Path
--------------------------------------------
The following is an example of saving files to an HDFS path:

.. code-block:: psql
   
   	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = 'hdfs://pp_namenode:8020/nba_export.csv');

Exporting a Table to a Parquet File
------------------------------
The following is an example of exporting a table to a Parquet file:

.. code-block:: psql
   
	COPY nba TO WRAPPER parquet_fdw OPTIONS (LOCATION = '/tmp/nba_export.parquet');

Exporting a Query to a Parquet File
--------------------------------
The following is an example of exporting a query to a Parquet file:

.. code-block:: psql

	COPY (select x,y from t where z=0) TO WRAPPER parquet_fdw OPTIONS (LOCATION = '/tmp/file.parquet');

Exporting a Table to an ORC File
------------------------------
The following is an example of exporting a table to an ORC file:

.. code-block:: psql
   
	COPY nba TO WRAPPER orc_fdw OPTIONS (LOCATION = '/tmp/nba_export.orc');

Permissions
=============
The role must have the ``SELECT`` permission on every table or schema that is referenced by the statement.