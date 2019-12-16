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

* The result is given in radians, in the range ``[-π/2, π/2]``.

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
   f      | atan       
   -------+------------
    -9999 | -1.57069632
       -3 | -1.24904577
       -2 | -1.10714872
   -1.732 | -1.04718485
       -1 | -0.78539816
     -0.5 | -0.46364761
        0 |         0.0
      0.5 |  0.46364761
        1 |  0.78539816
    1.732 |  1.04718485
        2 |  1.10714872
        3 |  1.24904577
     9999 |  1.57069632




