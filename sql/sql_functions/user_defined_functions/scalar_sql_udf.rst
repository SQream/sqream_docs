:orphan:

.. _scalar_sql_udf:

**************
Scalar SQL UDF
**************

A **scalar SQL UDF** is a user-defined function that returns a single value, such as the sum of a group of values. Scalar UDFs are different than table-value functions, which return a result set in the form of a table.

Syntax
======

.. code-block:: console

	create_function_statement ::=
	CREATE [ OR REPLACE ] FUNCTION function_name (argument_list)
	RETURNS return_type
	AS $$
	{ function_body }
	$$ LANGUAGE SQL
	;

	function_name ::= identifier
	argument_list :: = { value_name type_name [, ...] }
	value_name ::= identifier
	return_type ::= type_name
	function_body ::= A valid SQL statement
	  
Examples
=========

Support for Different Syntax
----------------------------

Scalar SQL UDF supports standard functionality even when different syntax is used.

In the example below, the syntax ``dateadd`` is used instead of ``add_months``, although the function of each is identical. In addition, the operation works correctly even though the order of the expressions in ``add_months`` (``dt``, ``datetime``, and ``n int``) is different than ``MONTH``, ``n``, and ``dt`` in ``dateadd``.

.. code-block:: console

	CREATE OR REPLACE FUNCTION add_months(dt datetime,n int)
	RETURNS datetime
	AS $$
	SELECT  dateadd(MONTH ,n,dt)
	$$ LANGUAGE SQL;

Manipulating Strings
--------------------

The Scalar SQL UDF can be used to manipulate strings.

The following example shows the correct syntax for converting a TEXT date to the DATE type:

.. code-block:: console

	CREATE OR REPLACE FUNCTION  STR_TO_DATE(f text)
	RETURNS date
	AS $$
	SELECT (substring(f,1,4)||'-'||substring(f,5,2)||'-'||substring(f,7,2))::date
	$$ LANGUAGE SQL;
	  
Manually Building Functionality
-------------------------------

You can use the Scalar SQL UDF to manually build functionality for otherwise unsupported operations.

.. code-block:: console

	CREATE OR REPLACE function "least_sq" (a float, b float) -- Replace the LEAST(from hql) function
	returns float AS
	  $$SELECT CASE
		WHEN a <= b THEN a
		WHEN b < a THEN b
		WHEN a IS NULL THEN b
		WHEN b IS NULL THEN a
		ELSE NULL
	   END;
	  $$
	LANGUAGE SQL;
	  
Usage Notes
===========

The following usage notes apply when using simple scalar SQL UDF's:

* During this stage, the SQL embedded in the function body must be of the type ``SELECT expr;``. Creating a UDF with invalid SQL, or with valid SQL of any other type, results in an error.
* The argument list can be left empty.
* SQL UDFs can reference other UDF's.

**NOTICE:** A function cannot (directly or indirectly) reference itself (such as by referencing another function that references it).

Restriction
===========

Simple scalar SQL UDF's cannot currently reference other UDFs.

