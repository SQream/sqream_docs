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
     - Supported
     - Boolean values
   * - ``TINTINT``
     - Supported
     - Unsigned 1 byte integer (0 - 255)
   * - ``SMALLINT``
     - Supported
     - 2 byte integer (-32,768 - 32,767)
   * - ``INT``
     - Supported
     - 4 byte integer (-2,147,483,648 - 2,147,483,647)
   * - ``BIGINT``
     - Supported
     - 8 byte integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
   * - ``REAL``
     - Supported
     - 4 byte floating point
   * - ``DOUBLE``, ``FLOAT``
     - Supported
     - 8 byte floating point
   * - ``DECIMAL``, ``NUMERIC``
     - Supported
     - Fixed-point numbers.
   * - ``TEXT``
     - Supported
     - Variable length string - ASCII only
   * - ``TEXT``
     - Supported
     - Variable length string - UTF-8 encoded
   * - ``DATE``
     - Supported
     - Date
   * - ``DATETIME``, ``TIMESTAMP``
     - Supported
     - Date and time
   * - ``NULL``
     - Supported
     - ``NULL`` values
   * - ``TIME``
     - Not supported
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
     - Supported
     - ``NOT NULL``
   * - Default values
     - Supported
     - ``DEFAULT``
   * - ``AUTO INCREMENT``
     - Supported - Different name
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
     - Supported
     - :ref:`alter_table` - Add column, alter column, drop column, rename column, rename table, modify clustering keys
   * - Rename database
     - Not supported
     - 
   * - Rename table
     - Supported
     - :ref:`rename_table`
   * - Rename column
     - Supported 
     - :ref:`rename_column`
   * - Add column
     - Supported
     - :ref:`add_column`
   * - Remove column
     - Supported
     - :ref:`drop_column`
   * - Alter column data type
     - Not supported
     - 
   * - Add / modify clustering keys
     - Supported
     - :ref:`cluster_by`
   * - Drop clustering keys
     - Supported
     - :ref:`drop_clustering_key`
   * - Add / Remove constraints
     - Not supported
     - 
   * - Rename schema
     - Not supported
     - 
   * - Drop schema
     - Supported
     - :ref:`drop_schema`
   * - Alter default schema per user
     - Supported
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
     - Supported
     - :ref:`select`
   * - CREATE TABLE
     - Supported
     - :ref:`create_table`
   * - CREATE FOREIGN / EXTERNAL TABLE
     - Supported
     - :ref:`create_foreign_table`
   * - DELETE
     - Supported
     - :ref:`delete_guide`
   * - INSERT
     - Supported
     - :ref:`insert`, :ref:`copy_from`
   * - TRUNCATE
     - Supported
     - :ref:`truncate`
   * - UPDATE
     - Not supported
     -
   * - VALUES
     - Supported
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
     - Supported
     -
   * - ``LIMIT`` with ``OFFSET``
     - Not supported
     -
   * - ``WHERE``
     - Supported
     -
   * - ``HAVING``
     - Supported
     -
   * - ``OVER``
     - Supported
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
     - Supported
     -
   * - Aliases, ``AS``
     - Supported
     -
   * - ``JOIN`` - ``INNER``, ``LEFT [ OUTER ]``, ``RIGHT [ OUTER ]``, ``CROSS``
     - Supported
     -
   * - Table expression subqueries
     - Supported
     -
   * - Scalar subqueries
     - Not supported
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
     - Supported
     - ``CURRENT_TIMESTAMP``, ``SUBSTRING``, ``TRIM``, ``EXTRACT``, etc.
   * - Comparison operators
     - Supported
     - ``<``, ``<=``, ``>``, ``>=``, ``=``, ``<>, !=``, ``IS``, ``IS NOT``
   * - Boolean operators
     - Supported
     - ``AND``, ``NOT``, ``OR``
   * - Conditional expressions
     - Supported
     - ``CASE .. WHEN``
   * - Conditional functions
     - Supported
     - ``COALESCE``
   * - Pattern matching
     - Supported
     - ``LIKE``, ``RLIKE``, ``ISPREFIXOF``, ``CHARINDEX``, ``PATINDEX``
   * - REGEX POSIX pattern matching
     - Supported
     - ``RLIKE``, ``REGEXP_COUNT``, ``REGEXP_INSTR``, ``REGEXP_SUBSTR``, 
   * - ``EXISTS``
     - Not supported
     - 
   * - ``IN``, ``NOT IN``
     - Partial
     - Literal values only
   * - Bitwise arithmetic
     - Supported
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
     - Supported
     - 
   * - Object default permissions
     - Supported
     - 
   * - Column / Row based permissions
     - Not supported
     -
   * - Object ownership
     - Not supported
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
     - Supported
     - :ref:`catalog_reference`
   * - Views
     - Supported
     - :ref:`create_view`
   * - Window functions
     - Supported
     - :ref:`window_functions`
   * - CTEs
     - Supported
     - :ref:`common_table_expressions`
   * - Saved queries, Saved queries with parameters
     - Supported
     - :ref:`saved_queries`
   * - Sequences
     - Supported
     - :ref:`identity`
