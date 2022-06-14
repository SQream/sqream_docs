.. _subqueries:

***************************
Subqueries
***************************

Subqueries allows you to reuse of results from another query.

SQream DB supports relational (also called *derived table*) subqueries, which appear as :ref:`select` queries as part of a table expression.

SQream DB also supports :ref:`common_table_expressions`, which are a form of subquery. With CTEs, a subquery can be named for reuse in a query.

.. note::
   * SQream DB does not currently support correlated subqueries or scalar subqueries.
   
   * There is no limit to the number of subqueries or nesting limits in a statement



   
   
Table Subqueries
===========================   

The following is an example of table named ``nba`` with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      "Name" text,
      "Team" text,
      "Number" tinyint,
      "Position" text,
      "Age" tinyint,
      "Height" text,
      "Weight" real,
      "College" text,
      "Salary" float
    );


To see the table contents, click :download:`Download nba.csv </_static/samples/nba.csv>`:

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1
   
Scalar Subqueries
===================
The following are examples of scalar subqueries.

Simple Subquery
------------------

.. code-block:: psql
   
   t=> SELECT AVG("Age") FROM 
   .        (SELECT "Name","Team","Age" FROM nba WHERE "Height" > '7-0');
   avg
   ---
   26

Combining a Subquery with a Join
----------------------------------

.. code-block:: psql

   t=> SELECT * FROM
   .     (SELECT "Name" FROM nba WHERE "Height" > '7-0') AS t(name)
   .     , nba AS n
   .       WHERE n."Name"=t.name;
   name               | Name               | Team                   | Number | Position | Age | Height | Weight | College    | Salary  
   -------------------+--------------------+------------------------+--------+----------+-----+--------+--------+------------+---------
   Alex Len           | Alex Len           | Phoenix Suns           |     21 | C        |  22 | 7-1    |    260 | Maryland   |  3807120
   Alexis Ajinca      | Alexis Ajinca      | New Orleans Pelicans   |     42 | C        |  28 | 7-2    |    248 | \N         |  4389607
   Boban Marjanovic   | Boban Marjanovic   | San Antonio Spurs      |     40 | C        |  27 | 7-3    |    290 | \N         |  1200000
   Kristaps Porzingis | Kristaps Porzingis | New York Knicks        |      6 | PF       |  20 | 7-3    |    240 | \N         |  4131720
   Marc Gasol         | Marc Gasol         | Memphis Grizzlies      |     33 | C        |  31 | 7-1    |    255 | \N         | 19688000
   Meyers Leonard     | Meyers Leonard     | Portland Trail Blazers |     11 | PF       |  24 | 7-1    |    245 | Illinois   |  3075880
   Roy Hibbert        | Roy Hibbert        | Los Angeles Lakers     |     17 | C        |  29 | 7-2    |    270 | Georgetown | 15592217
   Rudy Gobert        | Rudy Gobert        | Utah Jazz              |     27 | C        |  23 | 7-1    |    245 | \N         |  1175880
   Salah Mejri        | Salah Mejri        | Dallas Mavericks       |     50 | C        |  29 | 7-2    |    245 | \N         |   525093
   Spencer Hawes      | Spencer Hawes      | Charlotte Hornets      |      0 | PF       |  28 | 7-1    |    245 | Washington |  6110034
   Tibor Pleiss       | Tibor Pleiss       | Utah Jazz              |     21 | C        |  26 | 7-3    |    256 | \N         |  2900000
   Timofey Mozgov     | Timofey Mozgov     | Cleveland Cavaliers    |     20 | C        |  29 | 7-1    |    275 | \N         |  4950000
   Tyson Chandler     | Tyson Chandler     | Phoenix Suns           |      4 | C        |  33 | 7-1    |    240 | \N         | 13000000
   Walter Tavares     | Walter Tavares     | Atlanta Hawks          |     22 | C        |  24 | 7-3    |    260 | \N         |  1000000

``WITH`` subqueries
---------------------

See :ref:`common_table_expressions` for more information. 

.. code-block:: psql
   
   nba=> WITH
   .        nba_ct AS (SELECT "Name", "Team" FROM nba WHERE "College"='Connecticut'),
   .        nba_az AS (SELECT "Name", "Team" FROM nba WHERE "College"='Arizona')
   .        SELECT * FROM nba_az JOIN nba_ct ON nba_ct."Team" = nba_az."Team";
   Name            | Team            | name0          | team0          
   ----------------+-----------------+----------------+----------------
   Stanley Johnson | Detroit Pistons | Andre Drummond | Detroit Pistons
   Aaron Gordon    | Orlando Magic   | Shabazz Napier | Orlando Magic  