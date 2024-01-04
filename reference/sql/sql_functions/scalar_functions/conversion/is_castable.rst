.. _is_castable:

************
IS CUSTABLE
************

The ``IsCastable`` function checks whether a cast operation is possible or supported for the given column and data type. If the cast is not supported, the ``CASE`` statement handles the exception by providing an alternative.

Syntax
======

.. code-block:: sql

	-- Checks if a cast is supported

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
	    | TEXT
	    | NUMERIC
	    | DATE
	    | DATETIME
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

* ``true`` when the cast is supported
* ``false`` if the cast is not supported
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
	
