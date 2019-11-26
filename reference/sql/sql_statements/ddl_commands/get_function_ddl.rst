.. _get_function_ddl:

*****************
GET_FUNCTION_DDL
*****************

``GET_FUNCTION_DDL(<function name>)`` is a function that shows the :ref:`CREATE FUNCTION<create_function>` statement for a function.

.. tip:: 
   * For tables, see :ref:`GET_DDL<get_ddl>`.
   * For views, see :ref:`GET_VIEW_DDL<get_view_ddl>`.
   * For the entire database, see :ref:`DUMP_DATABASE_DDL<dump_database_ddl>`.

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.

Synopsis
==========

.. code-block:: postgres

   get_function_ddl_statement ::=
       SELECT GET_FUNCTION_DDL('function_name')
       ;

   function_name ::= identifier  

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``function_name``
     - The name of the function.

Examples
===========

Getting the DDL for a function
---------------------------------

The result of the ``GET_FUNCTION_DDL`` function is a verbose version of the CREATE FUNCTION statement, which may include additional information that was added by SQream DB. For example, some type names and identifiers may be quoted or altered.

.. code-block:: psql

   master=> CREATE  OR  REPLACE  FUNCTION  my_distance  (x1  float,  y1  float,  x2  float,  y2  float)  RETURNS  float  as  $$  
      import  math  
      if  y1  <  x1:  
          return  0.0  
      else:  
          return  math.sqrt((y2  -  y1)  **  2  +  (x2  -  x1)  **  2)  
      $$  LANGUAGE  PYTHON;  
   executed
   
   master=> SELECT GET_FUNCTION_DDL('my_distance');
   create function "my_distance" (x1 float,
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
------------------------------------

.. code-block:: postgres

   COPY (SELECT GET_FUNCTION_DDL('my_distance')) TO '/home/rhendricks/my_distance.sql';
