:orphan:

.. _create_function:

*****************
CREATE FUNCTION
*****************

``CREATE FUNCTION`` creates a new user-defined function (UDF) in an existing database.

Permissions
=============

The role must have the ``CREATE FUNCTION`` permission at the database level.

Syntax
==========

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
   
   function_body ::= Valid SQL code

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``OR REPLACE``
     - Create a new function, and overwrite any existing function by the same name. Does not return an error if the function already exists. ``CREATE OR REPLACE`` does not check the function contents or structure, only the function name.
   * - ``function_name``
     - The name of the function to create, which must be unique inside the database.
   * - ``argument_list``
     - A comma separated list of column definitions. A column definition includes a name identifier and a datatype.
   * - ``return_type``
     - The SQL datatype of the return value, such as ``INT``, ``TEXT``, etc.
   * - ``function_body``
     - SQL code, dollar-quoted (``$$``). 

Examples
===========

Calculate distance between two points

.. code-block:: postgres

	CREATE OR REPLACE FUNCTION my_distance(x1 FLOAT, y1 FLOAT, x2 FLOAT, y2 FLOAT) 
	RETURNS FLOAT AS $$
	SELECT CASE
		WHEN y1 < x1 THEN 0.0
		ELSE SQRT(POWER(y2 - y1, 2) + POWER(x2 - x1, 2))
	END;
	$$ LANGUAGE sql;


	-- Usage:
	SELECT my_distance(1.0, 2.0, 4.0, 6.0);
