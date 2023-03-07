.. _cot:

**************************
COT
**************************

Calculates the cotangent value of a numeric expression

Syntax
==========


.. code-block:: postgres

   COT( expr )

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

When using the ``COT`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

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


Cotangent of π/4 (= 1)
------------------------------

.. tip:: Use :ref:`RADIANS<radians>` to convert degrees to radians

.. code-block:: psql

   numbers=> SELECT COT(PI()/4), COT(RADIANS(45));
   cot | cot0
   ----+-----
     1 |    1


Computing cotangents for a column, in radians
-----------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT f, COT(f) FROM trig;
   f      | cot              
   -------+------------------
        0 | 16331239353195370
   0.2618 |            3.7321
   0.3927 |            2.4142
   0.5236 |            1.7321
   0.7854 |                 1
   1.0472 |            0.5774
   1.1781 |            0.4142
    1.309 |            0.2679
   1.5708 |                 0


