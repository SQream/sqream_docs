.. _bitwise_or:

**********************
``|`` (bitwise ``OR``)
**********************

Returns the bitwise ``OR`` of two numeric expressions

Syntax
==========

.. code-block:: postgres

   expr1 | expr2 --> integer

   expr1 ::= integer
   
   expr2 ::= integer


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr1``, ``expr2``
     - Integer expressions

Returns
============

Returns an integer that is the bitwise ``OR`` of the inputs.

Notes
=======

* If either value is NULL, the result is NULL.

Examples
===========

.. code-block:: psql

   master=> SELECT 16 | 24;
   24
   
   master=> SELECT 101 | 110;
   111
   
   master=> SELECT 32 | 64;
   96

.. code-block:: psql

   master=> CREATE TABLE bit(b1 int, b2 int, b3 int);
   executed
   
   master=> INSERT INTO bit VALUES (1,2,3), (2, 4, 6), (4, 2, 6), (2, 8, 16), (null, null, 64), (5, 3, 1), (6, 1, 0);
   executed
   
   SELECT b1, b2, b3, b1 | b2, b2 | b3, b1 | b3 FROM bit;
   b1 | b2 | b3 | ?column? | ?column?0 | ?column?1
   ---+----+----+----------+-----------+----------
    1 |  2 |  3 |        3 |         3 |         3
    2 |  4 |  6 |        6 |         6 |         6
    4 |  2 |  6 |        6 |         6 |         6
    2 |  8 | 16 |       10 |        24 |        18
      |    | 64 |          |           |          
    5 |  3 |  1 |        7 |         3 |         5
    6 |  1 |  0 |        7 |         1 |         6
