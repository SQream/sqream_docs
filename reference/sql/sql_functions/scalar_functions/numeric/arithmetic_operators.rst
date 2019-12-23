.. _arithmetic_operators:

**************************
Arithmetic operators
**************************

Arithmetic operators are functions that can be used as infix operators, or as prefix operators.

Syntax
==========

.. code-block:: postgres

   arithmetic_expr ::=
      | value_expr binary_operator value_expr
      | unary_operator value_expr

   arithmetic_infix_operator ::=
      + | - | * | / | %
      
   arithmetic_unary_operator ::=
      + | -

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``value_expr``
     - Numeric expression, or expression that can be cast to a numeric expression

Arithmetic operators
=======================

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Operator
     - Syntax
     - Description
   * - ``+`` (unary)
     - ``+a``
     - Converts a string to a numeric value. Identical to ``a :: double``
   * - ``+``
     - ``a + b``
     - Adds two expressions together
   * - ``-`` (unary)
     - ``-a``
     - Negates a numeric expression
   * - ``-``
     - ``a - b``
     - Subtracts ``b`` from ``a``
   * - ``*``
     - ``a * b``
     - Multiplies ``a`` by ``b``
   * - ``/``
     - ``a / b``
     - Divides ``a`` by ``b``
   * - ``%``
     - ``a % b``
     - Modulu of ``a`` by ``b``. See also :ref:`mod`

Notes
=======

* If any of the inputs value are NULL, the result is NULL.


Examples
===========

Coercing with a unary ``+``
--------------------------------

.. code-block:: psql

   numbers=> SELECT +'5';
   5.00


Using infix operators
---------------------------

.. code-block:: psql

   numbers=> SELECT 5*3 AS "5*3", 5+3 AS "5+3", 2-5 AS "2-5"
   .>               , 2.0-5 AS "2.0-5", 11 % 5 AS "11%5", 11/5 AS "11/5", 11.0 / 5 AS "11.0/5";
   5*3 | 5+3 | 2-5 | 2.0-5 | 11%5 | 11/5 | 11.0/5
   ----+-----+-----+-------+------+------+-------
    15 |   8 |  -3 |    -3 |    1 |    2 |    2.2



