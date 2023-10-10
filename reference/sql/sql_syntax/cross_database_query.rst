.. _cross_database_query:

***************************
Cross Database Query
***************************

Cross-database queries allow the retrieval and manipulation of data from different databases within a single SQL statement or transaction. This capability is crucial when information relevant to a query spans multiple databases. By specifying the database context and employing fully qualified object names, such as database.schema.table, it becomes possible to seamlessly integrate and analyze data distributed across diverse databases.

Syntax
==========

.. code-block:: sql

	SELECT 
		<column_name2> [,column_name_2] [, ...]
	FROM 
		<database_name>.<schema_name>.<table_name>
	JOIN 
		<database_name>.<schema_name>.<table_name>
	ON	
	<database_name>.<schema_name>.<table_name>.<column_name> =<database_name>.<schema_name>.<table_name>.<column_name>
	WHERE 
		<condition>
		
Parameters
===========

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``column_name``
     - The column to perform a ``JOIN`` operation on
   * - ``database_name``
     - The SQreamDB database to perform a ``JOIN`` operation on
   * - ``schema_name``
     - The schema name of the database to perform a ``JOIN`` operation on
   * - ``table_name`` 
     - The table to perform a ``JOIN`` operation on
   * - ``condition``
     - The condition for performing a ``JOIN`` operation
	 
Examples
=========

Querying data from two tables in different databases:

.. code-block:: sql

	SELECT *
	FROM database1.schema1.table1 t1
	JOIN database2.schema2.table2 t2
	ON t1.id = t2.id
	WHERE t1.date >= '2022-01-01' AND t2.status = 'active';

Querying data from two tables in different schemas and databases:

.. code-block:: sql

	SELECT *
	FROM database1.schema1.table1 t1
	JOIN database2.schema2.table2 t2
	ON t1.id = t2.id
	WHERE t1.date >= '2022-01-01' AND t2.status = 'active';
	
Querying data from two tables in different databases with a where clause:
	
.. code-block:: sql
	
	SELECT t1.*, t2.*
	FROM database1.schema1.table1 t1
	JOIN database2.schema2.table2 t2
	ON t1.id = t2.id
	WHERE t1.date >= '2022-01-01' AND t2.status = 'active';
	
Querying data from three tables in different databases:

.. code-block:: sql

	SELECT t1.*, t2.*, t3.*
	FROM database1.schema1.table1 t1
	JOIN database2.schema2.table2 t2
	ON t1.id = t2.id
	JOIN database3.schema3.table3 t3
	ON t2.id = t3.id
	WHERE t1.date >= '2022-01-01' AND t2.status = 'active' AND t3.quantity > 10;