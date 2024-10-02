:orphan:

.. _round:

*****
ROUND
*****

Rounds a numeric expression to the nearest precision. 

Supported data types: ``INT``, ``TINYINT``, ``SMALLINT``, ``BIGINT``, ``REAL``, ``DOUBLE``, ``NUMERIC``.

See also :ref:`ceiling`, :ref:`floor`.

Syntax
======

.. code-block:: postgres

   ROUND( expr [, scale ] )

Arguments
=========

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
=======

* ``ROUND(DECIMAL)`` returns a ``DOUBLE``

* ``ROUND(DOUBLE, 2)`` returns a ``DECIMAL``

Usage Notes
===========

If the input value is ``NULL``, the result is ``NULL``.

Examples
========

Rounding to the Nearest Integer
-------------------------------

.. code-block:: psql

	SELECT
	  ROUND(x)
	FROM
	  (
	    VALUES
	      (0.0001),
	      (PI()),
	      (-2.718281),
	      (500.1234),
	      (0.5),
	      (1.5)
	  ) as t(x);
  
Output:

.. code-block:: none
  
	round
	------
	   0
	   3
	  -3
	 500
	   1
	   2

Rounding to 2 Digits After the Decimal Point
--------------------------------------------

.. code-block:: psql

	SELECT
	  ROUND(x, 2)
	FROM
	  (
	    VALUES
	      (0.0001),
	      (PI()),
	      (-2.718281),
	      (500.1234)
	  ) as t(x);
  
Output:

.. code-block:: none
  
	round 
	-------
	 0.0
	 3.14
	-2.72
	500.12
   
``FLOOR`` Vs. ``CEILING`` Vs. ``ROUND``
---------------------------------------

.. code-block:: psql

	SELECT
	  FLOOR(x),
	  CEIL(x),
	  ROUND(x)
	FROM
	  (
	    VALUES
	      (0.0001),
	      (-0.0001),
	      (PI()),
	      (-2.718281),
	      (500.1234)
	  ) as t(x);
  
Output:

.. code-block:: none
  
	floor | ceil | round
	------+------+------
	    0 |    1 |    0
	   -1 |    0 |    0
	    3 |    4 |    3
	   -3 |   -2 |   -3
	  500 |  501 |  500
