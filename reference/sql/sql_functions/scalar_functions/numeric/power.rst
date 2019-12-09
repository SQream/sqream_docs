.. _power:

**************************
POWER
**************************

Returns the value of x to the power of y (x\ :sup:`y`).

``POWER(x,2)`` is equivalent to ``SQUARE(x)``. See :ref:`SQUARE<square>`.

Syntax
==========

.. code-block:: postgres

   POWER( expr )

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

returns the same type as the argument supplied.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

On integers
---------------

.. code-block:: psql

   numbers=> SELECT POWER(3,x) FROM (VALUES (1), (2), (3), (4), (5)) AS t(x);
   power
   -----
       3
       9
      27
      81
     243



On floating point
-------------------

.. code-block:: psql

   numbers=> SELECT POWER(3.0,x) FROM (VALUES (1), (2), (3), (4), (5)) AS t(x);
   power
   -----
     3.0
     9.0
    27.0
    81.0
   243.0

