.. _exp:

**************************
EXP
**************************

Returns the natural exponent value of a numeric expression (*e*\ :sup:`x`).

See also :ref:`log`.

Syntax
==========

.. code-block:: postgres

   EXP( expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Positive numeric expression

Returns
============

When using the ``EXP`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.

Notes
=======

* If the input value is NULL, the result is NULL.

Examples
===========

Natural exponent values
--------------------------

.. code-block:: psql

   numbers=> SELECT EXP(x) FROM (VALUES (1.0), (2.0), (4.0)) as t(x);
      exp 
   -------
    2.7183
    7.3891
   54.5982

