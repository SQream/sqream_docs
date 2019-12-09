.. _log10:

**************************
LOG10
**************************

Returns the 10-base logarithm value of a numeric expression

See also :ref:`LOG (natural)<log>`.

Syntax
==========

.. code-block:: postgres

   LOG10( expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Positive numeric expression

Returns
============

Always returns a floating point result.

Notes
=======

* If the input value is NULL, the result is NULL.

Examples
===========

Log (base 10) values
--------------------------

.. code-block:: psql

   numbers=> SELECT LOG10(0.0001), LOG10(1), LOG10(100), LOG10(1000000);
   log10 | log100 | log101 | log102
   ------+--------+--------+-------
      -4 |      0 |      2 |      6

