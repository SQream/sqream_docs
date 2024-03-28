.. _csv:

***
CSV
***

This guide covers ingesting data from CSV files into BLUE using the :ref:`copy_from` method. 

Foreign Data Wrapper Prerequisites
===================================

Before proceeding, ensure the following Foreign Data Wrapper (FDW) prerequisites:

* **File Existence:** Verify that the file you are ingesting data from exists at the specified path.

* **Path Accuracy:** Confirm that all path elements are present and correctly spelled. Any inaccuracies may lead to data retrieval issues.
* **Bucket Access Permissions:** Ensure that you have the necessary access permissions to the bucket from which you are ingesting data. Lack of permissions can hinder the data retrieval process.

* **Wildcard Accuracy:** If using wildcards, double-check their spelling and configuration. Misconfigured wildcards may result in unintended data ingestion.

Figure Out The Table Structure
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


Bulk Load The Data With COPY FROM
=================================

The CSV is a standard CSV, but with two differences from BLUE defaults:

* The record delimiter is not a Unix newline (``\n``), but a Windows newline (``\r\n``)

* The first row of the file is a header containing column names, which we'll want to skip.

.. code-block:: postgres
   
	COPY
	  nba
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    RECORD_DELIMITER = '\r\n',
	    OFFSET = 2;
	);
	
Repeat steps 3 and 4 for every CSV file you want to import.


Loading A PSV (Pipe Separated Value) File
-----------------------------------------

.. code-block:: postgres
   
	COPY
	  nba
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DELIMITER = '|'
	);


Loading A TSV (Tab Separated Value) File
----------------------------------------

.. code-block:: postgres
   
	COPY
	  nba 
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DELIMITER = '\t';
	);	

Loading A Text File With Non-Printable Delimiter
------------------------------------------------

In the file below, the separator is ``DC1``, which is represented by ASCII 17 decimal or 021 octal.

.. code-block:: postgres
   
	COPY 
	  nba 
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DELIMITER = E'\021'
	);

Loading A Text File With Multi-Character Delimiters
---------------------------------------------------

In the file below, the separator is ``'|``.

.. code-block:: postgres
   
	COPY 
	  nba 
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DELIMITER = '''|'
	);
  

Loading Files With A Header Row
-------------------------------

Use ``OFFSET`` to skip rows.

.. note:: When loading multiple files (e.g. with wildcards), this setting affects each file separately.

.. code-block:: postgres

	COPY 
	  nba 
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DELIMITER = '|',
	    OFFSET  2
	);

.. _changing_record_delimiter:

Loading Files Formatted For Windows (``\r\n``)
----------------------------------------------

.. code-block:: postgres

	COPY 
	  nba 
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DELIMITER = '|',
	    RECORD_DELIMITER = '\r\n'
	);

Loading Non-Standard Dates
--------------------------

If files contain dates not formatted as ``ISO8601``, tell ``COPY`` how to parse the column. After parsing, the date will appear as ``ISO8601`` inside BLUE.

In this example, ``date_col1`` and ``date_col2`` in the table are non-standard. ``date_col3`` is mentioned explicitly, but can be left out. Any column that is not specified is assumed to be ``ISO8601``.

.. code-block:: postgres

	COPY 
	  nba 
	FROM
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 's3://sqream-docs/nba.csv',
	    DATETIME_FORMAT = 'date_col1=YMD,date_col2=MDY,date_col3=default'
	);

.. tip:: The full list of supported date formats can be found under the :ref:`Supported date formats section<copy_date_parsers>` of the :ref:`copy_from` reference.
