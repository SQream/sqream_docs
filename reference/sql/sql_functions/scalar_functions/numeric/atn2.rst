.. _atn2:

**************************
``ATN2``
**************************

Returns the inverse tangent of the ratio of x and y.

``ATN2(y,x) = ATAN(y/x)``

This represents the angle in radians from the positive x-axis of a plane and the point (x, y) on it, with positive sign for the upper half-plane.

Syntax
==========


.. code-block:: postgres

   ATN2( expr1, expr2 )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr1``
     - Numeric expression representing the ``y`` component.
   * - ``expr2``
     - Numeric expression representing the ``x`` component

Returns
============

Always returns a floating point result of the inverse tangent, in radians.

Notes
=======

* The result is given in radians, in the range ``(-π, π]``.

* If the input value is NULL, the result is NULL.

Examples
===========

Inverse tangent of (1, 0) (= π/2)
-----------------------------------

.. code-block:: psql

   numbers=> SELECT ATN2(1,0);
   atn2
   ----
   1.5707963267948966

Inverse tangent of ``x=0.5``, ``y=SQRT(3)/2`` (= π/3, or 60°)
----------------------------------------------------------------

Use :ref:`SQRT<sqrt>` to simplify input and :ref:`DEGREES<degrees>` to convert the result from radians.

.. code-block:: psql

   numbers=> SELECT ATN2(0.5*SQRT(3), 0.5), DEGREES(ATN2(0.5*SQRT(3), 0.5));
   atn2   | degrees
   -------+--------
   1.0472 |      60





