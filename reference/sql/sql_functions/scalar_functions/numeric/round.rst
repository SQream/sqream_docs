.. _round:

**********
ROUND
**********

Rounds a numeric expression to the nearest precision. 

Supported data types: ``INT``, ``TINYINT``, ``SMALLINT``, ``BIGINT``, ``REAL``, ``DOUBLE``, ``NUMERIC``.

See also :ref:`ceiling`, :ref:`floor`.

Syntax 
======

.. code-block:: postgres

   ROUND( expr [, scale ] )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Numeric expression to round
   * - ``scale``
     - Number of digits after the decimal point to round to. Defaults to 0 if not specified.

Returns
============

``REAL`` arguments are automatically cast to double precision, while all other supported data types retain the supplied data type.

Notes
=======

If the input value is ``NULL``, the result is ``NULL``.

Examples
===========

Rounding to the nearest integer
-------------------------------------

.. code-block:: psql

   SELECT ROUND(x) FROM (VALUES (0.0001), (PI()), (-2.718281), (500.1234), (0.5), (1.5)) as t(x);
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

   SELECT ROUND(x,2) FROM (VALUES (0.0001), (PI()), (-2.718281), (500.1234)) as t(x);
   round 
   -------
        0
     3.14
    -2.72
   500.12
   
:ref:`floor` vs. :ref:`ceiling` vs. ``ROUND``
------------------------------------------------------------

.. code-block:: psql

   SELECT FLOOR(x), CEIL(x), ROUND(x) 
   .      FROM (VALUES (0.0001), (-0.0001)
   .           , (PI()), (-2.718281), (500.1234)) as t(x);
   floor | ceil | round
   ------+------+------
       0 |    1 |    0
      -1 |    0 |    0
       3 |    4 |    3
      -3 |   -2 |   -3
     500 |  501 |  500
