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
     - ✓
     - Boolean values
   * - ``TINTINT``
     - ✓
     - Unsigned 1 byte integer (0 - 255)
   * - ``SMALLINT``
     - ✓
     - 2 byte integer (-32,768 - 32,767)
   * - ``INT``
     - ✓
     - 4 byte integer (-2,147,483,648 - 2,147,483,647)
   * - ``BIGINT``
     - ✓
     - 8 byte integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
   * - ``REAL``
     - ✓
     - 4 byte floating point
   * - ``DOUBLE``, ``FLOAT``
     - ✓
     - 8 byte floating point
   * - ``DECIMAL``, ``NUMERIC``
     - ✓
     - Fixed-point numbers.
   * - ``TEXT``
     - ✓
     - Variable length string - UTF-8 encoded
   * - ``DATE``
     - ✓
     - Date
   * - ``DATETIME``, ``TIMESTAMP``
     - ✓
     - Date and time
   * - ``NULL``
     - ✓
     - ``NULL`` values
   * - ``TIME``
     - ✗
     - Can be stored as a text string or as part of a ``DATETIME``


Constraints
===============

.. list-table:: Constraints
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Not null
     - ✓
     - ``NOT NULL``
   * - Default values
     - ✓
     - ``DEFAULT``
   * - ``AUTO INCREMENT``
     - ✓ Different name
     - ``IDENTITY``


Transactions
================

SQream DB treats each statement as an auto-commit transaction. Each transaction is isolated from other transactions with serializable isolation. 

If a statement fails, the entire transaction is cancelled and rolled back. The database is unchanged.



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
     - ✓
     - :ref:`alter_table` - Add column, alter column, drop column, rename column, rename table, modify clustering keys
   * - Rename database
     - ✗
     - 
   * - Rename table
     - ✓
     - :ref:`rename_table`
   * - Rename column
     - ✓ 
     - :ref:`rename_column`
   * - Add column
     - ✓
     - :ref:`add_column`
   * - Remove column
     - ✓
     - :ref:`drop_column`
   * - Alter column data type
     - ✗
     - 
   * - Add / modify clustering keys
     - ✓
     - :ref:`cluster_by`
   * - Drop clustering keys
     - ✓
     - :ref:`drop_clustering_key`
   * - Add / Remove constraints
     - ✗
     - 
   * - Rename schema
     - ✗
     - 
   * - Drop schema
     - ✓
     - :ref:`drop_schema`
   * - Alter default schema per user
     - ✓
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
     - ✓
     - :ref:`select`
   * - CREATE TABLE
     - ✓
     - :ref:`create_table`
   * - CREATE FOREIGN TABLE
     - ✓
     - :ref:`create_foreign_table`
   * - DELETE
     - ✓
     - :ref:`delete_guide`
   * - INSERT
     - ✓
     - :ref:`insert`, :ref:`copy_from`
   * - TRUNCATE
     - ✓
     - :ref:`truncate`
   * - UPDATE
     - ✓
     -
   * - VALUES
     - ✓
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
     - ✓
     -
   * - ``LIMIT`` with ``OFFSET``
     - ✗
     -
   * - ``WHERE``
     - ✓
     -
   * - ``HAVING``
     - ✓
     -
   * - ``OVER``
     - ✓
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
     - ✓
     -
   * - Aliases, ``AS``
     - ✓
     -
   * - ``JOIN`` - ``INNER``, ``LEFT [ OUTER ]``, ``RIGHT [ OUTER ]``, ``CROSS``
     - ✓
     -
   * - Table expression subqueries
     - ✓
     -
   * - Scalar subqueries
     - ✗
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
     - ✓
     - ``CURRENT_TIMESTAMP``, ``SUBSTRING``, ``TRIM``, ``EXTRACT``, etc.
   * - Comparison operators
     - ✓
     - ``<``, ``<=``, ``>``, ``>=``, ``=``, ``<>, !=``, ``IS``, ``IS NOT``
   * - Boolean operators
     - ✓
     - ``AND``, ``NOT``, ``OR``
   * - Conditional expressions
     - ✓
     - ``CASE .. WHEN``
   * - Conditional functions
     - ✓
     - ``COALESCE``
   * - Pattern matching
     - ✓
     - ``LIKE``, ``RLIKE``, ``ISPREFIXOF``, ``CHARINDEX``, ``PATINDEX``
   * - REGEX POSIX pattern matching
     - ✓
     - ``RLIKE``, ``REGEXP_COUNT``, ``REGEXP_INSTR``, ``REGEXP_SUBSTR``, 
   * - ``EXISTS``
     - ✗
     - 
   * - ``IN``, ``NOT IN``
     - Partial
     - Literal values only
   * - Bitwise arithmetic
     - ✓
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
     - ✓
     - 
   * - Object default permissions
     - ✓
     - 
   * - Column / Row based permissions
     - ✗
     -
   * - Object ownership
     - ✗
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
     - ✓
     - :ref:`catalog_reference`
   * - Views
     - ✓
     - :ref:`create_view`
   * - Window functions
     - ✓
     - :ref:`window_functions`
   * - CTEs
     - ✓
     - :ref:`common_table_expressions`
   * - Sequences
     - ✓
     - :ref:`identity`
