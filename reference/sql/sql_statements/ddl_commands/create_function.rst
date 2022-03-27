.. _create_function:

*****************
CREATE FUNCTION
*****************

``CREATE FUNCTION`` creates a new user-defined function (UDF) in an existing database. 

See more in our :ref:`Python UDF (user-defined functions)<python_functions>` guide.

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
       $$ LANGUAGE python
       ;

   function_name ::= identifier  

   argument_list :: = { value_name type_name [, ...] }

   value_name ::= identifier
   
   return_type ::= type_name
   
   function_body ::= Valid Python code

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
     - The SQL datatype of the return value, such as ``INT``, ``VARCHAR``, etc.
   * - ``function_body``
     - Python code, dollar-quoted (``$$``). 

Examples
===========

Calculate distance between two points
--------------------------------------

.. code-block:: postgres

   CREATE OR REPLACE FUNCTION my_distance (x1 float, y1 float, x2 float, y2 float) 
     RETURNS FLOAT
     AS $$  
   import  math
   if  y1  <  x1:  
       return  0.0  
   else:
       return  math.sqrt((y2  -  y1)  **  2  +  (x2  -  x1)  **  2)
   $$ LANGUAGE PYTHON;

   -- Usage:
   SELECT  city, my_location, my_distance(x1,y1,x2,y2)  from  cities;


Calling files from other locations
---------------------------------------

.. code-block:: postgres

   -- Our script my_code.py is in ~/my_python_stuff
   
   CREATE FUNCTION write_log()
     RETURNS INT 
     AS $$ 
   import sys
   sys.path.append("/home/user/my_python_stuff")  
   
   import my_code as f
   
   f.main()
   
   return 1
   
   $$ LANGUAGE PYTHON;  

   -- Usage:  
   SELECT write_log();
