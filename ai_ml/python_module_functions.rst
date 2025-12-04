.. _python_table_functions:

Python Functions
------------------------

Python functions in SQream allow you to execute custom Python logic on your data and return the results. This functionality integrates the power of Python’s data processing libraries (like Pandas) directly into your SQL queries, supporting two main types: **Table Functions** (which return a table) and **Scalar Functions** (which return a single value).


1. Syntax Overview
^^^^^^^^^^^^^^^^^^

Python Table Functions (PTFs) and Python Scalar Functions (PSFs) are based on creating a Module.

**Module Creation:**
====================

.. code:: sql

	CREATE MODULE module_name OPTIONS (
		PATH = 'module.py', 
		ENTRY_POINTS = [
			[
				NAME = 'function_name',
				ARGUMENTS [type1, type2, ...] | LIKE table_name,
				RETURNS TABLE (col1 type1, col2 type2, ...) | LIKE table_name | SCALAR type,
				LITERAL_PARAMETERS = number,
				GPU = true/false
			]
		]
	);

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| **Syntax**             | **Description**                                                                                                                       | **Mandatory/Optional** |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| PATH                   | Specifies the file path to your Python script on the server.                                                                          | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| ENTRY_POINTS           | A list of the Python functions within the script that can be called from SQream.                                                      | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| NAME                   | The name of the Python function.                                                                                                      | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| ARGUMENTS              | Can specify explicit types ``[int, text, float]`` or reference existing table structure ``LIKE table_name``.                          | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| RETURNS                | The RETURNS clause supports the following options:                                                                                    | Mandatory              |
|                        | 1. ``TABLE (column_name data_type, ...)`` – Defines an explicit table structure.                                                      |                        |
|                        | 2. ``LIKE table_name`` – Inherits structure from an existing table.                                                                   |                        |
|                        | 3. ``SCALAR data_type`` – Specifies a scalar return type.                                                                             |                        |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| GPU=true/false         | Whether the function executes on GPU or CPU. Default is CPU.                                                                          | Optional               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| LITERAL_PARAMETERS     | Number of literal parameters the function accepts.                                                                                    | Optional               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+

**Notes:**

**1. Input Casting** 

The system applies automatic type casting to all input arguments.

**2. Output Casting**

  * All return types are automatically marked as nullable (isNullable = true).
  * Output columns are typed according to the function’s declared return specification.
  
**3. Literal Parameters**

  * Literal values can be passed to table functions.
  * Literal parameters are stored as Seq[String] and provided to the function at execution time.

**Python Table Functions (PTFs): The <function_clause>**
========================================================

This clause defines the execution of your Python Table Function. It has the following structure:

  .. code:: sql

    table(<table_function>([cursor(<sub_query>)], <literal_param>*));

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| **Syntax**             | **Description**                                                                                                                       | **Mandatory/Optional** |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| table()                | This is the main function wrapper that tells SQream to execute the Python Table Function and treat its result as a relation (a table).| Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| table_function         | This is the fully qualified name of the Python function, including the module name. For example, arr_varif.final_array.               | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| cursor(<sub_query>)    | This is an optional argument that passes the result of a subquery (any valid SELECT statement) to your Python function.               | Optional               |
|                        | The data is provided to the Python function as a Pandas DataFrame.                                                                    |                        |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| <literal_param>*       | These are optional string literals that are passed as additional arguments to your Python function.                                   | Optional               |
|                        | They must be defined in the module’s literal_parameters option and will be cast to strings in the Python code.                        |                        |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+


**Python Scalar Functions (PSFs): The <scalar_function>**
=========================================================

A Python Scalar Function is called directly by its fully qualified name and accepts one or more arguments, which can be **column names** or **literal values**.

  .. code:: sql

    <module_name>.<scalar_function>([<arg1>, <arg2>, ...]);

	
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| **Syntax**             | **Description**                                                                                                                       | **Mandatory/Optional** |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| <module_name>          | See the section for :ref:`Python Module<PythonModule>`                                                                                | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| <scalar_function>      | The fully qualified name of the Python Scalar Function                                                                                | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| [<arg1>, <arg2>, ...]  | The arguments passed to the function. These can be columns from the queried table (e.g., t.my_column)                                 | Optional               |
|                        | or literal values (e.g., 10, 'hello').                                                                                                |                        |   
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+

**Example: Defining a Module with Both Function Types**
=======================================================

.. code:: sql

    CREATE OR REPLACE MODULE my_funcs
	OPTIONS(
    path='/home/sqream/udf/my_functions.py',
    entry_points =
    [
        -- PTF Definition
        [
            name = 'process_data_table',
            arguments [text, int],
            returns table (processed_text text, processed_value int),
            gpu=true
        ],
        -- PSF Definition
        [
            name = 'add_one',
            arguments [int],
            returns int,
            gpu=false
        ]
    ]
	);

2. Usage Examples
^^^^^^^^^^^^^^^^^^^^^

Example 1: Python Scalar Function (PSF)
=======================================

This example demonstrates calling a PSF in the SELECT list.

* **Python Function:**

.. code:: python

    # Defined in 'my_functions.py'
    def my_add(a, b):
        return a + b

	# Defined in 'my_functions.py'
	def my_sub(a, b)
		return b - a
		
**Creating the Module in Sqream:**

.. code:: sql

	CREATE OR REPLACE MODULE my_mod1
	OPTIONS (
		PATH = '/tmp/arith.py',
		ENTRY_POINTS = [
			[
				NAME = 'my_add',
				ARGUMENTS [int, int],
				RETURNS SCALAR int
			],
			[
				NAME = 'my_sub',
				ARGUMENTS [int, int],
				RETURNS SCALAR int
			]
		]
	);


* **How to use the Module?**

.. code:: sql

	create or replace table t (x int, y int);
	
	insert into t values (10,20),(30,40),(50,60);

	SELECT my_mod1.my_add(x,y) FROM t; 

	SELECT x, y, my_mod1.my_add(x,y), my_mod1.my_sub(x,y) FROM t where my_mod1.my_add(x,y) > 10; 

.. note:: The ``my_add`` function is executed row-by-row, taking the value from the value column as input and returning a single integer.

Example 2: Python Table Function (PTF)
======================================

This example demonstrates how to use cursor() to pass an entire table’s data to a PTF.

* **Python Function:**

.. code:: python

    # Defined in 'array_print.py'
    def last_column(df):
        df_new = df.iloc[:, -1:]
        return df_new

**Creating the Module in Sqream:**	

.. code:: sql

	CREATE OR REPLACE MODULE my_mod2
	OPTIONS (
		PATH = '/tmp/array_print.py',
		ENTRY_POINTS = [
			[
				NAME = 'last_column',
				ARGUMENTS [date, datetime, text],
				RETURNS TABLE (col_name text),
				GPU = true
			]
		]
	);

	 
* **How to use the Module?**

.. code:: sql

    create or replace table t (xdate date, xdatetime datetime, xtext text);
	INSERT INTO t VALUES ( DATE '2025-09-11',   DATETIME '2025-09-11 14:30:00',   'some sample text' );
	SELECT * FROM table(my_mod2.last_column(Cursor(SELECT * FROM t)));

	
.. note:: The ``select * from t`` subquery passes the t table to the function.

Example 3: Passing Literal Parameters For Python Table Function (PTF)
=====================================================================

This example demonstrates how to pass a string literal to PTF.

* **Python Function:**

.. code:: python

	#Defined in 'array_print.py'
    def add_literal_column(df, literal_str):
    df_new = df.copy()
    df_new["col4"] = literal_str
		return df_new

**Creating the Module in Sqream:**	

.. code:: sql

	CREATE OR REPLACE MODULE my_mod3
	OPTIONS (
		PATH = '/tmp/array_print.py',
		ENTRY_POINTS = [
			[
				NAME = 'add_text_col',
				ARGUMENTS [boolean, int, date],
				LITERAL_PARAMETERS = 1,
				RETURNS TABLE (col1 boolean, col2 int, col3 date, col4 text)
			]
		]
	);

* **How to use the Module?**

* **Python Function:**

.. code:: python

    # df will be empty here since ARGUMENTS is empty, but it's always passed first
    print(df)
    print(p) # This will print 'param1'
    # ... function must return a Pandas DataFrame

* **SQream Query:**

.. code:: sql

    create or replace table t (col1 boolean, col2 int, col3 date);
	insert into t values (0,1,'2025-09-11');
	SELECT col1, col2, col3 , col4 FROM TABLE(my_mod3.add_literal_column(cursor(SELECT * FROM source_table),'Adding Any Text'));

3. Return Values
^^^^^^^^^^^^^^^^

* **Python Table Function(PTF):** Your Python function **must return a Pandas DataFrame**. The column names and data types of this DataFrame must exactly match the schema defined in the returns table(...) clause of the module’s entry point.

* **Python Scalar Function(PSF):** Your Python function **must return a single, non-DataFrame Python value** (e.g., an integer, string, or float). This value will be automatically converted to the single SQL data type defined in the returns <data_type> clause of the module’s entry point.
