.. _sql_data_type_array:

*****
Array
*****

The ``ARRAY`` data type offers a convenient way to store ordered collections of elements in a single column. It provides storage efficiency by allowing multiple values of the same data type to be compactly stored, optimizing space utilization and enhancing database performance. Working with arrays simplifies queries as operations and manipulations can be performed on the entire array, resulting in more concise and readable code.

Each data type has its companion array type, such as ``INT[]`` for integers and ``TEXT[]`` for text values. An array represents a sequence of zero or more elements of the same data type. Arrays in the same column can contain varying numbers of elements across different rows. Arrays can include null values, eliminating the need for separate SQL declarations.

Syntax
======

Defining an array is done by appending the ``[]`` notation to a supported data type, for example, ``int[]`` for an array of integers.

.. code-block::

	CREATE TABLE <table_name> (<column1> TEXT[], <column2> INT[])
	
	INSERT INTO TABLE <table_name> VALUES ARRAY[<'a','b','c'>], ARRAY[<1,2,3>]

Size
====

The maximum size of an array, indicating the number of elements it can hold, is 65535. You have the option to specify the array size, providing a maximum allowed size, while each row can have a different number of elements up to the specified maximum. If the array size is not specified, the maximum size is assumed. 

Supported Operators
===================

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Operator
     - Description
   * - Literals
     - An array literal can be created using the ``ARRAY`` operator. For example, ``ARRAY[1,2,3];``
   * - Mapping
     - Parquet, ORC, JSON, and AVRO array types may be mapped into SQreamDB arrays
   * - Indexing
     - Access to specific elements within the array by using a zero-based index. For example, ``arr[2]`` returns the second array element
   * - ``UNNEST``
     - Converts arrayed elements into a set of rows
   * - Concatenate ``||``
     - Converts arrayed elements into one string
   * - 
     - 
   * - 
     - 
   * - 
     - 
   * - 
     - 
   * - 
     - 
   * - 
     - 
   * - 
     - 
   * - 
     - 

Examples
========
Creating a table with arrayed columns:

.. code-block::

	CREATE TABLE array (column1 TEXT[], column2 INT[]);
	
Inserting array values into a table:

.. code-block::
	
	INSERT INTO TABLE array VALUES ARRAY['a','b','c'], ARRAY[1,2,3];
	
Converting arrayed elements into a set of rows:

.. code-block::
	
	SELECT UNNEST(ARRAY['a','b','c'], ARRAY[1,2,3]);

.. code-block::
	
	column1	| column2
	--------+----------
	a       | 1
	b       | 2
	c       | 3
	
Updating table values:

.. code-block::

	INSERT INTO TABLE array VALUES ARRAY['a','b','c'], ARRAY[1,2,3];
	
	UPDATE array SET arr[0] = '{7,8,9}';
	
	SELECT * FROM array;
	
.. code-block::

	column1	| column2
	--------+----------
	
	