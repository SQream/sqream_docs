.. _pi:

**************************
PI
**************************

Returns a constant value of π

Syntax
==========


.. code-block:: postgres

   PI( )

Arguments
============

None

Returns
============

Always returns a floating point value of π, to 10 digits after the decimal.


Examples
===========

Using PI() to represent degrees in radians
----------------------------------------------

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

Sine of π/2 (= 1)
------------------------------

.. code-block:: psql

   numbers=> SELECT SIN(PI()/2), SIN(RADIANS(90));
   sin | sin0
   ----+-----
     1 |    1
