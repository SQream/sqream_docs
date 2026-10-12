:orphan:

.. _pivot_unpivot:

********************
PIVOT & UNPIVOT
********************

``PIVOT`` allows to convert row-level data into columnar representation. This technique is particularly useful when you need to summarize and visualize data.
``UNPIVOT`` does the opposite by transforming columnar data into rows. This operation is invaluable for scenarios where you wish to explore data in a more granular manner.

Both statements produce one column for every value listed in the ``IN`` clause. To pivot a large number of values into
a single array column instead, see :ref:`PIVOT ARRAY & UNPIVOT ARRAY<pivot_unpivot_array>`.


Syntax
========

.. code-block:: postgres

   SELECT <selected_columns>
   
	FROM <from_clause>
	[
	  PIVOT [DISTINCT]
	  (<pivot_expression1> AS <pivot_expression1_name> [, <pivot_expression2> AS <pivot_expression2_name>, .... , <pivot_expressionN> AS <pivot_expressionN_name>]
		FOR <column_name>
		IN ([<expression1> AS] <name1>, [<expression2> AS] <name2>, ... , [<expressionN> AS] <nameN>)
	  )
	  [AS <pivoted_result_name>]
	]
	[
	  UNPIVOT
	  (<unpivot_expression> 
		FOR <column_name>
		IN ([<name1> AS] expression1, [<name2> AS] expression2, ... , [<nameN> AS] <expressionN>)
	  )
	  [AS <unpivoted_result_name>]
	]
	
	<rest of the query ...>

	pivot_expression := <aggregation function> ( <column being aggregated> )

	-- with DISTINCT, a value rather than an aggregation:
	pivot_expression := <scalar expression over one column>

	unpivot_expression := <new output column created for values in result of the source query>


Limitations
=================
* The number of resulting columns for ``PIVOT`` is limited to 8,000.
* The number of resulting columns for ``UNPIVOT`` is limited to 2,000.
* These limits apply because each listed value becomes a column. The :ref:`PIVOT ARRAY & UNPIVOT ARRAY<pivot_unpivot_array>` forms produce one column per aggregation rather than one per value, and their value lists are not bounded by the maximum number of columns.
* ``PIVOT DISTINCT`` takes a value, not an aggregation. Passing an aggregate such as ``SUM(Revenue)`` returns ``PIVOT DISTINCT takes a value, not an aggregate``.
* ``PIVOT DISTINCT`` does not check that the rows are unique. If a group has more than one row for the same pivoted value, the column holds one of those rows' values, and which one is not defined.
* The columns produced by ``PIVOT DISTINCT`` are always nullable, because a group may have no row for a listed value.



PIVOT Example  
=================
Create a sales table

.. code-block:: postgres
   
   CREATE OR REPLACE TABLE Sales (
    ProductID int,
    ProductName varchar(50),
    SalesDate date,
    Revenue decimal(10, 2)
	);
	
Populate data

.. code-block:: postgres

	INSERT INTO Sales (ProductID, ProductName, SalesDate, Revenue) VALUES
	(1, 'Product A', '2024-01-01', 100.00),
	(2, 'Product B', '2024-01-01', 150.00),
	(3, 'Product C', '2024-01-01', 200.00),
	(1, 'Product A', '2024-01-02', 120.00),
	(2, 'Product B', '2024-01-02', 180.00);
	

Pivots the SalesDate column, creating new columns for each specified date.
The ``SUM(Revenue)`` aggregates the Revenue for each product and date combination.
The ``PIVOT`` operation creates a new table with ProductName as the first column and additional columns for each specified SalesDate. The values in these columns are the summed Revenue for each product on that date.

.. code-block:: postgres

	SELECT * FROM (
		SELECT ProductName, SalesDate, Revenue
		FROM Sales
	) AS SourceTable
	PIVOT (
		SUM(Revenue) AS RevenueSum
		FOR SalesDate IN ("2024-01-01", "2024-01-02")
	) AS PivotTable;

	Product A                                         ,100.00,120.00
	Product B                                         ,150.00,180.00
	Product C                                         ,200.00,\N
	3 rows

PIVOT DISTINCT Example
======================
Each product in the ``Sales`` data above has at most one row per date, so ``SUM`` has nothing to add up. When you know
that the source holds at most one row for each group and pivoted value, ``PIVOT DISTINCT`` takes each value as it is and
skips the aggregation work. The pivot expression is then a plain value such as ``Revenue``, not an aggregate.

.. code-block:: postgres

	SELECT * FROM (
		SELECT ProductName, SalesDate, Revenue
		FROM Sales
	) AS SourceTable
	PIVOT DISTINCT (
		Revenue AS Rev
		FOR SalesDate IN ("2024-01-01", "2024-01-02")
	) AS PivotTable;

	productname | 2024-01-01_rev | 2024-01-02_rev
	------------+----------------+---------------
	Product A   | 100.00         | 120.00
	Product B   | 150.00         | 180.00
	Product C   | 200.00         | \N
	3 rows

``DISTINCT`` is a promise you make about the data, and it is not checked. If a product had two rows for the same date,
the column would hold one of the two revenues rather than their sum, so use it only where the source guarantees
uniqueness. For pivoting many values, :ref:`PIVOT DISTINCT ARRAY<pivot_distinct_array>` removes the aggregation entirely.

UNPIVOT Example 
=================
Create a sales table

.. code-block:: postgres

	CREATE OR REPLACE TABLE Sales (
		ProductID int,
		ProductName varchar(50),
		JanuaryRevenue decimal(10, 2),
		FebruaryRevenue decimal(10, 2),
		MarchRevenue decimal(10, 2)
	);
	
Populate data

.. code-block:: postgres

	INSERT INTO Sales (ProductID, ProductName, JanuaryRevenue, FebruaryRevenue, MarchRevenue) VALUES
	(1, 'Product A', 100.00, 120.00, 150.00),
	(2, 'Product B', 150.00, 180.00, 200.00),
	(3, 'Product C', 200.00, 220.00, 250.00);

Unpivots the JanuaryRevenue, FebruaryRevenue, and MarchRevenue columns, creating a new column Month and a column Revenue to store the corresponding values. The ``UNPIVOT`` operation creates a new table with ProductID, ProductName, Month, and Revenue columns, effectively transforming the column-based data into a row-based format.

.. code-block:: postgres

	SELECT ProductID, ProductName, Month, Revenue
	FROM (
		SELECT ProductID, ProductName, JanuaryRevenue, FebruaryRevenue, MarchRevenue
		FROM Sales
	) AS SourceTable
	UNPIVOT (
		Revenue FOR Month IN (JanuaryRevenue, FebruaryRevenue, MarchRevenue)
	) AS UnpivotTable;

	1,Product A                                         ,JanuaryRevenue,100.00
	2,Product B                                         ,JanuaryRevenue,150.00
	3,Product C                                         ,JanuaryRevenue,200.00
	1,Product A                                         ,FebruaryRevenue,120.00
	2,Product B                                         ,FebruaryRevenue,180.00
	3,Product C                                         ,FebruaryRevenue,220.00
	1,Product A                                         ,MarchRevenue,150.00
	2,Product B                                         ,MarchRevenue,200.00
	3,Product C                                         ,MarchRevenue,250.00
	9 rows


See Also
=========
* :ref:`PIVOT ARRAY & UNPIVOT ARRAY<pivot_unpivot_array>` - the array forms, for pivoting a large number of values into a single column
