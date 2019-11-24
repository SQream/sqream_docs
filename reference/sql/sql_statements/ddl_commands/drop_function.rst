.. _drop_function:

**********************
DROP FUNCTION
**********************

``DROP FUNCTION`` can be used to remove a user defined function.

Privileges
=============

The role must have the ``DDL`` permission at the database level.

Synopsis
==========

.. code-block:: postgres

   drop_function_statement ::=
       DROP FUNCTION [ IF EXISTS ] function_name();
       ;

   function_name ::= identifier
   


Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``IF EXISTS``
     - Drop the function if it exists. Does not error if the function does not exist.
   * - ``function_name()``
     - The name of the function to drop.

Examples
===========

Dropping a function
---------------------------------------------

.. code-block:: postgres

   DROP FUNCTION my_distance();


Dropping a function (always succeeds)
-------------------------------------

.. code-block:: psql

   farm=> DROP FUNCTION my_distance();
   executed
   
   farm=> DROP FUNCTION my_distance();
   Function 'my_distance' not found
   
   -- This will succeed, even though the function does not exist
   farm=> DROP FUNCTION IF EXISTS my_distance();
   executed
   
