.. _sql_functions:

****************
SQL Functions
****************

SQream DB supports commands from ANSI SQL.

Summary of functions
=======================

Scalar functions
-------------------

Bitwise operations
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`bitwise_and`
     - Bitwise AND
   * - :ref:`bitwise_not`
     - Bitwise NOT
   * - :ref:`bitwise_or`
     - Bitwise OR
   * - :ref:`bitwise_shift_left`
     - Bitwise shift left
   * - :ref:`bitwise_shift_right`
     - Bitwise shift right
   * - :ref:`bitwise_xor`
     - Bitwise XOR

Conditionals
^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`between`
     - Value is in [ or not within ] the range
   * - :ref:`case`
     - Test a conditional expression, and depending on the result, evaluate additional expressions.
   * - :ref:`coalesce`
     - Evaluate first non-NULL expression
   * - :ref:`in`
     - Value is in [ or not within ] a set of values
   * - :ref:`isnull`
     - Alias for :ref:`coalesce` with two expressions
   * - :ref:`is_ascii`
     - Test an ``NVARCHAR`` for ASCII-only characters
   * - :ref:`is_null`
     - Check for ``NULL`` [ or non ``NULL`` ] values

Conversion
^^^^^^^^^^^^

Date and time
^^^^^^^^^^^^^^^^

Numeric
^^^^^^^^^^^


Aggregate functions
---------------------

Window functions
-------------------

Table functions
-----------------

System functions
------------------



.. toctree::
   :maxdepth: 2
   :caption: All Functions:
   :glob:

   scalar_functions/index
   aggregate_functions/*
   window_functions/*
   table_functions/*
   system_functions/*

