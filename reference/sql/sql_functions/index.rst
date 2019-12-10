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

