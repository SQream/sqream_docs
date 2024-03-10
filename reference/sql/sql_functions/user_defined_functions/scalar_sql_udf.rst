.. _scalar_sql_udf:

Scalar SQL UDF
-----------------------

A **scalar SQL UDF** is a user-defined function that returns a single value, such as the sum of a group of values. Scalar UDFs are different than table-value functions, which return a result set in the form of a table.

This page describes the correct syntax when building simple scalar UDFs and provides three examples.

Syntax
~~~~~~~~~~~~

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
	  
Examples
~~~~~~~~~~

Example 1 – Support for Different Syntax
#########################################

Scalar SQL UDF supports standard functionality even when different syntax is used.

In the example below, the syntax ``dateadd`` is used instead of ``add_months``, although the function of each is identical. In addition, the operation works correctly even though the order of the expressions in ``add_months`` (``dt``, ``datetime``, and ``n int``) is different than ``MONTH``, ``n``, and ``dt`` in ``dateadd``.

.. code-block:: console

      $ CREATE or replace FUNCTION add_months(dt datetime,n int)
      $ RETURNS datetime
      $ AS $$
      $ SELECT  dateadd(MONTH ,n,dt)
      $ $$ LANGUAGE SQL;

Example 2 – Manipulating Strings
################################

The Scalar SQL UDF can be used to manipulate strings.

The following example shows the correct syntax for converting a TEXT date to the DATE type:

.. code-block:: console

      $ CREATE or replace FUNCTION  STR_TO_DATE(f text)
      $ RETURNS date
      $ AS $$
      $ select (substring(f,1,4)||'-'||substring(f,5,2)||'-'||substring(f,7,2))::date
      $ $$ LANGUAGE SQL;
	  
Example 3 – Manually Building Functionality
############################################

You can use the Scalar SQL UDF to manually build functionality for otherwise unsupported operations.

.. code-block:: console

      $ CREATE OR REPLACE function "least_sq" (a float, b float) -- Replace the LEAST(from hql) function
      $ returns float as
      $ $$select case
      $            when a <= b then a
      $            when b < a then b
      $            when a is null then b
      $            when b is null then a
      $            else null
      $          end;
      $ $$
      $ language sql;
	  
Usage Notes
~~~~~~~~~~~~~~

The following usage notes apply when using simple scalar SQL UDF's:

* During this stage, the SQL embedded in the function body must be of the type ``SELECT expr;``. Creating a UDF with invalid SQL, or with valid SQL of any other type, results in an error.
* SQL UDFs can reference other UDF's.

**NOTICE:** A function cannot (directly or indirectly) reference itself (such as by referencing another function that references it).

Restriction
~~~~~~~~~~~~~~~~

Simple scalar SQL UDF's cannot currently reference other UDFs.

