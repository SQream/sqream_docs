.. _create_external_table:

:download:`Download a PDF of this page <C:/Users/Yaniv/Desktop/Yaniv/Local Work/New_Documentation/Q4/V2_Documentation/Foreign_Data_Wrapper/PDFs/CREATE EXTERNAL TABLE.pdf>`

***********************
CREATE EXTERNAL TABLE
***********************
The **CREATE EXTERNAL TABLE** page includes the following sections:

.. contents:: 
   :local:
   :depth: 1

Overview
==============
The ``CREATE TABLE`` command creates a new external table in an existing database.

In Release `2020.2 <https://docs.sqream.com/en/latest/releases/2020.2.html>`_ external tables were renamed **foreign tables** and use a more flexible foreign data wrapper. When creating a new external tables, use the new foreign table syntax.

Note that upgrading to a new version of SQream DB converts existing tables automatically. 

.. tip::

   Data in an external table can change if the sources change, and frequent access to remote files may harm performance. Creating a regular table may avoid issues related to external tables that change. For more information, see :ref:`CREATE TABLE <create_table>`.
   
For related information, see the following:

* `Creating foreign data wrappers <https://docs.sqream.com/en/latest/guides/features/external_data/foreign_data_wrapper.html>`_
* `Creating foreign tables <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/create_foreign_table.html>`_
* `More information about foreign tables <https://docs.sqream.com/en/latest/guides/features/external_tables.html#external-tables>`_


**Comment - The content on the Foreign Tables page has to be reviewed in light of Foreign Data Wrappers.**



Syntax
==========

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] EXTERNAL TABLE [schema_name].table_name (
           { column_def [, ...] }
       )
       USING FORMAT format_def
       WITH { external_table_option [ ...] }
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

   format_def ::= { PARQUET | ORC | CSV }
   
   external_table_option ::= {
      PATH '{ path_spec }' 
      | FIELD DELIMITER '{ field_delimiter }'
      | RECORD DELIMITER '{ record_delimiter }'
      | AWS_ID '{ AWS ID }'
      | AWS_SECRET '{ AWS SECRET }'
   }
   
   path_spec ::= { local filepath | S3 URI | HDFS URI }
   
   field_delimiter ::= delimiter_character
   
   record_delimiter ::= delimiter_character
      
   column_def ::= { column_name type_name [ default ] [ column_constraint ] }

   column_name ::= identifier
   
   column_constraint ::=
       { NOT NULL | NULL }
   
   default ::=
   
       DEFAULT default_value
       | IDENTITY [ ( start_with [ , increment_by ] ) ]

.. _cet_parameters:






Parameters
================	 
The following table shows the available parameters for **CSV** foreign data wrappers:

**Comment - We need the missing descriptions in all three of the following tables.**

**Comment - Do we want the parameters in alphabetical order?**

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\csv_foreign_data_wrappers.csv
   
.. _supported_datetime_formats:

CSV supports the following ``datetime`` formats:

* DEFAULT
* ISO8601
* ISO8601C
* DMY
* YMD
* MDY
* YYYYMMDD
* YYYY-M-D
* YYYY/M/D
* DD-mon-YYYY
* YYYY-mon-DD

**Comment - I think we should use this table instead of the list above. I took this table from the COPY FROM page.**

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

The following table shows the available parameters for **Parquet** foreign data wrappers:

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\parquet_foreign_data_wrappers.csv

The following table shows the available parameters for **ORC** foreign data wrappers:

.. csv-table::
   :widths: 3 15 2 2 2
   :file: C:\Users\Yaniv\Desktop\Yaniv\Local Work\New_Documentation\Q4\V2_Documentation\Foreign_Data_Wrapper\PDFs\orc_foreign_data_wrappers.csv   



**Comment - I want to remove this table, but it includes some parameters, such as OR REPLACE, that are not included in the other tables. I want to determine whether they are needed before removing them.**

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``OR REPLACE``
     - Create a new table, and overwrite any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check the table contents or structure, only the table name.
   * - ``schema_name``
     - The name of the schema in which to create the table.
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema.
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.
   * - ``USING FORMAT ...``
     - Specifies the format of the source files, such as ``PARQUET``, ``ORC``, or ``CSV``.
   * - ``WITH PATH ...``
     - Specifies a path or URI of the source files, such as ``/path/to/*.parquet``.
   * - ``FIELD DELIMITER``
     - Specifies the field delimiter for CSV files. Defaults to ``,``.
   * - ``RECORD DELIMITER``
     - Specifies the record delimiter for CSV files. Defaults to a newline, ``\n``
   * - ``AWS_ID``, ``AWS_SECRET``
     - Credentials for authenticated S3 access
	 
Examples
===========
For examples of creating foreign data wrappers, see the Examples section of `Foreign Data Wrappers <https://docs.sqream.com/en/latest/guides/features/external_data/foreign_data_wrapper.html#id4>`_.

**Comment - The Foreign Data Wrappers page isn't public yet, so the link above will be dead until it's published.**
	 
Permissions
=============

The role must have the ``CREATE`` permission at the database level.
