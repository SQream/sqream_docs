:orphan:

.. _get_function_ddl:

*****************
GET FUNCTION DDL
*****************

``GET_FUNCTION_DDL`` is a function that shows the :ref:`create_function` statement for a function.

Syntax
======

.. code-block:: postgres


	SELECT GET_FUNCTION_DDL("<function_name>")

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
========

.. code-block:: postgres

	CREATE OR REPLACE FUNCTION my_distance (x1 float,
	                                        y1 float,
	                                        x2 float,
	                                        y2 float) returns float as
	  $$ import mathIF y1 < X1:RETURN 0.0
	  else:
	     return math.Sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2) 
	  $$ 
	  language python;

   
	SELECT
	  GET_FUNCTION_DDL("my_distance");
	  
	CREATE FUNCTION "my_distance" (x1 float,
                               y1 float,
                               x2 float,
                               y2 float) returns float as
	  $$  
	  import  math  
	  if  y1  <  x1:  
		  return  0.0  
	  else:  
		  return  math.sqrt((y2  -  y1)  **  2  +  (x2  -  x1)  **  2)  
	  $$
	language python volatile;



Exporting function DDL to a file
--------------------------------

.. code-block:: postgres

	COPY
	  (
	    SELECT
	      GET_FUNCTION_DDL("my_distance")
	  ) TO
	WRAPPER
	  csv_fdw
	OPTIONS
	  (LOCATION = 's3://sqream-docs/cool_animals_ddl.csv');

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.
