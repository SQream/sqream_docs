.. _lead:

**************************
LEAD
**************************

Returns a value from a subsequent row within the partition of a result set.

See also: :ref:`lag`.

Syntax
==========

.. code-block:: postgres

   LEAD ( expr [, offset ])
      OVER (   
            [ PARTITION BY partition_expr [, ...] ]  
            [ ORDER BY order [ ASC | DESC ] [, ...]]   
         )

   offset ::= integer


Arguments
============


.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Any value expression
   * - ``offset``
     - Specifies the offset of rows to scan forward. If not specified, defaults to 1.


Returns
============

Same type as ``expr``.

Notes
=======

* ``offset`` is evaluated with respect to the current row. If not specified, ``offset`` defaults to 1.

* If there is no subsequent row (calculated against the current row), ``LEAD`` returns ``NULL``.

Examples
===========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      "Name" text(40),
      "Team" text(40),
      "Number" tinyint,
      "Position" text(2),
      "Age" tinyint,
      "Height" text(4),
      "Weight" real,
      "College" text(40),
      "Salary" float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Using ``LEAD`` to access next rows
-----------------------------------------------------------

.. versionchanged:: 2020.2
   :ref:`lag` and :ref:`lead` are supported from v2020.2.

This example calculates the salary between two players, starting from the highest salary.


.. code-block:: psql
   
   t=> SELECT "Name",
   .          "Salary",
   .          LEAD("Salary") OVER (ORDER BY "Salary" DESC) AS "Salary - next",
   .          "Salary" - LEAD("Salary",1) OVER (ORDER BY "Salary" DESC) AS "Salary - diff"
   .          -- LEAD("Salary",1) is equivalent to LEAD("Salary")
   .   FROM   nba
   .   LIMIT 11 ;
   Name            | Salary   | Salary - next | Salary - diff
   ----------------+----------+---------------+--------------
   Kobe Bryant     | 25000000 |      22970500 |       2029500
   LeBron James    | 22970500 |      22875000 |         95500
   Carmelo Anthony | 22875000 |      22359364 |        515636
   Dwight Howard   | 22359364 |      22192730 |        166634
   Chris Bosh      | 22192730 |      21468695 |        724035
   Chris Paul      | 21468695 |      20158622 |       1310073
   Kevin Durant    | 20158622 |      20093064 |         65558
   Derrick Rose    | 20093064 |      20000000 |         93064
   Dwyane Wade     | 20000000 |      19689000 |        311000
   Brook Lopez     | 19689000 |      19689000 |             0
   DeAndre Jordan  | 19689000 |      19689000 |             0


