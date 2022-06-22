.. _sql_feature_support:

*************************
SQL Feature Checklist
*************************


To understand which ANSI SQL and other SQL features SQream DB supports, use the tables below.

.. contents:: In this topic:
   :local:
   

Data Types and Values
=========================

Read more about :ref:`supported data types<data_types>`.

.. list-table:: Data Types and Values
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - ``BOOL``
     - Yes
     - Boolean values
   * - ``TINTINT``
     - Yes
     - Unsigned 1 byte integer (0 - 255)
   * - ``SMALLINT``
     - Yes
     - 2 byte integer (-32,768 - 32,767)
   * - ``INT``
     - Yes
     - 4 byte integer (-2,147,483,648 - 2,147,483,647)
   * - ``BIGINT``
     - Yes
     - 8 byte integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
   * - ``REAL``
     - Yes
     - 4 byte floating point
   * - ``DOUBLE``, ``FLOAT``
     - Yes
     - 8 byte floating point
   * - ``DECIMAL``, ``NUMERIC``
     - Yes
     - Fixed-point numbers.
   * - ``VARCHAR``
     - Yes
     - Variable length string - UTF-8 encoded
   * - ``DATE``
     - Yes
     - Date
   * - ``DATETIME``, ``TIMESTAMP``
     - Yes
     - Date and time
   * - ``NULL``
     - Yes
     - ``NULL`` values
   * - ``TIME``
     - No
     - Can be stored as a text string or as part of a ``DATETIME``


Contraints
===============

.. list-table:: Contraints
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Not null
     - Yes
     - ``NOT NULL``
   * - Default values
     - Yes
     - ``DEFAULT``
   * - ``AUTO INCREMENT``
     - Yes Different name
     - ``IDENTITY``


Transactions
================

SQream DB treats each statement as an auto-commit transaction. Each transaction is isolated from other transactions with serializable isolation. 

If a statement fails, the entire transaction is cancelled and rolled back. The database is unchanged.

Read more about :ref:`transactions in SQream DB<transactions>`.


Indexes
============

SQream DB has a range-index collected on all columns as part of the metadata collection process.

SQream DB does not support explicit indexing, but does support clustering keys.

Read more about :ref:`clustering keys<data_clustering>` and our :ref:`metadata system<metadata_system>`.

Schema Changes
================

.. list-table:: Schema Changes
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - ``ALTER TABLE``
     - Yes
     - :ref:`alter_table` - Add column, alter column, drop column, rename column, rename table, modify clustering keys
   * - Rename database
     - No
     - 
   * - Rename table
     - Yes
     - :ref:`rename_table`
   * - Rename column
     - Yes 
     - :ref:`rename_column`
   * - Add column
     - Yes
     - :ref:`add_column`
   * - Remove column
     - Yes
     - :ref:`drop_column`
   * - Alter column data type
     - No
     - 
   * - Add / modify clustering keys
     - Yes
     - :ref:`cluster_by`
   * - Drop clustering keys
     - Yes
     - :ref:`drop_clustering_key`
   * - Add / Remove constraints
     - No
     - 
   * - Rename schema
     - No
     - 
   * - Drop schema
     - Yes
     - :ref:`drop_schema`
   * - Alter default schema per user
     - Yes
     - :ref:`alter_default_schema`


Statements
==============

.. list-table:: Statements
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - SELECT
     - Yes
     - :ref:`select`
   * - CREATE TABLE
     - Yes
     - :ref:`create_table`
   * - CREATE FOREIGN / EXTERNAL TABLE
     - Yes
     - :ref:`create_foreign_table`
   * - DELETE
     - Yes
     - :ref:`delete_guide`
   * - INSERT
     - Yes
     - :ref:`insert`, :ref:`copy_from`
   * - TRUNCATE
     - Yes
     - :ref:`truncate`
   * - UPDATE
     - No
     -
   * - VALUES
     - Yes
     - :ref:`values`

Clauses
===========

.. list-table:: Clauses
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - ``LIMIT`` / ``TOP``
     - Yes
     -
   * - ``LIMIT`` with ``OFFSET``
     - No
     -
   * - ``WHERE``
     - Yes
     -
   * - ``HAVING``
     - Yes
     -
   * - ``OVER``
     - Yes
     -

Table Expressions
====================

.. list-table:: Table Expressions
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Tables, Views
     - Yes
     -
   * - Aliases, ``AS``
     - Yes
     -
   * - ``JOIN`` - ``INNER``, ``LEFT [ OUTER ]``, ``RIGHT [ OUTER ]``, ``CROSS``
     - Yes
     -
   * - Table expression subqueries
     - Yes
     -
   * - Scalar subqueries
     - No
     - 


Scalar Expressions
====================

Read more about :ref:`scalar_expressions`.

.. list-table:: Scalar Expressions
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Common functions
     - Yes
     - ``CURRENT_TIMESTAMP``, ``SUBSTRING``, ``TRIM``, ``EXTRACT``, etc.
   * - Comparison operators
     - Yes
     - ``<``, ``<=``, ``>``, ``>=``, ``=``, ``<>, !=``, ``IS``, ``IS NOT``
   * - Boolean operators
     - Yes
     - ``AND``, ``NOT``, ``OR``
   * - Conditional expressions
     - Yes
     - ``CASE .. WHEN``
   * - Conditional functions
     - Yes
     - ``COALESCE``
   * - Pattern matching
     - Yes
     - ``LIKE``, ``RLIKE``, ``ISPREFIXOF``, ``CHARINDEX``, ``PATINDEX``
   * - REGEX POSIX pattern matching
     - Yes
     - ``RLIKE``, ``REGEXP_COUNT``, ``REGEXP_INSTR``, ``REGEXP_SUBSTR``, 
   * - ``EXISTS``
     - No
     - 
   * - ``IN``, ``NOT IN``
     - Partial
     - Literal values only
   * - Bitwise arithmetic
     - Yes
     - ``&``, ``|``, ``XOR``, ``~``, ``>>``, ``<<``



Permissions
===============

Read more about :ref:`access_control` in SQream DB.

.. list-table:: Permissions
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Roles as users and groups
     - Yes
     - 
   * - Object default permissions
     - Yes
     - 
   * - Column / Row based permissions
     - No
     -
   * - Object ownership
     - No
     - 



Extra Functionality
======================

.. list-table:: Extra Functionality
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Information schema
     - Yes
     - :ref:`catalog_reference`
   * - Views
     - Yes
     - :ref:`create_view`
   * - Window functions
     - Yes
     - :ref:`window_functions`
   * - CTEs
     - Yes
     - :ref:`common_table_expressions`
   * - Saved queries, Saved queries with parameters
     - Yes
     - :ref:`saved_queries`
   * - Sequences
     - Yes
     - :ref:`identity`
