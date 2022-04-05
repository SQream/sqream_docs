.. _covar_samp:

**************************
COVAR_SAMP
**************************

Returns the sample covariance of value pairs. 

See also: :ref:`covar_pop`

Syntax
==========

.. code-block:: postgres

   -- As an aggregate
   COVAR_SAMP( expr1, expr2 )

   -- As a window function
   COVAR_SAMP ( expr1, expr2 ) OVER (   
            [ PARTITION BY value_expression [, ...] ]
            [ ORDER BY value_expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] ]
            [ frame_clause ]
         )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr1``, ``expr2``
     - Numeric expression

Returns
============

Returns the sample covariance with type ``DOUBLE``.

Notes
=======

* When all rows contain ``NULL`` values, the function returns ``NULL``.

* The function also returns ``NULL`` when only one value is non-``NULL``.

Examples
===========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      "Name" varchar(40),
      "Team" varchar(40),
      "Number" tinyint,
      "Position" varchar(2),
      "Age" tinyint,
      "Height" varchar(4),
      "Weight" real,
      "College" varchar(40),
      "Salary" float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Simple covariance
----------------------------

.. code-block:: psql

   t=> SELECT "Team", COVAR_SAMP("Age","Salary") FROM nba GROUP BY 1 ORDER BY 2 ASC;
   Team                   | covar_samp   
   -----------------------+--------------
   Cleveland Cavaliers    | -9899969.4945
   San Antonio Spurs      | -7434481.0571
   Oklahoma City Thunder  | -3960471.5619
   Detroit Pistons        | -1407390.5429
   Los Angeles Clippers   | -1037225.7619
   New Orleans Pelicans   |  -464825.0117
   Utah Jazz              |   997312.2524
   Philadelphia 76ers     |  1570272.6593
   Sacramento Kings       |  2470827.9429
   Dallas Mavericks       |  2591500.1095
   Washington Wizards     |  2601352.3905
   Milwaukee Bucks        |  2790831.8458
   Orlando Magic          |  3029242.3187
   Golden State Warriors  |  3591810.3571
   Portland Trail Blazers |  4223202.2714
   Denver Nuggets         |  4271493.8132
   Toronto Raptors        |  4847589.7762
   Minnesota Timberwolves |  4867005.0256
   Charlotte Hornets      |  5418069.4286
   Houston Rockets        |   5688478.081
   Phoenix Suns           |   5979617.881
   Indiana Pacers         |  6169271.6857
   Boston Celtics         |  6243718.6264
   Brooklyn Nets          |  6556855.7857
   Chicago Bulls          |  6971097.7714
   Atlanta Hawks          |  9492270.0714
   Memphis Grizzlies      | 10256905.0769
   New York Knicks        | 10949120.7333
   Miami Heat             | 14093744.6795
   Los Angeles Lakers     |    16500218.2

