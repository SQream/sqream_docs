.. _drop_function:

**********************
DROP FUNCTION
**********************

``DROP FUNCTION`` can be used to remove a user defined function.

Permissions
=============

The role must have the ``DDL`` permission at the database level.

Syntax
==========

.. code-block:: postgres

	DROP FUNCTION [ IF EXISTS ] function_name()

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

Dropping a function:

.. code-block:: sql

   DROP FUNCTION my_distance();

   
