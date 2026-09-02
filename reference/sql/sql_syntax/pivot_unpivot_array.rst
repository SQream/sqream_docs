:orphan:

.. _pivot_unpivot_array:

****************************
PIVOT ARRAY & UNPIVOT ARRAY
****************************

``PIVOT ARRAY`` converts row-level data into a single array column instead of one column per pivoted value.
``UNPIVOT ARRAY`` does the opposite, expanding an array column into one row per array cell.

The array forms exist for wide pivots. A plain :ref:`PIVOT<pivot_unpivot>` creates one output column for every value
listed in its ``IN`` clause, so a query pivoting thousands of values produces thousands of columns and is bounded by
the maximum number of columns. ``PIVOT ARRAY`` creates one column per aggregation regardless of how many values are
listed, so its value list is not bounded by that limit.

Use ``PIVOT ARRAY`` when you are pivoting a large number of values and your client can read an array column. Use
``PIVOT`` when you want each value as a column of its own, which is what most reporting and business intelligence
tools expect.

Syntax
========

.. code-block:: postgres

   SELECT <selected_columns>

   FROM <from_clause>
   [
     PIVOT ARRAY
     (<pivot_expression1> [AS <pivot_expression1_name>] [, <pivot_expression2> [AS <pivot_expression2_name>], ... , <pivot_expressionN> [AS <pivot_expressionN_name>]]
       FOR <column_name>
       IN (<value1>, <value2>, ... , <valueN>)
     )
     [AS <pivoted_result_name>]
   ]
   [
     UNPIVOT ARRAY
     (<array_column>
       FOR <label_column>
       IN (<value1>, <value2>, ... , <valueN>)
     )
     [AS <unpivoted_result_name>]
   ]

   <rest of the query ...>

   pivot_expression := <aggregation function> ( <column being aggregated> )

Parameters
==========

.. list-table:: PIVOT ARRAY
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``pivot_expression``
     - An aggregation over the column being summarized, such as ``SUM(Revenue)``. Each expression produces one array column in the result
   * - ``pivot_expression_name``
     - Optional name for the resulting array column. When omitted, the name of the aggregated column is used
   * - ``column_name``
     - The column whose values are being pivoted
   * - ``value1 ... valueN``
     - The values of ``column_name`` to pivot on. Their order is the order of the cells in the resulting array. Values may be literals or expressions, and must be distinct

.. list-table:: UNPIVOT ARRAY
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``array_column``
     - The array column to expand. This must be a column of an array type, not an expression. Its name is reused in the result, where it holds the scalar value of each cell
   * - ``label_column``
     - The name of the new column holding the value that labels each cell
   * - ``value1 ... valueN``
     - The labels for the array cells, given in cell order starting at the first cell. All the values must share one type. An unquoted word is read as that word's text

Limitations
=================
* The value list of ``PIVOT ARRAY`` and ``UNPIVOT ARRAY`` is not bounded by the maximum number of columns, because the array forms produce one column per aggregation rather than one per value. The plain ``PIVOT`` and ``UNPIVOT`` forms are bounded, as described in :ref:`PIVOT & UNPIVOT<pivot_unpivot>`.
* ``PIVOT ARRAY`` values must be distinct. Repeating a value returns ``Pivot values should be distinct``.
* ``UNPIVOT ARRAY`` requires an array column. Passing a column of any other type returns ``UNPIVOT ARRAY needs an array column``.
* ``UNPIVOT ARRAY`` does not accept an expression in place of the array column. A cast such as ``vals::bigint[]`` is a parsing error.
* The array column and the label column of ``UNPIVOT ARRAY`` must have different names.
* Listing fewer values than the array has cells expands only the listed cells. Cells beyond the end of the list produce no rows.

PIVOT ARRAY Example
====================
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
   (1, 'Product A', '2024-01-02', 120.00),
   (2, 'Product B', '2024-01-02', 180.00);

Pivots the SalesDate column into a single array column.
The ``SUM(Revenue)`` aggregates the Revenue for each product and date combination, and the resulting array holds one
cell per listed date, in the order the dates are listed.

.. code-block:: postgres

   SELECT * FROM (
      SELECT ProductName, SalesDate, Revenue
      FROM Sales
   ) AS SourceTable
   PIVOT ARRAY (
      SUM(Revenue) AS RevenueSums
      FOR SalesDate IN ('2024-01-01', '2024-01-02')
   );

   productname | revenuesums
   ------------+------------------
   Product A   | [100.00, 120.00]
   Product B   | [150.00, 180.00]
   2 rows

Each aggregation produces its own array column. Aggregating twice returns two arrays:

.. code-block:: postgres

   SELECT * FROM (
      SELECT ProductName, SalesDate, Revenue
      FROM Sales
   ) AS SourceTable
   PIVOT ARRAY (
      SUM(Revenue) AS RevenueSums, COUNT(Revenue) AS SaleCounts
      FOR SalesDate IN ('2024-01-01', '2024-01-02')
   );

   productname | revenuesums      | salecounts
   ------------+------------------+------------
   Product A   | [100.00, 120.00] | [1, 1]
   Product B   | [150.00, 180.00] | [1, 1]
   2 rows

A pivot does not filter. A group whose rows all fall outside the listed values still produces a row, with every array
cell set to null.

Comparing PIVOT and PIVOT ARRAY
================================
Both statements below run against the same ``Sales`` data and compute the same sums. They differ only in the shape of
the result: ``PIVOT`` returns one column per date, and ``PIVOT ARRAY`` returns one array column holding both dates.

Using ``PIVOT``, where each date becomes a column of its own. Note that ``PIVOT`` takes its values as double-quoted
names:

.. code-block:: postgres

   SELECT * FROM (
      SELECT ProductName, SalesDate, Revenue
      FROM Sales
   ) AS SourceTable
   PIVOT (
      SUM(Revenue) AS RevenueSum
      FOR SalesDate IN ("2024-01-01", "2024-01-02")
   );

   productname | 2024-01-01_revenuesum | 2024-01-02_revenuesum
   ------------+-----------------------+-----------------------
   Product A   | 100.00                | 120.00
   Product B   | 150.00                | 180.00
   2 rows

Using ``PIVOT ARRAY`` on the same data, where both dates become cells of one array column. Note that ``PIVOT ARRAY``
takes its values as single-quoted literals:

.. code-block:: postgres

   SELECT * FROM (
      SELECT ProductName, SalesDate, Revenue
      FROM Sales
   ) AS SourceTable
   PIVOT ARRAY (
      SUM(Revenue) AS RevenueSums
      FOR SalesDate IN ('2024-01-01', '2024-01-02')
   );

   productname | revenuesums
   ------------+------------------
   Product A   | [100.00, 120.00]
   Product B   | [150.00, 180.00]
   2 rows

Adding a third date adds a third column to the ``PIVOT`` result and a third cell to the ``PIVOT ARRAY`` result. This is
the difference that matters at scale: the width of the ``PIVOT`` result grows with the value list, while the width of
the ``PIVOT ARRAY`` result does not.

UNPIVOT ARRAY Example
======================
Create a table holding monthly revenue as an array

.. code-block:: postgres

   CREATE OR REPLACE TABLE SalesByMonth (
     ProductName varchar(50),
     MonthlyRevenue decimal(10, 2)[]
   );

Populate data

.. code-block:: postgres

   INSERT INTO SalesByMonth (ProductName, MonthlyRevenue) VALUES
   ('Product A', ARRAY[100.00, 120.00, 150.00]),
   ('Product B', ARRAY[150.00, 180.00, 200.00]);

Expands the MonthlyRevenue array into one row per cell. The ``MonthlyRevenue`` column holds the value of each cell in
the result, and the new ``Month`` column holds the label listed for that cell's position.

.. code-block:: postgres

   SELECT ProductName, Month, MonthlyRevenue
   FROM SalesByMonth
   UNPIVOT ARRAY (
      MonthlyRevenue FOR Month IN ('January', 'February', 'March')
   ) AS u;

   productname | month    | monthlyrevenue
   ------------+----------+----------------
   Product A   | January  | 100.00
   Product B   | January  | 150.00
   Product A   | February | 120.00
   Product B   | February | 180.00
   Product A   | March    | 150.00
   Product B   | March    | 200.00
   6 rows

Comparing UNPIVOT and UNPIVOT ARRAY
====================================
Both statements below turn the same monthly revenue into one row per product per month. They differ in the shape of
the input: ``UNPIVOT`` reads three separate columns, and ``UNPIVOT ARRAY`` reads one array column.

The ``UNPIVOT`` form needs the revenue held as one column per month:

.. code-block:: postgres

   CREATE OR REPLACE TABLE SalesByColumn (
     ProductName varchar(50),
     JanuaryRevenue decimal(10, 2),
     FebruaryRevenue decimal(10, 2),
     MarchRevenue decimal(10, 2)
   );

   INSERT INTO SalesByColumn (ProductName, JanuaryRevenue, FebruaryRevenue, MarchRevenue) VALUES
   ('Product A', 100.00, 120.00, 150.00),
   ('Product B', 150.00, 180.00, 200.00);

Using ``UNPIVOT``, where the source is three columns and the label column holds the source column names:

.. code-block:: postgres

   SELECT ProductName, Month, Revenue
   FROM (
      SELECT ProductName, JanuaryRevenue, FebruaryRevenue, MarchRevenue
      FROM SalesByColumn
   ) AS SourceTable
   UNPIVOT (
      Revenue FOR Month IN (JanuaryRevenue, FebruaryRevenue, MarchRevenue)
   ) AS UnpivotTable;

   productname | month           | revenue
   ------------+-----------------+---------
   Product A   | JanuaryRevenue  | 100.00
   Product B   | JanuaryRevenue  | 150.00
   Product A   | FebruaryRevenue | 120.00
   Product B   | FebruaryRevenue | 180.00
   Product A   | MarchRevenue    | 150.00
   Product B   | MarchRevenue    | 200.00
   6 rows

Using ``UNPIVOT ARRAY`` on the same data held as an array, where the label column holds the values you list rather than
column names:

.. code-block:: postgres

   SELECT ProductName, Month, MonthlyRevenue
   FROM SalesByMonth
   UNPIVOT ARRAY (
      MonthlyRevenue FOR Month IN ('January', 'February', 'March')
   ) AS u;

   productname | month    | monthlyrevenue
   ------------+----------+----------------
   Product A   | January  | 100.00
   Product B   | January  | 150.00
   Product A   | February | 120.00
   Product B   | February | 180.00
   Product A   | March    | 150.00
   Product B   | March    | 200.00
   6 rows

The two results carry the same numbers. The labels differ because ``UNPIVOT`` can only name the columns it read, while
``UNPIVOT ARRAY`` takes whatever labels you give it.

Round Trip
===========
Listing the same values in both directions returns the original rows, with the pivoted column holding the values it
started with rather than the array positions.

.. code-block:: postgres

   SELECT ProductName, SalesDate, RevenueSums
   FROM (
      SELECT * FROM (
         SELECT ProductName, SalesDate, Revenue
         FROM Sales
      ) AS SourceTable
      PIVOT ARRAY (
         SUM(Revenue) AS RevenueSums
         FOR SalesDate IN ('2024-01-01', '2024-01-02')
      )
   ) AS p
   UNPIVOT ARRAY (
      RevenueSums FOR SalesDate IN ('2024-01-01', '2024-01-02')
   ) AS u;

   productname | salesdate  | revenuesums
   ------------+------------+-------------
   Product A   | 2024-01-01 | 100.00
   Product B   | 2024-01-01 | 150.00
   Product A   | 2024-01-02 | 120.00
   Product B   | 2024-01-02 | 180.00
   4 rows

See Also
=========
* :ref:`PIVOT & UNPIVOT<pivot_unpivot>` - the forms that produce one column per value
* :ref:`inListJoinThreshold<in_list_join_threshold>` - the flag controlling how large ``IN`` lists are compiled
