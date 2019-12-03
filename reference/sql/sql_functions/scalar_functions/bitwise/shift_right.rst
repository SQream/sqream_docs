.. _bitwise_shift_right:

******************************
``>>`` (bitwise shift right)
******************************

Returns the bitwise shift right of a numeric expression

Syntax
==========

.. code-block:: postgres

   expr >> n → integer

   expr ::= integer
   
   n ::= integer


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Integer expressions
   * - ``n``
     - Number of bits to shift by

Returns
============

Returns an integer that is the input shifted right by ``n`` positions.

Notes
=======

* If either value is NULL, the result is NULL.

Examples
===========

.. code-block:: psql

   master=> SELECT 16 >> 1;
   8
   
   master=> SELECT 16 >> 2;
   4
   
   master=> select 1 >> 1;
   0

.. code-block:: psql

   master=> CREATE TABLE bit(b1 int, b2 int, b3 int);
   executed
   
   master=> INSERT INTO bit VALUES (1,2,3), (2, 4, 6), (4, 2, 6), (2, 8, 16), (null, null, 64), (5, 3, 1), (6, 1, 0);
   executed
   
   SELECT b1, b2, b3, b1 >> b2, b2 >> b3, b1 >> 1 FROM bit;
   b1 | b2 | b3 | ?column? | ?column?0 | ?column?1
   ---+----+----+----------+-----------+----------
    1 |  2 |  3 |        0 |         0 |         0
    2 |  4 |  6 |        0 |         0 |         1
    4 |  2 |  6 |        1 |         0 |         2
    2 |  8 | 16 |        0 |         0 |         1
      |    | 64 |          |           |          
    5 |  3 |  1 |        0 |         1 |         2
    6 |  1 |  0 |        3 |         1 |         3

