.. _sql_clauses:

***********
SQL Clauses
***********

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Clause
     - Description
   * - :ref:`between`
     - Simplifies range tests by returning TRUE when the input is within two boundaries
   * - :ref:`distinct`
     - Returns only unique (distinct) values from a column or a set of columns, eliminating duplicate rows in the result set
   * - :ref:`exists`
     - Tests for the existence of any rows in a subquery
   * - :ref:`group_by`
     - Groups rows that have the same values in specified columns into summary rows, like aggregating data
   * - :ref:`having`
     - Filters groups of rows created by the GROUP BY clause
   * - :ref:`in`
     - Tests if an expression is contained in a list of values
   * - :ref:`joins`
     - Combine rows from two or more tables, based on a related column between them
   * - :ref:`limit`
     - Specifies the maximum number of rows that should be returned in the result set
   * - :ref:`offset`
     - Skips a specified number of rows before returning the result set
   * - :ref:`order_by`
     - Sorts the result set of a query by one or more columns
   * - :ref:`union`
     - Combine the result sets of two or more ``SELECT`` statements, removing duplicates
   * - :ref:`where`
     - Filters records that meet a specified condition