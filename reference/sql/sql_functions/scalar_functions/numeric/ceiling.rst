.. _ceiling:

**************************
CEILING / CEIL
**************************

Calculates the smallest integer greater than the numeric expression given.

See also :ref:`ROUND<round>`, :ref:`FLOOR<floor>`.

Syntax
==========

.. code-block:: postgres

   CEILING( expr )
   
   CEIL ( expr )

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


``CEILING`` returns the same type as the argument supplied.

Notes
=======

* If the input value is NULL, the result is NULL.

Examples
===========

:ref:`floor` vs. ``CEIL`` vs. :ref:`round`
------------------------------------------------------------

.. code-block:: psql

   numbers=> SELECT FLOOR(x), CEIL(x), ROUND(x) 
   .      FROM (VALUES (0.0001), (-0.0001)
   .           , (PI()), (-2.718281), (500.1234)) as t(x);
   floor | ceil | round
   ------+------+------
       0 |    1 |    -0
       3 |    4 |     3
      -3 |   -2 |    -3
     500 |  501 |   500