.. _corr:

**************************
CORR
**************************

Returns the Pearson correlation coefficient of value pairs.

Syntax
==========

.. code-block:: postgres

   CORR( expr1, expr2 )


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

Returns the Perason correlation coefficient with type ``DOUBLE``.

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

Simple correlation
----------------------------

.. code-block:: psql

   t=> SELECT "Team", CORR("Age","Salary") FROM nba GROUP BY 1 ORDER BY 2 ASC;
   Team                   | corr   
   -----------------------+--------
   Cleveland Cavaliers    | -0.3219
   San Antonio Spurs      | -0.2015
   Oklahoma City Thunder  | -0.1236
   Detroit Pistons        | -0.0678
   New Orleans Pelicans   | -0.0459
   Los Angeles Clippers   | -0.0279
   Utah Jazz              |  0.0913
   Washington Wizards     |  0.1217
   Dallas Mavericks       |  0.1388
   Sacramento Kings       |  0.1489
   Milwaukee Bucks        |  0.1626
   Golden State Warriors  |  0.1648
   Minnesota Timberwolves |  0.1909
   Denver Nuggets         |  0.2035
   Houston Rockets        |  0.2051
   Philadelphia 76ers     |  0.2645
   Chicago Bulls          |  0.2663
   Phoenix Suns           |  0.2808
   Orlando Magic          |  0.2878
   Toronto Raptors        |  0.2916
   Memphis Grizzlies      |  0.3225
   Miami Heat             |  0.3635
   Charlotte Hornets      |  0.3779
   Brooklyn Nets          |  0.4084
   Indiana Pacers         |  0.4261
   Atlanta Hawks          |  0.4321
   New York Knicks        |  0.4401
   Los Angeles Lakers     |  0.4563
   Portland Trail Blazers |  0.4856
   Boston Celtics         |  0.6904



