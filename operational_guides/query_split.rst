.. _query_split:

****************************
Query Split
****************************

The split query operation optimizes long-running queries by executing them in parallel on different GPUs, thereby reducing overall run time. It's crucial to note that not every query may benefit from this approach, as the splitting mechanism introduces some overhead runtime. Additionally, it's emphasized that splitting can only be performed in the UI, leveraging Meta-scripting, a feature currently exclusive to the UI environment.

The four stages of using the query split operation are:

* Creating an empty table with an identical DDL of what would have been the result set table if we were to run the query we wish to split into 4 small queries. This empty table would eventually hold the results of all 4 small queries.

* Deciding by which column to split your query by. Columns to split by can only be of ``INTEGER``, ``DATE``, or ``DATETIME`` data types, or otherwise, an Identity column. 

* Executing the query split  

* Executing a query that collects the results of all 4 small queries into our empty table.

.. contents::
   :local:
   :depth: 1
   
Syntax
========

**Creating an empty table that is based on the query we wish to split:**

.. code-block:: sql

	CREATE TABLE <final_result_table> AS (
	SELECT <column_to_split_by> [,...]
	FROM <my_table>
	WHERE (<false_filter>)
	);
	
	#A false_filter example: (1=2)
	
	
**Using the @@SetResult operator to create a minMax variable:**

The ``minMax`` variable is used to define minimum and maximum values of ``INTEGER``, ``DATE``, ``DATETIME`` or Identity columns by which we can split our query.
	 
.. code-block:: sql
	 
	@@SetResult minMax
	SELECT min(<integer_column>) AS min, max(<integer_column>) AS max 
	FROM <my_table>
	[WHERE <condition>]
	;
	
**Splitting a query using an INTEGER column:**
	
Using the ``@@SplitQueryByNumber`` operator to create an ``instances`` variable.
	
.. code-block:: sql
	
	@@SplitQueryByNumber instances = <number of instances>, from = minMax[0].min, to = minMax[0].max
	INSERT INTO <final_result_table>
	SELECT <column_to_split_by> [,...]
	FROM <my_table>
	WHERE <column_to_split_by> between ${from} and ${to}
	);
	
**Splitting a query using a DATE column:**
	
Using the ``@@SplitQueryByDate`` operator to create an ``instances`` variable.

.. code-block:: sql
	
	@@SplitQueryByDate instances = <number of instances>, from = minMax[0].min, to = minMax[0].max
	INSERT INTO <final_result_table>
	SELECT <column_to_split_by> [,...]
	FROM <my_table>
	WHERE <column_to_split_by> between ${from} and ${to}
	);
	
**Splitting a query using a DATETIME column:**
	
Using the ``@@SplitQueryByDateTime`` operator to create an ``instances`` variable.

.. code-block:: postgres
	
	@@SplitQueryByDateTime instances = <number of instances>, from = minMax[0].min, to = minMax[0].max
	INSERT INTO <final_result_table>
	SELECT <column_to_split_by> [,...]
	FROM <my_table>
	WHERE <column_to_split_by> between ${from} and ${to}
	);
	
**Outputting the results of our 4 small queries:**

.. code-block:: sql

	#Basic execution for queries which do not use aggregations:
	
	SELECT * 
	FROM <final_result_table>
	;
	
	#Execution for queries which use aggregations:
	
	SELECT <column1>, <column2> [,...], SUM(<column4>)
	FROM <final_result_table>
	GROUP BY <column1>, <column2> [,...]
	ORDER BY SUM(<column4>)
	);
	
	##Do not use a WHERE clause

