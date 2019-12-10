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
     - Check for ``NULL`` [ or non-``NULL`` ] values

Conversion
^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`from_unixts`
     - Converts a UNIX Timestamp to ``DATE`` or ``DATETIME``
   * - :ref:`to_hex`
     - Converts a number to a hexadecimal string representation
   * - :ref:`to_unixts`
     - Converts a ``DATE`` or ``DATETIME`` to a UNIX Timestamp

Date and time
^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`curdate`
     - Special syntax, equivalent to :ref:`current_date`
   * - :ref:`current_date`
     - Returns the current date as ``DATE``
   * - :ref:`current_timestamp`
     - Equivalent to :ref:`getdate`
   * - :ref:`datepart`
     - Extracts a date or time element from a date expression
   * - :ref:`dateadd`
     - Adds an interval to a date expression
   * - :ref:`datediff`
     - Calculates the time difference between two date expressions
   * - :ref:`eomonth`
     - Calculates the last day of the month of a given date expression
   * - :ref:`extract`
     - ANSI syntax for extracting date or time element from a date expression
   * - :ref:`getdate`
     - Returns the current timestamp as ``DATETIME``
   * - :ref:`sysdate`
     - Equivalent to :ref:`getdate`
   * - :ref:`date_trunc`
     - Truncates a date element down to a specified date or time element

Numeric
^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`abs`
     - Calculates the absolute value of an argument
   * - :ref:`acos`
     - Calculates the inverse cosine of an argument
   * - :ref:`asin`
     - Calculates the inverse sine of an argument
   * - :ref:`atan`
     - Calculates the inverse tangent of an argument
   * - :ref:`atn2`
     - Calculates the inverse tangent for a point (y, x)
   * - :ref:`ceiling`
     - Calculates the next integer for an argument
   * - :ref:`cos`
     - Calculates the cosine of an argument
   * - :ref:`cot`
     - Calculates the cotangent of an argument
   * - :ref:`crc64`
     - Calculates a CRC-64 hash of an argument
   * - :ref:`degrees`
     - Converts a value from radian values to degrees
   * - :ref:`exp`
     - Calcalates the natural exponent for an argument (*e*\ :sup:`x`)
   * - :ref:`floor`
     - Calculates the largest integer smaller than the argument
   * - :ref:`log`
     - Calculates the natural log for an argument
   * - :ref:`log10`
     - Calculates the 10-based log for an argument
   * - :ref:`mod`
     - Calculates the modulu (remainder) of two arguments
   * - :ref:`pi`
     - Returns the constant value for π
   * - :ref:`power`
     - Calculates x to the power of y (x\ :sup:`y`)
   * - :ref:`radians`
     - Converts a value from degree values to radians
   * - :ref:`round`
     - Rounds an argument down to the nearest integer, or an arbitrary precision
   * - :ref:`sin`
     - Calculates the sine  of an argument
   * - :ref:`sqrt`
     - Calculates the square root of an argument (√x)
   * - :ref:`square`
     - Raises an argument to the power of 2 (x\ :sup:`y`)
   * - :ref:`tan`
     - Calculates the tangent of an argument
   * - :ref:`trunc`
     - Rounds a number to its integer representation towards 0

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

