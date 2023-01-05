.. _round:

**************************
ROUND
**************************

Rounds a numeric expression to the nearest precision.

See also :ref:`ceiling`, :ref:`floor`.

Syntax
==========

.. code-block:: postgres

   ROUND( numeric ) -> numeric
   ROUND( numeric [, int ] ) -> numeric
   ROUND( double ) -> double
   
Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``numeric``
     - Stores numeric values such as integers, decimal numbers, and currency values
   * - ``int``
     - Stores integer values

Returns
============

The ``ROUND()`` function returns a ``numeric`` value when used with numeric input types, such as ``integer`` or ``decimal``. When the input is ``double``, the return type is also ``double``.


.. note:: ``integer`` data types are automatically cast to ``numeric`` data types.

Notes
=======

If the input value is NULL, the result is NULL.

Examples
===========

Rounding to the nearest integer
-------------------------------------

.. code-block:: psql

   numbers=> SELECT ROUND(x) FROM (VALUES (0.0001), (PI()), (-2.718281), (500.1234), (0.5), (1.5)) as t(x);
   round
   ------
       0
       3
      -3
     500
       1
       2

Rounding to 2 digits after the decimal point
--------------------------------------------------

.. code-block:: psql

   numbers=> SELECT ROUND(x,2) FROM (VALUES (0.0001), (PI()), (-2.718281), (500.1234)) as t(x);
   round 
   -------
        0
     3.14
    -2.72
   500.12
   
:ref:`floor` vs. :ref:`ceiling` vs. ``ROUND``
------------------------------------------------------------

.. code-block:: psql

   numbers=> SELECT FLOOR(x), CEIL(x), ROUND(x) 
   .      FROM (VALUES (0.0001), (-0.0001)
   .           , (PI()), (-2.718281), (500.1234)) as t(x);
   floor | ceil | round
   ------+------+------
       0 |    1 |    0
      -1 |    0 |    0
       3 |    4 |    3
      -3 |   -2 |   -3
     500 |  501 |  500
