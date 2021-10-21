.. _copy_to:

**********************
COPY TO
**********************
The **COPY TO** page includes the following sections:

.. contents:: 
   :local:
   :depth: 1

Overview
===============   
The ``COPY ... TO`` statement lets you export data from a SQream database or query to a file on the filesystem. In general, the ``COPY`` statement moves data between filesystem files and SQream tables.

For more information on copying data from a file to a table, see :ref:`COPY FROM<copy_from>`.

Syntax
==========
**Comment - I'm going to replace the following syntax example with the one below it:**

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
  
.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] FOREIGN TABLE [schema_name].table_name (
           { column_def [, ...] }
       )
       [ FOREIGN DATA ] WRAPPER fdw_name
       [ OPTIONS ( option_name = option_value [, ...  ] ) ]
       ;

   schema_name ::= identifier

   table_name ::= identifier

   option_name ::= identifier
   
   option_value ::= {identifier | literal}

Elements
============
**Comment - Are the parameters in this table only relevant to CSV?**

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``[schema_name].table_name``
     - Display the name of the expored table.
   * - ``query``
     - Displays an SQL query that returns a table result or table name.
   * - ``fdw_name``
     - Displays the name of the foreign data wrapper.
   * - ``LOCATION``
     - Displays the path on the local filesystem, S3, or HDFS URI. For example, ``/tmp/foo.csv``, ``s3://my-bucket/foo.csv``, or ``hdfs://my-namenode:8020/foo.csv``. The local path must be an absolute path that SQream can access.
   * - ``HEADER``
     - The CSV file will contain a header line with the names of each column in the file. This option is allowed only when using CSV format.
   * - ``DELIMITER``
     - Specifies the character that separates fields (columns) within each row of the file. The default is a comma character (``,``).
   * - ``AWS_ID``, ``AWS_SECRET``
     - Specifies the authentication details for secured S3 buckets.


Supported Field Delimiters
------------------------------
Field delimiters can be one or more characters.

The **Supported Field Delimiters** section includes the following field delimiter examples:

.. contents:: 
   :local:
   :depth: 1
   
Printable Characters
^^^^^^^^^^^^^^^^^^^^^
Any **printable ASCII character** (or characters) can be used as a delimiter without special syntax. The default CSV field delimiter is a comma (``,``). A printable character is any ASCII character in the range 32 - 126. Literal quoting rules apply when using delimiters. For example, you must use  ``DELIMITER ''''`` to use ``'`` as a field delimiter.

For more information about literal quoting rules, see :ref:`Literal quoting rules<string_literals>`. 

Non-Printable Characters
^^^^^^^^^^^^^^^^^^^^^
A non-printable character (1 - 31, 127) can be used in its octal form. A tab can be specified by escaping it, for example ``\t``. Other non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character. For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. _capturing_rejected_rows:

Date Format
^^^^^^^^^^^^^^^^^^^^^
The date format in the output CSV is formatted as ISO 8601 (``2019-12-31 20:30:55.123``) regardless of the parsing method used.

For the supported date parsers, see the table called :ref:`Supported Date Parsers<supported_datetime_formats>` above.

Examples
===========
The **Supported Field Delimiters** section includes the following field delimiter examples:

.. contents:: 
   :local:
   :depth: 1

Exporting a Table to a CSV Without a HEADER Row
------------------------------------
The following is an example of exporting a table to a CSV without a HEADER row:

.. code-block:: psql
   
   COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = ',', HEADER = false);
   
The following is an example of the ouput of exporting a table to a CSV without a HEADER row:
 
.. code-block:: console
   
   $ head -n6 nba.csv
   Avery Bradley,Boston Celtics,0,PG,25,6-2,180,Texas,7730337
   Jae Crowder,Boston Celtics,99,SF,25,6-6,235,Marquette,6796117
   John Holland,Boston Celtics,30,SG,27,6-5,205,Boston University,\N
   R.J. Hunter,Boston Celtics,28,SG,22,6-5,185,Georgia State,1148640
   Jonas Jerebko,Boston Celtics,8,PF,29,6-10,231,\N,5000000
   Amir Johnson,Boston Celtics,90,PF,29,6-9,240,\N,12000000

Exporting a Table to a CSV With a HEADER Row
-----------------------------------------
The following is an example of exporting a table to a CSV with a HEADER row:

.. code-block:: psql
   
   COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = ',', HEADER = true);

The following is an example of the ouput of exporting a table to a CSV with a HEADER row:

.. code-block:: console
   
   $ head -n6 nba_h.csv
   Name,Team,Number,Position,Age,Height,Weight,College,Salary
   Avery Bradley,Boston Celtics,0,PG,25,6-2,180,Texas,7730337
   Jae Crowder,Boston Celtics,99,SF,25,6-6,235,Marquette,6796117
   John Holland,Boston Celtics,30,SG,27,6-5,205,Boston University,\N
   R.J. Hunter,Boston Celtics,28,SG,22,6-5,185,Georgia State,1148640
   Jonas Jerebko,Boston Celtics,8,PF,29,6-10,231,\N,5000000

Exporting a Table to a TSV With a HEADER Row
-----------------------------------------
The following is an example of exporting a table to a TSV with a HEADER row:

.. code-block:: psql

   COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = '|', HEADER = true);

The following is an example of the ouput of exporting a table to a TSV with a HEADER row:
   
.. code-block:: console
   
   $ head -n6 nba_h.tsv
   Name    Team    Number  Position        Age     Height  Weight  College Salary
   Avery Bradley   Boston Celtics  0       PG      25      6-2     180     Texas  7730337
   Jae Crowder     Boston Celtics  99      SF      25      6-6     235     Marquette       6796117
   John Holland    Boston Celtics  30      SG      27      6-5     205     Boston University       \N
   R.J. Hunter     Boston Celtics  28      SG      22      6-5     185     Georgia State   1148640
   Jonas Jerebko   Boston Celtics  8       PF      29      6-10    231     \N     5000000

Using Non-Printable ASCII Characters as a Delimiter
-------------------------------------------------------
Non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

The following examples show using non-printable ASCII characters as a delimiter.

**Example 1**

In the following example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = E'\017');   

**Example 2**

.. code-block:: psql
   
	COPY nba TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv', DELIMITER = E'\011'); -- 011 is a tab character

Exporting a Query Result to a CSV
--------------------------------------------
The following is an example of exporting a query result to a CSV:

.. code-block:: psql
   
	COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO WRAPPER csv_fdw OPTIONS (LOCATION = '/tmp/nba_export.csv');

The following is an example of the ouput of exporting a query result to a CSV:

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