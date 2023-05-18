.. _csv:

***
CSV
***

This guide covers ingesting data from CSV files into BLUE using the :ref:`copy_from` method. 


Figure out the table structure
==============================

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


Bulk load the data with COPY FROM
====================================

The CSV is a standard CSV, but with two differences from BLUE defaults:

* The record delimiter is not a Unix newline (``\n``), but a Windows newline (``\r\n``)

* The first row of the file is a header containing column names, which we'll want to skip.

.. code-block:: postgres
   
   COPY nba
      FROM 's3://sqream-demo-data/nba.csv'
      WITH RECORD DELIMITER '\r\n'
           OFFSET 2;


Repeat steps 3 and 4 for every CSV file you want to import.


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


Loading non-standard dates
----------------------------------

If files contain dates not formatted as ``ISO8601``, tell ``COPY`` how to parse the column. After parsing, the date will appear as ``ISO8601`` inside BLUE.

In this example, ``date_col1`` and ``date_col2`` in the table are non-standard. ``date_col3`` is mentioned explicitly, but can be left out. Any column that is not specified is assumed to be ``ISO8601``.

.. code-block:: postgres

   COPY table_name FROM '/path/to/files/*.csv' WITH PARSERS 'date_col1=YMD,date_col2=MDY,date_col3=default';

.. tip:: The full list of supported date formats can be found under the :ref:`Supported date formats section<copy_date_parsers>` of the :ref:`copy_from` reference.
