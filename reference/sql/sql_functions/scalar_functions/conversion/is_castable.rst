.. _is_castable:

************
IS CUSTABLE
************

The ``IsCastable`` function checks whether a cast operation is possible or supported for the given column and data type. If the cast is not supported, the ``CASE`` statement handles the exception by providing an alternative.

Syntax
======

.. code-block:: sql

	-- Checking if a cast is supported for literal value:

	SELECT 
	   IsCastable(
	    BOOL 
	    | TINYINT
	    | SMALLINT
	    | INT
	    | BIGINT
	    | REAL
	    | DOUBLE
		| FLOAT
	    | TEXT
	    | NUMERIC
	    | DATE
	    | DATETIME
		| ARRAY
		, BOOL 
	      | TINYINT
	      | SMALLINT
	      | INT
	      | BIGINT
	      | REAL
	      | DOUBLE
		  | FLOAT
	      | TEXT
	      | NUMERIC
	      | DATE
	      | DATETIME
		  | ARRAY
		) 
		
	-- Checking if cast is supported for columns:
		
	SELECT
	   IsCastable(
	    <column_name>,
		BOOL 
	    | TINYINT
	    | SMALLINT
	    | INT
	    | BIGINT
	    | REAL
	    | DOUBLE
		| FLOAT
	    | TEXT
	    | NUMERIC
	    | DATE
	    | DATETIME
		| ARRAY
		)
	FROM 
	<table_name>;
	
	-- Returns query result set 
	
	SELECT 
	  <colum_mame>,
	  CASE
	    WHEN IsCastable(
	     <colum_mame>,
	     BOOL 
	     | TINYINT
	     | SMALLINT
	     | INT
	     | BIGINT
	     | REAL
	     | DOUBLE
	     | TEXT
	     | NUMERIC
	     | DATE
	     | DATETIME
	     ) 
	    THEN 
		 <colum_mame> ::
	     BOOL 
	     | TINYINT
	     | SMALLINT
	     | INT
	     | BIGINT
	     | REAL
	     | DOUBLE
	     | TEXT
	     | NUMERIC
	     | DATE
	     | DATETIME		
	    ELSE <expression>
	  END
	FROM
	<table_mame>;

Return
=======

``IsCastable`` returns:

* 1 when the cast is supported
* 0 if the cast is not supported
* Your query result set if used within a ``CASE`` statement

Example
=======

.. code-block:: sql

	SELECT number,
	  CASE
	    WHEN IsCastable(number, DOUBLE) THEN number :: DOUBLE
	    ELSE NULL
	  END
	FROM
	my_numbers;
	
