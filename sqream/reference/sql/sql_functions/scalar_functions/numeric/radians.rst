.. _radians:

**************************
RADIANS
**************************

Converts a numeric expression from degree values to radian values.

See also :ref:`DEGREES<degrees>`.

Syntax
==========

.. code-block:: postgres

   RADIANS( expr )

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

Always returns a floating point result of the value in radians.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE trig(f DOUBLE);
   
   INSERT INTO trig VALUES (0), (15), (22.5)
      , (30), (45), (60), (67.5), (75), (90);
   
    -- Equivalent to these values in radians:
    --  (0), (PI()/12), (PI()/8), (PI()/6)
    -- ,(PI()/4), (PI()/3), (3*PI()/8), (5*PI()/12), (PI()/2);

.. code-block:: psql

   numbers=> SELECT f, RADIANS(f) FROM trig;
   f    | radians
   -----+--------
      0 |       0
     15 |  0.2618
   22.5 |  0.3927
     30 |  0.5236
     45 |  0.7854
     60 |  1.0472
   67.5 |  1.1781
     75 |   1.309
     90 |  1.5708


