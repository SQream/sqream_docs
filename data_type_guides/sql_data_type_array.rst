.. _sql_data_type_array:

*****
Array
*****

The ``ARRAY`` data type offers a convenient way to store ordered collections of elements in a single column. It provides storage efficiency by allowing multiple values of the same data type to be compactly stored, optimizing space utilization and enhancing database performance. Working with ``ARRAY`` simplifies queries as operations and manipulations can be performed on the entire ``ARRAY``, resulting in more concise and readable code.

An ``ARRAY`` represents a sequence of zero or more elements of the same data type. Arrays in the same column can contain varying numbers of elements across different rows. Arrays can include null values, eliminating the need for separate SQL declarations.

Each data type has its companion ``ARRAY`` type, such as ``INT[]`` for integers and ``TEXT[]`` for text values.

.. seealso:: A full list of :ref:`data types<supported_data_types>` supported by SQreamDB.

Syntax
======

Defining an ``ARRAY`` is done by appending the ``[]`` notation to a supported data type, for example, ``INT[]`` for an array of integers.

.. code-block:: sql

	CREATE TABLE <table_name> (<column1> TEXT[], <column2> INT[])
	
	INSERT INTO TABLE <table_name> VALUES ARRAY[<'a','b','c'>], ARRAY[<1,2,NULL>]

Size
====

The maximum size of an ``ARRAY``, indicating the number of elements it can hold, is 65535. You have the option to specify the size of an ``ARRAY``, providing a maximum allowed size, while each row can have a different number of elements up to the specified maximum. If the ``ARRAY`` size is not specified, the maximum size is assumed. 

Supported Operators
===================

.. list-table::
   :widths: 8 40
   :header-rows: 1
   
   * - Operator
     - Description
   * - Literals ``ARRAY []``
     - Literals are created using the ``ARRAY`` operator. For example, ``ARRAY[1,2,3]``
   * - Mapping
     - Parquet, ORC, JSON, and AVRO ``ARRAY`` types may be mapped into SQreamDB ``ARRAY``
   * - Indexing
     - Access to specific elements within the array by using a **zero-based index**. For example, ``SELECT <column_name>[2] FROM <table_name>`` returns the third element of the specified column
   * - ``UNNEST``
     - Converts the arrayed elements within a single row into a set of rows. For example, ``SELECT UNNEST <column_name> FROM <table_name>``
   * - Concatenate ``||``
     - Converts arrayed elements into one string. For example, ``SELECT <column_name> || <column2_name> FROM <table_name>``
   * - ``array_length``
     - Returns the number of arrayed elements within the specified column. For example, ``SELECT array_length(<column_name>) FROM <table_name>``
   * - ``array_position``
     - Locates the position of the specified value within the specified array. For example, ``SELECT array_position(<column_name>,<value>) FROM <table_name>;``. Returns ``NULL`` if the value is not found.
   * - ``array_remove``
     - Returns the specified ``ARRAY`` column with the specified value deducted. For example, ``SELECT array_remove(<column_name>,<value>) FROM <table_name>;``
   * - ``array_replace``
     - Enables replacing values within an ``ARRAY`` column. For example, ``SELECT array_replace(<column_name>,<value_to_replace>,<replacing_value>) FROM <table_name>;``
   * - Limiting number of arrayed elements 
     - You may limit the number of arrayed elements within an ``ARRAY``. For example, ``CREATE TABLE <table_name> (<column1> TEXT[]);``
   * - Creating different column types
     - You may create a table that has arrayed columns and non-arrayed columns. For example, ``CREATE TABLE <table_name> (<column1> TEXT('a','b','c')['d']);`` 


Examples
========

Creating a table with arrayed columns:

.. code-block:: sql

	CREATE TABLE my_array (clmn1 TEXT[], clmn2 TEXT[], clmn3 INT[]);
	
Inserting arrayed values into a table:

.. code-block:: sql
	
	INSERT INTO my_array VALUES (ARRAY['1','2','3'], ARRAY['4','5','6'], ARRAY[7,8,9,10]);
	
Converting arrayed elements into a set of rows:

.. code-block:: sql
	
	SELECT UNNEST(ARRAY['1','2','3'], ARRAY['4','5','6']);

.. code-block:: console
	
	clmn1     | clmn2     | clmn3
	----------+-----------+-----------
	"1"       | "4"       | [7,8,9,10]
	"2"       | "5"       |
	"3"       | "6"       |
	
Updating table values:

.. code-block:: sql
	
	UPDATE my_array SET clmn1[0] = 'A';
	
	SELECT * FROM my_array;
	
.. code-block:: console

	clmn1                | clmn2            | clmn3
	---------------------+------------------+-----------
	["A","1","2","3"]    | ["4","5","6"]    | [7,8,9,10]

Limitations
===========

