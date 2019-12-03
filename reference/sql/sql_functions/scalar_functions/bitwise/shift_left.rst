.. _bitwise_shift_left:

******************************
``<<`` (bitwise shift left)
******************************

Returns the bitwise shift left of a numeric expression

Syntax
==========

.. code-block:: postgres

   expr << n → integer

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

Returns an integer that is the input shifted left by ``n`` positions.

Notes
=======

* If either value is NULL, the result is NULL.

Examples
===========

.. code-block:: psql

   master=> SELECT 16 << 1;
   32
   
   master=> SELECT 16 << 2;
   64
   
   master=> select 1 << 1;
   2

.. code-block:: psql

   master=> CREATE TABLE bit(b1 int, b2 int, b3 int);
   executed
   
   master=> INSERT INTO bit VALUES (1,2,3), (2, 4, 6), (4, 2, 6), (2, 8, 16), (null, null, 64), (5, 3, 1), (6, 1, 0);
   executed
   
   SELECT b1, b2, b3, b1 << b2, b2 << b3, b1 << 1 FROM bit;
   b1 | b2 | b3 | ?column? | ?column?0 | ?column?1
   ---+----+----+----------+-----------+----------
    1 |  2 |  3 |        4 |        16 |         2
    2 |  4 |  6 |       32 |       256 |         4
    4 |  2 |  6 |       16 |       128 |         8
    2 |  8 | 16 |      512 |    524288 |         4
      |    | 64 |          |           |          
    5 |  3 |  1 |       40 |         6 |        10
    6 |  1 |  0 |       12 |         1 |        12


