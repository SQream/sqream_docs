.. _isnull:

**************************
ISNULL
**************************

Evaluates an expression and returns a default value if the expression is ``NULL``.

Syntax
==========

.. code-block:: postgres

   ISNULL( expr, value_expr )
   

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Expressions to evaluate
   * - ``value_expr``
     - Default value to return if ``expr`` is null

Returns
============

Returns either ``expr`` or ``value_expr``.

Notes
=======

* All expressions must have the same type, which is also the type of the result.

* See also :ref:`COALESCE<coalesce>`. ``ISNULL(x,y)`` is equivalent to ``COALESCE(x,y)``.

Examples
===========

ISNULL
------------
.. code-block:: psql

   master=> SELECT ISNULL(NULL, 5);
   5
   

Replacing ``NULL`` values in aggregations
--------------------------------------------

In some cases, replacing ``NULL`` values with a default can affect results.


.. code-block:: psql

   master=> SELECT 
   .>               AVG(num_eyes),
   .>               AVG(ISNULL(num_eyes,2)) AS "Corrected average"
   .>
   .>       FROM (
   .>             VALUES ('Copepod',1),('Spider',8)
   .>                   ,('Starfish',5),('Praying mantis',5)
   .>                   ,('Human (average)',2),('Eagle',2)
   .>                   ,('Horseshoe crab',10),('Kiwi',NULL)
   .>                   ,('Fox',NULL),('Badger',NULL)
   .>             ) AS cool_animals (name , num_eyes);
   avg | Corrected average
   ----+------------------
     4 |                 3

