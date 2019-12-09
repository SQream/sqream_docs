.. _atan:

**************************
ATAN
**************************

Returns the inverse tangent value of a numeric expression

Syntax
==========


.. code-block:: postgres

   ATAN( expr )

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

Always returns a floating point result of the inverse tangent, in radians.

Notes
=======

* The result is given in radians, in the range ``[-pi/2, pi/2]``.

* If the input value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE trig(f DOUBLE);
   
   INSERT INTO trig VALUES (-9999), (-3), (-2), (-1.732)
   , (-1), (-0.5), (0), (0.5)
   , (1), (1.732), (2), (3), (9999);


Inverse tangent of 1 (= π/4)
-------------------------------

.. code-block:: psql

   numbers=> SELECT ATAN(1);
   atan
   ----
   0.7853981633974483


Computing inverse tangent for a column
-------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, ASIN(f) FROM trig;
   f     | atan 
   ------+------
   -9999 | -1.57
      -3 | -1.25
      -2 | -1.11
   -1.73 | -1.05
      -1 | -0.79
    -0.5 | -0.46
       0 |     0
     0.5 |  0.46
       1 |  0.79
    1.73 |  1.05
       2 |  1.11
       3 |  1.25
    9999 |  1.57



