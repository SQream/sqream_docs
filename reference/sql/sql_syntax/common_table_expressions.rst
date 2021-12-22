.. _common_table_expressions:

*********************************
Common Table Expressions
*********************************
**Common Table Expressions**, or **CTEs**, allow a complex subquery to be represented in a short way later on for improved readability, and reuse multiple times in a query.

Note that CTEs do not affect query performance.

Overview
---------
The **Common Table Expressions** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Syntax
==========
The following is the correct syntax when using CTEs:

.. code-block:: postgres

   cte ::=
       [ WITH table_alias AS (query)
            [, ...]
       ]


   query ::=
      query_term
      [ UNION ALL query_term [ ...] ]
      [ ORDER BY order [, ... ] ]
      [ LIMIT num_rows ]
      ;

   query_term ::= 
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

Examples
==========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1

Using a Simple CTE
--------------
The following is an example of using a simple CTE:

.. code-block:: psql
   
   nba=> WITH s AS (SELECT "Name" FROM nba WHERE "Salary" > 20000000)
   .        SELECT * FROM nba AS n, s WHERE n."Name" = s."Name";
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

Using Nested CTEs
---------------
The following is an example of using a simple CTE:

.. code-block:: postgres

   WITH w AS
       (SELECT * FROM
           (WITH x AS (SELECT * FROM nba) SELECT * FROM x ORDER BY "Salary" DESC))
     SELECT * FROM w ORDER BY "Weight" DESC;
	 
Note that SQream supports any amount of nested CTEs.

Reusing CTEs
----------------
The following is an example of reusing CTEs, separated by commas:

.. code-block:: psql
   
   nba=> WITH
   .        nba_ct AS (SELECT "Name", "Team" FROM nba WHERE "College"='Connecticut'),
   .        nba_az AS (SELECT "Name", "Team" FROM nba WHERE "College"='Arizona')
   .        SELECT * FROM nba_az JOIN nba_ct ON nba_ct."Team" = nba_az."Team";
   Name            | Team            | name0          | team0          
   ----------------+-----------------+----------------+----------------
   Stanley Johnson | Detroit Pistons | Andre Drummond | Detroit Pistons
   Aaron Gordon    | Orlando Magic   | Shabazz Napier | Orlando Magic  
   
SQream supports reusing CTEs multiple times per query.  

Using CTEs with the CREATE TABLE AS Statement
----------------------------------------
The following is an example of using CTEs with the ``CREATE TABLE AS`` statement:

When used with ``CREATE_TABLE_AS`` statement, the ``CREATE TABLE`` statement should appear before the ``WITH`` argument:

.. code-block:: postgres

   CREATE TABLE weights AS
   
   WITH w AS
       (SELECT * FROM
           (WITH x AS (SELECT * FROM nba) SELECT * FROM x ORDER BY "Salary" DESC))
     SELECT * FROM w ORDER BY "Weight" DESC;
	 
For more information about the ``CREATE_TABLE_AS`` statement, see :ref:`create_table_as`.