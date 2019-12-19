.. _case:

**************************
CASE
**************************

A case expression can test a conditional expression, and depending on the result, evaluate additional expressions.

``CASE`` works like nested ``IF ... THEN ... ELSE ...``. When one of the conditions evaluates to ``TRUE``, the evaluation stops and the expression or operand assosicated with the result (``THEN ...``) is evaulated. Otherwise, the evaluation continues to the next condition. If no conditional matches, the ``ELSE`` result is returned.


Syntax
==========


.. code-block:: postgres

   case_expression ::=
       searched_case | simple_case

   searched_case ::=
       CASE 
         WHEN conditional_value_expr THEN result_value_expr
         [WHEN ...]
         [ELSE result_value_expr]
       END

   simple_case ::=
       CASE value_expr
           WHEN value_expr THEN result_value_expr
           [WHEN ...]
           [ELSE result_value_expr]
       END


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``conditional_value_expr``
     - A condition that evaluates to a boolean (``TRUE``, ``FALSE``, or ``NULL``)
   * - ``value_expr``
     - A general value expression or a literal.
   * - ``result_value_expr`` 
     - A general value expression or a literal. All data types of ``result_value_expr`` must match within a ``CASE``.

Returns
============

Returns an expression consistent with the type of ``result_value_expr``.

Notes
=======

* SQream DB does not support the ``IF .. THEN .. ELSE`` Syntax. A simple case expression can replace it.

* If no ``ELSE`` is specified, the default result will be ``NULL``.

* All ``WHEN ...`` expressions must have the same data type.

* All ``THEN ...`` and the ``ELSE`` results must have the same data type.

Simple case expression
-------------------------

.. code-block:: postgres
   
   simple_case ::=
       CASE value_expr
           WHEN value_expr THEN result_value_expr
           [WHEN ...]
           [ELSE result_value_expr]
       END

A simple case expression evaluates the condition (``conditional_value_expr``), and then evaluates and returns the result from the corresponding ``THEN``. 

If no matches are found, ``NULL`` is returned.

Searched case expression
---------------------------

.. code-block:: postgres

   searched_case ::=
       CASE 
         WHEN conditional_value_expr THEN result_value_expr
         [WHEN ...]
         [ELSE result_value_expr]
       END

A searched case expression evaluates every ``conditional_value_expr`` listed. At the first ``conditional_value_expr`` that evaluates to ``TRUE``, the result of the ``THEN`` will be returned.

If no matches are found, ``NULL`` is returned..

Examples
===========

Simple case
----------------

.. code-block:: psql

   master=> SELECT name, CASE num_eyes
   .>          WHEN 1 THEN 'Cyclops'
   .>          WHEN 2 THEN 'Binocular'
   .>          WHEN 5 THEN 'Pentocular'
   .>          WHEN 8 then 'Octocular'
   .>          ELSE 'Other'
   .>       END
   .>       FROM (VALUES ('Copepod',1), ('Spider',8), ('Starfish', 5), ('Praying mantis', 5), ('Human (average)', 2), ('Eagle', 2), ('Horseshoe crab', 10)) 
   .>          AS cool_animals(name, num_eyes);

   name            | ?column?  
   ----------------+-----------
   Copepod         | Cyclops   
   Spider          | Octocular 
   Starfish        | Pentocular
   Praying mantis  | Pentocular
   Human (average) | Binocular 
   Eagle           | Binocular 
   Horseshoe crab  | Other     

Searched case
-------------------------

.. code-block:: postgres

   SELECT age, CASE 
        WHEN age < 3 THEN 'Toddler'
        WHEN age < 12 THEN 'Child'
        WHEN age < 20 THEN 'Teenager'
        WHEN age < 34 THEN 'Young adult'
        WHEN age < 65 THEN 'Adult'
        ELSE 'Senior'
    END AS "Age Group"
   FROM (VALUES (2), (5), (15), (19), (32), (44), (87)) AS t(age);

.. code-block::

   age | Age group  
   ----+------------
     2 | Toddler    
     5 | Child      
    15 | Teenager   
    19 | Teenager   
    32 | Young adult
    44 | Adult      
    87 | Senior     

Replacing ``IF`` with ``CASE``
-----------------------------------

As SQream DB does not support the ``IF`` function found on some other DBMSs, use ``CASE`` instead.

.. code-block:: mysql
   
   -- MySQL Syntax:
   IF (age > 65, "Senior", "Other")

is functionally identical to:

.. code-block:: postgres

   CASE 
      WHEN age > 65 THEN 'Senior'
      ELSE 'Other'
   END



