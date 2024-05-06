:orphan:

.. _simple_scalar_sql_udf:

**********************
Simple Scalar SQL UDFs
**********************

Syntax
======

.. code-block:: postgres

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

Usage Notes
===========

The following usage notes apply when using simple scalar SQL UDF's:

* During this stage, the SQL embedded in the function body must be of the type ``SELECT expr;``. Creating a UDF with invalid SQL, or with valid SQL of any other type, results in an error.
* The argument list can be left empty.
* SQL UDFs can reference other UDF's.

**NOTICE:** A function cannot (directly or indirectly) reference itself (such as by referencing another function that references it).

Restriction
===========

Simple scalar SQL UDF's cannot currently reference other UDF's.

