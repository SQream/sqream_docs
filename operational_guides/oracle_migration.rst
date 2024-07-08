.. _oracle_migration:

**********************
Oracle Migration Guide
**********************

This guide is designed to assist those who wish to migrate their database systems from Oracle to SQreamDB. Use this guide to learn how to use the most commonly used Oracle functions with their equivalents in SQreamDB. For functions that do not have direct equivalents in SQreamDB, we provide User-Defined Functions (UDFs). If you need further assistance, our `SQream support team <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ is available to help with any custom UDFs or additional migration questions.

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
   * - ``+`` (unary)
     - ``+`` (unary)
     - +a
   * - ``+``
     - ``+``
     - a+ b
   * - ``-`` (unary)
     - ``-`` (unary)
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
   
Conversion Functions
--------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``TO_DATE``
     - ``+`` (unary)
     - Converts a string to a date
   * - ``TO_NUMBER``
     - .. code-block:: postgres
	 
		CREATE OR REPLACE FUNCTION SIGN(n,numeric)
		RETURNS numeric
		AS $$
		 CAST(TEXT AS NUMERIC)
		$$ LANGUAGE SQL
		;
     - Converts a string to a number
   
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
     - Calculates the modulus (remainder) of two arguments
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
   * - ``ADD_MONTHS``
     - NA
     - Returns a number of months are added to a specified date
   * - NA
     - ``CURDATE``
     - This function is equivalent to CURRENT_DATE
   * - ``CURRENT_DATE``
     - ``CURRENT_DATE``
     - Returns the current date as DATE
   * - ``CURRENT_TIMESTAMP``
     - ``CURRENT_TIMESTAMP``
     - Equivalent to ``GETDATE``
   * - ``DBTIMEZONE``
     - NA
     - Returns the value of the database time zone
   * - ``EXTRACT`` (datetime)
     - ``EXTRACT``
     - ANSI syntax for extracting date or time element from a date expression
   * - ``FROM_TZ``
     - NA
     - Converts a timestamp value and a time zone
   * - ``LAST_DAY``
     - ``EOMONTH``
     - Returns the last day of the month in which the specified date value falls
   * - NA
     - ``CURRENT_TIMESTAMP``
     - Returns the current date and time in the session time zone
   * - ``MONTHS_BETWEEN``
     - NA
     - Returns the number of months between specified date values
   * - ``NEW_TIME``
     - NA
     - returns the date and time in time zone
   * - ``NEXT_DAY``
     - NA
     - Returns the date of the first weekday that is later than a specified data
   * - ``NUMTODSINTERVAL``
     - NA
     - Converts n to an INTERVAL DAY TO SECOND literal
   * - ``NUMTOYMINTERVAL``
     - NA
     - Converts number n to an INTERVAL YEAR TO MONTH literal
   * - ``ORA_DST_AFFECTED``
     - NA
     - Changing the time zone data file
   * - ``ORA_DST_CONVERT``
     - NA
     - Changing the time zone data file for specify error handling
   * - ``ORA_DST_ERROR``
     - NA
     - Changing the time zone data file for takes as an argument a datetime
   * - ``ROUND`` (date)
     - ``ROUND``
     - Rounds an argument down to the nearest integer, or an arbitrary precision
   * - ``SESSIONTIMEZONE``
     - NA
     - Returns the time zone of the current session
   * - ``SYS_EXTRACT_UTC``
     - NA
     - extracts the UTC from a datetime value with time zone offset
   * - ``SYSDATE``
     - ``SYSDATE``
     - Equivalent to ``GETDATE``
   * - ``SYSTIMESTAMP``
     - ``CURRENT_TIMESTAMP``
     - Returns the current timestamp
   * - ``TO_CHAR`` (datetime)
     - NA
     - Converts a date value to a string in a specified format
   * - ``TO_TIMESTAMP``
     - NA
     - Converts datatype to a value of TIMESTAMP datatype
   * - ``TO_TIMESTAMP_TZ``
     - NA
     - Converts datatype to a value of TIMESTAMP WITH TIME ZONE datatype
   * - ``TO_DSINTERVAL``
     - NA
     - Converts a character string of CHAR datatype
   * - ``TO_YMINTERVAL``
     - NA
     - Converts a character string of CHAR datatype
   * - ``TRUNC`` (date)
     - ``TRUNC``
     - Truncates a date element down to a specified date or time element
   * - ``TZ_OFFSET``
     - NA
     - Returns the time zone offset
   * - NA
     - ``DATEADD``
     - 
   * - NA
     - ``DATEDIFF``
     - 
   * - NA
     - ``DATEPART``
     - 
   * - NA
     - ``GETDATE``
     - 
   * - NA
     - ``TO_UNIXTS``, ``TO_UNIXTSMS``
     - 
   * - NA
     - ``FROM_UNIXTS``, ``FROM_UNIXTSMS``
     - 

	 
General Comparison Functions
----------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``GREATEST``
     - NA
     - Returns the greatest of a list of one or more expressions
   * - ``LEAST``
     - NA
     - Returns the least of a list of one or more expressions
	 
NULL-Related Functions
----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``COALESCE``
     - ``COALESCE``
     - Returns the first non-null
   * - ``LNNVL``
     - NA
     - Provides a concise way to evaluate a condition when one or both operands of the condition may be null
   * - ``NANVL``
     - NA
     - Takes as arguments any numeric data type or any nonnumeric data type
   * - ``NULLIF``
     - ``IS NULL``
     - If they are equal, then the function returns null
   * - ``NVL``
     - ``ISNULL``
     - Replace null (returned as a blank) with a string in the results of a query
   * - ``NVL2``
     - NA
     - Determine the value returned by a specified expression is null or not null
	 
Aggregate Functions
-------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``AVG``
     - ``AVG``
     - Calculates the average of all of the values
   * - ``CHECKSUM``
     - NA
     - Detect changes in a table
   * - ``COLLECT``
     - NA
     - Takes as its argument a column of any type and creates a nested table
   * - ``CORR``
     - ``CORR``
     - Calculates the Pearson correlation coefficient
   * - ``COUNT``
     - ``COUNT``
     - Calculates the count of all of the values or only distinct values
   * - ``COVAR_POP``
     - ``COVAR_POP``
     - Calculates population covariance of values
   * - ``COVAR_SAMP``
     - ``COVAR_SAMP``
     - Calculates sample covariance of values
   * - ``CUME_DIST``
     - ``CUME_DIST``
     - Calculates the cumulative distribution of a value in a group of values
   * - ``FIRST``
     - ``FIRST_VALUE``
     - The FIRST_VALUE function returns the value located in the selected column of the first row of a segment
   * - ``GROUP_ID``
     - NA
     - Distinguishes duplicate groups resulting from a GROUP BY specification
   * - ``GROUPING``
     - NA
     - Distinguishes superaggregate rows from regular grouped rows
   * - ``GROUPING_ID``
     - NA
     - Returns a number corresponding to the GROUPING bit vector associated with a row
   * - ``LAST``
     - ``LAST_VALUE``
     - The LAST_VALUE function returns the value located in the selected column of the last row of a segment
   * - NA
     - ``NTH_VALUE``
     - The NTH_VALUE function returns the value located in the selected column of a specified row of a segment
   * - ``MAX``
     - ``MAX``
     - Returns maximum value of all values
   * - ``MEDIAN``
     - NA
     - Calculates the median value of a column
   * - ``MIN``
     - ``MIN``
     - Returns minimum value of all values
   * - NA
     - ``NTILE``
     - Divides an ordered data set into a number of buckets
   * - ``PERCENTILE_CONT``
     - ``PERCENTILE_CONT``
     - Inverse distribution function that assumes a continuous distribution model
   * - ``PERCENTILE_DISC``
     - ``PERCENTILE_DISC``
     - Inverse distribution function that assumes a discrete distribution model
   * - ``PERCENT_RANK``
     - ``PERCENT_RANK``
     - Range of values returned by PERCENT_RANK is 0 to 1, inclusive
   * - ``RANK``
     - ``RANK``
     - Calculates the rank of a value in a group of values
   * - ``DENSE_RANK``
     - ``DENSE_RANK``
     - Computes the rank of a row in an ordered group of rows
   * - ``STATS_BINOMIAL_TEST``
     - NA
     - Exact probability test used for dichotomous variables
   * - ``STATS_CROSSTAB``
     - NA
     - Method used to analyze two nominal variables
   * - ``STATS_F_TEST``
     - NA
     - Tests whether two variances are significantly different
   * - ``STATS_KS_TEST``
     - NA
     - Kolmogorov-Smirnov function that compares two samples to test
   * - ``STATS_MODE``
     - NA
     - Takes as its argument a set of values and returns the value
   * - ``STDDEV``
     - ``STDDEV``
     - Returns the population standard deviation of all input values
   * - ``STDDEV_POP``
     - ``STDDEV_POP``
     - Calculates population standard deviation of values
   * - ``STDDEV_SAMP``
     - ``STDDEV_SAMP``
     - Calculates sample standard deviation of values
   * - ``SUM``
     - ``SUM``
     - Calculates the sum of all of the values or only distinct values
   * - ``VAR_POP``
     - ``VAR_POP``
     - Calculates population variance of values
   * - ``VAR_SAMP``
     - ``VAR_SAMP``
     - Calculates sample variance of values
   * - ``VARIANCE``
     - ``VAR``, ``VARIANCE``
     - Returns the variance of expr
	 
Analytic Functions
------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - NA
     - ``MODE``
     - 
   * - ``FEATURE_DETAILS``
     - NA
     - Returns feature details for each row in the selection
   * - ``FEATURE_ID``
     - NA
     - Returns the identifier of the highest value feature for each row
   * - ``FEATURE_SET``
     - NA
     - Returns a set of feature ID and feature value pairs for each row
   * - ``FEATURE_VALUE``
     - NA
     - Returns a feature value for each row in the selection
   * - ``LEAD``
     - ``LEAD``
     - Returns a value from a subsequent row within the partition of a result set
   * - ``LAG``
     - ``LAG``
     - Returns a value from a previous row within the partition of a result set
   * - ``PREDICTION``
     - NA
     - Returns a prediction for each row in the selection
   * - ``PREDICTION_COST``
     - NA
     - Returns prediction details for each row in the selection
   * - ``PREDICTION_DETAILS``
     - NA
     - Returns prediction details for each row in the selection
   * - ``PREDICTION_PROBABILITY``
     - NA
     - Returns a probability for each row in the selection
   * - ``PREDICTION_SET``
     - NA
     - Returns a set of predictions with either probabilities or costs for each row
   * - ``ROW_NUMBER``
     - ``ROW_NUMBER``
     - Assigns a unique number to each row to which it is applied