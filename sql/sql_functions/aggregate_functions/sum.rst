:orphan:

.. _sum:

***
SUM 
***

The ``SUM`` function returns the sum value of an expression.

Syntax
======

.. code-block:: postgres

	-- As an aggregate
	SUM( [ DISTINCT ] expr )
   
	-- As a window function
	SUM (expr) OVER (
	  [ PARTITION BY value_expression [, ...] ] [ ORDER BY value_expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] ] [ frame_clause ]
	)

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Numeric expression
   * - ``DISTINCT``
     - Specifies that the operation should operate only on unique values

Returns
=======

* Returns ``REAL`` for the sum of ``REAL`` arguments.
 
* If the running sum exceeds its limit, an exception is thrown.

Notes
=====

* ``NULL`` values are ignored

* Because ``SUM`` returns the same data type, it can very quickly overflow on large data sets. If the SUM is over 2\ :sup:`31` for example, up-cast to a larger type like ``BIGINT``: ``SUM(expr :: BIGINT)``

Examples
========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      "Name" TEXT,
      "Team" TEXT,
      "Number" TINYINT,
      "Position" TEXT,
      "Age" TINYINT,
      "Height" TEXT,
      "Weight" REAL,
      "College" TEXT,
      "Salary" FLOAT
    );

Simple ``SUM``
--------------

.. code-block:: psql

	SELECT
	  SUM("Age")
	FROM
	  nba;

Output:

.. code-block:: none

	sum  
	-----
	12311

``SUM`` Distinct Values
-----------------------

.. code-block:: psql

	SELECT
	  SUM(DISTINCT "Age")
	FROM
	  nba;
   
Output:

.. code-block:: none

	sum
	---
	649

Combine ``SUM`` with ``GROUP BY``
---------------------------------

.. code-block:: psql

	SELECT
	  "Age",
	  SUM("Salary")
	FROM
	  nba
	GROUP BY
	  1;
	  
Output:

.. code-block:: none

	Age | sum      
	----+----------
	 19 |   3860880
	 20 |  51790026
	 21 |  39280213
	 22 |  61307050
	 23 |  79355103
	 24 | 170338514
	 25 | 172958166
	 26 | 247196385
	 27 | 267069647
	 28 | 153305658
	 29 | 168052779
	 30 | 211855757
	 31 | 187250724
	 32 | 100320456
	 33 |  55030346
	 34 |  76060300
	 35 |  27693918
	 36 |  22381196
	 37 |  38333334
	 38 |   7360164
	 39 |   5035745
	 40 |  14000750
