.. _oracle:

**********************
Migrating from Oracle
**********************

This guide covers actions required for migrating from Oracle to SQream DB with CSV files.

.. contents:: In this topic:
   :local:


1. Preparing Your Tools and Login Information
====================================================

* Migrating data from Oracle requires a username and password for your Oracle system.

* In this guide, we'll use the `Oracle Data Pump <https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump.html>`_ , specifically the `Data Pump Export utility <https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-utility.html>`_ .


2. Exporting Your Schema
===================================

Use the Data Pump Export utility to export the database schema.

The format for using the Export utility is

   ``expdp <user>/<password> DIRECTORY=<directory> DUMPFILE=<dump file> CONTENT=metadata_only NOLOGFILE``

The resulting Oracle-only schema is stored in a dump file.


Examples
------------

Dump All Tables
^^^^^^^^^^^^^^^^^^^^^^
The following shows the correct syntax for dumping all tables:

.. code-block:: console

   $ expdp rhendricks/secretpassword DIRECTORY=dpumpdir DUMPFILE=tables.dmp CONTENT=metadata_only NOLOGFILE


Dumping Specific Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following shows the correct syntax for dumping specific tables:

In this example, we specify two tables for dumping.

.. code-block:: console

   $ expdp rhendricks/secretpassword DIRECTORY=dpumpdir DUMPFILE=tables.dmp CONTENT=metadata_only TABLES=employees,jobs NOLOGFILE

3. Converting the Oracle Dump to Standard SQL
=======================================================

Oracle's Data Pump Import utility helps convert the dump from the previous step to standard SQL.

The following is the correct Import utility format:

   ``impdp <user>/<password> DIRECTORY=<directory> DUMPFILE=<dump file> SQLFILE=<sql file> TRANSFORM=SEGMENT_ATTRIBUTES:N:table PARTITION_OPTIONS=MERGE``

* ``TRANSFORM=SEGMENT_ATTRIBUTES:N:table`` excludes segment attributes (both STORAGE and TABLESPACE) from the tables

* ``PARTITON_OPTIONS=MERGE`` combines all partitions and subpartitions into one table.

Example
----------
The following shows the correct syntax for converting the Oracle dump to standard SQL:

.. code-block:: console
   
   $ impdp rhendricks/secretpassword DIRECTORY=dpumpdir DUMPFILE=tables.dmp SQLFILE=sql_export.sql TRANSFORM=SEGMENT_ATTRIBUTES:N:table PARTITION_OPTIONS=MERGE

4. Identify Database Structures
===============================================

Using the SQL file created in the previous step, write ``CREATE TABLE`` statements to match the schemas of the tables.

Removing Unsupported Attributes
-----------------------------------

Trim unsupported primary keys, indexes, constraints, and other unsupported Oracle attributes.

Matching Data Types
---------------------

Refer to the table below to match the Oracle source data type to a new SQream type:

.. list-table:: Data Types
   :widths: auto
   :header-rows: 1
   
   * - Oracle Data Type
     - Precision
     - SQream Data Type
   * - ``CHAR(n)``, ``CHARACTER(n)``
     - Any ``n``
     - ``VARCHAR(n)``
   * - ``BLOB``, ``CLOB``, ``NCLOB``, ``LONG``
     - 
     - ``TEXT``
   * - ``DATE``
     - 
     - ``DATE``
   * - ``FLOAT(p)``
     - p <= 63
     - ``REAL``
   * - ``FLOAT(p)``
     - p > 63
     - ``FLOAT``, ``DOUBLE``

   * - ``NCHAR(n)``, ``NVARCHAR2(n)``
     - Any ``n``
     - ``TEXT`` (alias of ``NVARCHAR``)

   * - ``NUMBER(p)``, ``NUMBER(p,0)``
     - p < 5
     - ``SMALLINT``

   * - ``NUMBER(p)``, `NUMBER(p,0)``
     - p < 9
     - ``INT``

   * - ``NUMBER(p)``, `NUMBER(p,0)``
     - p < 19
     - ``INT``

   * - ``NUMBER(p)``, `NUMBER(p,0)``
     - p >= 20
     - ``BIGINT``

   * - ``NUMBER(p,f)``, ``NUMBER(*,f)``
     - f > 0
     - ``FLOAT`` / ``DOUBLE``

   * - ``VARCHAR(n)``, ``VARCHAR2(n)``
     - Any ``n``
     - ``VARCHAR(n)`` or ``TEXT``
   * - ``TIMESTAMP``
     -  
     - ``DATETIME``

Read more about :ref:`supported data types in SQream DB<data_types>`.

Additional Considerations
-----------------------------
Note the following when migrating from Oracle to SQream using CSV files:

* Understand how :ref:`tables are created in SQream DB<create_table>`

* Learn how :ref:`SQream DB handles null values<null_handling>`, particularly with regards to constraints.

* Oracle roles and user management commands need to be rewritten to SQream DB's format. SQream DB supports :ref:`full role-based access control (RBAC)<access_control>` similar to Oracle.

5. Creating the Tables in SQream
======================================
After rewriting the table strucutres, you can create them in SQream.

Example
---------
The following example of creating a table in SQream is based on Oracle's ``HR.EMPLOYEES`` sample table:

.. code-block:: sql

      CREATE TABLE employees
         ( employee_id NUMBER(6)
         , first_name VARCHAR2(20)
         , last_name VARCHAR2(25)
         CONSTRAINT emp_last_name_nn NOT NULL
         , email VARCHAR2(25)
         CONSTRAINT emp_email_nn NOT NULL
         , phone_number VARCHAR2(20)
         , hire_date DATE
         CONSTRAINT emp_hire_date_nn NOT NULL
         , job_id VARCHAR2(10)
         CONSTRAINT emp_job_nn NOT NULL
         , salary NUMBER(8,2)
         , commission_pct NUMBER(2,2)
         , manager_id NUMBER(6)
         , department_id NUMBER(4)
         , CONSTRAINT emp_salary_min
         CHECK (salary > 0) 
         , CONSTRAINT emp_email_uk
         UNIQUE (email)
         ) ;
      CREATE UNIQUE INDEX emp_emp_id_pk
               ON employees (employee_id) ;
             
      ALTER TABLE employees
               ADD ( CONSTRAINT emp_emp_id_pk
         PRIMARY KEY (employee_id)
         , CONSTRAINT emp_dept_fk
         FOREIGN KEY (department_id)
         REFERENCES departments
         , CONSTRAINT emp_job_fk
         FOREIGN KEY (job_id)
         REFERENCES jobs (job_id)
         , CONSTRAINT emp_manager_fk
         FOREIGN KEY (manager_id)
         REFERENCES employees
         ) ;

This table is rewritten for SQream as follows:

.. code-block:: postgres
   
   CREATE TABLE employees
   (
     employee_id      SMALLINT NOT NULL,
     first_name       VARCHAR(20),
     last_name        VARCHAR(25) NOT NULL,
     email            VARCHAR(20) NOT NULL,
     phone_number     VARCHAR(20),
     hire_date        DATE NOT NULL,
     job_id           VARCHAR(10) NOT NULL,
     salary           FLOAT,
     commission_pct   REAL,
     manager_id       SMALLINT,
     department_id    TINYINT
   );


6. Exporting Tables to CSV Files
===============================

The following options can be used for exporting tables to CSV files:

.. contents:: 
   :local:

Using SQL*Plus to Export Data Lists
------------------------------------------

The following is a :download:`sample SQL*Plus script <to_csv.sql>` for exporting PSVs in a SQream readable format:

.. literalinclude:: to_csv.sql
    :language: sql
    :caption: Oracle SQL*Plus CSV export script
    :linenos:

Enter SQL*Plus and export tables one-by-one interactively:

.. code-block:: console
   
   $ sqlplus rhendricks/secretpassword

   @spool employees
   @spool jobs
   [...]
   EXIT

Each table is exported as a data list file (``.lst``).

Creating CSVs Using Stored Procedures
-------------------------------------------

You can use stored procedures if they have been set-up.

Examples of `stored procedures for generating CSVs <https://asktom.oracle.com/pls/apex/asktom.search?tag=automate-the-generation-of-sql-query-output-to-csv>`_` can be found in the Ask The Oracle Mentors forums.

CSV Generation Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


7. Storing CSV Files in a SQream Worker Accessible Location
=======================================================

During data load, the :ref:`copy_from` command can run on any worker (unless explicitly speficied with the :ref:`workload_manager`).
It is important that every node has the same view of the storage being used - meaning, every SQream DB worker should have access to the files.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream DB servers can access the HDFS name node with the correct user-id

* For S3, ensure network access to the S3 endpoint

8. Bulk Load CSV Files
=================================

Issue the :ref:`copy_from` commands to SQream DB to insert a table from the CSVs created.

Repeat the ``COPY FROM`` command for each table exported from Oracle.

Example
-------------
The following shows the correct syntax of bulk loading CSV files based on the ``employees`` table:

.. code-block:: postgres
   
   COPY employees FROM 'employees.lst' WITH DELIMITER '|';

9. Rewriting Oracle Queries
=====================================

SQream supports a large subset of ANSI SQL. You must refactor much of Oracle's SQL and functions that often are not ANSI SQL. 

SQream recommends the following resources:

* :ref:`sql_feature_support` - to understand SQream DB's SQL feature support.

* :ref:`sql_best_practices` - to understand best practices for SQL queries and schema design.

* :ref:`common_table_expressions` - CTEs can be used to rewrite complex queries in a compact form.

* :ref:`concurrency_and_locks` - to understand the difference between Oracle's transactions and SQream DB's concurrency.

* :ref:`identity` - SQream DB supports sequences, but no triggers for auto-increment.

* :ref:`joins` - SQream DB supports ANSI join syntax. Oracle uses the ``+`` operator which SQream DB doesn't support.

* :ref:`saved_queries` - Saved queries can be used to emulate some stored procedures.

* :ref:`subqueries` - SQream DB supports a limited set of subqueries.

* :ref:`python_functions` - SQream DB supports Python User Defined Functions which can be used to run complex operations in-line.

* :ref:`Views<create_view>` - SQream DB supports logical views, but does not support materialized views.

* :ref:`window_functions` - SQream DB supports a wide array of window functions.
