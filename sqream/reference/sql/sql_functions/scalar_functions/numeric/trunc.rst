.. _trunc:

**************************
TRUNC
**************************

Rounds a number to its integer representation towards 0.

.. note:: This function is overloaded. The function :ref:`TRUNC<date_trunc>` can also modify the precision of ``DATE`` and ``DATETIME`` values.

See also :ref:`ROUND<round>`.

Syntax
==========

.. code-block:: postgres

   TRUNC( expr )

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

* If the input value is NULL, the result is NULL.

Examples
===========

Rounding to the nearest integer
-------------------------------------

.. code-block:: psql

   numbers=> SELECT TRUNC(x) FROM (VALUES (0.0001), (PI()), (-2.718281), (500.1234)) as t(x);
   trunc
   -----
     0.0
     3.0
    -2.0
   500.0


TRUNC vs. :ref:`ROUND<round>`
------------------------------------------------------------

.. code-block:: psql

   numbers=> SELECT TRUNC(x), ROUND(x) 
   .      FROM (VALUES (0.0001), (-0.0001)
   .           , (PI()), (-2.718281), (500.1234)) as t(x);
   trunc | round
   ------+------
     0.0 |  -0.0
    -0.0 |  -0.0
     3.0 |   3.0
    -2.0 |  -3.0
   500.0 | 500.0
