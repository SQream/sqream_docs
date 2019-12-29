.. _copy_to:

**********************
COPY TO
**********************

``COPY ... TO`` is a statement that allows writing data from a table or query to a file.

In general, ``COPY`` moves data between SQream DB tables and file-system files.

.. note:: To copy data from a file to a table, see :ref:`COPY FROM<copy_from>`.

Permissions
=============

The role must have the ``SELECT`` permission on every table or schema that is referenced by the statement.

Syntax
==========

.. code-block:: postgres

   copy_to_stmt ::= COPY ( table_ref ) TO 'filepath_spec'
        [ [ WITH ] copy_opt [ ...] ]
   ;

   table_ref ::= 
      table_reference
      | query

   table_reference ::= identifier
   
   copy_opt ::= 
      DELIMITER '{ delimiter }'
      | HEADER
      | AWS_ID '{ AWS ID }'
      | AWS_SECRET '{ AWS secret }'
   
   filepath_spec ::=
      filename
      | S3 URI
      | HDFS URI


Elements
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``query``
     - An SQL query that returns a table or a table name
   * - ``filepath_spec``
     - A path on the local filesystem, S3, or HDFS URI. For example, ``/tmp/foo.csv``, ``s3://my-bucket/foo.csv``, or ``hdfs://my-namenode:8020/foo.csv``. The local path must be an absolute path that SQream DB can access.
   * - ``HEADER``
     - The CSV file will contain a header line with the names of each column in the file. This option is allowed only when using CSV format.
   * - ``DELIMITER``
     - Specifies the character that separates fields (columns) within each row of the file. The default is a comma character (``,``).
   * - ``AWS_ID``, ``AWS_SECRET``
     - Specifies the authentication details for secured S3 buckets

Supported delimiters
=====================================================

Any printable ASCII character can be used as a delimiter without special syntax. The default CSV field delimiter is a comma (``,``).

The delimiter can be any printable ASCII character (32-127), or a non-printable character when referred to in it's octal representation.

A tab can be specified by escaping it, for example ``\t``.

Other non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.


Examples
===========

Export table to a CSV
-------------------------

.. code-block:: psql
   
   nba=> COPY nba TO '/home/rhendricks/nba.csv';  -- Standard CSV
   executed

.. code-block:: console
   
   $ head -n6 nba.csv
   Avery Bradley,Boston Celtics,0,PG,25,6-2,180,Texas,7730337
   Jae Crowder,Boston Celtics,99,SF,25,6-6,235,Marquette,6796117
   John Holland,Boston Celtics,30,SG,27,6-5,205,Boston University,\N
   R.J. Hunter,Boston Celtics,28,SG,22,6-5,185,Georgia State,1148640
   Jonas Jerebko,Boston Celtics,8,PF,29,6-10,231,\N,5000000
   Amir Johnson,Boston Celtics,90,PF,29,6-9,240,\N,12000000

Export table to a CSV with a header row
-----------------------------------------

Use ``WITH ...`` to control output options

.. code-block:: psql
   
   nba=> COPY nba TO '/home/rhendricks/nba_h.csv' WITH HEADER;  -- CSV with header
   executed

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

When combining multiple options, use ``WITH`` followed by all options, separated by a space.

.. code-block:: psql
   
   nba=> COPY nba TO '/home/rhendricks/nba_h.tsv' WITH HEADER DELIMITER '|';  -- TSV with header
   executed

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

Any printable ASCII character can be used as the delimiter without special syntax.

Tab and newline can be specified by escaping them, for example ``\t`` or ``\n`` respectively.

Other non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. code-block:: psql
   
   nba=> COPY nba TO '/home/rhendricks/nba_shiftin.txt' WITH HEADER DELIMITER E'\017';
   executed

.. code-block:: psql
   
   nba=> COPY nba TO '/home/rhendricks/nba.tsv' WITH HEADER DELIMITER E'\011'; -- 011 is a tab character
   executed

Exporting the result of a query to a CSV
--------------------------------------------

.. code-block:: psql
   
   nba=> COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) TO '/home/rhendricks/nba_salaries.csv';
   executed

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
   
   nba=> COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) 
   .>    TO 's3://my_bucket/salaries/nba_salaries.csv'
   .>    WITH AWS_ID 'my_aws_id' AWS_SECRET 'my_aws_secret';
   executed

Saving files to an HDFS path
--------------------------------------------

.. code-block:: psql
   
   nba=> COPY (SELECT "Team", AVG("Salary") FROM nba GROUP BY 1) 
   .>    TO 'hdfs://pp_namenode:8020/salaries/nba_salaries.csv';
   executed


