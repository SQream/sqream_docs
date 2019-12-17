.. _joins:

***************************
Joins
***************************

Joins combine results from two or more table expressions (tables, external tables, views) to form a new result set.

The combination of these table expressions ca nbe based on a set of conditions, such as equality of columns.

Joins are useful when data in tables are related. For example, when two tables contain one or more columns in common, so that rows can be matched or correlated with rows from the other table.

Syntax
==========

.. code-block:: postgres

   table_ref ::=
       | left_side join_type right_side
           [ ON value_expr ]
       | table_alias

   join_type ::=
       [ INNER ] [ join_hint ] JOIN
       | LEFT [ OUTER ] [ join_hint ] JOIN
       | RIGHT [ OUTER ] [ join_hint ] JOIN
       | CROSS [ join_hint ] JOIN

   join_hint ::=
       MERGE | LOOP

Join types
-------------

Inner join
^^^^^^^^^^^^

.. code-block:: postgres

   left_side [ INNER ] JOIN right_side ON value_expr
   left_side [ INNER ] JOIN right_side USING ( join_column [, ... ] )


This is the default join type.
Rows from the ``left_side`` and ``right_side`` that match the condition are returned.

An inner join can also be specified by listing several tables in the ``FROM`` clause.
Omitting the ``ON`` or ``WHERE`` will result in a ``CROSS JOIN``, where every row of ``left_side`` is matched with every row on ``right_side``.

Left outer join
^^^^^^^^^^^^^^^^^^

.. code-block:: postgres

   left_side LEFT [ OUTER ] JOIN right_side ON value_expr
   left_side LEFT [ OUTER ] JOIN right_side USING ( join_column [, ... ] )

Similar to the inner join - but for every row of ``left_side`` that does not match, ``NULL`` values are returned for columns on ``right_side``


Right outer join
^^^^^^^^^^^^^^^^^^^

.. code-block:: postgres

   left_side RIGHT [ OUTER ] JOIN right_side ON value_expr
   left_side RIGHT [ OUTER ] JOIN right_side USING ( join_column [, ... ] )

Similar to the inner join - but for every row of ``right_side`` that does not match, ``NULL`` values are returned for columns on ``left_side``

Cross join
^^^^^^^^^^^^^

.. code-block:: postgres

   left_side CROSS JOIN right_side

A cartesian product - all rows match on all sides. For every row from ``left_side`` and ``right_side``, the result set will contain a row with all columns from ``left_side`` and all columns from ``right_side``. 

The ``CROSS JOIN`` can't have an ``ON`` clause, but ``WHERE`` can be used to limit the result set.

Join conditions
--------------------------------------------------------

``ON value_expr``
^^^^^^^^^^^^^^^^^^^^^^

The ``ON`` condition is an expression that evaluates to a boolean to identify whether the rows match.

For example, ``ON left_side.name = right_side.name`` matches when both name columns match.

For ``LEFT`` and ``RIGHT`` joins, the ``ON`` clause is optional. However, if it is not specified, the result is a computationally intensive ``CROSS JOIN``.

.. tip:: SQream DB does not support the ``USING`` syntax. However, queries can be easily rewritten. ``left_side JOIN right_side using (name)`` is equivalent to ``ON left_side.name = right_side.name``



Examples
=============

Assume a pair of tables with the following structure and content:

.. code-block:: postgres
   
   CREATE TABLE left_side (x INT);
   INSERT INTO left_side VALUES (1), (2), (4), (5);

   CREATE TABLE right_side (x INT);
   INSERT INTO right_side VALUES (2), (3), (4), (5), (6);

Inner join
------------

In inner joins, values that are not matched do not appear in the result set.

.. code-block:: psql

   t=> SELECT * FROM left_side AS l JOIN right_side AS r 
   .>         ON l.x = r.x;
   x | x0
   --+---
   2 |  2
   4 |  4
   5 |  5

Left join
------------

.. note:: Note the null values for ``1`` which were not matched. SQream DB outputs nulls last.

.. code-block:: psql

   t=> SELECT * FROM left_side AS l LEFT JOIN right_side AS r 
   .>         ON l.x = r.x;
   x | x0
   --+---
   2 |  2
   4 |  4
   5 |  5
   1 | \N

Right join
------------

.. note:: Note the null values for ``3``, ``6`` which were not matched. SQream DB outputs nulls last. 

.. code-block:: psql

   t=> SELECT * FROM left_side AS l LEFT JOIN right_side AS r 
   .>         ON l.x = r.x;
   x  | x0
   ---+---
   2  |  2
   4  |  4
   5  |  5
   \N |  3
   \N |  6

Cross join
-------------

.. code-block:: psql

   t=> SELECT * FROM left_side AS l CROSS JOIN right_side AS r;
   x | x0
   --+---
   1 |  2
   1 |  3
   1 |  4
   1 |  5
   1 |  6
   2 |  2
   2 |  3
   2 |  4
   2 |  5
   2 |  6
   4 |  2
   4 |  3
   4 |  4
   4 |  5
   4 |  6
   5 |  2
   5 |  3
   5 |  4
   5 |  5
   5 |  6

Specifying multiple comma-separated tables is equivalent to a cross join, that can then be filtered with a ``WHERE`` clause..

.. code-block:: psql

   t=> SELECT * FROM left_side l, right_side r;
   x | x0
   --+---
   1 |  2
   1 |  3
   1 |  4
   1 |  5
   1 |  6
   2 |  2
   2 |  3
   2 |  4
   2 |  5
   2 |  6
   4 |  2
   4 |  3
   4 |  4
   4 |  5
   4 |  6
   5 |  2
   5 |  3
   5 |  4
   5 |  5
   5 |  6

   t=> SELECT * FROM left_side l, right_side r WHERE (r.x=l.x);
   x | x0
   --+---
   2 |  2
   4 |  4
   5 |  5

Join hints
-------------

Join hints can be used to override the query compiler and choose a particular join algorithm.

The available algorithms are ``LOOP`` (corresponding to non-indexed nested loop join algorithm), and ``MERGE`` (corresponding to sort merge join algorithm).

If no algorithm is specified, a loop join is performed by default.

.. code-block:: psql
   
   t=> SELECT * FROM left_side AS l INNER MERGE JOIN right_side AS r  ON l.x = r.x;
   x | x0
   --+---
   2 |  2
   4 |  4
   5 |  5
   
   t=> SELECT * FROM left_side AS l INNER LOOP JOIN right_side AS r  ON l.x = r.x; 
   x | x0
   --+---
   2 |  2
   4 |  4
   5 |  5


