.. _covar_pop:

**************************
COVAR_POP
**************************

Returns the population covariance of value pairs. 

See also: :ref:`covar_samp`

Syntax
==========

.. code-block:: postgres

   -- As an aggregate
   COVAR_POP( expr1, expr2 )

   -- As a window function
   COVAR_POP ( expr1, expr2 ) OVER (   
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

Returns the population covariance with type ``DOUBLE``.

Notes
=======

* When all rows contain ``NULL`` values, the function returns ``NULL``.


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

   t=> SELECT "Team", COVAR_POP("Age","Salary") FROM nba GROUP BY 1 ORDER BY 2 ASC;
   Team                   | covar_pop    
   -----------------------+--------------
   Cleveland Cavaliers    | -9192828.8163
   San Antonio Spurs      | -6938848.9867
   Oklahoma City Thunder  | -3696440.1244
   Detroit Pistons        | -1313564.5067
   Los Angeles Clippers   |  -968077.3778
   New Orleans Pelicans   |  -440360.5374
   Utah Jazz              |   930824.7689
   Philadelphia 76ers     |  1458110.3265
   Sacramento Kings       |    2306106.08
   Dallas Mavericks       |  2418733.4356
   Washington Wizards     |  2427928.8978
   Milwaukee Bucks        |  2616404.8555
   Orlando Magic          |  2812867.8673
   Golden State Warriors  |  3352356.3333
   Portland Trail Blazers |  3941655.4533
   Denver Nuggets         |  3966387.1122
   Minnesota Timberwolves |  4492620.0237
   Toronto Raptors        |  4524417.1244
   Charlotte Hornets      |     5056864.8
   Houston Rockets        |  5309246.2089
   Phoenix Suns           |  5580976.6889
   Indiana Pacers         |  5757986.9067
   Boston Celtics         |  5797738.7245
   Brooklyn Nets          |  6119732.0667
   Chicago Bulls          |    6506357.92
   Atlanta Hawks          |  8859452.0667
   Memphis Grizzlies      |       9524269
   New York Knicks        | 10264800.6875
   Miami Heat             | 13009610.4734
   Los Angeles Lakers     | 15400203.6533


