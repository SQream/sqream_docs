.. _degrees:

**************************
``DEGREES``
**************************

Converts a numeric expression from radian values to degree values.

See also :ref:`radians`.

Syntax
==========

.. code-block:: postgres

   DEGREES( expr )

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

Always returns a floating point result of the value in degrees.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE trig(f DOUBLE);
   
   INSERT INTO trig VALUES (0), (PI()/12), (PI()/8), (PI()/6)
      , (PI()/4), (PI()/3), (3*PI()/8), (5*PI()/12), (PI()/2);

.. code-block:: psql

   numbers=> SELECT f, DEGREES(f) FROM trig;
   f      | degrees
   -------+--------
        0 |       0
   0.2618 |      15
   0.3927 |    22.5
   0.5236 |      30
   0.7854 |      45
   1.0472 |      60
   1.1781 |    67.5
    1.309 |      75
   1.5708 |      90

