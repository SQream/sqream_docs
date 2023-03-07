.. _cos:

**************************
COS
**************************

Returns the cosine value of a numeric expression.

Syntax
==========


.. code-block:: postgres

   COS( expr )

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

When using the ``COS`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

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


Cosine of 0 (= 1)
------------------------------

.. code-block:: psql

   numbers=> SELECT COS(0);
   cos
   ---
   1.0

Computing cosine for a column, in radians
-------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, COS(f) FROM trig;
   f      | cos   
   -------+-------
        0 |      1
   0.2618 | 0.9659
   0.3927 | 0.9239
   0.5236 |  0.866
   0.7854 | 0.7071
   1.0472 |    0.5
   1.1781 | 0.3827
    1.309 | 0.2588
   1.5708 |      0

