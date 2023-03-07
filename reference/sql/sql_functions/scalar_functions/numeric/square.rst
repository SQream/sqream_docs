.. _square:

**************************
SQUARE
**************************

Returns the square value of a numeric expression (x\ :sup:`2`).

``SQUARE(x)`` is equivalent to ``POWER(x,2)``. See :ref:`POWER<power>`.

Syntax
==========

.. code-block:: postgres

   SQUARE( expr )

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

When using the ``SQUARE`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

.. code-block:: psql

   numbers=> SELECT SQUARE(3);
   square
   ------
      9.0
