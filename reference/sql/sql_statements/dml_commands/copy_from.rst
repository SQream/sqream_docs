.. _copy_from:

**********************
COPY FROM
**********************

``COPY ... FROM`` is a statement that allows loading data from files on the filesystem and importing them into SQream tables.

This is the recommended way for bulk loading CSV files into SQream DB.

In general, ``COPY`` moves data between filesystem files and SQream DB tables.

.. note:: 
   * Learn how to migrate from CSV files in the :ref:`csv` guide
   * To copy data from a table to a file, see :ref:`COPY TO<copy_to>`.
   * To load Parquet or ORC files, see :ref:`CREATE FOREIGN TABLE<create_foreign_table>`

Permissions
=============

The role must have the ``INSERT`` permission to the destination table.

Syntax
==========

.. code-block:: postgres

   COPY [schema name.]table_name
     FROM WRAPPER fdw_name
     OPTIONS 
     (
       [ copy_from_option [, ...] ]
     )
   ;
  
   schema_name ::= identifer
  
   table_name ::= identifier

   copy_from_option ::= 

      LOCATION = { filename | S3 URI | HDFS URI }   
      
      | OFFSET = { offset }
      
      | LIMIT = { limit }
      
      | DELIMITER = '{ delimiter }'
      
      | RECORD_DELIMITER = '{ record delimiter }'
      
      | ERROR_LOG = '{ local filepath }'
      
      | REJECTED_DATA = '{ local filepath }'
      
      | CONTINUE_ON_ERROR = { true | false }
      
      | ERROR_COUNT = '{ error count }'
      
      | DATETIME_FORMAT = '{ parser format }'
      
      | AWS_ID = '{ AWS ID }'
      
      | AWS_SECRET = '{ AWS Secret }'

  offset ::= positive integer

  limit ::= positive integer

  delimiter ::= string

  record delimiter ::= string

  error count ::= integer

  parser_format ::= see supported parser table below

  AWS ID ::= string

  AWS Secret ::= string

.. note:: 

   Some options are applicable to CSVs only.

   These include:
   ``OFFSET``, ``LIMIT``, ``DELIMITER``, ``RECORD_DELIMITER``, ``REJECTED_DATA``, ``DATETIME_FORMAT``

.. _copy_from_config_options:

Elements
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Default value
     - Value range
     - Description
   * - ``[schema_name.]table_name``
     - None
     - 
     - Table to copy data into
   * - ``name_fdw``
     - 
     - ``csv_fdw``, ``orc_fdw``, or ``parquet_fdw``
     - The name of the Foreign Data Wrapper to use
   * - ``LOCATION``
     - None
     -
     - A path on the local filesystem, S3, or HDFS URI. For example, ``/tmp/foo.csv``, ``s3://my-bucket/foo.csv``, or ``hdfs://my-namenode:8020/foo.csv``. The local path must be an absolute path that SQream DB can access. Wildcards are premitted in this field.
   * - ``OFFSET``
     - ``1``
     - >1, but no more than the number of lines in the first file
     - The row number to start with. The first row is ``1``.
   * - ``LIMIT``
     - unlimited
     - 1 to 2147483647.
     - When specified, tells SQream DB to stop loading after the specified number of rows. Unlimited if unset.
   * - ``DELIMITER``
     - ``','``
     - Almost any ASCII character, :ref:`See field delimiters section below<field_delimiters>`
     - Specifies the field terminator - the character (or characters) that separates fields or columns within each row of the file.
   * - ``RECORD_DELIMITER``
     - ``\n`` (UNIX style newline)
     - ``\n``, ``\r\n``, ``\r``
     - Specifies the row terminator - the character that separates lines or rows, also known as a new line separator.
   * - ``ERROR_LOG``
     - No error log
     - 
     -  
         When used, the ``COPY`` process will write error information from unparsable rows to the file specified by this parameter. 
         
         * If an existing file path is specified, it will be overwritten.
         
         * Specifying the same file for ``ERROR_LOG`` and ``REJECTED_DATA`` is not allowed and will result in error.
         
         * Specifing an error log when creating a foreign table will write a new error log for every query on the foreign table.

   * - ``REJECTED_DATA``
     - Inactive
     - 
     - 
         When used, the ``COPY`` process will write the rejected record lines to this file.
         
         * If an existing file path is specified, it will be overwritten.
         
         * Specifying the same file for ``ERROR_LOG`` and ``REJECTED_DATA`` is not allowed and will result in error.
         
         * Specifing an error log when creating a foreign table will write a new error log for every query on the foreign table.

   * - ``CONTINUE_ON_ERROR``
     - ``false``
     - true, false
     - 
         Specifies if errors should be ignored or skipped. When set to ``true``, the transaction will continue despite rejected data.
         
         This parameter should be set together with ``ERROR_COUNT``
         When reading multiple files, if an entire file can't be opened it will be skipped.
   * - ``ERROR_COUNT``
     - ``unlimited``
     - 1 to 2147483647
     - 
         Specifies the threshold for the maximum number of faulty records that will be ignored.
     
         This setting must be used in conjunction with ``CONTINUE_ON_ERROR``.
   * - ``DATETIME_FORMAT``
     - ISO8601 for all columns
     - :ref:`See table below<copy_date_parsers>`
     - Allows specifying a non-default date formats for specific columns
   * - ``AWS_ID``, ``AWS_SECRET``
     - None
     - 
     - Specifies the authentication details for secured S3 buckets

.. _copy_date_parsers:

Supported date formats
=========================

.. list-table:: Supported date parsers
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Pattern
     - Examples
   * - ``ISO8601``, ``DEFAULT``
     - ``YYYY-MM-DD [hh:mm:ss[.SSS]]``
     - ``2017-12-31 11:12:13.456``, ``2018-11-02 11:05:00``, ``2019-04-04``
   * - ``ISO8601C``
     - ``YYYY-MM-DD [hh:mm:ss[:SSS]]``
     - ``2017-12-31 11:12:13:456``
   * - ``DMY``
     - ``DD/MM/YYYY [hh:mm:ss[.SSS]]``
     - ``31/12/2017 11:12:13.123``
   * - ``YMD``
     - ``YYYY/MM/DD [hh:mm:ss[.SSS]]``
     - ``2017/12/31 11:12:13.678``
   * - ``MDY``
     - ``MM/DD/YYYY [hh:mm:ss[.SSS]]``
     - ``12/31/2017 11:12:13.456``
   * - ``YYYYMMDD``
     - ``YYYYMMDD[hh[mm[ss[SSS]]]]``
     - ``20171231111213456``
   * - ``YYYY-M-D``
     - ``YYYY-M-D[ h:m[:s[.S]]]``
     - ``2017-9-10 10:7:21.1`` (optional leading zeroes)
   * - ``YYYY/M/D``
     - ``YYYY/M/D[ h:m[:s[.S]]]``
     - ``2017/9/10 10:7:21.1`` (optional leading zeroes)
   * - ``DD-mon-YYYY``
     - ``DD-mon-YYYY[ hh:mm[:ss[.SSS]]]``
     - ``31-Dec-2017 11:12:13.456``
   * - ``YYYY-mon-DD``
     - ``YYYY-mon-DD[ hh:mm[:ss[.SSS]]]``
     - ``2017-Dec-31 11:12:13.456``

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Pattern
     - Description
   * - ``YYYY``
     - four digit year representation (0000-9999)
   * - ``MM``
     - two digit month representation (01-12)
   * - ``DD``
     - two digit day of month representation (01-31)
   * - ``m``
     - short month representation (Jan-Dec)
   * - ``a``
     - short day of week representation (Sun-Sat).
   * - ``hh``
     - two digit 24 hour representation (00-23)
   * - ``h``
     - two digit 12 hour representation (00-12)
   * - ``P``
     - uppercase AM/PM representation
   * - ``mm``
     - two digit minute representation (00-59)
   * - ``ss``
     - two digit seconds representation (00-59)
   * - ``SSS``
     - 3 digits fraction representation for milliseconds (000-999)

.. note:: These date patterns are not the same as date parts used in the :ref:`datepart` function.

.. _field_delimiters:

Supported field delimiters
=====================================================

Field delimiters can be one or more characters.

Multi-character delimiters
----------------------------------

SQream DB supports multi-character field delimiters, sometimes found in non-standard files.

A multi-character delimiter can be specified. For example, ``DELIMITER '%%'``, ``DELIMITER '{~}'``, etc.

Printable characters
-----------------------

Any printable ASCII character (or characters) can be used as a delimiter without special syntax. The default CSV field delimiter is a comma (``,``).

A printable character is any ASCII character in the range 32 - 126.

:ref:`Literal quoting rules<string_literals>` apply with delimiters. For example, to use ``'`` as a field delimiter, use ``DELIMITER ''''``

Non-printable characters
----------------------------

A non-printable character (1 - 31, 127) can be used in its octal form. 

A tab can be specified by escaping it, for example ``\t``. Other non-printable characters can be specified using their octal representations, by using the ``E'\000'`` format, where ``000`` is the octal value of the character.

For example, ASCII character ``15``, known as "shift in", can be specified using ``E'\017'``.

.. _capturing_rejected_rows:

Capturing rejected rows
==========================

Prior to the column process and storage, the ``COPY`` command parses the data.
Whenever the data can’t be parsed because it is improperly formatted or doesn’t match the data structure, the entire record (or row) will be rejected. 

.. image:: /_static/images/copy_from_rejected_rows.png


#. When ``ERROR_LOG`` is not used, the ``COPY`` command will stop and roll back the transaction upon the first error.

#. When ``ERROR_LOG`` is set and ``ERROR_VERBOSITY`` is set to ``1`` (default), all errors and rejected rows are saved to the file path specified.

#. When ``ERROR_LOG`` is set and ``ERROR_VERBOSITY`` is set to ``0``, rejected rows are saved to the file path specified, but errors are not logged. This is useful for replaying the file later.

CSV support
================

By default, SQream DB's CSV parser can handle `RFC 4180 standard CSVs <https://tools.ietf.org/html/rfc4180>`_ , but can also be modified to support non-standard CSVs (with multi-character delimiters, unquoted fields, etc).

All CSV files shoudl be prepared according to these recommendations:

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

Null markers
---------------

``NULL`` values can be marked in two ways in the CSV:

* An explicit null marker. For example, ``col1,\N,col3``
* An empty field delimited by the field delimiter. For example, ``col1,,col3``

.. note:: If a text field is quoted but contains no content (``""``) it is considered an empty text field. It is not considered ``NULL``.

Examples
===========

Loading a standard CSV file
------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.csv');


Skipping faulty rows
------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.csv', continue_on_error = true);


Skipping at most 100 faulty rows
-----------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.csv', continue_on_error = true, error_count = 100);


Loading a PSV (pipe separated value) file
-------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.psv', delimiter = '|');

Loading a TSV (tab separated value) file
-------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.tsv', delimiter = '\t');
   

Loading a ORC file
-------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER orc_fdw OPTIONS (location = '/tmp/file.orc');


Loading a Parquet file
-------------------------------------------

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER parquet_fdw OPTIONS (location = '/tmp/file.parquet');


Loading a text file with non-printable delimiter
-----------------------------------------------------

In the file below, the separator is ``DC1``, which is represented by ASCII 17 decimal or 021 octal.

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER psv_fdw OPTIONS (location = '/tmp/file.txt', delimiter = E'\021');   

Loading a text file with multi-character delimiters
-----------------------------------------------------

In the file below, the separator is ``^|``.

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER psv_fdw OPTIONS (location = '/tmp/file.txt', delimiter = '^|');   

In the file below, the separator is ``'|``. The quote character has to be repeated, as per the :ref:`literal quoting rules<string_literals>`.

.. code-block:: postgres
   
   COPY table_name FROM WRAPPER psv_fdw OPTIONS (location = '/tmp/file.txt', delimiter = ''''|');
   

Loading files with a header row
-----------------------------------

Use ``OFFSET`` to skip rows.

.. note:: When loading multiple files (e.g. with wildcards), this setting affects each file separately.

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.psv', delimiter = '|', offset = 2);      

Loading files formatted for Windows (``\r\n``)
---------------------------------------------------

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.psv', delimiter = '\r\n');         

Loading a file from a public S3 bucket
------------------------------------------

.. note:: The bucket must be publicly available and objects can be listed

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = 's3://sqream-demo-data/file.csv', delimiter = '\r\n', offset = 2);         

Loading files from an authenticated S3 bucket
---------------------------------------------------

.. code-block:: postgres

   COPY table_name FROM WRAPPER psv_fdw OPTIONS (location = 's3://secret-bucket/*.csv', DELIMITER = '\r\n', OFFSET = 2, AWS_ID = '12345678', AWS_SECRET = 'super_secretive_secret');
   
Saving rejected rows to a file
----------------------------------

.. note:: When loading multiple files (e.g. with wildcards), this error threshold is for the entire transaction.

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.csv', 
												                        ,continue_on_error  = true 
                                                ,error_log  = '/temp/load_error.log'
                                                );         

.. code-block:: postgres

    COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/file.psv'
												                         ,delimiter '|'
                                                 ,error_log = '/temp/load_error.log' -- Save error log
                                                 ,rejected_data = '/temp/load_rejected.log' -- Only save rejected rows
                                                 ,limit = 100 -- Only load 100 rows
                                                 ,error_count = 5 -- Stop the load if 5 errors reached
                                                 );         


Load CSV files from a set of directories
------------------------------------------

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/2019_08_*/*.csv');

Rearrange destination columns
---------------------------------

When the source of the files does not match the table structure, tell the ``COPY`` command what the order of columns should be

.. code-block:: postgres

   COPY table_name (fifth, first, third) FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/*.csv');

.. note:: Any column not specified will revert to its default value or ``NULL`` value if nullable

Loading non-standard dates
----------------------------------

If files contain dates not formatted as ``ISO8601``, tell ``COPY`` how to parse the column. After parsing, the date will appear as ``ISO8601`` inside SQream DB.

These are called date parsers. You can find the supported dates in the :ref:`'Supported date parsers' table<copy_date_parsers>` above

In this example, ``date_col1`` and ``date_col2`` in the table are non-standard. ``date_col3`` is mentioned explicitly, but can be left out. Any column that is not specified is assumed to be ``ISO8601``.

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/*.csv', datetime_format = 'DMY');
      

