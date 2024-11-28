:orphan:

.. _common_table_expressions:

************************
Common Table Expressions
************************

A Common Table Expression (CTE) is a temporary named result set that can be referenced within a statement, allowing for more readable and modular queries. CTEs do not affect query performance.

Syntax
======

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
========

Create the following ``nba`` table:

.. code-block:: psql

	CREATE OR REPLACE TABLE nba (
		Name TEXT,
		Team TEXT,
		Number INTEGER,
		Position TEXT,
		Age INTEGER,
		Height TEXT,
		Weight INTEGER,
		College TEXT,
		Salary INTEGER,
		name0 TEXT
	);
	
	INSERT INTO nba (Name, Team, Number, Position, Age, Height, Weight, College, Salary, name0)
	VALUES
		('Carmelo Anthony', 'New York Knicks', 7, 'SF', 32, '6-8', 240, 'Syracuse', 22875000, 'Carmelo Anthony'),
		('Chris Bosh', 'Miami Heat', 1, 'PF', 32, '6-11', 235, 'Georgia Tech', 22192730, 'Chris Bosh'),
		('Chris Paul', 'Los Angeles Clippers', 3, 'PG', 31, '6-0', 175, 'Wake Forest', 21468695, 'Chris Paul'),
		('Derrick Rose', 'Chicago Bulls', 1, 'PG', 27, '6-3', 190, 'Memphis', 20093064, 'Derrick Rose'),
		('Dwight Howard', 'Houston Rockets', 12, 'C', 30, '6-11', 265, NULL, 22359364, 'Dwight Howard'),
		('Kevin Durant', 'Oklahoma City Thunder', 35, 'SF', 27, '6-9', 240, 'Texas', 20158622, 'Kevin Durant'),
		('Kobe Bryant', 'Los Angeles Lakers', 24, 'SF', 37, '6-6', 212, NULL, 25000000, 'Kobe Bryant'),
		('LeBron James', 'Cleveland Cavaliers', 23, 'SF', 31, '6-8', 250, NULL, 22970500, 'LeBron James')
		('Stanley Johnson', 'Detroit Pistons', 3, 'SF', 26, '6-7', 245, 'Connecticut', 3120360, 'Stanley Johnson'),
		('Andre Drummond', 'Detroit Pistons', 0, 'C', 28, '6-10', 279, 'Connecticut', 27093019, 'Andre Drummond'),
		('Aaron Gordon', 'Orlando Magic', 0, 'PF', 26, '6-8', 235, 'Arizona', 18136364, 'Aaron Gordon'),
		('Shabazz Napier', 'Orlando Magic', 13, 'PG', 31, '6-1', 175, 'Connecticut', 1378242, 'Shabazz Napier');

Simple CTE
----------

.. code-block:: psql
   
   WITH s AS (SELECT Name FROM nba WHERE Salary > 20000000)
      SELECT * FROM nba AS n, s WHERE n.Name = s.Name;
	name           |team                 |number|position|age|height|weight|college     |salary  |name0          |name1          |
	---------------+---------------------+------+--------+---+------+------+------------+--------+---------------+---------------+
	Kobe Bryant    |Los Angeles Lakers   |    24|SF      | 37|6-6   |   212|            |25000000|Kobe Bryant    |Kobe Bryant    |
	LeBron James   |Cleveland Cavaliers  |    23|SF      | 31|6-8   |   250|            |22970500|LeBron James   |LeBron James   |
	Dwight Howard  |Houston Rockets      |    12|C       | 30|6-11  |   265|            |22359364|Dwight Howard  |Dwight Howard  |
	Carmelo Anthony|New York Knicks      |     7|SF      | 32|6-8   |   240|Syracuse    |22875000|Carmelo Anthony|Carmelo Anthony|
	Chris Bosh     |Miami Heat           |     1|PF      | 32|6-11  |   235|Georgia Tech|22192730|Chris Bosh     |Chris Bosh     |
	Chris Paul     |Los Angeles Clippers |     3|PG      | 31|6-0   |   175|Wake Forest |21468695|Chris Paul     |Chris Paul     |
	Kevin Durant   |Oklahoma City Thunder|    35|SF      | 27|6-9   |   240|Texas       |20158622|Kevin Durant   |Kevin Durant   |
	Derrick Rose   |Chicago Bulls        |     1|PG      | 27|6-3   |   190|Memphis     |20093064|Derrick Rose   |Derrick Rose   |

In this example, the ``WITH`` clause defines the temporary name ``s`` for the subquery which finds salaries over $20 million. The result set becomes a valid table reference in any table expression of the subsequent ``SELECT`` clause.

Nested CTEs
-----------

SQreamDB also supports any amount of nested CTEs, such as this:

.. code-block:: postgres

   WITH w AS
       (SELECT * FROM
           (WITH x AS (SELECT * FROM nba) SELECT * FROM x ORDER BY Salary DESC))
     SELECT * FROM w ORDER BY Weight DESC;
	name           |team                 |number|position|age|height|weight|college     |salary  |name0          |
	---------------+---------------------+------+--------+---+------+------+------------+--------+---------------+
	Dwight Howard  |Houston Rockets      |    12|C       | 30|6-11  |   265|            |22359364|Dwight Howard  |
	LeBron James   |Cleveland Cavaliers  |    23|SF      | 31|6-8   |   250|            |22970500|LeBron James   |
	Carmelo Anthony|New York Knicks      |     7|SF      | 32|6-8   |   240|Syracuse    |22875000|Carmelo Anthony|
	Kevin Durant   |Oklahoma City Thunder|    35|SF      | 27|6-9   |   240|Texas       |20158622|Kevin Durant   |
	Chris Bosh     |Miami Heat           |     1|PF      | 32|6-11  |   235|Georgia Tech|22192730|Chris Bosh     |
	Kobe Bryant    |Los Angeles Lakers   |    24|SF      | 37|6-6   |   212|            |25000000|Kobe Bryant    |
	Derrick Rose   |Chicago Bulls        |     1|PG      | 27|6-3   |   190|Memphis     |20093064|Derrick Rose   |
	Chris Paul     |Los Angeles Clippers |     3|PG      | 31|6-0   |   175|Wake Forest |21468695|Chris Paul     |

Reusing CTEs
------------

SQreamDB supports reusing CTEs several times in a query.

CTEs are separated with commas.

.. code-block:: psql
   
   WITH
       nba_ct AS (SELECT "Name", "Team" FROM nba WHERE "College"='Connecticut'),
       nba_az AS (SELECT "Name", "Team" FROM nba WHERE "College"='Arizona')
       SELECT * FROM nba_az JOIN nba_ct ON nba_ct."Team" = nba_az."Team";
	name        |team         |name0         |team0        |
	------------+-------------+--------------+-------------+
	Aaron Gordon|Orlando Magic|Shabazz Napier|Orlando Magic|
   
   

Using CTEs with ``CREATE TABLE AS``
-----------------------------------

When used with :ref:`create_table_as`, the ``CREATE TABLE`` statement should appear before ``WITH``.

.. code-block:: postgres

   CREATE TABLE weights AS
   
   WITH w AS
     (SELECT * FROM
     (WITH x AS (SELECT * FROM nba) SELECT * FROM x ORDER BY Salary DESC))
     SELECT * FROM w ORDER BY Weight DESC;
	 
	 SELECT * FROM weights;
	 
		 name           |team                 |number|position|age|height|weight|college     |salary  |name0     |
	---------------+---------------------+------+--------+---+------+------+------------+--------+---------------+
	Andre Drummond |Detroit Pistons      |     0|C       | 28|6-10  |   279|Connecticut |27093019|Andre Drummond |
	Dwight Howard  |Houston Rockets      |    12|C       | 30|6-11  |   265|            |22359364|Dwight Howard  |
	LeBron James   |Cleveland Cavaliers  |    23|SF      | 31|6-8   |   250|            |22970500|LeBron James   |
	Stanley Johnson|Detroit Pistons      |     3|SF      | 26|6-7   |   245|Connecticut | 3120360|Stanley Johnson|
	Carmelo Anthony|New York Knicks      |     7|SF      | 32|6-8   |   240|Syracuse    |22875000|Carmelo Anthony|
	Kevin Durant   |Oklahoma City Thunder|    35|SF      | 27|6-9   |   240|Texas       |20158622|Kevin Durant   |
	Chris Bosh     |Miami Heat           |     1|PF      | 32|6-11  |   235|Georgia Tech|22192730|Chris Bosh     |
	Aaron Gordon   |Orlando Magic        |     0|PF      | 26|6-8   |   235|Arizona     |18136364|Aaron Gordon   |
	Kobe Bryant    |Los Angeles Lakers   |    24|SF      | 37|6-6   |   212|            |25000000|Kobe Bryant    |
	Derrick Rose   |Chicago Bulls        |     1|PG      | 27|6-3   |   190|Memphis     |20093064|Derrick Rose   |
	Chris Paul     |Los Angeles Clippers |     3|PG      | 31|6-0   |   175|Wake Forest |21468695|Chris Paul     |
	Shabazz Napier |Orlando Magic        |    13|PG      | 31|6-1   |   175|Connecticut | 1378242|Shabazz Napier |
	 
Using CTEs with ``INSERT``
--------------------------

The :ref:`insert` statement should appear before ``WITH``.  

.. code-block:: postgres

	CREATE OR REPLACE TABLE nba_archive (
    Name TEXT,
    Team TEXT,
    Number INTEGER,
    Position TEXT,
    Age INTEGER,
    Height TEXT,
    Weight INTEGER,
    College TEXT,
    Salary INTEGER,
    name0 TEXT
	);
	
	INSERT INTO nba_archive
	WITH nba_info AS(
		SELECT * 
		FROM nba
	)
	SELECT * 
	FROM nba_info;
	
	SELECT * FROM nba_archive ;
	
	