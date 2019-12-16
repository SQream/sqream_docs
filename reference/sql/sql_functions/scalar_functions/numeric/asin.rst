.. _asin:

**************************
``ASIN``
**************************

Returns the inverse sine value of a numeric expression

Syntax
==========


.. code-block:: postgres

   ASIN( expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Numeric expression in range ``[-1.0, 1.0]``

Returns
============

Always returns a floating point result of the inverse sine, in radians.

Notes
=======

* Valid inputs for an inverse sine are in the range ``[ -1.0 , 1.0]``. Inputs exceeding this range will result in an error.

* The result is given in radians, in the range ``[-π/2, π/2]``.

* If the input value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE trig(i INT, f DOUBLE);
   
   INSERT INTO trig VALUES (0,0.0), (1,-0.866)
   , (2,-0.707), (3,-0.5)
   , (4,0.5), (5,0.707)
   , (6, 0.866), (7, 1);


Inverse sine of 1 (= π/2)
-------------------------------

.. code-block:: psql

   numbers=> SELECT ASIN(1);
   asin
   -------------------
   1.5707963267948966

Computing inverse sine for a column
-------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, ASIN(f) FROM trig;
   f     | asin 
   ------+------
       0 |     0
   -0.87 | -1.05
   -0.71 | -0.79
    -0.5 | -0.52
     0.5 |  0.52
    0.71 |  0.79
    0.87 |  1.05
       1 |  1.57



