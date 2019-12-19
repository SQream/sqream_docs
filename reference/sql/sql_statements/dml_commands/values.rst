.. _values:

**********************
VALUES
**********************

``VALUES`` is a table constructor - a clause that can be used to define tabular data.

.. tip:: 
   * Use VALUES in conjunction with :ref:`INSERT<insert>` statements to insert a set of one or more rows.

.. note:: The maximum number of values in the ``VALUE`` clause is limited to 500.

Permissions
=============

This clause requires no special permissions.

Syntax
==========

.. code-block:: postgres

   values_expr ::=
        VALUES ( value_expr [, ... ] ) [, ... ]
       ;

Notes
===========

Each set of comma-separated ``value_expr`` in parentheses represents a single row in the result set.

Column names of the result table are auto-generated. To rename the column names, add an ``AS`` clause.

Examples
===========

Tabular data with VALUES
--------------------------

.. code-block:: psql

   master=> VALUES (1,2,3,4), (5,6,7,8), (9,10,11,12);
   1,2,3,4
   5,6,7,8
   9,10,11,12
   3 rows

Using VALUES with a SELECT query
----------------------------------

To use VALUES in a select query, assign a :ref:`name<identifiers>` to the ``VALUES`` clause with ``AS``

.. code-block:: postgres

   master=> SELECT t.* FROM (VALUES (1,2,3,'a'), (5,6,7,'b'), (9,10,11,'c')) AS t;
   1,2,3,a
   5,6,7,b
   9,10,11,c
   
   3 rows

You can also use this to rename the columns

.. code-block:: postgres

   SELECT t.* FROM (VALUES (1,2,3,'a'), (5,6,7,'b'), (9,10,11,'c')) AS t(a,b,c,d);


Creating a table with ``VALUES``
---------------------------------

Use ``AS`` to assign names to columns

.. code-block:: postgres

   CREATE TABLE cool_animals AS 
      (SELECT t.* 
      FROM   (VALUES (1, 'dog'), 
                     (2, 'cat'), 
                     (3, 'horse'), 
                     (4, 'hippopotamus')
              ) AS t(id, name)
      ); 