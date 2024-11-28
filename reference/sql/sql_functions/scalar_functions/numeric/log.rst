.. _log:

**************************
LOG
**************************

Returns the natural logarithm value of a numeric expression

The natural logarithm is also known as *ln* or logarithm to the base of the mathematical constant *e*.

See also :ref:`LOG10<log10>`.

Syntax
==========

.. code-block:: postgres

   LOG( expr )

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

When using the ``LOG`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

Notes
=======

* If the input value is NULL, the result is NULL.

Examples
===========

Natural log values
--------------------------

.. code-block:: psql

   numbers=> SELECT LOG(0.0001), LOG(1), LOG(2.718281), LOG(5000000000000000);
   log     | log0 | log1 | log2   
   --------+------+------+--------
   -9.2103 |    0 |    1 | 36.1482
