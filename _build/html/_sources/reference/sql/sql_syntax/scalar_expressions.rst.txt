.. _scalar_expressions:

***************************
Scalar expressions
***************************

Scalar expressions are functions that calculate a single (scalar) value, even if executed on an entire column. They can be stored as a row value, as opposed to a table value which is a result set consisting of more than one column and/or row.

A scalar expression can be any one of these:

.. contents::
   :local:
   :depth: 1

.. 
  *_string_literal_*
    | *_number_literal_*
    | NULL | TRUE | FALSE
    | *_typed_literal_*
    | *_value_expr_* *_binary_operator_* *_value_expr_*
    | *_unary_operator_* *_value_expr_*
    | *_value_expr_* *_postfix_unary_operator_*
    | *_special_operator_*
    | *_extract_operator_*
    | *_case_expression_*
    | *_conditional_expression_*
    | ( *_value_expr_* )
    | *_identifier_*
    | *_star_*
    | *_function_app_*
    | *_aggregate_function_app_*
    | *_window_function_app_*
    | *_cast_operator_*

           

Literals
=============

:ref:`Literals<literals>` are constant values.

Column references
=====================

A column reference is a column name, alias, or ordinal.

For example, in ``SELECT name FROM users``, the column reference refers to the column titled ``name``.

Column names may be aliased. For example in ``SELECT name as "First name" from users``, the column reference is the alias ``"First name"``, which is quoted to maintain the case and use of space.

A column may also be referneced using an ordinal, for example in a ``GROUP BY`` or ``ORDER BY``. In this query ``SELECT AVG(Salary),Team FROM nba GROUP BY 2``, the ordinal ``2`` refers to the second column in the select list, ``Team``.

Operators
=================

Operators, frequently used for comparison, usually come in three forms:

Unary operator
----------------

A prefix or postfix to an expression or literals. For example, ``-``, which is used to negate numbers.

.. code-block:: postgres
   
   prefix_unary_operator ::=
      + | - | NOT

   postfix_unary_operator ::=
      IS NULL | IS NOT NULL


Binary operator
-----------------

Two expressions or literals separated by an operator. For example, ``+`` which is used to add two numbers.

.. code-block:: postgres

   binary_operator ::= 
      . | + | ^ | * | / | % | + | - | >= | <= | != | <> | ||
      | LIKE | NOT LIKE | RLIKE | NOT RLIKE | < | > | = | OR | AND


Special operators for set membership
----------------------------------------

.. code-block:: postgres

   special_operator ::=
       value_expr IN ( value_expr [, ... ] )
       | value_expr NOT IN ( value_expr [, ... ] )
       | value_expr BETWEEN value_expr AND value_expr
       | value_expr NOT BETWEEN value_expr AND value_expr

These operators return TRUE if the ``value_expr``  on the left matches the expression on the right for set membership or if the value is in-range.

.. note:: The data type of the left ``value_expr`` must match the type of the right side ``value_expr``.

Comparisons
-------------

Binary operators are frequently used to compare values.

Comparison operators (``<`` ``>`` ``=`` ``<=`` ``>=`` ``<>`` ``!=``, ``IS NULL``, ``IS NOT NULL`` always returns ``BOOL``

These operators are:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Operator
     - Name
   * - ``<``
     - Smaller than
   * - ``<=``
     - Smaller than or equal to
   * - ``>``
     - Greater than
   * - ``>=``
     - Greater than or equal to
   * - ``=``
     - Equals
   * - ``<>`` or ``!=``
     - Not equal to
   * - ``IS``
     - Identical to 
   * - ``IS NOT``
     - Not identical to

.. note::
   NULL values are handled differently than other value expressions:
   
   * ``NULL`` is always smaller than anything, including another ``NULL``.

   * ``NULL`` is never equal to anything, including another ``NULL`` (``=``). To check if a value is null, use ``IS NULL``

Operator precedence
---------------------

The table below lists the operators in decreasing order of precedence.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Precedence
     - Operator
     - Associativity
   * - Highest
     - ``.``
     - left
   * -
     - ``+`` ``-`` (unary)
     -
   * -
     - ``^``
     - left
   * - 
     - ``*`` ``/`` ``%``
     - left
   * - 
     - ``+`` ``-`` (binary)
     - left
   * - 
     - ``||``
     - right
   * - 
     - ``BETWEEN``, ``IN``, ``LIKE``, ``RLIKE``
     -
   * -
     -  ``<`` ``>`` ``=`` ``<=`` ``>=`` ``<>`` ``!=``
     -
   * -
     - ``IS NULL``, ``IS NOT NULL``
     -
   * -
     - ``NOT``
     -
   * - 
     - ``AND``
     - left
   * - Lowest
     - ``OR``
     - left

.. tip:: Use parentheses to avoid ambiguous situations when using binary operators.

.. note:: The NOT variations, such as ``NOT BETWEEN``, ``NOT IN``, ``NOT LIKE``, ``NOT RLIKE`` have the same precedence as their non-``NOT`` variations.

