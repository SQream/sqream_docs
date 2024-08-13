.. _sql_functions:

*************
SQL Functions
*************

BLUE supports functions from ANSI SQL, as well as others for compatibility.

.. _scalar_functions:

Built-In Scalar Functions
-------------------------

Bitwise Operations
^^^^^^^^^^^^^^^^^^

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

Conditional Functions
^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`case`
     - Test a conditional expression, and depending on the result, evaluate additional expressions.
   * - :ref:`coalesce`
     - Evaluate first non-NULL expression
   * - :ref:`isnull`
     - Alias for :ref:`coalesce` with two expressions
   * - :ref:`is_ascii`
     - Test a ``TEXT`` for ASCII-only characters
   * - :ref:`is_null`
     - Check for ``NULL`` [ or non-``NULL`` ] values

Conversion Functions
^^^^^^^^^^^^^^^^^^^^

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
   * - :ref:`chr`
     - Returns the ASCII character representation of the supplied integer
   * - :ref:`is_castable`
     - Checks whether a cast operation is possible or supported for a given column and data type and provides an alternative when there is an exception

Date and Time Functions
^^^^^^^^^^^^^^^^^^^^^^^

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

Numeric Functions
^^^^^^^^^^^^^^^^^

.. list-table:: Arithmetic Operators
   :widths: auto
   :header-rows: 1
   
   * - Operator
     - Syntax
     - Description
   * - ``+`` (unary)
     - ``+a``
     - Converts a string to a numeric value. Identical to ``a :: double``
   * - ``+``
     - ``a + b``
     - Adds two expressions together
   * - ``-`` (unary)
     - ``-a``
     - Negates a numeric expression
   * - ``-``
     - ``a - b``
     - Subtracts ``b`` from ``a``
   * - ``*``
     - ``a * b``
     - Multiplies ``a`` by ``b``
   * - ``/``
     - ``a / b``
     - Divides ``a`` by ``b``
   * - ``%``
     - ``a % b``
     - Modulu of ``a`` by ``b``. See also :ref:`mod`


.. list-table:: Arithemtic Operator Functions
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
   * - :ref:`sign`
     - Returns a value of -1, 0, or 1, depending on the sign of the input argument
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

Strings Functions
^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`char_length`
     - Calculates number of characters in an argument
   * - :ref:`charindex`
     - Calculates the position where a string starts inside another string
   * - :ref:`concat`
     - Concatenates two strings
   * - :ref:`crc64`
     - Calculates a CRC-64 hash of an argument
   * - :ref:`decode`
     - Decodes or extracts binary data from a textual input string
   * - :ref:`isprefixof`
     - Matches if a string is the prefix of another string
   * - :ref:`left`
     - Returns the first number of characters from an argument
   * - :ref:`len`
     - Calculates the length of a string in characters
   * - :ref:`like`
     - Tests if a string argument matches a pattern
   * - :ref:`lower`
     - Converts an argument to a lower-case equivalent
   * - :ref:`ltrim`
     - Trims whitespaces from the left side of an argument
   * - :ref:`octet_length`
     - Calculates the length of a string in bytes
   * - :ref:`patindex`
     - Calculates the position where a pattern matches a string
   * - :ref:`regexp_count`
     - Calculates the number of matches of a regular expression match in an argument
   * - :ref:`regexp_instr`
     - Returns the start position of a regular expression match in an argument
   * - :ref:`regexp_replace`
     - Replaces and returns the text column substrings of a regular expression match in an argument
   * - :ref:`regexp_substr`
     - Returns a substring of an argument that matches a regular expression
   * - :ref:`repeat`
     - Repeats a string as many times as specified
   * - :ref:`replace`
     - Replaces characters in a string
   * - :ref:`reverse`
     - Reverses a string argument
   * - :ref:`right`
     - Returns the last number of characters from an argument
   * - :ref:`rlike`
     - Tests if a string argument matches a regular expression pattern
   * - :ref:`rtrim`
     - Trims whitespace from the right side of an argument
   * - :ref:`substring`
     - Returns a substring of an argument
   * - :ref:`trim`
     - Trims whitespaces from an argument
   * - :ref:`upper`
     - Converts an argument to an upper-case equivalent
   * - :ref:`select_ascii`
     - Returns an ``INT`` value representing the ASCII code of the leftmost character in a string

User-Defined Scalar Functions
-----------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
   * - :ref:`scalar_sql_udf`
   * - :ref:`simple_scalar_sql_udf`


Aggregate Functions
-------------------

The following table shows the **aggregate** functions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Aliases
     - Description
   * - :ref:`avg`
     -
     - Calculates the average of all of the values
   * - :ref:`corr`
     -
     - Calculates the Pearson correlation coefficient
   * - :ref:`count`
     -
     - Calculates the count of all of the values or only distinct values
   * - :ref:`covar_pop`
     - 
     - Calculates population covariance of values
   * - :ref:`covar_samp`
     - 
     - Calculates sample covariance of values
   * - :ref:`max`
     - 
     - Returns maximum value of all values
   * - :ref:`min`
     -
     - Returns minimum value of all values
   * - :ref:`percentile_cont`
     - 
     - Returns the value located in the selected percentile of a specified column
   * - :ref:`percentile_disc`
     - 
     - Returns an exact value located in the selected percentile of a specified column based on the closest values in your data to the requested percentile		
   * - :ref:`stddev_pop`
     - ``stdevp``
     - Calculates population standard deviation of values
   * - :ref:`stddev_samp`
     - ``stdev``, ``stddev``
     - Calculates sample standard deviation of values
   * - :ref:`sum`
     - 
     - Calculates the sum of all of the values or only distinct values
   * - :ref:`var_pop`
     - ``varp``
     - Calculates population variance of values
   * - :ref:`var_samp`
     - ``var``, ``variance``
     - Calculates sample variance of values


Window Functions
----------------

The following table shows the **window** functions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`cume_dist`
     - Returns the cumulative distribution of rows
   * - :ref:`dense_rank`
     - Returns the rank of the current row with no gaps
   * - :ref:`first_value`
     - Returns the value in the first row of a window
   * - :ref:`lag`
     - Calculates the value evaluated at the row that is before the current row within the partition
   * - :ref:`last_value`
     - Returns the value in the last row of a window
   * - :ref:`lead`
     - Calculates the value evaluated at the row that is after the current row within the partition
   * - :ref:`nth_value`
     - Returns the value in a specified ``(n)`` row of a window
   * - :ref:`ntile`
     - Returns an integer ranging between ``1`` and the argument value, dividing the partitions as equally as possible
   * - :ref:`percent_rank`
     - Returns the relative rank of the current row
   * - :ref:`max`
     - Calculates the maximum value
   * - :ref:`min`
     - Calculates the minimum value
   * - :ref:`sum`
     - Calculates the sum of all of the values  
   * - :ref:`rank`
     - Calculates the rank of a row	
   * - :ref:`row_number`
     - Returns the row number of each row within the partition of a result set   
