.. _oracle_migration:

**********************
Oracle Migration Guide
**********************

.. contents::
   :local:
   :depth: 2

Before You Begin
================



Using SQream Commands, Statements, and UDFs
===========================================

Operation Functions
-------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``+ (unary)``
     - ``+ (unary)``
     - +a
   * - ``+``
     - ``+``
     - a+ b
   * - ``- (unary)``
     - ``- (unary)``
     - -a
   * - ``-``
     - ``-``
     - a - b
   * - ``*``
     - ``*``
     - a * b
   * - ``/``
     - ``/``
     - a / b
   * - ``%``
     - ``%``
     - a % b
   * - ``&``
     - ``&``
     - AND
   * - ``~``
     - ``~``
     - NOT
   * - ``|``
     - ``|``
     - OR
   * - ``<<``
     - ``<<``
     - Shift left
   * - ``>>``
     - ``>>``
     - Shift right
   * - ``XOR``
     - ``XOR``
     - XOR

Conditional Functions
---------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``BETWEEN``
     - ``BETWEEN``
     - Value is in [ or not within ] the range
   * - ``CASE``
     - ``CASE``
     - Tests a conditional expression, depending on the result
   * - ``COALESCE``
     - ``COALESCE``
     - Evaluate first non-NULL expression
   * - ``IN``
     - ``IN``
     - Value is in [ or not within ] a set of values
   * - ``ISNULL``
     - ``ISNULL``
     - Alias for COALESCE with two expressions
   * - ``IS_ASCII``
     - ``IS_ASCII``
     - Test a TEXT for ASCII-only characters
   * - ``IS_NULL``
     - ``IS NULL``
     - Check for NULL [ or non-NULL ] values
   * - ``DECODE``
     - ``DECODE``
     - Decodes or extracts binary data from a textual input string
   
Numeric Functions
-----------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``ABS``
     - ``ABS``
     - Calculates the absolute value of an argument
   * - ``ACOS``
     - ``ACOS``
     - Calculates the inverse cosine of an argument
   * - ``ASIN``
     - ``ASIN``
     - Calculates the inverse sine of an argument
   * - ``ATAN``
     - ``ATAN``
     - Calculates the inverse tangent of an argument
   * - ``ATN2``
     - ``ATN2``
     - Calculates the inverse tangent for a point (y, x)
   * - ``BITAND``
     - ``&``
     - Computes an AND operation on the bits of expr1 and expr2
   * - ``CEIL``
     - ``CEILING``, ``CEIL``
     - Calculates the next integer for an argument
   * - ``COS``
     - ``COS``
     - Calculates the cosine of an argument
   * - ``COSH``
     - .. code-block:: postgres
	 
		CREATE or replace FUNCTION COSH(x double)
		RETURNS double
		AS $$
		 SELECT  (exp(x) + exp(-1*x))/2
		$$ LANGUAGE SQL 
		;
     - Returns the hyperbolic cosine of n
   * - NA
     - ``COT``
     - Calculates the cotangent of an argument
   * - NA
     - ``CRC64``
     - Calculates a CRC-64 hash of an argument
   * - NA
     - ``DEGREES``
     - Converts a value from radian values to degrees
   * - ``EXP``
     - ``EXP``
     - Calculates the natural exponent for an argument
   * - ``FLOOR``
     - ``FLOOR``
     - Calculates the largest integer smaller than the argument
   * - ``LN``
     - ``LOG``
     - Returns the natural logarithm of n
   * - ``LOG(b,n)``
     - .. code-block:: postgres
	 
		CREATE or replace FUNCTION log(b double, n double) 
		RETURNS double 
		AS $$ 
		SELECT (log(n)/log(b)) 
		$$ LANGUAGE SQL 
		;
     - Calculates the natural log for an argument
   * - ``LOG(10,x)``
     - ``LOG10``
     - Calculates the 10-based log for an argument
   * - ``MOD``
     - ``MOD``, ``%``
     - Calculates the modulu (remainder) of two arguments
   * - NA
     - ``PI``
     - Returns the constant value for π
   * - ``NANVL``
     - NA
     - Useful only for floating-point numbers of type
   * - ``POWER``
     - ``POWER``
     - Calculates x to the power of y (xy)
   * - NA
     - ``SQUARE``
     - Returns the square value of a numeric expression (x2)
   * - NA
     - ``RADIANS``
     - Converts a value from degree values to radians
   * - ``REMAINDER``
     - .. code-block:: postgres
	
		CREATE or replace FUNCTION remainder(n1 bigint, n2 bigint)
		RETURNS bigint
		AS $$
		 SELECT  (n1 - floor(n1/n2)*n2) 
		$$ LANGUAGE SQL 
		;
     - Returns the arguments any numeric datatype
   * - ``ROUND (number)``
     - ``ROUND``
     - Rounds an argument down to the nearest integer
   * - ``SIGN``
     - .. code-block:: postgres
	
		CREATE or replace FUNCTION my_sign(n bigint)
		RETURNS int
		AS $$
		 SELECT  case when n < 0 then -1  when n = 0 then 0 when n > 0 then 1 end 
		$$ LANGUAGE SQL 
		;
     - Returns the sign of the input value
   * - ``SIN``
     - ``SIN``
     - Calculates the sine
   * - ``SINH``
     - .. code-block:: postgres
	
		CREATE or replace FUNCTION SINH(x double)
		RETURNS double
		AS $$
		 SELECT  (exp(x) - exp(-1*x))/2
		$$ LANGUAGE SQL 
		;
     - Calculates the hyperbolic sine
   * - ``SQRT``
     - ``SQRT``
     - Calculates the square root
   * - ``TAN``
     - ``TAN``
     - Calculates the tangent
   * - ``TANH``
     - .. code-block:: postgres
	
		CREATE or replace FUNCTION TANH(x double)
		RETURNS double
		AS $$
		 SELECT  (exp(x) - exp(-1*x))/(exp(x) + exp(-1*x))
		$$ LANGUAGE SQL 
		;
     - Calculates the hyperbolic tangent
   * - ``TRUNC (number)``
     - ``TRUNC``
     - Rounds a number to its integer representation towards 0
   * - ``WIDTH_BUCKET(value, low, high, num_buckets)``
     - .. code-block:: postgres
	
		CREATE or replace FUNCTION myWIDTH_BUCKET(value float, low float, high float, num_buckets int ) 
		RETURNS INT
		AS $$ 
		select CASE 
		WHEN value < low THEN 0
		WHEN value >= high THEN num_buckets + 1
		ELSE CEIL(((value - low) / ((high - low) / num_buckets))+1)::INT END
		$$ LANGUAGE SQL
		;
     - Returns the ID of the bucket into which the value of a specific expression falls
   * - NA
     - ``TO_HEX``
     - Converts an integer to a hexadecimal representation
	 
Character Functions Returning Character Values
----------------------------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``CHR``
     - ``CHR``
     - Returns the character having the binary equivalent
   * - ``CONCAT``
     - ``||`` (Concatenate)
     - Concatenates all the specified strings and returns the final string
   * - ``INITCAP``
     - NA
     - Returns char, with the first letter of each word in uppercase
   * - ``LOWER``
     - ``LOWER``
     - Returns char, with all letters lowercase
   * - ``LPAD``
     - NA
     - Returns expr1, left-padded to length n characters
   * - ``LTRIM``
     - ``LTRIM``
     - Removes from the left end of char
   * - ``NLS_INITCAP``
     - NA
     - Returns char, with the first letter of each word in uppercase
   * - ``NLS_LOWER``
     - NA
     - Returns char, with all letters lowercase
   * - ``NLSSORT``
     - NA
     - Returns the string of bytes used to sort char
   * - ``NLS_UPPER``
     - NA
     - Returns char, with all letters uppercase
   * - ``REGEXP_REPLACE``
     - ``REGEXP_REPLACE``
     - Replaces a substring in a string that matches a specified pattern
   * - ``REGEXP_SUBSTR``
     - ``REGEXP_SUBSTR``
     - Returns a substring of an argument that matches a regular expression
   * - ``REPLACE``
     - ``REPLACE``
     - Replaces characters in a string
   * - ``RPAD``
     - NA
     - Right pads a string to a specified length
   * - ``RTRIM``
     - ``RTRIM``
     - Removes the space from the right side of a string
   * - ``SOUNDEX``
     - NA
     - Converts a normal string into a string of the SOUNDEX type
   * - ``SUBSTR``
     - ``SUBSTRING``, ``SUBSTR``
     - Returns a substring of an argument
   * - ``TRANSLATE``
     - NA
     - Returns ``expr`` with all occurrences of each character in ``from_string``, replaced by its corresponding character
   * - ``TRIM``
     - ``TRIM``
     - Trims whitespaces from an argument
   * - ``UPPER``
     - ``UPPER``
     - Converts an argument to an upper-case equivalent
   * - NA
     - ``REPEAT``
     - Repeats a string as many times as specified
   * - NA
     - ``REVERSE``
     - Returns a reversed order of a character string
   * - NA
     - ``LEFT``
     - Returns the left part of a character string with the specified number of characters
   * - NA
     - ``RIGHT``
     - Returns the right part of a character string with the specified number of characters
   * - NA
     - ``LIKE``
     - Tests if a string matches a given pattern. SQL patterns
   * - NA
     - ``RLIKE``
     - Tests if a string matches a given regular expression pattern. POSIX regular expressions
   * - NA
     - ``ISPREFIXOF``
     - Checks if one string is a prefix of the other
	 
Character Functions Returning Number Values
-------------------------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``ASCII``
     - NA
     - Returns the decimal representation in the database character set
   * - ``INSTR``
     - ``CHARINDEX``
     - Search string for substring
   * - ``LENGTH``
     - ``CHAR_LENGTH``
     - Calculates the length of a string in characters
   * - NA
     - ``LEN``
     - Calculates the number of characters in a string. (This function is provided for SQL Server compatibility)
   * - NA
     - ``OCTET_LENGTH``
     - Calculates the number of bytes in a string
   * - NA
     - ``CHARINDEX``
     - Returns the starting position of a string inside another string
   * - NA
     - ``PATINDEX``
     - Returns the starting position of a string inside another string
   * - ``REGEXP_COUNT``
     - ``REGEXP_COUNT``
     - Calculates the number of matches of a regular expression
   * - ``REGEXP_INSTR``
     - ``REGEXP_INSTR``
     - Returns the start position of a regular expression match in an argument
   * - NA
     - ``REGEXP_REPLACE``
     - 
	 
Datetime Functions
------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
	 
General Comparison Functions
----------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 