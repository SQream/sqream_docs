.. _bitwise_not:

***************************
``~`` (bitwise ``NOT``)
***************************

Returns the bitwise ``NOT`` (negation) of two numeric expressions. This is the bitwise complement.

Syntax
==========

.. code-block:: postgres

   ~ expr --> integer

   expr ::= integer
   


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Integer expression

Returns
============

Returns an integer that is the bitwise ``NOT`` of the input.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

.. code-block:: psql

   master=> SELECT ~16, ~24;
   -17,-25
   
   master=> SELECT ~101, ~110;
   -102,-111
   
   master=> SELECT ~32, ~64;
   -33,-65


.. code-block:: psql

   master=> CREATE TABLE bit(b1 int, b2 int, b3 int);
   executed
   
   master=> INSERT INTO bit VALUES (1,2,3), (2, 4, 6), (4, 2, 6), (2, 8, 16), (null, null, 64), (5, 3, 1), (6, 1, 0);
   executed
   
   SELECT b1, b2, b3, ~b1, ~b2, ~b3 FROM bit;
   b1 | b2 | b3 | ?column? | ?column?0 | ?column?1
   ---+----+----+----------+-----------+----------
    1 |  2 |  3 |       -2 |        -3 |        -4
    2 |  4 |  6 |       -3 |        -5 |        -7
    4 |  2 |  6 |       -5 |        -3 |        -7
    2 |  8 | 16 |       -3 |        -9 |       -17
      |    | 64 |          |           |       -65
    5 |  3 |  1 |       -6 |        -4 |        -2
    6 |  1 |  0 |       -7 |        -2 |        -1


