.. _scalar_sql_udf:

Scalar SQL UDF
-----------------------
Syntax
~~~~~~~~~~~~
A scalar UDF is a user-defined function that returns a single value such as the sum of a group of values. Scalar UDFs are different than table-valued functions, which return a result set in the form of a table.

The following example shows the correct syntax for simple scalar SQL UDF's returning the type name:

.. code-block:: console

      $ create_function_statement ::=
      $     CREATE [ OR REPLACE ] FUNCTION function_name (argument_list)
      $     RETURNS return_type
      $     AS $$
      $     { function_body }
      $     $$ LANGUAGE SQL
      $     ;
      $ 
      $ function_name ::= identifier
      $ argument_list :: = { value_name type_name [, ...] }
      $ value_name ::= identifier
      $ return_type ::= type_name
      $ function_body ::= A valid SQL statement

Usage Notes
~~~~~~~~~~~~~~
The following usage notes apply when using simple scalar SQL UDF's:

* During this stage, the SQL embedded in the function body must be of the type ``SELECT expr;``. Creating a UDF with invalid SQL, or with valid SQL of any other type, results in an error.
* As with Python UDFs, the argument list can be left empty.
* SQL UDFs can reference other UDF's, including Python UDF's.

**NOTICE:** A function cannot (directly or indirectly) reference itself (such as by referencing another function that references it).

Because SQL UDF's are one type of supported UDFs, the following Python UDF characteristics apply:

* UDF permission rules - see `Access Control <https://docs.sqream.com/en/latest/guides/features/access_control.html#access-control>`_.

* The ``get_function_ddl`` utility function works on these functions - see `Getting the DDL for a Function <https://docs.sqream.com/en/latest/guides/features/python_functions.html#getting-the-ddl-for-a-function>`_.

* SQL UDF's should appear in the catalog with Python UDF's - see `Finding Existing UDFs in the Catalog <https://docs.sqream.com/en/latest/guides/features/python_functions.html#finding-existing-udfs-in-the-catalog>`_.

Restrictions
~~~~~~~~~~~~~~~~
The following restrictions apply to simple scalar SQL UDF's:

* Simple scalar SQL UDF's cannot currently reference other UDF's.
* Like Python UDF's, Sqream does not support overloading.
