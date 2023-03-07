.. _acos:

**************************
ACOS
**************************

Returns the inverse cosine value of a numeric expression

Syntax
==========


.. code-block:: postgres

   ACOS( expr )

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

When using the ``ACOS`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

Notes
=======

* Valid inputs for an inverse cosine are in the range ``[ -1.0 , 1.0]``. Inputs exceeding this range will result in an error.

* The result is given in radians, in the range ``[0, π]``.

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


Inverse cosine of 0 (= π/2)
-------------------------------

.. code-block:: psql

   numbers=> SELECT ACOS(0);
   acos
   -------------------
   1.5707963267948966

Computing inverse cosine for a column
-------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, ACOS(f) FROM trig;
   f     | acos
   ------+-----
       0 | 1.57
   -0.87 | 2.62
   -0.71 | 2.36
    -0.5 | 2.09
     0.5 | 1.05
    0.71 | 0.79
    0.87 | 0.52
       1 |    0


