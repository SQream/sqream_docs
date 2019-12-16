.. _abs:

**************************
``ABS``
**************************

Returns the absolute (positive) value of a numeric expression

Syntax
==========


.. code-block:: postgres

   ABS( expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Numeric expression

Returns
============

Returns the same type as the argument supplied.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE cool_numbers(i INT, f DOUBLE);
   
   INSERT INTO cool_numbers VALUES (1,1.618033), (-12, -34)
   , (22, 3.141592), (-26538, 2.7182818284)
   , (NULL, NULL), (NULL,1.4142135623)
   , (42,NULL), (-42, NULL)
   , (-474, 365);


Absolute value on an integer
-------------------------------

.. code-block:: psql

   numbers=> SELECT ABS(-24);
   24

Absolute value on integer and floating point
-----------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT i, ABS(i), f, ABS(f) FROM cool_numbers;
   i      | abs   | f    | abs0
   -------+-------+------+-----
        1 |     1 | 1.62 | 1.62
      -12 |    12 |  -34 |   34
       22 |    22 | 3.14 | 3.14
   -26538 | 26538 | 2.72 | 2.72
          |       |      |     
          |       | 1.41 | 1.41
       42 |    42 |      |     
      -42 |    42 |      |     
     -474 |   474 |  365 |  365

