.. _create_foreign_table:

:download:`Download a PDF of this page <C:/Users/Yaniv/Desktop/Yaniv/Local Work/New_Documentation/Q4/V2_Documentation/Foreign_Data_Wrapper/PDFs/CREATE FOREIGN TABLE.pdf>`

***********************
CREATE FOREIGN TABLE
***********************
The **CREATE FOREIGN TABLE** page includes the following sections:

.. contents:: 
   :local:
   :depth: 1
   
Overview
==============

The ``CREATE FOREIGN TABLE`` statement creates a new foreign table in an existing database.

.. note:: 
   
   Starting with SQream DB v2020.2, external tables have been renamed to foreign tables, and use a more flexible foreign data wrapper concept. Upgrading to a new version of SQream DB converts existing external tables automatically. 

.. tip::

   * Data in a foreign table can change if the sources change, and frequent access to remote files may harm performance.

   * To create a regular table, see :ref:`CREATE TABLE <create_table>`
   
For more information on foreign tables, see :ref:`Foreign tables<external_tables>`.



Parameters
================	
The Parameters section describes the parameters for the following foreign data wrappers:

* :ref:`CSV foreign data wrappers<csv_params>`
* :ref:`Parquet foreign data wrappers<parquet_params>`
* :ref:`ORC foreign data wrappers<orc_params>`

.. _csv_params:
   
CSV Foreign Data Wrappers
------------------------- 
The following table shows the available parameters for **CSV** foreign data wrappers:

**Comment - Do we want the parameters in alphabetical order?**

.. csv-table::
   :widths: 3 10 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\csv_foreign_data_wrappers.csv
   
.. _supported_datetime_formats:

Loading Standard Dates
----------------------------------
CSV supports the following ``datetime`` formats:

.. list-table:: Supported Date Parsers
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
	 
The following table describes the name values:

**Comment - See "a" below. I don't see "a" in any of the pattern examples in the above table. Should we 1) remove "a" from the table below, or b) include an example with "a" in the table above?**

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Pattern
     - Description
   * - ``YYYY``
     - Represents the four-digit year format (0000 - 9999).
   * - ``MM``
     - Represents the two-digit month format (01 - 12).
   * - ``DD``
     - Represents the two-digit day of month (01 - 31).
   * - ``m``
     - Represents the shortened month format (Jan - Dec).
   * - ``a``
     - Represents the shortened day of the week format (Sun - Sat).
   * - ``hh``
     - Represents the two-digit 24-hour time format (00 - 23).
   * - ``h``
     - Represents the two-digit 12-hour time format (00 - 12).
   * - ``P``
     - Represents the uppercase AM/PM time format.
   * - ``mm``
     - Represents the two-digit minute time format (00 - 59).
   * - ``ss``
     - Represents the two-digit second format (00 - 59).
   * - ``SSS``
     - Represents the three-digit fraction millisecond format (000 - 999).

.. note:: The date patterns in the table above are different than the date parts used in the :ref:`datepart` function.

Loading Non-Standard Dates
----------------------------------
**Comment - I moved this section here from the COPY FROM page.**

If files contain dates not formatted as ``ISO8601``, use the ``COPY`` statement to parse the column. Parsing the column displays the date as ``ISO8601`` in SQream.

**Comment - It will appear "as" ISO8601, or "in" the ISO8601 format?**

``ISO8601`` is a date parser.

The following is an example of loading non-standard dates:

.. code-block:: postgres

   COPY table_name FROM WRAPPER csv_fdw OPTIONS (location = '/tmp/*.csv', datetime_format = 'DMY');
   
In the above example, ``date_col1`` and ``date_col2`` in the table are non-standard. ``date_col3`` is mentioned explicitly, but can be left out. Any column that is not specified is assumed to be ``ISO8601``.
   
For the supported date parsers, see the table called :ref:`Supported Date Parsers<supported_datetime_formats>` above.

.. _parquet_params:

Parquet Foreign Data Wrappers
------------------------- 
The following table shows the available parameters for **Parquet** foreign data wrappers:

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\parquet_foreign_data_wrappers.csv

.. _orc_params:

ORC Foreign Data Wrappers
------------------------- 
The following table shows the available parameters for **ORC** foreign data wrappers:

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\orc_foreign_data_wrappers.csv   

Permissions
=============
The role must have the ``CREATE`` permission at the schema level.