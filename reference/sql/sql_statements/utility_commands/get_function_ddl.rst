.. _get_function_ddl:

*****************
GET_FUNCTION_DDL
*****************

``GET_FUNCTION_DDL(<function name>)`` is a function that shows the :ref:`CREATE FUNCTION<create_function>` statement for a function.


Syntax
==========

.. code-block:: postgres

   get_function_ddl_statement ::=
       SELECT GET_FUNCTION_DDL('function_name')

   function_name ::= identifier  

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``function_name``
     - The name of the function

Examples
===========

The result of the ``GET_FUNCTION_DDL`` function is a verbose version of the ``CREATE FUNCTION`` statement, which may include additional information that was added by BLUE. For example, some type names and identifiers may be quoted or altered.

1. Get the DDL for a function:


   .. code-block:: postgres

	CREATE OR REPLACE FUNCTION my_distance(x1 FLOAT, y1 FLOAT, x2 FLOAT, y2 FLOAT) 
	RETURNS FLOAT AS $$
	SELECT 
		CASE 
			WHEN y1 < x1 THEN 0.0
			ELSE SQRT(POWER(y2 - y1, 2) + POWER(x2 - x1, 2))
		END;
	$$ LANGUAGE sql;
   
	SELECT GET_FUNCTION_DDL('my_distance');

	CREATE FUNCTION "my_distance" (x1 DOUBLE, y1 DOUBLE, x2 DOUBLE, y2 DOUBLE)
	RETURNS DOUBLE AS $$ 
	SELECT
		CASE 
			WHEN y1 < x1 then 0.0 
			ELSE sqrt(power(y2 - y1, 2) + power(x2 - x1, 2)) 
		END; 
	$$ LANGUAGE SQL

2. Export function DDL to a file:

   .. code-block:: postgres

	COPY (SELECT GET_FUNCTION_DDL('my_distance')) TO '/home/rhendricks/my_distance.sql';




Permissions
=============

The role must have the ``CONNECT`` permission at the database level.


For tables, see :ref:`GET_DDL<get_ddl>`

For views, see :ref:`GET_VIEW_DDL<get_view_ddl>`

For the entire database, see :ref:`DUMP_DATABASE_DDL<dump_database_ddl>`