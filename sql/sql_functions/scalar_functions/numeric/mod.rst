.. _mod:

**************************
MOD, ``%``
**************************

Calculates the modulu (remainder) of ``x`` divided by ``y``.

This function can be also be called with an infix operator, ``x % y``.

Syntax
==========

.. code-block:: postgres

   modulu ::= MOD( expr1, expr2 )

              | expr1 % expr2

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr1``
     - Integer expression (dividend)
   * - ``expr2``
     - Integer expression (divisor)

Returns
============

Always returns a integer result.

Notes
=======

* If the input value is NULL, the result is NULL.

* Both inputs are expected to be integers

Examples
===========

Using the MOD function
-----------------------------------

.. code-block:: psql

   numbers=> SELECT MOD(11,-5), MOD(8,5), MOD(1,1);
   mod | mod0 | mod1
   ----+------+-----
     1 |    3 |    0


Using the infix operator
---------------------------

.. code-block:: psql

   numbers=> SELECT 11 % -5, 8 % 5, 1 % 1;
   ?column? | ?column?0 | ?column?1
   ---------+-----------+----------
          1 |         3 |         0
