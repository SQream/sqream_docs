.. _python_functions:

*************************************
Python UDF (User-Defined Functions)
*************************************

User-defined functions (UDFs) are a feature that extends SQream DB's built in SQL functionality. SQream DB's Python UDFs allow developers to create new functionality in SQL by writing the lower-level language implementation in Python. 

.. contents:: In this topic:
   :local:

A simple example
=====================

Most databases have an :ref:`UPPER` function, including SQream DB. However, assume that this function is missing for the sake of this example.

You can write a function in Python to uppercase a text value using the :ref:`create_function` syntax.

.. code-block:: postgres

   CREATE FUNCTION my_upper (x1 text)
     RETURNS text
     AS $$  
   return x1.upper()
   $$ LANGUAGE PYTHON;

Let's break down this example:

* ``CREATE FUNCTION my_upper`` - :ref:`Create a function<create_function>` called ``my_upper``. This name must be unique in the current database
* ``(x1 text)`` - the function accepts one argument named ``x1`` which is of the SQL type ``TEXT``. All :ref:`data types<data_types>` are supported.
* ``RETURNS text`` - the function returns the same type - ``TEXT``. All :ref:`data types<data_types>` are supported.
* ``AS $$`` - what follows is some code that we don't want to quote, so we use dollar-quoting (``$$``) instead of single quotes (``'``).
* ``return x1.upper()`` - the Python function's body is the argument named ``x1``, uppercased.
* ``$$ LANGUAGE PYTHON`` - this is the end of the function, and it's in the Python language.

.. rubric:: Running this example

After creating the function, you can use it in any SQL query.

For example:

.. code-block:: psql
   
   master=>CREATE TABLE jabberwocky(line text);
   executed
   master=> INSERT INTO jabberwocky VALUES 
   .   ('''Twas brillig, and the slithy toves '), ('      Did gyre and gimble in the wabe: ')
   .   ,('All mimsy were the borogoves, '), ('      And the mome raths outgrabe. ')
   .   ,('"Beware the Jabberwock, my son! '), ('      The jaws that bite, the claws that catch! ')
   .   ,('Beware the Jubjub bird, and shun '), ('      The frumious Bandersnatch!" ');
   executed
   master=> SELECT line, my_upper(line) FROM jabberwocky;
   line                                             | my_upper                                        
   -------------------------------------------------+-------------------------------------------------
   'Twas brillig, and the slithy toves              | 'TWAS BRILLIG, AND THE SLITHY TOVES             
         Did gyre and gimble in the wabe:           |       DID GYRE AND GIMBLE IN THE WABE:          
   All mimsy were the borogoves,                    | ALL MIMSY WERE THE BOROGOVES,                   
         And the mome raths outgrabe.               |       AND THE MOME RATHS OUTGRABE.              
   "Beware the Jabberwock, my son!                  | "BEWARE THE JABBERWOCK, MY SON!                 
         The jaws that bite, the claws that catch!  |       THE JAWS THAT BITE, THE CLAWS THAT CATCH! 
   Beware the Jubjub bird, and shun                 | BEWARE THE JUBJUB BIRD, AND SHUN                
         The frumious Bandersnatch!"                |       THE FRUMIOUS BANDERSNATCH!"               

Why use UDFs?
=====================

* They allow simpler statements - You can create the function once, store it in the database, and call it any number of times in a statement.

* They can be shared - UDFs can be created by a database administrator, and then used by other roles.

* They can simplify downstream code - UDFs can be modified in SQream DB independently of program source code.

SQream DB's UDF support
=============================

Scalar functions
---------------------

SQream DB's UDFs are scalar functions. This means that the UDF returns a single data value of the type defined in the ``RETURNS`` clause. For an inline scalar function, the returned scalar value is the result of a single statement.

Python
-------------------

At this time, SQream DB's UDFs are supported for Python.

Python 3.6.7 is installed alongside SQream DB, for use exclusively by SQream DB.
You may have a different version of Python installed on your server.

To find which version of Python is installed for use by SQream DB, create and run this UDF:

.. code-block:: psql
   
   master=> CREATE OR REPLACE FUNCTION py_version()
   .  RETURNS text
   .  AS $$
   . import sys
   . return ("Python version: " + sys.version + ". Path: " + sys.base_exec_prefix)
   .  $$ LANGUAGE PYTHON;
   executed
   master=> SELECT py_version();
   py_version                                                                           
   -------------------------------------------------------------------------------------
   Python version: 3.6.7 (default, Jul 22 2019, 11:03:54) [GCC 5.4.0].
   Path: /opt/sqream/python-3.6.7-5.4.0

Using modules
---------------------

To import a Python module, use the standard ``import`` syntax in the first lines of the user-defined function.


Finding existing UDFs in the catalog
========================================

The ``user_defined_functions`` catalog view contains function information.

Here's how you'd list all UDFs in the system:

.. code-block:: psql
   
   master=> SELECT * FROM sqream_catalog.user_defined_functions;
   database_name | function_id | function_name
   --------------+-------------+--------------
   master        |           1 | my_upper  


Getting the DDL for a function
=====================================

.. code-block:: psql

   master=> SELECT GET_FUNCTION_DDL('my_upper');
   ddl                                                 
   ----------------------------------------------------
   create function "my_upper" (x1 text) returns text as
   $$  
      return x1.upper()
   $$
   language python volatile;

See :ref:`get_function_ddl` for more information.

Error handling
=====================

In UDFs, any error that occurs causes the execution of the function to stop. This in turn causes the statement that invoked the function to be canceled.

Permissions and sharing
============================

To create a UDF, the creator needs the ``CREATE FUNCTION`` permission at the database level.

For example, to grant ``CREATE FUNCTION`` to a non-superuser role:

.. code-block:: postgres
   
   GRANT CREATE FUNCTION ON DATABASE master TO mjordan;

To execute a UDF, the role needs the ``EXECUTE FUNCTION`` permission for every function. 

For example, to grant the permission to the ``r_bi_users`` role group, run:

.. code-block:: postgres
   
   GRANT EXECUTE ON FUNCTION my_upper TO r_bi_users;

.. note:: Functions are stored for each database, outside of any schema.

See more information about permissions in the :ref:`Access control guide<access_control>`.


Best practices
=====================

Although user-defined functions add flexibility, they may have some performance drawbacks. They are not usually a replacement for subqueries or views.

In some cases, the user-defined function provides benefits like sharing extended functionality which makes it very appealing.

Use user-defined functions sparingly in the ``WHERE`` clause. SQream DB can't optimize the function's usage, and it will be called once for every value. If possible, you should narrow down the number of results before the UDF is called by using a subquery.



.. python udfs are trusted

.. working with python modules

.. performance considerations