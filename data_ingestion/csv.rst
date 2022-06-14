.. _csv:

**********************
Inserting Data from a CSV File
**********************

This guide covers inserting data from CSV files into SQream DB using the :ref:`copy_from` method. 


.. contents:: In this topic:
   :local:

1. Prepare CSVs
=====================

Prepare the source CSVs, with the following requirements:

* Files should be a valid CSV. By default, SQream DB's CSV parser can handle `RFC 4180 standard CSVs <https://tools.ietf.org/html/rfc4180>`_ , but can also be modified to support non-standard CSVs (with multi-character delimiters, unquoted fields, etc).

* Files are UTF-8 or ASCII encoded

* Field delimiter is an ASCII character or characters

* Record delimiter, also known as a new line separator, is a Unix-style newline (``\n``), DOS-style newline (``\r\n``), or Mac style newline (``\r``).

* Fields are optionally enclosed by double-quotes, or mandatory quoted if they contain one of the following characters:

   * The record delimiter or field delimiter

   * A double quote character

   * A newline

* 
   If a field is quoted, any double quote that appears must be double-quoted (similar to the :ref:`string literals quoting rules<string_literals>`. For example, to encode ``What are "birds"?``, the field should appear as ``"What are ""birds""?"``.
   
   Other modes of escaping are not supported (e.g. ``1,"What are \"birds\"?"`` is not a valid way of escaping CSV values).

* ``NULL`` values can be marked in two ways in the CSV:
   
   - An explicit null marker. For example, ``col1,\N,col3``
   - An empty field delimited by the field delimiter. For example, ``col1,,col3``
   
   .. note:: If a text field is quoted but contains no content (``""``) it is considered an empty text field. It is not considered ``NULL``.


2. Place CSVs where SQream DB workers can access
=======================================================

During data load, the :ref:`copy_from` command can run on any worker (unless explicitly speficied with the :ref:`workload_manager`).
It is important that every node has the same view of the storage being used - meaning, every SQream DB worker should have access to the files.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream DB servers can access the HDFS name node with the correct user-id. See our :ref:`hdfs` guide for more information.

* For S3, ensure network access to the S3 endpoint. See our :ref:`s3` guide for more information.

3. Figure out the table structure
===============================================

Prior to loading data, you will need to write out the table structure, so that it matches the file structure.

For example, to import the data from ``nba.csv``, we will first look at the file:

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

* The file format in this case is CSV, and it is stored as an S3 object.

* The first row of the file is a header containing column names.

* The record delimiter was a DOS newline (``\r\n``).

* The file is stored on S3, at ``s3://sqream-demo-data/nba.csv``.


We will make note of the file structure to create a matching ``CREATE TABLE`` statement.

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name text,
      Team text,
      Number tinyint,
      Position text,
      Age tinyint,
      Height text,
      Weight real,
      College text,
      Salary float
    );


4. Bulk load the data with COPY FROM
====================================

The CSV is a standard CSV, but with two differences from SQream DB defaults:

* The record delimiter is not a Unix newline (``\n``), but a Windows newline (``\r\n``)

* The first row of the file is a header containing column names, which we'll want to skip.

.. code-block:: postgres
   
   COPY nba
      FROM 's3://sqream-demo-data/nba.csv'
      WITH RECORD DELIMITER '\r\n'
           OFFSET 2;


Repeat steps 3 and 4 for every CSV file you want to import.


Loading different types of CSV files
=======================================

:ref:`copy_from` contains several configuration options. See more in :ref:`the COPY FROM elements section<copy_from_config_options>`.


Loading a standard CSV file from a local filesystem
---------------------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM '/home/rhendricks/file.csv';


Loading a PSV (pipe separated value) file
-------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM '/home/rhendricks/file.psv' WITH DELIMITER '|';

Loading a TSV (tab separated value) file
-------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM '/home/rhendricks/file.tsv' WITH DELIMITER '\t';

Loading a text file with non-printable delimiter
-----------------------------------------------------

In the file below, the separator is ``DC1``, which is represented by ASCII 17 decimal or 021 octal.

.. code-block:: postgres
   
   COPY table_name FROM 'file.txt' WITH DELIMITER E'\021';

Loading a text file with multi-character delimiters
-----------------------------------------------------

In the file below, the separator is ``'|``.

.. code-block:: postgres
   
   COPY table_name FROM 'file.txt' WITH DELIMITER '''|';

Loading files with a header row
-----------------------------------

Use ``OFFSET`` to skip rows.

.. note:: When loading multiple files (e.g. with wildcards), this setting affects each file separately.

.. code-block:: postgres

   COPY  table_name FROM 'filename.psv' WITH DELIMITER '|' OFFSET  2;

.. _changing_record_delimiter:

Loading files formatted for Windows (``\r\n``)
---------------------------------------------------

.. code-block:: postgres

   COPY table_name FROM 'filename.psv' WITH DELIMITER '|' RECORD DELIMITER '\r\n';

Loading a file from a public S3 bucket
------------------------------------------

.. note:: The bucket must be publicly available and objects can be listed

.. code-block:: postgres

   COPY nba FROM 's3://sqream-demo-data/nba.csv' WITH OFFSET 2 RECORD DELIMITER '\r\n';

Loading files from an authenticated S3 bucket
---------------------------------------------------

.. code-block:: postgres

   COPY nba FROM 's3://secret-bucket/*.csv' WITH OFFSET 2 RECORD DELIMITER '\r\n' AWS_ID '12345678' AWS_SECRET 'super_secretive_secret';

.. _hdfs_copy_from_example:

Loading files from an HDFS storage
---------------------------------------------------

.. code-block:: postgres

   COPY nba FROM 'hdfs://hadoop-nn.piedpiper.com/rhendricks/*.csv' WITH OFFSET 2 RECORD DELIMITER '\r\n';


Saving rejected rows to a file
----------------------------------

See :ref:`capturing_rejected_rows` for more information about the error handling capabilities of ``COPY FROM``.

.. code-block:: postgres

   COPY  table_name FROM 'filename.psv'  WITH DELIMITER '|'
                                         ERROR_LOG  '/temp/load_error.log' -- Save error log
                                         ERROR_VERBOSITY 0; -- Only save rejected rows


Stopping the load if a certain amount of rows were rejected
------------------------------------------------------------------

.. code-block:: postgres

   COPY  table_name  FROM  'filename.csv'   WITH  delimiter  '|'  
                                            ERROR_LOG  '/temp/load_err.log' -- Save error log
                                            OFFSET 2 -- skip header row
                                            LIMIT  100 -- Only load 100 rows
                                            STOP AFTER 5 ERRORS; -- Stop the load if 5 errors reached

Load CSV files from a set of directories
------------------------------------------

Use glob patterns (wildcards) to load multiple files to one table.

.. code-block:: postgres

   COPY table_name  from  '/path/to/files/2019_08_*/*.csv';


Rearrange destination columns
---------------------------------

When the source of the files does not match the table structure, tell the ``COPY`` command what the order of columns should be

.. code-block:: postgres

   COPY table_name (fifth, first, third) FROM '/path/to/files/*.csv';

.. note:: Any column not specified will revert to its default value or ``NULL`` value if nullable

Loading non-standard dates
----------------------------------

If files contain dates not formatted as ``ISO8601``, tell ``COPY`` how to parse the column. After parsing, the date will appear as ``ISO8601`` inside SQream DB.

In this example, ``date_col1`` and ``date_col2`` in the table are non-standard. ``date_col3`` is mentioned explicitly, but can be left out. Any column that is not specified is assumed to be ``ISO8601``.

.. code-block:: postgres

   COPY table_name FROM '/path/to/files/*.csv' WITH PARSERS 'date_col1=YMD,date_col2=MDY,date_col3=default';

.. tip:: The full list of supported date formats can be found under the :ref:`Supported date formats section<copy_date_parsers>` of the :ref:`copy_from` reference.