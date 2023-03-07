.. _sqrt:

**************************
SQRT
**************************

Calculates the square root value of a non-negative numeric expression.

Syntax
==========

.. code-block:: postgres

   SQRT( expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Non-negative numeric expression

Returns
============

When using the ``SQRT`` floating point number scalar function, ``real`` arguments are automatically cast to ``double`` precision.


Notes
=======

* If the value is NULL, the result is NULL.

* If the numeric expression is negative (<0), an error will be shown.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE cool_numbers(i INT, f DOUBLE);
   
   INSERT INTO cool_numbers VALUES (1,1.618033), (-12, -34)
   , (22, 3.141592), (-26538, 2.7182818284)
   , (NULL, NULL), (NULL,1.4142135623)
   , (42,NULL), (-42, NULL)
   , (-474, 365);

.. code-block:: psql

   numbers=> SELECT SQRT(2);
   sqrt
   ------------------
   1.4142135623730951

.. note:: 

   * Some clients may show fewer digits. See your client settings to change the precision shown.

Replacing negative values with ``NULL``
-------------------------------------------

Combine with ``CASE`` to filter out negative results:

.. code-block:: psql

   numbers=> SELECT i, SQRT(CASE WHEN i>=0 THEN i ELSE NULL END) FROM cool_numbers;
   i      | sqrt
   -------+-----
        1 |    1
      -12 |     
       22 | 4.69
   -26538 |     
          |     
          |     
       42 | 6.48
      -42 |     
     -474 |     

