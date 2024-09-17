:orphan:

.. _pivot_unpivot:

********************
PIVOT & UNPIVOT
********************

``PIVOT`` allows to convert row-level data into columnar representation. This technique is particularly useful when you need to summarize and visualize data.
``UNPIVOT`` does the opposite by transforming columnar data into rows. This operation is invaluable for scenarios where you wish to explore data in a more granular manner.


Syntax
========

.. code-block:: postgres

   SELECT <selected_columns>
   
	FROM <from_clause>
	[
	  PIVOT
	  (<pivot_expression> 
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
	
	unpivot_expression := <new output column created for values in result of the source query>


Limitations
=================
The number of resulting columns for ``PIVOT`` and the number of input columns for ``UNPIVOT`` is limited to 10,000.



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
		SUM(Revenue)
		FOR SalesDate IN ("2024-01-01", "2024-01-02")
	) AS PivotTable;

	Product A                                         ,100.00,120.00
	Product B                                         ,150.00,180.00
	Product C                                         ,200.00,\N
	3 rows
	
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
