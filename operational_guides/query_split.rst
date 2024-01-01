.. _query_split:

****************************
Query Split
****************************

The split query operation optimizes long-running queries by executing them in parallel on different GPUs, reducing overall runtime. This involves breaking down a complex query into parallel executions on small data subsets. To ensure an ordered result set aligned with the original complex query, two prerequisites are essential. First, create an empty table mirroring the original result set's structure. Second, define the ``@@SetResult`` operator to split the query using an ``INTEGER``, ``DATE``, or ``DATETIME`` column, as these types are compatible with the operator's ``min`` and ``max`` variables.   

Splitting is exclusive to the UI, utilizing Meta-scripting, a unique UI feature. Keep in mind that not all queries benefit, as this method introduces overhead runtime. 

.. contents::
   :local:
   :depth: 1
   
Syntax
========

Creating an empty table mirroring the original query result set's structure using the same DDL: 

.. code-block:: sql

	CREATE TABLE <final_result_table> 
	AS 
	(
	  SELECT 
	    <column_to_split_by> [,...]
	  FROM 
	    <my_table>
	  WHERE
	    <false_filter>
	)
	
	-- A false_filter example: 1=2
	
Defining the ``@@setresult`` operator to split the original query using an ``INTEGER``, ``DATE``, or ``DATETIME`` column with ``min`` and ``max`` variables. If the column you're splitting by is used in a ``WHERE`` clause in the original query, use a ``WHERE`` clause when setting the ``SetResult`` operator as well.

.. code-block:: sql
	
	@@SetResult minMax
	SELECT 
	  MIN(<column>) AS min, 
	  MAX(<column>) AS max 
	FROM 
	  <my_table>
	[WHERE 
	  <column> BETWEEN
	   -- Integer Range:
	   1 AND 100 
	   | -- Date Range:
	   '2022-01-01' AND '2022-12-31' 
	   | -- DateTime Range:
	   '2022-01-01 01:24:00:000' AND '2022-12-31 08:51:24:000'] 

Defining the operator that determines the number of instances (splits) based on the data type of the column by which the query is split:
	
* **INTEGER column:** use the ``@@SplitQueryByNumber`` operator
	
.. code-block:: sql
	
	@@SplitQueryByNumber instances = <number of instances>, from = minMax[0].min, to = minMax[0].max
	INSERT INTO <final_result_table>
	(
	  SELECT 
	    <column_to_split_by> [,...]
	  FROM
	    <my_table>
	  WHERE
	  <column_to_split_by> BETWEEN ${from} and ${to}
	)
	
* **DATE column:** use the ``@@SplitQueryByDate`` operator

.. code-block:: sql
	
	@@SplitQueryByDate instances = <number of instances>, from = minMax[0].min, to = minMax[0].max
	INSERT INTO <final_result_table>
	(
	  SELECT
	    <column_to_split_by> [,...]
	  FROM 
	    <my_table>
	  WHERE 
	    <column_to_split_by> BETWEEN ${from} and ${to}
	)
	
* **DATETIME column:** use the ``@@SplitQueryByDateTime`` operator

.. code-block:: sql
	
	@@SplitQueryByDateTime instances = <number of instances>, from = minMax[0].min, to = minMax[0].max
	INSERT INTO <final_result_table>
	(
	  SELECT 
	    <column_to_split_by> [,...]
	  FROM 
	    <my_table>
	  WHERE <column_to_split_by> BETWEEN ${from} and ${to}
	)
	
Outputting the results of your small queries by running a query that gathers the results of all small queries into the initially created empty table.

.. code-block:: sql

	-- Basic execution for queries which do not use aggregations:
	
	SELECT * 
	FROM 
	  <final_result_table>
	;
	
	-- Execution for queries which use aggregations:
	
	SELECT 
	  <column1>, [,...],
	  [SUM([DISTINCT] expr) AS <sum_column>], 
	  [SUM(count_column) AS <sum_count_column>],
	  [SUM(avg_column1) / SUM(avg_column2) AS <avg_column>]
	FROM 
	  <final_result_table>
	GROUP BY 
	  <column1>, <column2> [,...]
	ORDER BY 
	  <column4>
	
	-- Do not use a WHERE clause

Example
========

.. contents::
   :local:
   :depth: 1

Creating a Sample Table and Query
----------------------------------

To split your first query, create the following table and insert data into it:

.. code-block:: sql

	CREATE TABLE MyTable (
	  id INT,
	  name TEXT NOT NULL,
	  age INT,
	  salary INT,
	  quantity INT 
	  );

	-- Inserting data into the table
	INSERT INTO MyTable (id, name, age, salary, quantity)
	VALUES
	  (1, 'John', 25, 50000, 10),
	  (2, 'Jane', 30, 60000, 20),
	  (3, 'Bob', 28, 55000, 15),
	  (4, 'Emily', 35, 70000, 18),
	  (5, 'David', 32, 62000, 22),
	  (6, 'Sarah', 27, 52000, 12),
	  (7, 'Michael', 40, 75000, 17),
	  (8, 'Olivia', 22, 48000, 25),
	  (9, 'William', 31, 58000, 14),
	  (10, 'Sophia', 29, 56000, 19),
	  (11, 'Liam', 26, 51000, 13),
	  (12, 'Emma', 33, 64000, 16),
	  (13, 'Daniel', 24, 49000, 23),
	  (14, 'Ava', 37, 69000, 21),
	  (15, 'Matthew', 23, 47000, 28),
	  (16, 'Ella', 34, 67000, 24),
	  (17, 'James', 28, 55000, 11),
	  (18, 'Grace', 39, 72000, 26),
	  (19, 'Benjamin', 30, 60000, 18),
	  (20, 'Chloe', 25, 50000, 14),
	  (21, 'Logan', 38, 71000, 20),
	  (22, 'Mia', 27, 52000, 16),
	  (23, 'Christopher', 32, 62000, 22),
	  (24, 'Aiden', 29, 56000, 19),
	  (25, 'Lily', 36, 68000, 15),
	  (26, 'Jackson', 31, 58000, 23),
	  (27, 'Harper', 24, 49000, 12),
	  (28, 'Ethan', 35, 70000, 17),
	  (29, 'Isabella', 22, 48000, 25),
	  (30, 'Carter', 37, 69000, 14),
	  (31, 'Amelia', 26, 51000, 21),
	  (32, 'Lucas', 33, 64000, 19),
	  (33, 'Abigail', 28, 55000, 16),
	  (34, 'Mason', 39, 72000, 18),
	  (35, 'Evelyn', 30, 60000, 25),
	  (36, 'Alexander', 23, 47000, 13),
	  (37, 'Addison', 34, 67000, 22),
	  (38, 'Henry', 25, 50000, 20),
	  (39, 'Avery', 36, 68000, 15),
	  (40, 'Sebastian', 29, 56000, 24),
	  (41, 'Layla', 31, 58000, 11),
	  (42, 'Wyatt', 38, 71000, 26),
	  (43, 'Nora', 27, 52000, 19),
	  (44, 'Grayson', 32, 62000, 17),
	  (45, 'Scarlett', 24, 49000, 14),
	  (46, 'Gabriel', 35, 70000, 23),
	  (47, 'Hannah', 22, 48000, 16),
	  (48, 'Eli', 37, 69000, 25),
	  (49, 'Paisley', 28, 55000, 18),
	  (50, 'Owen', 33, 64000, 12);

Next, we'll split the following query:

.. code-block:: sql

	SELECT
	  age,
	  COUNT(*) AS total_people,
	  AVG(salary) AS avg_salary,
	  SUM(quantity) AS total_quantity,
	  SUM(CASE WHEN quantity > 20 THEN 1 ELSE 0 END) AS high_quantity_count,
	  SUM(CASE WHEN age BETWEEN 25 AND 30 THEN salary ELSE 0 END) AS total_salary_age_25_30
	FROM
	  MyTable
	WHERE
	  salary > 55000
	GROUP BY
	  age
	ORDER BY
	  age;

Splitting the Query
--------------------

1. Prepare an empty table mirroring the original query result set’s structure with the same DDL, using a false filter under the ``WHERE`` clause.
 
   An **empty** table named ``FinalResult`` is created.	
	
.. code-block:: sql

	CREATE OR TABLE FinalResult
	AS
	(
	  SELECT
	  age,
	  COUNT(*) AS total_people,
	  AVG(salary) AS avg_salary,
	  SUM(quantity) AS total_quantity,
	  SUM(CASE WHEN quantity > 20 THEN 1 ELSE 0 END) AS high_quantity_count,
	  SUM(CASE WHEN age BETWEEN 25 AND 30 THEN salary ELSE 0 END) AS total_salary_age_25_30
	FROM
	  MyTable
	WHERE
	  1=0
	  AND salary > 55000
	GROUP BY
	  age
	ORDER BY
	  age
	  );		
		
2. Set the ``@@setresult`` operator to split the original query using ``min`` and ``max`` variables.
	
.. code-block:: sql

	@@ SetResult minMax
	SELECT min(id) as min, max(id) as max 
	FROM mytable
	;

3. Set the ``@@SplitQueryByNumber`` operator with the number of instances (splits) of your query (here based on an ``INTEGER`` column), and set the ``between ${from} and ${to}`` clause with the name of the column by which you wish to split your query (here the query is split by the ``id`` column.

.. code-block:: sql

	@@SplitQueryByNumber instances = 4, from = minMax[0].min, to = minMax[0].max
	INSERT INTO FinalResult
	(
	SELECT
	  age,
	  COUNT(*) AS total_people,
	  AVG(salary) AS avg_salary,
	  SUM(quantity) AS total_quantity,
	  SUM(CASE WHEN quantity > 20 THEN 1 ELSE 0 END) AS high_quantity_count,
	  SUM(CASE WHEN age BETWEEN 25 AND 30 THEN salary ELSE 0 END) AS total_salary_age_25_30
	FROM
	  MyTable
	WHERE
	  id between ${from} and ${to}
	  AND salary > 55000
	GROUP BY
	  age
	ORDER BY
	  age
	  );
	
4. Create a query that gathers the results of all instances (splits) into the empty table you created in step 1.

.. code-block:: sql

	SELECT
	  age,
	  SUM(total_people) AS total_people,
	  SUM(avg_salary) / SUM(avg_salary) AS avg_salary,
	  SUM(total_quantity) AS total_quantity,
	  SUM(high_quantity_count) AS high_quantity_count,
	  SUM(total_salary_age_25_30) AS total_salary_age_25_30
	FROM
	  FinalResult
	GROUP BY
	  age
	ORDER BY
	  age
	  ;

5. Arrange ALL five sequential scripts on one Editor tab.

6. Ensure that EACH script ends with a ``;``.

7. Ensure that the **Execute** button is set to **All** so that all five queries are consecutively executed. 

8. Select the **Execute** button.

   All five scripts are executed, resulting in the splitting of the initial query and a table containing the final result set.

Best Practices
================

General
--------

* When incorporating the ``LIMIT`` clause or any aggregate function in your query, split the query based only on a ``GROUP BY`` column. If no relevant columns are present in the ``GROUP BY`` clause, the query might not be suitable for splitting. If you are not using aggregations, it's best to split the query using a column that appears in the a ``WHERE`` or ``JOIN`` clause.

* When using the ``JOIN`` key, it is usually better to use the key of the smaller table.

* For simple queries involving just one table, splitting is unlikely to enhance performance.

Choosing a Column to Split by
------------------------------

The column you split by must be sorted or mostly sorted. Meaning, that even if the column values may not be perfectly ordered, they still follow a general sequence or trend.
	
Aggregation Best Practices
--------------------------

Aggregation functions, or special functions need to have adjustments in the query that gathers the results of all instances (splits) into the empty table:

* ``COUNT`` becomes ``SUM``

* ``AVERAGE`` is split into two columns in the split query and then merged as ``AVERAGE`` in the output query


Special functions should be split into different columns as well - **What special functions?**

Date as Number best practices
-------------------------------

When date is stored as number, using the number of workers as the instances number may not result in the expected way.
e.g. if date run from 20210101 to 20210630 splitting to 8 will result in 6 relevant splits, as SQream only checks min and max and splits accordingly (20210630-20210101)/8. we get an instance of empty data with dates ranging from 20210432 to 20210499 (not really dates, but real numbers).
In this case, we need to adjust the number of instance to get the right size splits. In the above example we need to split to 64, and each worker will run 3 splits with actual data.

Using the ``SetResult``
-------------------------

When the column you split by is used in a ``WHERE`` clause in the original query, add it with the ``WHERE`` clause when you set the ``SetResult`` operator.

.. code-block::

	@@ SetResult minMax
	SELECT min(ship_dates) AS min, max(ship_dates) AS max FROM shipments
	/*optional - WHERE ship_dates BETWEEN '1995-01-01' AND '1996-01-01'*/
	;
	
Include?
-----------

* Setting the column boundaries for the split - This is an optional query, but very useful, and can only be optional if you know in advance the boundaries.

* The query that outputs the results from the table we created in the first query - This is an optional query, but most use cases will require have it and if we created the first query and used INSERT INTO in the splitting we have to use it.
	
* Limit and group by together, can significantly reduce runtime.
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	