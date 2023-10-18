.. _cross_database_query:

***************************
Cross-Database Query
***************************

Cross-database queries allow the retrieval and manipulation of data from different databases within a single SQL statement or transaction. This capability is crucial when information relevant to a query spans multiple databases. By specifying the database context and employing fully qualified object names, such as database.schema.table, it becomes possible to seamlessly integrate and analyze data distributed across diverse databases.

Syntax
==========

.. code-block:: sql

	-- SELECT statement

	SELECT 
		<column_name1>,
		<column_name2>,
		...
	FROM 
		<database_name>.<schema_name>.<table_name> AS <alias1>
	JOIN 
		<database_name>.<schema_name>.<table_name> AS <alias2>
	ON 
		<alias1>.<join_column> = <alias2>.<join_column>
	WHERE 
		<condition1>
		AND <condition2>

	-- CREATE TABLE statement

	CREATE TABLE 
		<database_name>.<schema_name>.<table_name> (
			<column_name1> <data_type1>,
			<column_name2> <data_type2>,
			...
		)

	-- CREATE FOREIGN TABLE statement

	CREATE FOREIGN TABLE 
		<foreign_database_name>.<foreign_schema_name>.<foreign_table_name> (
			<column_name1> <data_type1>,
			<column_name2> <data_type2>,
			...
			)

	-- ALTER TABLE statement

	ALTER TABLE 
		<database_name>.<schema_name>.<table_name>
	ADD COLUMN 
		<new_column_name> <new_column_data_type>

	-- CREATE VIEW statement

	CREATE VIEW 
		<database_name>.<schema_name>.<view_name> (<column_name1>, <column_name2>, ...)
	AS 
		SELECT 
			<alias1>.<column_name1>,
			<alias1>.<column_name2>,
			...
		FROM 
			<database_name1>.<schema_name1>.<table_name1> AS <alias1>
		JOIN 
			<database_name2>.<schema_name2>.<table_name2> AS <alias2>
		ON 
			<alias1>.<join_column> = <alias2>.<join_column>
		WHERE 
			<condition1>
			AND <condition2>

	-- INSERT INTO statement

	INSERT INTO 
		<database_name>.<schema_name>.<table_name> (<column_name1>, <column_name2>, ...)
	VALUES 
		(<value1>, <value2>, ...)

	-- UPDATE statement

	UPDATE 
		<database_name>.<schema_name>.<table_name>
	SET 
		<column_name1> = <new_value1>,
		<column_name2> = <new_value2>
	WHERE 
		<condition>

	-- DELETE statement

	DELETE FROM 
		<database_name>.<schema_name>.<table_name>
	WHERE 
		<condition>

	-- TRUNCATE TABLE statement

	TRUNCATE TABLE 
		<database_name>.<schema_name>.<table_name>

	-- DROP TABLE statement

	DROP TABLE 
		<database_name>.<schema_name>.<table_name>


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
	
Set default schema:

.. code-block:: sql

ALTER DEFAULT SCHEMA 