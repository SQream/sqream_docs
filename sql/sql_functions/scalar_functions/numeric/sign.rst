:orphan:

.. _sign:

****
SIGN
****

The ``SIGN`` function takes a single argument, which can be any numeric data type such as INTEGER, FLOAT, or DECIMAL, and returns a value of -1, 0, or 1, depending on the sign of the input argument.



Syntax
======

.. code-block:: postgres

	SELECT SIGN(expr);

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``numeric_expression``
     - Numeric data types

Return
======

The ``SIGN`` function returns the same data type as inserted, with the exception of ``REAL``, which is converted to ``DOUBLE``.

Depending on the sign of the input argument, the return is:

* -1, if the input expression is negative

* 0, if the input expression is zero

* 1, if the input expression is positive
 


Example
=======

.. code-block:: postgres

	SELECT SIGN(-10), SIGN(0), SIGN(5) ;
	
Output:

.. code-block:: none

   sign | sign0 | sign1
   -----+------+-------
     -1 |   0  |   1
