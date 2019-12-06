.. _select:

**********************
SELECT
**********************

``SELECT`` is the main statement that allows reading and processing of data. It is used to retrieve rows and columns from one or more tables.

When used alone, the statement is known as a "``SELECT`` statement" or "``SELECT`` query", but it can also be combined to create more elaborate statements like :ref:`CREATE TABLE AS<create_table_as>`.

.. note:: The ``SELECT`` keyword is also used to execute utility functions, such as ``SELECT get_ddl();``. These are covered in their respective locations.

.. contents:: In this topic:
   :local:

Permissions
=============

The role must have the ``SELECT`` permission on every table or schema that is referenced by the ``SELECT`` query.

Synopsis
==========

.. code-block:: postgres

   query ::=
      query_term
      [ UNION ALL query_term [ ...] ]
      [ ORDER BY order [, ... ] ]
      [ LIMIT num_rows ]
      ;

   query_term ::=
       [ WITH table_alias AS (query_term)
            [, ...]
       ]
       SELECT
           [ TOP num_rows ]
           [ DISTINCT ]
           select_list
           [ FROM table_ref [, ... ]
               [ WHERE value_expr
               [ GROUP BY value_expr [, ... ]
                  [ HAVING value_expr ]
               ]
       | ( VALUES ( value_expr [, ... ] ) [, ... ] )

   select_list ::=
       value_expr [ [ AS ] column_alias ] [, ... ]
       | window_expr [ [ AS ] column alias ]

   column_alias ::= identifier

   table_alias ::= identifier

   window_expr ::= 
   OVER (   
       [ PARTITION BY value_expr [, ...] ]  
       [ ORDER BY order [, ...]]   
      )
   
   table_ref ::=
       [schema_name.]table_name [ [ AS ] alias [ ( column_alias [, ... ] ) ] ]
       | ( query ) [ [AS] alias [ ( column_alias [, ... ] ) ] ]
       | table_ref join_type  table_ref
           [ ON value_expr | USING ( join_column [, ... ] ) ]
       | table_alias

   schema_name ::= identifier
   
   table_name ::= identifier
   
   alias ::= identifier 

   join_type ::=
       [ INNER ] [ join_hint ] JOIN
       | LEFT [ OUTER ] [ join_hint ] JOIN
       | RIGHT [ OUTER ] [ join_hint ] JOIN
       | CROSS [ join_hint ] JOIN

   join_hint ::=
       MERGE | LOOP

   order ::=
       value_expr [ ASC | DESC ] [, ...]  [NULLS FIRST | LAST ]


Elements
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``DISTINCT``
     - Remove duplicates
   * - ``FROM table_ref``
     - A table name or another sub-clause that creates a table, such as :ref:`VALUES<values>` or a subquery.
   * - ``WHERE value_expr``
     - An expression that returns Boolean values using columns, such as ``<column> = <value>``. Rows that do not match the expression will not show up in the result set.
   * - ``GROUP BY value_expr``
     - Aggregate on specific columns or values. Often used with aggregate functions.
   * - ``HAVING value_expr``
     - Only return values that match the expression. ``HAVING`` is like ``WHERE``, but for results of the aggregate functions.
   * - ``ORDER BY order``
     - A comma separated list of ordering specifications, used to change the order of the results.
   * - ``LIMIT num_rows``
     - Restricts the operation to only retrieve the first ``num_rows`` rows.
   * - ``UNION ALL``
     - Concatenates the results of two queries together. ``UNION ALL`` does not remove duplicates.

Notes
===========

Query processing
-----------------

Queries are processed in a manner equivalent to the following order:

#. ``FROM``, including nested queries in the ``FROM``
#. ``WHERE``
#. ``SELECT`` list row → value functions and these functions inside aggregates and window function calls in select list
#. ``GROUP BY`` and aggregates
#. ``HAVING``
#. Window functions
#. ``SELECT`` list row → value functions on the outside of aggregates and window functions
#. ``DISTINCT``
#. ```UNION ALL``
#. ``ORDER BY``
#. ``LIMIT`` / ``TOP``

Inside the ``FROM`` clause, the processing occurs in the usual way, from the outside in.

.. _select_lists:

Select lists
----------------

The ``select_list`` is a comma separated list of column names and value expressions.

* Use ``LIMIT num_rows`` to retrieve only the first ``num_rows`` results. SQream DB also supports the ``TOP num_rows`` syntax from SQL Server.
* ``DISTINCT`` can be used to remove duplicate rows.
* Value expressions in select lists support aggregate and window functions as well as normal value expressions.

.. tip::
   Each expression in the select list is given an ordinal number, from 1 to the number of expressions. When using ``ORDER BY`` or ``GROUP BY``, these ordinals are used as shorthand to refer to these expressions.
   
   .. code-block:: postgres
   
      SELECT a, SUM(b) FROM t GROUP BY a ORDER BY SUM(b) DESC;
      -- is equivalent to:
      SELECT a, SUM(b) FROM t GROUP BY 1 ORDER BY 2 DESC;

Examples
===========

Assume a table named ``nba``, with the following structure:

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


Here's a peek at the table contents (:download:`Download nba.csv <nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1


Simple queries
------------------

This query will get the Name, Team name, and Age from the NBA table, but only show the first 10 results.

.. code-block:: psql
   
   nba=> SELECT Name, Team, Age FROM nba LIMIT 10;
   Avery Bradley,Boston Celtics,25
   Jae Crowder,Boston Celtics,25
   John Holland,Boston Celtics,27
   R.J. Hunter,Boston Celtics,22
   Jonas Jerebko,Boston Celtics,29
   Amir Johnson,Boston Celtics,29
   Jordan Mickey,Boston Celtics,21
   Kelly Olynyk,Boston Celtics,25
   Terry Rozier,Boston Celtics,22
   Marcus Smart,Boston Celtics,22

Show a count of the rows
---------------------------

Use ``COUNT(*)`` to retrieve the number of rows in a result.

.. code-block:: psql
   
   nba=> SELECT COUNT(*) FROM nba;
   457

Get all columns
-----------------

``*`` is used as shorthand for "all columns".

.. warning:: Running a ``SELECT *`` query on very large tables can occupy the client for a long time, if the result set is big.

.. code-block:: psql
   
   nba=> SELECT * FROM nba;
   Name                     | Team                   | Number | Position | Age | Height | Weight | College               | Salary  
   -------------------------+------------------------+--------+----------+-----+--------+--------+-----------------------+---------
   Avery Bradley            | Boston Celtics         |      0 | PG       |  25 | 6-2    |    180 | Texas                 |  7730337
   Jae Crowder              | Boston Celtics         |     99 | SF       |  25 | 6-6    |    235 | Marquette             |  6796117
   John Holland             | Boston Celtics         |     30 | SG       |  27 | 6-5    |    205 | Boston University     |         
   R.J. Hunter              | Boston Celtics         |     28 | SG       |  22 | 6-5    |    185 | Georgia State         |  1148640
   Jonas Jerebko            | Boston Celtics         |      8 | PF       |  29 | 6-10   |    231 |                       |  5000000
   Amir Johnson             | Boston Celtics         |     90 | PF       |  29 | 6-9    |    240 |                       | 12000000
   Jordan Mickey            | Boston Celtics         |     55 | PF       |  21 | 6-8    |    235 | LSU                   |  1170960
   Kelly Olynyk             | Boston Celtics         |     41 | C        |  25 | 7-0    |    238 | Gonzaga               |  2165160
   Terry Rozier             | Boston Celtics         |     12 | PG       |  22 | 6-2    |    190 | Louisville            |  1824360
   Marcus Smart             | Boston Celtics         |     36 | PG       |  22 | 6-4    |    220 | Oklahoma State        |  3431040

Filter on conditions
-----------------------

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary" FROM nba WHERE "Age" < 24 LIMIT 5;
   R.J. Hunter,22,1148640
   Jordan Mickey,21,1170960
   Terry Rozier,22,1824360
   Marcus Smart,22,3431040
   James Young,20,1749840
   
   nba=> SELECT "Name","Age","Salary" FROM nba WHERE "Age" < 24 AND "Salary" > 1800000 LIMIT 5;
   Terry Rozier,22,1824360
   Marcus Smart,22,3431040
   Kristaps Porzingis,20,4131720
   Joel Embiid,22,4626960
   Nerlens Noel,22,3457800

Filter based on a list
------------------------

``WHERE column IN (value_expr in comma separated list)`` matches the column with any value in the list.

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" IN ('Utah Jazz', 'Portland Trail Blazers');
   Cliff Alexander,20,525093,Portland Trail Blazers
   Al-Farouq Aminu,25,8042895,Portland Trail Blazers
   Pat Connaughton,23,625093,Portland Trail Blazers
   [...]
   Shelvin Mack,26,2433333,Utah Jazz
   Raul Neto,24,900000,Utah Jazz
   Tibor Pleiss,26,2900000,Utah Jazz
   Jeff Withey,26,947276,Utah Jazz


Select only distinct rows
---------------------------

.. code-block:: psql
   
   nba=> SELECT DISTINCT "Team" FROM nba;
   Atlanta Hawks
   Boston Celtics
   Brooklyn Nets
   Charlotte Hornets
   Chicago Bulls
   Cleveland Cavaliers
   Dallas Mavericks
   Denver Nuggets
   Detroit Pistons
   Golden State Warriors
   Houston Rockets
   Indiana Pacers
   Los Angeles Clippers
   Los Angeles Lakers
   Memphis Grizzlies
   Miami Heat
   Milwaukee Bucks
   Minnesota Timberwolves
   New Orleans Pelicans
   New York Knicks
   Oklahoma City Thunder
   Orlando Magic
   Philadelphia 76ers
   Phoenix Suns
   Portland Trail Blazers
   Sacramento Kings
   San Antonio Spurs
   Toronto Raptors
   Utah Jazz
   Washington Wizards

Count distinct values
-----------------------

.. code-block:: psql
   
   nba=> SELECT COUNT(DISTINCT "Team") FROM nba;
   30

Rename columns with aliases
-----------------------------

.. code-block:: psql
   
   nba=> SELECT "Name" AS "Player", -- Note usage of AS
   .>            "Team", 
   .>            "Salary" "Yearly salary" -- AS is optional.
   .>            -- This is identical to "Salary" AS "Yearly salary"
                
                FROM nba LIMIT 5;
   Player        | Team           | Yearly salary
   --------------+----------------+--------------
   Avery Bradley | Boston Celtics |       7730337
   Jae Crowder   | Boston Celtics |       6796117
   John Holland  | Boston Celtics |              
   R.J. Hunter   | Boston Celtics |       1148640
   Jonas Jerebko | Boston Celtics |       5000000

Searching with ``LIKE``
-------------------------

``LIKE`` allows pattern matching text in the ``WHERE`` clause.

* ``%`` matches 0 or more characters
* ``_`` matches exactly 1 character


.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" LIKE 'Portland%' LIMIT 5;
   Cliff Alexander,20,525093,Portland Trail Blazers
   Al-Farouq Aminu,25,8042895,Portland Trail Blazers
   Pat Connaughton,23,625093,Portland Trail Blazers
   Allen Crabbe,24,947276,Portland Trail Blazers
   Ed Davis,27,6980802,Portland Trail Blazers

Aggregate functions
----------------------

Aggregate functions compute a single result from a column. 

.. tip:: Aggregate functions can return ``NULL`` if no rows are selected or all input values are ``NULL``. The notable exception to this rule is ``COUNT``, which always returns an integer. Use :ref:`COALESCE<coalesce>` to substitute zero or another value for ``NULL`` when necessary.


.. code-block:: psql
   
   nba=> SELECT max("Salary") FROM nba;
   25000000

Aggregate functions are often combined with ``GROUP BY``.

.. code-block:: psql
   
   nba=> SELECT "Team",max("Salary") FROM nba GROUP BY "Team";
   Atlanta Hawks,18671659
   Boston Celtics,12000000
   Brooklyn Nets,19689000
   Charlotte Hornets,13500000
   [...]
   Utah Jazz,15409570
   Washington Wizards,15851950

.. note:: 
   Unlike some other databases, when using an aggregate function, all other items in the select list must either be aggregated or be specified in a ``GROUP BY``.
   
   A query like ``SELECT "Team",max("Salary") FROM nba`` is not valid, and will result in an error.

Filtering on aggregates
--------------------------

Filtering on aggregates is done with the ``HAVING`` clause, rather than the ``WHERE`` clause.

.. code-block:: psql
   
   nba=> SELECT "Team",AVG("Salary") FROM nba GROUP BY "Team" HAVING AVG("Salary") BETWEEN 4477884 AND 5018868;
   Atlanta Hawks,4860196
   Dallas Mavericks,4746582
   Detroit Pistons,4477884
   Houston Rockets,5018868
   Los Angeles Lakers,4784695
   Minnesota Timberwolves,4593053
   New York Knicks,4581493
   Sacramento Kings,4778911
   Toronto Raptors,4741174

Sorting results
-------------------

``ORDER BY`` takes a comma separated list of ordering specifications - a column followed by ``ASC`` for ascending or ``DESC`` for descending.

.. note:: 
   When ``ORDER BY`` is not specified in a query, rows are returned based on the order in which they were read, not by any consistent criteria.
   
   Unlike some databases, ``NULL`` values are neither first nor last - but can appear anywhere in the result set.

.. tip:: SQream DB does not support functions and complex arguments in the ``ORDER BY`` clause. To work around this limitation, use ordinals or aliases, as with the examples below, which are functionally identical.

.. code-block:: psql
   
   nba=> SELECT "Team",AVG("Salary") as "Average Salary" FROM nba GROUP BY "Team" ORDER BY "Average Salary" DESC;
   Team                   | Average Salary
   -----------------------+---------------
   Cleveland Cavaliers    |        7642049
   Miami Heat             |        6347359
   Los Angeles Clippers   |        6323642
   Oklahoma City Thunder  |        6251019
   [...]
   Brooklyn Nets          |        3501898
   Portland Trail Blazers |        3220121
   Philadelphia 76ers     |        2213778

.. code-block:: psql
   
   nba=> SELECT "Team",AVG("Salary") as "Average Salary" FROM nba GROUP BY "Team" ORDER BY 2 DESC;
      Team                   | Average Salary
      -----------------------+---------------
      Cleveland Cavaliers    |        7642049
      Miami Heat             |        6347359
      Los Angeles Clippers   |        6323642
      Oklahoma City Thunder  |        6251019
      [...]
      Brooklyn Nets          |        3501898
      Portland Trail Blazers |        3220121
      Philadelphia 76ers     |        2213778

Sorting with multiple columns
-----------------------------------

Order retrieved rows by multiple columns:

.. code-block:: psql
   
   nba=> SELECT "Name", "Position", "Weight", "Salary" FROM nba ORDER BY "Weight" DESC, "Salary" ASC;
   Name                     | Position | Weight | Salary  
   -------------------------+----------+--------+---------
   Nikola Pekovic           | C        |    307 | 12100000
   Boban Marjanovic         | C        |    290 |  1200000
   Al Jefferson             | C        |    289 | 13500000
   [...]
   Tim Frazier              | PG       |    170 |   845059
   Brandon Jennings         | PG       |    169 |  8344497
   Briante Weber            | PG       |    165 |         
   Bryce Cotton             | PG       |    165 |   700902
   Aaron Brooks             | PG       |    161 |  2250000


Combining two or more queries
---------------------------------

``UNION ALL`` can be used to combine the results of two or more queries into one result set.

``UNION ALL`` does not remove duplicate results.

.. code-block:: psql
   
   nba=> SELECT "Position" FROM nba WHERE "Weight" > 300
   .>    UNION ALL SELECT "Position" FROM nba WHERE "Weight" < 170;
   C
   PG
   PG
   PG
   PG

Common table expressions (CTE)
--------------------------------

Common table expressions or CTEs allow a possibly complex subquery to be represented in a short way later on, for improved readability.

It does not affect query performance.

.. code-block:: psql
   
   nba=> WITH s AS (SELECT "Name" FROM nba WHERE "Salary" > 20000000)
   .>       SELECT * FROM nba AS n, s WHERE n."Name" = s."Name";
   Name            | Team                  | Number | Position | Age | Height | Weight | College      | Salary   | name0          
   ----------------+-----------------------+--------+----------+-----+--------+--------+--------------+----------+----------------
   Carmelo Anthony | New York Knicks       |      7 | SF       |  32 | 6-8    |    240 | Syracuse     | 22875000 | Carmelo Anthony
   Chris Bosh      | Miami Heat            |      1 | PF       |  32 | 6-11   |    235 | Georgia Tech | 22192730 | Chris Bosh     
   Chris Paul      | Los Angeles Clippers  |      3 | PG       |  31 | 6-0    |    175 | Wake Forest  | 21468695 | Chris Paul     
   Derrick Rose    | Chicago Bulls         |      1 | PG       |  27 | 6-3    |    190 | Memphis      | 20093064 | Derrick Rose   
   Dwight Howard   | Houston Rockets       |     12 | C        |  30 | 6-11   |    265 |              | 22359364 | Dwight Howard  
   Kevin Durant    | Oklahoma City Thunder |     35 | SF       |  27 | 6-9    |    240 | Texas        | 20158622 | Kevin Durant   
   Kobe Bryant     | Los Angeles Lakers    |     24 | SF       |  37 | 6-6    |    212 |              | 25000000 | Kobe Bryant    
   LeBron James    | Cleveland Cavaliers   |     23 | SF       |  31 | 6-8    |    250 |              | 22970500 | LeBron James   

In this example, the ``WITH`` clause defines the temporary name ``r`` for the subquery which finds salaries over $20 million. The result set becomes a valid table reference in any table expression of the subsequent SELECT clause.

Nested CTEs
^^^^^^^^^^^^^^

SQream DB also supports any amount of nested CTEs, such as this:

.. code-block:: postgres

   WITH w AS
       (SELECT * FROM
           (WITH x AS (SELECT * FROM nba) SELECT * FROM x ORDER BY "Salary" DESC))
     SELECT * FROM w ORDER BY "Weight" DESC;

Reusing CTEs
^^^^^^^^^^^^^^^^

SQream DB supports reusing CTEs several times in a query:

.. code-block:: psql
   
   nba=> WITH
   .>       nba_ct AS (SELECT "Name", "Team" FROM nba WHERE "College"='Connecticut'),
   .>       nba_az AS (SELECT "Name", "Team" FROM nba WHERE "College"='Arizona')
   .>       SELECT * FROM nba_az JOIN nba_ct ON nba_ct."Team" = nba_az."Team";
   Name            | Team            | name0          | team0          
   ----------------+-----------------+----------------+----------------
   Stanley Johnson | Detroit Pistons | Andre Drummond | Detroit Pistons
   Aaron Gordon    | Orlando Magic   | Shabazz Napier | Orlando Magic  

   
