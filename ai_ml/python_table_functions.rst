.. _python_table_functions:

Python Table Functions
------------------------


Python Table Functions in SQream allow you to execute custom Python logic on your data and return the results as a new table. This functionality integrates the power of Python's data processing libraries (like Pandas) directly into your SQL queries.



1. Syntax Overview
^^^^^^^^^^^^^^^^^^

Python Table Functions are used within the FROM clause of SELECT and INSERT statements. The core component is the <table_function_clause>.

SELECT statement
To query data from a Python Table Function, you use the following syntax:

.. code:: sql

    SELECT <select_list> FROM <table_function_clause>

INSERT statement
To insert data returned by a Python Table Function into an existing table, you use this syntax:


.. code:: sql
    INSERT INTO <table> SELECT * FROM <table_function_clause>



2. The ``<table_function_clause>``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This clause defines the execution of your Python function. It has the following structure:


.. code:: sql

    table(<table_function>([cursor(<sub_query>)], <literal_param>*));

``table()``: This is the main function wrapper that tells SQream to execute the Python function.

``<table_function>``: This is the fully qualified name of the Python function, including the module name. For example, ``arr_varif.final_array``.

``cursor(<sub_query>)``: This is an optional argument that passes the result of a subquery (any valid ``SELECT`` statement) to your Python function. The data is provided to the Python function as a Pandas DataFrame.

``<literal_param>*``: These are optional string literals that are passed as additional arguments to your Python function. They must be defined in the module's literal_parameters option and will be cast to strings in the Python code.



3. Defining a Python Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you can use a Python Table Function, you must define it in SQream using a module. The ``CREATE OR REPLACE MODULE`` command is used for this purpose.

Example:
Based on your provided code, here is an example of defining a module with multiple entry points:


.. code:: sql

    CREATE OR REPLACE MODULE arr_varif
    OPTIONS
    (
        path='/home/sqream/git/debug/udf/array_print.py',
        entry_points =
        [
            [
                name = 'final_array',
                arguments [text[], int[], float[], date, datetime, text],
                returns table (varification text),
                gpu=true
            ],
            [
                name = 'final_array_cpu',
                arguments [text[], int[], float[], date, datetime, text],
                returns table (verification text, i int),
                gpu=false
            ]
        ]
    );

``path``: Specifies the file path to your Python script on the server.

``entry_points``: A list of the Python functions within the script that can be called from SQream.

``name``: The name of the Python function.

``arguments``: A list of the data types of the columns that the Python function expects from the cursor() subquery.

``returns table(...)``: The schema of the table that the Python function will return. The column names and data types must match the DataFrame returned by your Python code.

``gpu=true/false``: Determines whether the function will be executed on the GPU or the CPU.



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