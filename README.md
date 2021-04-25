.. _2021.2:

**************************
What's new in 2021.2
**************************


Performance Enhancements
=========================
* Major feature release targeted for all on-premises customers.
* Includes basic Cloud functionality.

New Features
=========================

SQream DB on Cloud
---------------------------
SQream now supports running SQream DB on AWS, GCP, and Azure.

Numeric Data Types
---------------------------
SQream now supports ``numeric(p, s)`` numeric data types where ``p`` is the total number of digits, (``38`` maximum), and ``s`` is the total number of decimal digits.
The following example shows how to use numeric data types:

The following example shows how to use numeric data types:
   ```
   $ create or replace table t(x numeric(20, 10), y numeric(38, 38));
   $ insert into t values(1234567890.1234567890, 0.123245678901234567890123456789012345678);
   $ select x + y from t;
   ```


The numeric data type feature supports the following operations:

* All join types.
* All aggregation types.
* Scalar functions (except for certain trigonometric and logarithmic functions).

***Question: Should this bullet be included in Known Issues and Limitations below?***

* Does not support Numeric Literal operations and known issues.

* Supports the following types:

   * All join types
   * All aggregation types
   * Scalar functions **(waiting for the list of limitations)**
   
Text Data Types
---------------------------

SQream now supports the following:

* TEXT data types for all operations.
* All VARCHAR functionality is supported for TEXT.
**Note:** VARCHAR should not be used in new projects except for concrete reasons. ***Comment: can you give me an example of a concrete reason?***
* The following TEXT data type enhancements (introduced in Release Notes version 2020.3.1):
 * Support text columns in queries with multiple distinct aggregates.
 * Text literal support for all functions.
 * Use LoopJoin instead of CrossJoin for join on Text keys.
    

Supports Partial Sub-Queries
---------------------------
See [currently supported functionality](https://sqream.atlassian.net/wiki/spaces/RF/pages/1433894919/Sub-Queries+support+and+limitations+in+SQream+DB+v2021.1).

Literal Arguments
---------------------------
SQream now supports literal arguments in all cases where column arguments are supported for a certain function. Literal arguments are only supported if the literal value is the same TYPE as the column, as shown in the following example:

```     
$ power(num1,num2)
$ exp(num)
$ isprefixof(string1,string2)
$ left(text, num)
```

Simple Scalar SQL UDFs
---------------------------
See [supported syntax and usage](https://sqream.atlassian.net/wiki/spaces/RF/pages/1433731135/Simple+Scalar+SQL+UDF+s).

Logging Enhancements
---------------------------
SQream now supports log information for the following events:

  * Compilation start time.
  * The first metadata callback in the compiler (if relevant).
  * The last metadata callback in the compiler (if relevant).
  * When it **(the compilation?)** started attempting to get locks
  * When queries prevent each other from running simultaneously.
  * When a statement enters the queue.
  * When a statement exits the queue.
  * When a client has connected to this a current instance of SQreamd (if it reconnects).
  * When a compilation starts executing.
  
Presented License Information Improvements
---------------------------
SQream has improved information related to data size limitations, expiration dates, and license types to be shown by the new UF. **Comment: what does UF stand for?**

Running ``get_license_info()`` returns the license information output in the following order:

* Compressed data size (GB)
* Uncompressed data size(GB)
* Compress type
* Data size limit(GB)
* Expiration date
* is date expired(0/1)
* is size exceeded(0/1)
* data_size_left(GB)

The following is an example of license information output:

.. code-block:: none
      
   $ 10,100,compressed,20,2045-03-18,0,0,10


Optimized Foreign Data Wrapper Export
-------------------------

SQream now parallels the **WriteToFile** chunk producer code to enhance performance.

The following is an example of the correct syntax when exporting foreign data wrappers:

.. code-block:: none
      
   $ COPY table_name TO fdw_name OPTIONS(max_file_size=size_in_bytes,enforce_single_file={TRUE|FALSE});
   
The following apply to the above syntax example:

* Both parameters are optional.
* The ``max_file_size`` parameter is specified in bytes and can be any positive value. The default value is ``16*2^20`` (16MB).
* Setting the ``enforce_single_file`` value to **TRUE** creates only one file. The file size is not limited by the ``max_file_size`` parameter, and its default value is **FALSE**.




Main Implemented Stories
================================
The following main stories have been implemented:

* Productize SKT inspection items and port them to the main product line
* SQreamDB on AWS
* SQreamDB on GCP
* SQreamDB on Azure
* Cloud IO optimization
* Microstrategy Support
* Subqueries MVP for SKT
* Licensing system MVP
* Text MVP
* Numeric MVP
* Set maxResultsChunkMB to 200MB
* Support a new kind of string literals which supports backslash-style escaping
* Foreign data wrappers export optimization
* Allow truncation of Numeric values on ingestion from ORC, CSV
* Additional catalog UF that accept SQL valid patterns and escape characters
* Create a basic random data FDW for non-text types
* Improve the internal errors message
* Simple Scalar SQL UDFs
* Support stdin as a file input for sqream sql
* SQream can always parse its own logs as CSVs.
* Log locks in system - sqreamd





Known Issues and Limitations
================================
* Production core dump from stability test
* Performance degradation - joins - outer_join1.sql
* Performance degradation - south_africa-sa4.sql
* Performance degradation - groupby - groupby_int_func_nvarchar40.sql





Bug Fixes
================================
* Copying content from a CSV to a TEXT column without closing quotations crashes sqreamd.
* Running the insert into command on SKT inspection queries generates an incorrect error. The correct error is Function call not supported. The incorrect error is Unsupported insert. The incorrect error is generated only on tables with more than one column.
* Running the insert into command from table_does_not_exist generates an incorrect error.
* When running SKT OGG hql, inserting * changed one column instead of all columns.
* Running two queries with expected identical results generated different results.
* Running hql’s with encode functions caused internal runtime errors.
* A compile error occurred when creating decimal data type tables. 
* Running rank in window function returns incorrect values.
* Memory smear returns incorrect results in a decimal data column.
* Inserting data saved with the double data type into the new decimal data type column causes incorrect results.
* Running the STDDEV_SAMP, STDDEV_POP, and STDEV functions resulted in Cannot take square root of a negative number error.
* Running the select table_name,row_count from sqream_catalog.tables order by row_count limit 5 query generates an internal runtime error.
* Using wildcards, such as *.x.y, produces no search results.
* Using the round (x,y) function in the where clause returns in a compiler error.
* Star not supported. ***Need clarification.***
* Window function query returns incorrect results.
* Running the window function **minimum/maximum/count** returns incorrect results.
* Running the window function **minimum/maximum/count** on a **null** value returns incorrect results.
* Running **charindex** returns different results for columns and literals.
* Running **log(x, y)** on more than one argument returns an incorrect error message.
* Running OGG encryption functions loaded as UDF to a column returns memory errors.
* **internal runtime error** type has no fixed size when running maximum on Text on develop (cisco poc). **(need clarification)**
* avg(len(xnvarchar70)) sum overflow.  **(need clarification)**
* The minimum and maximum on TEXT can be 15 times slower than **varchar**.
* **regexp_instr** returns an empty regular expression.
* Schemas with external tables can be dropped.

Naming Changes
================================
No relevant naming changes were made.

Deprecated Features
================================
No features were depecrated.

Version Acceptance Criteria
================================
See `Test Plan <https://docs.google.com/spreadsheets/d/1yZFf1R4ncCe3_fJii9mhrVCOahH2d3Nv_H_J5yKosFo/edit#gid=0>`_.
Functional Regression - pass
Stability Test - pass


Upgrading to v2021.2
========================

Versions are available for IBM POWER9, RedHat (CentOS) 7, Ubuntu 18.04, and other OSs via Docker.

Contact your account manager to get the latest release of SQream DB.
