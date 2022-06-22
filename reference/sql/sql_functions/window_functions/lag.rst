.. _lag:

**************************
LAG
**************************

Returns a value from a previous row within the partition of a result set.

See also: :ref:`lead`.

Syntax
==========

.. code-block:: postgres

   LAG ( expr [, offset ])
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
     - Specifies the offset of rows to scan back. If not specified, defaults to 1.


Returns
============

Same type as ``expr``.

Notes
=======

* ``offset`` is evaluated with respect to the current row. If not specified, ``offset`` defaults to 1.

* If there is no previous row (calculated against the current row), ``LAG`` returns ``NULL``.

Examples
===========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name varchar(40),
      Team varchar(40),
      Number tinyint,
      Position varchar(2),
      Age tinyint,
      Height varchar(4),
      Weight real,
      College varchar(40),
      Salary float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Using ``LAG`` to access previous rows
-----------------------------------------------------------

.. versionchanged:: 2020.2
   :ref:`lag` and :ref:`lead` are supported from v2020.2.

This example calculates the salary between two players, starting from the highest salary.


.. code-block:: psql
   
   t=> SELECT "Name",
   .          "Salary",
   .          LAG("Salary") OVER (ORDER BY "Salary" DESC) AS "Salary - previous",
   .          LAG("Salary",1) OVER (ORDER BY "Salary" DESC) - "Salary" AS "Salary - diff"
   .          -- LAG("Salary",1) is equivalent to LAG("Salary")
   .   FROM   nba
   .   LIMIT 11 ;
   Name            | Salary   | Salary - previous | Salary - diff
   ----------------+----------+-------------------+--------------
   Kobe Bryant     | 25000000 |                   |              
   LeBron James    | 22970500 |          25000000 |       2029500
   Carmelo Anthony | 22875000 |          22970500 |         95500
   Dwight Howard   | 22359364 |          22875000 |        515636
   Chris Bosh      | 22192730 |          22359364 |        166634
   Chris Paul      | 21468695 |          22192730 |        724035
   Kevin Durant    | 20158622 |          21468695 |       1310073
   Derrick Rose    | 20093064 |          20158622 |         65558
   Dwyane Wade     | 20000000 |          20093064 |         93064
   Brook Lopez     | 19689000 |          20000000 |        311000
   DeAndre Jordan  | 19689000 |          19689000 |             0

