.. _index:

*************************
SQream DB Documentation
*************************

For SQream version 2021.2.

.. only:: html

   .. tip::
      Want to read this offline?
      `Download the documentation as a single PDF <https://docs.sqream.com/_/downloads/en/latest/pdf/>`_ .

.. only:: pdf or latex
   
   .. tip:: This documentation is available online at https://docs.sqream.com/

SQream DB is a columnar analytic SQL database management system. SQream DB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements. Even a :ref:`basic SQream DB machine<hardware_guide>` can support tens to hundreds of terabytes of data. SQream DB easily plugs in to third-party tools like :ref:`Tableau<connect_to_tableau>` comes with standard SQL client drivers, including :ref:`JDBC<java_jdbc>`, :ref:`ODBC<odbc>`, and :ref:`Python DB-API<pysqream>`.

+----------------------------------+--------------+---------------------------+--------------+
| **Getting Started**                             | **Ingesting Data**                       |
+==================================+==============+===========================+==============+
| Topic                            | Description  | Topic                     | Description  |
+----------------------------------+--------------+---------------------------+--------------+
| Preparing your machine           | Description  | From CSV files            | Description  |
+----------------------------------+--------------+---------------------------+--------------+
| Executing statements             | Description  | From Avro files           | Description  |
+----------------------------------+--------------+---------------------------+--------------+
| Performing basic operations      | Description  | From Parquet files        | Description  |
+----------------------------------+--------------+---------------------------+--------------+
| Hardware guide                   | Description  | From ORC files            | Description  |
+----------------------------------+--------------+---------------------------+--------------+
| **Installation Guides**          |              | From Oracle               |              |
+----------------------------------+--------------+---------------------------+--------------+
| Installing and launching SQream  | Description  | **Connecting to SQream**  |              |
+----------------------------------+--------------+---------------------------+--------------+
| Installing Studio your machine   | Description  | Client platforms          | Description  |
+----------------------------------+--------------+---------------------------+--------------+
|                                  |              | Client drivers            | Description  |
+----------------------------------+--------------+---------------------------+--------------+




Getting Started
===============
Getting started refers to the following:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Topic
     - Description
   * - Preparing your machine
     - Description
   * - Executing statements
     - Description
   * - Performing basic operations
     - Description
   * - Hardware guide
     - Description
	 
Installation Guides
===============
The installation guides section include the following information:

.. list-table::
   :widths: 15 75
   :header-rows: 1 

   * - Topic
     - Description   
   * - Installing and launching SQream
     - Description
   * - Installing Studio your machine
     - Description

.. hlist::
   :columns: 5
		
   * Getting Started:

   .. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Role Type
     - Description
   * - Groups
     - Roles with no users.
   * - Enabled users
     - Users with log-in permissions and a password.
   * - Disabled users
     - Users with log-in permissions and with a disabled password. An admin may disable a user's password permissions to temporary disable access to the system.
   

.. hlist::
   :columns: 5

   * Getting Started:

     * Preparing your machine
     * Executing statements
     * Performing basic operations
     * Hardware guide

   Installation guides:

   * Installing and launching SQream
   * Installing Studio

   Ingesting data:

   * From CSV files
   * From Avro files
   * From Parquet files
   * From ORC files
   * From Oracle

   Connecting to SQream:

   * Client platforms
   * Client drivers

   External storage platforms:

   * Inserting data using Amazon S3 (make sure that this title is accurate)
   * Using SQream in an HDFS environment
   * Mounting an NFS shared drive (check this one)

   Loading and unloading data:

   * Loading data:

     * Overview of loading data
     * Alternatives to loading data (foreign tables)
     * Supported data types
     * Ingesting data from external sources
     * Inserting data from external tables
     * Ingesting data from third party client platforms
     * Using the **COPY FROM** statement
     * Importing data using Studio
     * Loading data using Amazon S3

   * Unloading data:

     * Overview of unloading data
     * Using the **COPY TO** statement

   Feature guides:

   * Query Healer
   * Automatic schema Identification
   * Compression
   * Python UDF (User-Defined Functions)
   * Workload Manager
   * Transactions
   * Concurrency and locks
   * Concurrency and scaling in SQream DB

   Operational guides:

   * Access control
   * Creating or cloning storage clusters
   * Foreign tables
   * Deleting data
   * Exporting data
   * Logging
   * Monitoring query performance
   * Security
   * Saved queries
   * Seeing system objects as DDL
   * Optimization and best practices

   SQream Accelerated Studio 5.4.3:

   * Getting started with SQream Acceleration Studio 5.4.3
   * Monitoring workers and services from the dashboard
   * Executing statements and running queries from the Editor
   * Viewing logs
   * Creating, assigning, and managing roles and permissions
   * Configuring Your instance of SQream

   System architecture:

   * Internals and architecture
   * Filesystem and usage

   Configuring SQream:

   * Configuration methods
   * Configuration flags

   Reference guides:

   * SQL syntax, statements, and functions
   * Catalog reference guide
   * Command Line programs
   * SQL feature checklist
   * Python API reference guide

   Data type guides:

   * Converting and casting
   * Supported data types
   * Supported casts

   Release notes:

   * 2022.1
   * 2021.2
   * 2021.1
   * 2020.3
   * 2020.2
   * 2020.1

   Troubleshooting:

   * Remedying slow queries
   * Resolving common issues
   * Examining logs
   * Identifying configuration issues
   * Lock related issues
   * SAS Viya related issues
   * Tableau related issues
   * Solving “Code 126” ODBC errors
   * Log related issues
   * Node.js related issues
   * Core dumping related issues
   * SQream SQL installation related issues
   * Gathering information for SQream support

   Glossary




.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://sqream.atlassian.net/servicedesk/>`_ for additional support.


.. rubric:: Looking for older versions?

This version of the documentation is for SQream DB Version 2021.2.

If you're looking for an older version of the documentation, versions 1.10 through 2019.2.1 are available at http://previous.sqream.com .

.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   getting_started/index
   installation_guides/index
   data_ingestion/index
   connecting_to_sqream/index
   loading_and_unloading_data/index
   feature_guides/index
   operational_guides/index
   sqream_studio_5.4.3/index
   architecture/index
   configuration_guides/index
   reference/index
   data_type_guides/index
   releases/index
   troubleshooting/index
   glossary

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
