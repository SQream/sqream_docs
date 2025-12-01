.. _python_table_functions:

Python Functions
------------------------

Python functions in SQream allow you to execute custom Python logic on your data and return the results. This functionality integrates the power of Python’s data processing libraries (like Pandas) directly into your SQL queries, supporting two main types: **Table Functions** (which return a table) and **Scalar Functions** (which return a single value).


1. Syntax Overview
^^^^^^^^^^^^^^^^^^

Python Table Functions (PTFs)
=============================

PTFs are used within the FROM clause of SELECT and INSERT statements and must return a table.

* **SELECT statement** – To query data from a Python table function, use the following syntax:

  .. code:: sql

      SELECT <select_list> FROM <function_clause>

* **INSERT statement** – To insert data returned by a Python table function into an existing table, use this syntax:

  .. code:: sql

      INSERT INTO <table> SELECT * FROM <function_clause>

Python Scalar Functions (PSFs)
==============================

PSFs are used anywhere a **standard expression** or scalar value is expected, such as in the **SELECT list**, WHERE clause, or ORDER BY clause. They must return a single, non-table value.

* **SELECT statement** – To use a Python scalar function, you use the following syntax:

  .. code:: sql

    SELECT <scalar_function>([<column> | <literal>]*) FROM <table>
	  
2. Python Table Functions (PTFs): The <function_clause>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


3. Python Scalar Functions (PSFs): The <scalar_function>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _PythonModule:

4. Defining a Python Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^
	
Before you can use a Python function (either Table or Scalar), you must define it in SQream using a **module**. The CREATE OR REPLACE MODULE command is used for this purpose.


Module Definition Syntax
========================

  .. code:: sql

    CREATE OR REPLACE MODULE <module_name>
    OPTIONS(
      path='/path/to/script.py',
      entry_points = [
        [
            name = '<python_function_name>',
            arguments [<data_type>...],
            returns table (<column_name> <data_type>...) | returns <data_type>,
            gpu=true/false,
            literal_parameters = <int>
        ],
        ...
    ]
    );


+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| **Syntax**             | **Description**                                                                                                                       | **Mandatory/Optional** |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| path                   | Specifies the file path to your Python script on the server.                                                                          | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| entry_points           | A list of the Python functions within the script that can be called from SQream.                                                      | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| name                   | The name of the Python function.                                                                                                      | Mandatory              |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| arguments              | For PTFs: A list of data types expected from the cursor() subquery.                                                                   | Mandatory              |
|                        | If no cursor() is used, this list is empty.                                                                                           |                        |
|                        | For PSFs: A list of data types for the function’s direct arguments.                                                                    |                        |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| returns table(...)     | For PTFs: The schema of the table returned by the Python function.                                                                    | Mandatory              |
|                        | Column names and types must match the DataFrame returned from Python.                                                                 |                        |
|                        | For PSFs: The scalar SQL type of the returned value (e.g., returns int, returns text).                                                |                        |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| gpu=true/false         | Whether the function executes on GPU or CPU. Default is CPU.                                                                          | Optional               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| literal_parameters     | Number of string literals passed after the DataFrame (PTFs) or standard arguments (PSFs).                                             | Optional               |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------+

Example: Defining a Module with Both Function Types
===================================================

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


4. Examples in Action
^^^^^^^^^^^^^^^^^^^^^^^

Example 1: Passing a Subquery
This example demonstrates how to use ``cursor()`` to pass an entire table's data to a Python function.

Python Function:

The final_array function takes a DataFrame df and returns a new DataFrame.



.. code:: python

    def final_array(df):
        df_new = df.iloc[:, -1:]
        return df_new

SQream Query:

This query executes final_array and selects all columns from the resulting table. The select * from t subquery passes the t table to the function.

.. code:: sql

    SELECT * FROM table(arr_varif.final_array(Cursor(SELECT * FROM t)));

Example 2: Passing Literal Parameters
This example shows how to pass a string literal to the Python function. This is useful for passing configuration or simple values that aren't part of a query.

Module Definition:

The literal_parameters = 1 option indicates that one literal parameter is expected.

.. code:: sql

    CREATE OR REPLACE MODULE test3
    OPTIONS (
        PATH = '/home/sqream/git/debug/udf/array_print.py',
        ENTRY_POINTS =
        [
            [
                NAME = 'empty_df',
                ARGUMENTS [],
                literal_parameters = 1,
                returns table(x text, y int)
            ]
        ]
    );

Python Function:

The empty_df function receives both the DataFrame and the literal parameter (p) as arguments.

.. code:: python

    def empty_df(df,p):
        print(df) # The df will be empty here since ARGUMENTS is empty
        print(p) # This will print 'param1'
        # ...


SQream Query:

The string literal 'param1' is passed to the function.

.. code:: sql

    SELECT * FROM table(test3.empty_boi('param1'));
    Note: The name of the Python function in the ``SELECT`` statement (``empty_boi``) does not match the name in the module definition (``empty_df``) in your example. These names must match for the query to work correctly.



5. Return Values
^^^^^^^^^^^^^^^^^^^^^

Your Python function must return a Pandas DataFrame. The column names and data types of this DataFrame must exactly match the schema defined in the ``returns table(...)`` clause of the module's entry point.
