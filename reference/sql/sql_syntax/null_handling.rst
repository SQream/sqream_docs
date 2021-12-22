.. _null_handling:

***************************
Null Handling
***************************
SQream handles ``NULL`` values similar to other RDBMSs, with some minor differences.

.. tip:: When using :ref:`sqream sql<sqream_sql_cli_reference>` ``NULL`` values are displayed as ``\N``. Different clients may show other values, including an empty string.

The **Null Handling
** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Comparisons
==============
Any comparison between a ``NULL`` and a value will result in ``NULL``. For example, writing ``WHERE a = NULL`` will never match to ``TRUE`` or ``FALSE``, because the comparison results in ``NULL``. Use :ref:`is_null` to check for ``NULL`` values in result sets.


Conditionals
===============
Functions such as **ISNULL** and **COALESCE** evaluate arguments in their given order, so they may never evaluate some arguments.

For example, ``COALESCE(a,b,c,d,NULL)`` will never evalulate ``b``, ``c``, ``d``, or ``NULL`` if ``a`` is not ``NULL``.

For more information, see the following:

* :ref:`isnull`
* :ref:`coalesce`

Operations
============
The **Operations** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Scalar Functions
---------------------
With all scalar functions, a ``NULL`` input to any one of the arguments means the result is ``NULL``:

.. code-block:: psql
   
   t=> SELECT x, y, z, x+y as "x+y", x*y as "x*y", y*z as "y*z", z-y as "z-y"  FROM n;
   x | y  | z  | x+y | x*y | y*z | z-y
   --+----+----+-----+-----+-----+----
   1 |  0 |  1 |   1 |   0 |   0 |   1
   2 |  1 |  1 |   3 |   2 |   1 |   0
   3 | \N |  4 |  \N |  \N |  \N |  \N
   4 | \N | \N |  \N |  \N |  \N |  \N
   5 |  6 | \N |  11 |  30 |  \N |  \N


Aggregates
---------------
With aggregates, ``NULL`` values are ignored, so they do not affect the result set:

.. code-block:: psql
   
   t=> SELECT SUM(x) AS "sum(x)", SUM(y) AS "sum(y)", SUM(z) AS "sum(z)" FROM n;
   sum(x) | sum(y) | sum(z)
   -------+--------+-------
       15 |      7 |      6
   
   t=> SELECT COUNT(x) AS "count(x)", COUNT(y) AS "count(y)", COUNT(z) AS "count(z)" FROM n;
   count(x) | count(y) | count(z)
   ---------+----------+---------
          5 |        3 |        3

The following applies when using aggregates:

* ``NULL`` values are not included in ``COUNT()`` of a column. ``COUNT(x)`` shows the full row-count because it's a non-nullable column. ``COUNT(y)`` returns 3 - just the non-``NULL`` values.

 ::

* ``NULL`` values are completely ignored when using the :ref:`min`, :ref:`max`, and :ref:`avg` functions.

Distincts
-----------
``NULL`` values are considered distinct, but only counted once:

.. code-block:: psql

   t=> SELECT DISTINCT z FROM n;
   z 
   --
    1
    4
   \N

Running :ref:`count` DISTINCT however, ignores the ``NULL`` values:

``NULL`` values are considered distinct, but only counted once.

.. code-block:: psql

   t=> SELECT COUNT(DISTINCT z) FROM n;
   count
   -----
       2

Sorting
========
When sorting a column containing ``NULL`` values, SQream DB sorts ``NULL`` values first with ``ASC`` and last with ``DESC``. 

SQream does not implement ``NULLS FIRST`` or ``NULLS LAST``, so where ``NULL`` appears cannot change where NULL values appear in the sort order:

.. code-block:: psql

   t=> SELECT * FROM n ORDER BY z ASC;
   x | y  | z 
   --+----+---
   4 | \N | \N
   5 |  6 | \N
   1 |  0 |  1
   2 |  1 |  1
   3 | \N |  4
   
   t=> SELECT * FROM n ORDER BY z DESC;
   x | y  | z 
   --+----+---
   3 | \N |  4
   1 |  0 |  1
   2 |  1 |  1
   4 | \N | \N
   5 |  6 | \N