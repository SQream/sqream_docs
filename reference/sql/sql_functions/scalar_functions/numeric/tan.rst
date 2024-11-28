.. _tan:

**************************
TAN
**************************

Returns the tangent value of a numeric expression

Syntax
==========


.. code-block:: postgres

   TAN( expr )

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

When using the ``TAN`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

Notes
=======

* The result is in the range ``[0, infinity)``.

* If the input value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE trig(f DOUBLE);
   
   INSERT INTO trig VALUES (0), (PI()/12), (PI()/8), (PI()/6)
      , (PI()/4), (PI()/3), (3*PI()/8), (5*PI()/12), (PI()/2);


Tangent of π/4 (= 1)
------------------------------

.. tip:: Use :ref:`RADIANS<radians>` to convert degrees to radians

.. code-block:: psql

   numbers=> SELECT TAN(PI()/4), TAN(RADIANS(45));
   tan | tan0
   ----+-----
     1 |    1


Computing tangents for a column, in radians
---------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, TAN(f) FROM trig;
   f      | tan              
   -------+------------------
        0 |                 0
   0.2618 |            0.2679
   0.3927 |            0.4142
   0.5236 |            0.5774
   0.7854 |                 1
   1.0472 |            1.7321
   1.1781 |            2.4142
    1.309 |            3.7321
   1.5708 | 16331239353195370



