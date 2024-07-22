.. _sql_data_type_array:

*****
Array
*****

The ``ARRAY`` data type offers a convenient way to store ordered collections of elements in a single column. It provides storage efficiency by allowing multiple values of the same data type to be compactly stored, optimizing space utilization and enhancing database performance. Working with ``ARRAY`` simplifies queries as operations and manipulations can be performed on the entire ``ARRAY``, resulting in more concise and readable code.

An ``ARRAY`` represents a sequence of zero or more elements of the same data type. Arrays in the same column can contain varying numbers of elements across different rows. Arrays can include null values, eliminating the need for separate SQL declarations.

Each data type has its companion ``ARRAY`` type, such as ``INT[]`` for integers and ``TEXT[]`` for text values.

You may use the ``ARRAY`` data type with the :ref:`Blue connectors <connecting_to_blue>`.

The maximum size of an ``ARRAY``, indicating the number of elements it can hold, is 65535. You have the option to specify the size of an ``ARRAY``, providing a maximum allowed size, while each row can have a different number of elements up to the specified maximum. If the ``ARRAY`` size is not specified, the maximum size is assumed. 

.. seealso:: A full list of supported :ref:`data types<supported_data_types>` 
             
             The full :ref:`create_foreign_table` syntax

Syntax
======

Defining an ``ARRAY`` is done by appending the ``[]`` notation to a supported data type, for example, ``INT[]`` for an array of integers.

.. code-block:: sql

	CREATE [ OR REPLACE ] [ FOREIGN ] TABLE [ "<schema_name>" ]."<table_name>" (
	  [ (<column1> <TEXT> [], <column2> <INT> []) [, ...]
	)
	  [ FOREIGN DATA ] WRAPPER fdw_name
	  [ OPTIONS ( option_def [, ...  ] ) ]

	INSERT INTO
	  TABLE <table_name>
	VALUES
	  (ARRAY ['a','b','c'], ARRAY [1,2,NULL])


Supported Operators
===================

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Operator
     - Description
     - Example	 
   * - Literals ``ARRAY []``
     - Literals are created using the ``ARRAY`` operator
     - ``ARRAY[1,2,3]``
   * - Mapping
     - Parquet, ORC, JSON, and AVRO ``ARRAY`` types may be mapped into SQream Blue ``ARRAY``
     - See extended section under **Examples** 
   * - Indexing
     - Access to specific elements within the array by using a **zero-based index**
     - ``SELECT (<column_name>[2]) FROM <table_name>`` returns the third element of the specified column  
   * - ``UNNEST``
     - Converts the arrayed elements within a single row into a set of rows
     - ``SELECT UNNEST(<column_name>) FROM <table_name>``  
   * - Concatenate ``||``
     - Converts arrayed elements into one string
     - * ``SELECT (<column_name>) || (<column2_name>) FROM <table_name>`` 
       * ``SELECT (<column_name>) || ARRAY[1,2,3] FROM <table_name>``  
   * - ``array_length``
     - Returns the number of arrayed elements within the specified column
     - ``SELECT array_length(<column_name>) FROM <table_name>``  
   * - ``array_position``
     - Locates the position of the specified value within the specified array. Returns ``NULL`` if the value is not found
     - ``SELECT array_position(<column_name>,<value>) FROM <table_name>;``  
   * - ``array_remove``
     - Returns the specified ``ARRAY`` column with the specified value deducted
     - ``SELECT array_remove(<column_name>,<value>) FROM <table_name>;``  
   * - ``array_replace``
     - Enables replacing values within an ``ARRAY`` column
     - ``SELECT array_replace(<column_name>,<value_to_replace>,<replacing_value>) FROM <table_name>;``  
   * - Limiting number of arrayed elements 
     - You may limit the number of arrayed elements within an ``ARRAY``
     - Limiting the number of arrayed elements to 4: ``CREATE TABLE <table_name> (<column1> TEXT[4]);``	 
   * - Aggregation
     - The ``array_agg()`` function arrays groups created using the ``GROUP BY`` clause
     - ``CREATE TABLE t2 (x INT, y INT);``
       
	``SELECT x, array_agg(y) FROM t2 GROUP BY x;``
   * - Sorting
     - ``TEXT[]`` elements are considered together as a single text, and comparisons are made based on their lexicographic order. In contrast, for arrays of non-TEXT data types, comparisons are performed on the individual elements of the arrays
     - ``CREATE TABLE t (x TEXT[]);``
	 
	``INSERT INTO t VALUES (ARRAY['1']),(ARRAY['1','22']),(ARRAY['1','3']);``
	``SELECT x FROM t ORDER BY x;``
	
	Output:
	           
	['1']      
	           
	['1','22'] 
	           
	['1','3']
	
Examples
========

``ARRAY`` Statements
--------------------

Creating a foreign table with arrayed columns:

.. code-block:: sql

	CREATE FOREIGN TABLE
	  my_array (
	    clmn1 TEXT [],
	    clmn2 TEXT [],
	    clmn3 INT [],
	    clmn4 NUMERIC(38, 20) []
	)
	WRAPPER
	  parquet_fdw
	OPTIONS
	   (LOCATION = 'gs://blue_docs/my_array.parquet',
	  );
	
Inserting arrayed values into a table:

.. code-block:: sql
	
	INSERT INTO
	  my_array
	VALUES
	  (
	    ARRAY ['1','2','3'],
	    ARRAY ['4','5','6'],
	    ARRAY [7,8,9,10],
	    ARRAY [0.4354,0.5365435,3.6456]
	  );
	
Converting arrayed elements into a set of rows:

.. code-block:: sql
	
	SELECT
	  UNNEST(clmn1) FROM my_array;

.. code-block:: console
	
	 clmn1  |     
	--------+
	 1      |     
	 2      |       
	 3      |      

Updating table values:

.. code-block:: sql
	
	UPDATE
	  my_array
	SET
	  clmn1 [0] = 'A';
	
	SELECT
	  *
	FROM
	  my_array;
	
.. code-block:: console

	clmn1                | clmn2            | clmn3
	---------------------+------------------+-----------
	["A","1","2","3"]    | ["4","5","6"]    | [7,8,9,10]

Ingesting Arrayed Data from External Files
------------------------------------------

Consider the following JSON file named ``t``, located under ``/tmp/``:

.. code-block:: json


    {
        "name": "Avery Bradley",
        "age": 25,
        "position": "PG",
        "years_in_nba": [
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021
        ]
    },
    {
        "name": "Jae Crowder",
        "age": 25,
        "position": "PG",
        "years_in_nba": [
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021
        ]
    },
    {
        "name": "John Holland",
        "age": 27,
        "position": "SG",
        "years_in_nba": [
            2017,
            2018
        ]
    }

Execute the following statement:

.. code-block:: sql

	CREATE FOREIGN TABLE nba (name text, age int, position text, years_in_nba int [])
	WRAPPER
	  json_fdw
	OPTIONS
	  (location = '/tmp/nba.json');
	
	SELECT
	  *
	FROM
	  nba;
	
Output:

.. code-block:: console

	name           | age    | position    | years_in_nba
	---------------+--------+-------------+-------------------------------------------------------------------------
	Avery Bradley  | 25     | PG          | [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
	Jae Crowder    | 25     | PG          | [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
	John Holland   | 27     | SG          | [2017, 2018]

Limitations
===========

Casting Limitations
-------------------

``NUMERIC``
"""""""""""

Numeric data types smaller than ``INT``, such as ``TINYINT``, ``SMALLINT``, and ``BOOL``, must explicitly be cast.

.. code-block:: sql

	CREATE OR REPLACE TABLE my_array (clmn1 tinyint []); 
	SELECT array_replace(clmn1 , 4::tinyint, 5::tinyint) FROM my_array;  
	
	CREATE OR REPLACE TABLE my_array (clmn1 bool []); 
	SELECT array_replace(clmn1 , 0::bool, 1::bool) FROM my_array;
	
``TEXT``
""""""""

Casting ``TEXT`` to non-``TEXT`` and non-``TEXT`` to ``TEXT`` data types is not supported.
	
.. code-block:: sql


	CREATE TABLE t_text (xtext TEXT[]);
	CREATE TABLE t_int (xint INT[]);
	INSERT INTO t_int VALUES (array[1,2,3]);
	INSERT INTO t_text SELECT xint::TEXT[] FROM t_int;

Connectors
----------

``ODBC``
""""""""

Please note that the ODBC connector does not support the use of ``ARRAY``. If your database schema includes ``ARRAY`` columns, you may encounter compatibility issues when using this connector.

``Pysqream``
""""""""""""

Please note that SQLAlchemy does not support the ``ARRAY`` data type.

Functions
---------

``|| (Concatenate)``
""""""""""""""""""""

Using the ``||`` (Concatenate) function with two different data types requires explicit casting.

.. code-block:: sql

	SELECT (clmn1, 4::tinyint) || (clmn2, 5::tinyint) FROM my_array;
	
``UNNEST``
""""""""""

It is possible to use the ``UNNEST`` operator within a statement only once.

Window
""""""

Window functions are not supported.
