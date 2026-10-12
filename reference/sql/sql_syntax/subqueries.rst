:orphan:

.. _subqueries:

**********
Subqueries
**********

Subqueries enable the reuse of results of other queries.

SQreamDB supports relational (also called *derived table*) subqueries, which appear as :ref:`select` queries as part of a table expression.

SQreamDB also supports :ref:`common_table_expressions`, which are a form of subquery. With CTEs, a subquery can be named for reuse in a query.

.. note::
   
	You may include an unlimited number of subqueries within a single SQL statement, and you can also nest subqueries to an unlimited depth
   
   
Table Subqueries
================  

The following is an example of table named ``nba`` with the following structure:

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


To see the table contents, click :download:`Download nba.csv </_static/samples/nba.csv>`:

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1
   
Scalar Subqueries
=================

The following are examples of scalar subqueries.

Simple Subquery
---------------

.. code-block:: sql
   
	SELECT
	  AVG("Age")
	FROM
	  (
	    SELECT
	      "Name",
	      "Team",
	      "Age"
	    FROM
	      nba
	    WHERE
	      "Height" > '7-0'
	  );
	  
.. code-block:: none 

	avg
	---
	26

Combining a Subquery with a Join
--------------------------------

.. code-block:: sql

	SELECT
	  *
	FROM
	  (
	    SELECT
	      "Name"
	    FROM
	      nba
	    WHERE
	      "Height" > '7-0'
	  ) AS t(name),
	  nba AS n
	WHERE
	  n."Name" = t.name;
	  
.. code-block:: none

   name               | Name               | Team                   | Number | Position | Age | Height | Weight | College    | Salary  
   -------------------+--------------------+------------------------+--------+----------+-----+--------+--------+------------+---------
   Alex Len           | Alex Len           | Phoenix Suns           |     21 | C        |  22 | 7-1    |    260 | Maryland   |  3807120
   Alexis Ajinca      | Alexis Ajinca      | New Orleans Pelicans   |     42 | C        |  28 | 7-2    |    248 | \N         |  4389607
   Boban Marjanovic   | Boban Marjanovic   | San Antonio Spurs      |     40 | C        |  27 | 7-3    |    290 | \N         |  1200000
   Kristaps Porzingis | Kristaps Porzingis | New York Knicks        |      6 | PF       |  20 | 7-3    |    240 | \N         |  4131720
   Marc Gasol         | Marc Gasol         | Memphis Grizzlies      |     33 | C        |  31 | 7-1    |    255 | \N         | 19688000
   Meyers Leonard     | Meyers Leonard     | Portland Trail Blazers |     11 | PF       |  24 | 7-1    |    245 | Illinois   |  3075880
   Roy Hibbert        | Roy Hibbert        | Los Angeles Lakers     |     17 | C        |  29 | 7-2    |    270 | Georgetown | 15592217
   Rudy Gobert        | Rudy Gobert        | Utah Jazz              |     27 | C        |  23 | 7-1    |    245 | \N         |  1175880
   Salah Mejri        | Salah Mejri        | Dallas Mavericks       |     50 | C        |  29 | 7-2    |    245 | \N         |   525093
   Spencer Hawes      | Spencer Hawes      | Charlotte Hornets      |      0 | PF       |  28 | 7-1    |    245 | Washington |  6110034
   Tibor Pleiss       | Tibor Pleiss       | Utah Jazz              |     21 | C        |  26 | 7-3    |    256 | \N         |  2900000
   Timofey Mozgov     | Timofey Mozgov     | Cleveland Cavaliers    |     20 | C        |  29 | 7-1    |    275 | \N         |  4950000
   Tyson Chandler     | Tyson Chandler     | Phoenix Suns           |      4 | C        |  33 | 7-1    |    240 | \N         | 13000000
   Walter Tavares     | Walter Tavares     | Atlanta Hawks          |     22 | C        |  24 | 7-3    |    260 | \N         |  1000000

``WITH`` subqueries
-------------------

See :ref:`common_table_expressions` for more information. 

.. code-block:: sql
   
	WITH nba_ct AS (
	  SELECT
	    "Name",
	    "Team"
	  FROM
	    nba
	  WHERE
	    "College" = 'Connecticut'
	),
	nba_az AS (
	  SELECT
	    "Name",
	    "Team"
	  FROM
	    nba
	  WHERE
	    "College" = 'Arizona'
	)
	SELECT
	  *
	FROM
	  nba_az
	  JOIN nba_ct ON nba_ct."Team" = nba_az."Team";
	
.. code-block:: none
	
	Name            | Team            | name0          | team0          
	----------------+-----------------+----------------+----------------
	Stanley Johnson | Detroit Pistons | Andre Drummond | Detroit Pistons
	Aaron Gordon    | Orlando Magic   | Shabazz Napier | Orlando Magic

.. _in_subqueries:

IN Subqueries and Multi-Column IN
=================================

``IN`` and ``NOT IN`` accept a subquery as their right side, and accept a row of several values as their left side.
Comparing a row checks every position at once, so ``(a, b) IN (...)`` matches only where ``a`` and ``b`` match the
same row of the list or subquery.

.. code-block:: postgres

   <expression> [NOT] IN ( <select_statement> )

   ( <expression1>, <expression2>, ... ) [NOT] IN ( <select_statement> )

   ( <expression1>, <expression2>, ... ) [NOT] IN ( ( <value1>, <value2>, ... ), ( <value1>, <value2>, ... ), ... )

The row can also be written as ``ROW(a, b)``, and a list of rows as ``VALUES (1, 2), (3, 4)``.

These forms may be used in the ``WHERE`` clause of a ``SELECT``, ``DELETE``, or ``UPDATE`` statement, and as a
true-or-false value in a select list or a ``CASE`` expression.

The examples below use the following table:

.. code-block:: postgres

   CREATE OR REPLACE TABLE Sales (
     ProductName TEXT NOT NULL,
     SalesDate DATE NOT NULL,
     Revenue NUMERIC(10, 2) NOT NULL
   );

   INSERT INTO Sales VALUES
   ('Product A', '2024-01-01', 100.00),
   ('Product B', '2024-01-01', 150.00),
   ('Product A', '2024-01-02', 120.00),
   ('Product B', '2024-01-02', 180.00),
   ('Product C', '2024-01-01', 200.00);

Filtering on a combination of columns against a list of rows:

.. code-block:: postgres

   SELECT * FROM Sales
   WHERE (ProductName, SalesDate) IN (('Product A', '2024-01-01'), ('Product B', '2024-01-02'));

   productname | salesdate  | revenue
   ------------+------------+---------
   Product A   | 2024-01-01 | 100.00
   Product B   | 2024-01-02 | 180.00

Returning each product's most recent sale, by comparing two columns against a subquery:

.. code-block:: postgres

   SELECT * FROM Sales
   WHERE (ProductName, SalesDate) IN (
     SELECT ProductName, MAX(SalesDate) FROM Sales GROUP BY ProductName
   );

   productname | salesdate  | revenue
   ------------+------------+---------
   Product C   | 2024-01-01 | 200.00
   Product A   | 2024-01-02 | 120.00
   Product B   | 2024-01-02 | 180.00

A long list of rows is compiled as a join against the listed rows, the same as a long single-column ``IN`` list, so
lists of many thousands of rows remain practical. The point at which this happens is set by
:ref:`inListJoinThreshold<in_list_join_threshold>`, counted in comparisons: one per column in each row.

**NOT IN and nullable columns**

``IN`` and ``NOT IN`` over columns declared ``NOT NULL`` compile into a single join. ``NOT IN`` with a subquery is
slower where the compared columns can be ``NULL``, because a ``NULL`` on either side may match any value: every
compared column that can be ``NULL``, on either side of the ``IN``, doubles the number of joins. The
:ref:`inSubqueryNullJoinLimit<in_subquery_null_join_limit>` flag caps that number, by default at ``8``, which allows up to
three nullable columns. A statement over the limit fails with an error naming the flag. Declaring the compared columns
``NOT NULL`` where the data allows it avoids the cost.

**Limitations**

* The subquery must return as many columns as the row on the left side has values. Otherwise the statement returns ``The IN subquery returns 1 columns, but the left side of IN has 2 values``.
* Every row in a list must have as many values as the left side. Otherwise the statement returns ``Every item of this IN list must be a row of 2 values``.
* A single value on the left side cannot be compared with a list of rows. This returns ``This IN list item is a row, but the left side of IN is a single value``.
* Rows cannot be nested inside rows.
* A subquery cannot supply the value list of a ``PIVOT`` or ``PIVOT ARRAY``.

Correlated subqueries
=====================

An ``IN`` subquery may be correlated, meaning that it refers to columns of the outer query, under two conditions:

* Every condition linking the subquery to the outer query is an equality. Any other comparison returns ``Only equality supported in correlated conditions``.
* The subquery is a plain ``SELECT``, with no ``DISTINCT``, ``GROUP BY``, ``HAVING``, aggregates, ``LIMIT``, or set operations.

Using the ``Sales`` table above, the following returns each sale on a date when the same product sold for more than
``110``:

.. code-block:: postgres

   SELECT s.ProductName, s.SalesDate, s.Revenue
   FROM Sales AS s
   WHERE s.SalesDate IN (
     SELECT t.SalesDate FROM Sales AS t
     WHERE t.ProductName = s.ProductName AND t.Revenue > 110
   );

   productname | salesdate  | revenue
   ------------+------------+---------
   Product B   | 2024-01-01 | 150.00
   Product C   | 2024-01-01 | 200.00
   Product A   | 2024-01-02 | 120.00
   Product B   | 2024-01-02 | 180.00

Other correlated subqueries are not supported. Where an ``IN`` subquery is not an option, the same filter can often be
written as a join. Note that the join returns a row of ``t`` once for every matching row of ``t1``, whereas ``IN``
returns it once:

.. code-block:: sql

	# IN subquery

	SELECT
	  x,
	  y,
	  z
	FROM
	  t
	WHERE
	  x in (
	    SELECT
	      x
	    FROM
	      t1
	  );

	# The same filter written as a join
	SELECT
	  x,
	  y,
	  z
	FROM
	  t
	  JOIN (
	    SELECT
	      x
	    FROM
	      t1
	  ) t1 ON t.x = t1.x;