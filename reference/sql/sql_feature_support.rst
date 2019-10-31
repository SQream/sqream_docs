.. _sql_feature_support:

*************************
SQL Feature Support
*************************


Even though SQL is standardized in various ANSI documents, no DBMS implements the entire standard.
Some features have no implementation at all.

To understand which SQL features SQream DB supports, use the tables below.

.. contents:: In this topic:
   :local:
   

Data types and values
=========================

.. list-table:: Value
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
     - Planned
     - Fixed-point numbers. Use ``DOUBLE`` instead
   * - ``VARCHAR``
     - ✓
     - Variable length string - ASCII only
   * - ``NVARCHAR``
     - ✓
     - Variable length string - UTF-8 encoded
   * - ``TEXT``
     - Planned
     - Use ``VARCHAR``, ``NVARCHAR``
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


Contraints
===============

.. list-table:: Contraints
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

SQream DB does not support explicit indexing.


Schema changes
================

.. list-table:: Schema changes
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - ``ALTER TABLE``
     - ✓
     - Add column, alter column, drop column, rename column, rename table
   * - Rename database
     - ✗
     - 
   * - Rename table
     - ✓
     - 
   * - Rename column
     - ✓ 
     - 
   * - Add column
     - ✓
     - 
   * - Remove column
     - ✓
     - 
   * - Add / Remove constraints
     - ✗
     - 
   * - Rename schema
     - ✗
     - 
   * - Drop schema
     - ✓
     - 
   * - Alter default schema per user
     - ✓
     - 


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
     -
   * - CREATE TABLE
     - ✓
     -
   * - DELETE
     - ✓
     -
   * - INSERT
     - ✓
     -
   * - TRUNCATE
     - ✓
     -
   * - UPDATE
     - ✗
     -
   * - VALUES
     - ✓
     -

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

Table expressions
====================

.. list-table:: Table expressions
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
   * - Subqueries as table expressions
     - ✓
     -
   * - Subqueries (correlated)
     - ✗
     - 


Scalar expressions
====================

.. list-table:: Scalar expressions
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
   * - Bitwise arithemtic
     - ✓
     - ``&``, ``|``, ``XOR``, ``~``, ``>>``, ``<<``



Permissions
===============

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



Extra functionality
======================

.. list-table:: Extra functionality
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Information schema
     - ✓
     - ``SQream Catalog``
   * - Views
     - ✓
     - 
   * - Window functions
     - ✓
     -
   * - CTEs
     - ✓
     -
   * - Saved queries, Saved queries with parameters
     - ✓
     -
   * - Sequences
     - ✓
     -