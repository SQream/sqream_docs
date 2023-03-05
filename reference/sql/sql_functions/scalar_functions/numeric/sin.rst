.. _sin:

**************************
SIN
**************************

Calculates the sine value of a numeric expression.

Syntax
==========


.. code-block:: postgres

   SIN( expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Numeric expression representing an angle in radians

Returns
============

When using the ``SIN`` floating point number scalar function, real arguments are automatically cast to double precision.

Notes
=======

* The result is in the range ``[-1, 1]``.

* If the input value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE trig(f DOUBLE);
   
   INSERT INTO trig VALUES (0), (PI()/12), (PI()/8), (PI()/6)
      , (PI()/4), (PI()/3), (3*PI()/8), (5*PI()/12), (PI()/2);


Sine of π/2 (= 1)
------------------------------

.. tip:: Use :ref:`RADIANS<radians>` to convert degrees to radians

.. code-block:: psql

   numbers=> SELECT SIN(PI()/2), SIN(RADIANS(90));
   sin | sin0
   ----+-----
     1 |    1


Computing sine for a column, in radians
-------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, SIN(f) FROM trig;
   f      | sin   
   -------+-------
        0 |      0
   0.2618 | 0.2588
   0.3927 | 0.3827
   0.5236 |    0.5
   0.7854 | 0.7071
   1.0472 |  0.866
   1.1781 | 0.9239
    1.309 | 0.9659
   1.5708 |      1


