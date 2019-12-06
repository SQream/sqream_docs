.. _coalesce:

**************************
COALESCE
**************************

Evaluates and returns the first non-null expression, or ``NULL`` if all expressions are ``NULL``.

Syntax
==========

.. code-block:: postgres

   COALESCE( expr, [, ...] )
   

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr1``, ``expr2``, ...
     - Expressions of the same type

Returns
============

Returns the first non-null argument or ``NULL`` if all expressions are null.

Notes
=======

* All expressions must have the same type, which is also the type of the result.

* ``ISNULL(x,y)`` is equivalent to ``COALESCE(x,y)``. Some RDBMSs call this function ``IFNULL``.

Examples
===========

Coalesece
------------
.. code-block:: psql

   master=> SELECT COALESCE(NULL, NULL, NULL, 5);
   5
   

Replacing ``NULL`` values in aggregations
--------------------------------------------

In some cases, replacing ``NULL`` values with a default can affect results.


.. code-block:: psql

   master=> SELECT 
   .>               AVG(num_eyes),
   .>               AVG(COALESCE(num_eyes,2)) AS "Corrected average"
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

