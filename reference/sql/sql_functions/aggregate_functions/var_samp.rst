.. _var_samp:

**************************
VAR_SAMP
**************************

Returns the sample variance of values.

.. note:: Aliases to this function include ``VAR`` and ``VARIANCE`` for compatibility.

See also: :ref:`var_pop`

Syntax
==========

.. code-block:: postgres

   -- As an aggregate
   VAR_SAMP( expr )
   
   VAR( expr )
   
   VARIANCE( expr )
   
   -- As a window function
   VAR_SAMP ( expr ) OVER (   
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
   * - ``expr``
     - Numeric expression

Returns
============

Returns the sample variance with type ``DOUBLE``.

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

Simple variance
----------------------------

.. code-block:: psql

   t=> SELECT "Team", VAR("Age") FROM nba GROUP BY 1 LIMIT 10;
   Team                  | var_samp
   ----------------------+---------
   Atlanta Hawks         |  17.8857
   Boston Celtics        |   8.0667
   Brooklyn Nets         |   9.1143
   Charlotte Hornets     |    9.981
   Chicago Bulls         |  17.5429
   Cleveland Cavaliers   |   16.981
   Dallas Mavericks      |   13.781
   Denver Nuggets        |  22.4952
   Detroit Pistons       |  19.7429
   Golden State Warriors |  14.8095



Combine ``VAR`` with other aggregates
-------------------------------------------

.. code-block:: psql

   t=> SELECT "Age", AVG("Salary"), VAR("Salary"), VARP("Salary") FROM nba GROUP BY 1;
   Age | avg      | var_samp           | var_pop           
   ----+----------+--------------------+-------------------
    19 |  1930440 |        77933520000 |        38966760000
    20 |  2725790 |  2282859395272.472 | 2162708900784.4473
    21 |  2067379 | 1994733541375.9124 | 1889747565514.0222
    22 |  2357963 | 2302436984278.0986 |  2213881715652.018
    23 |  2034746 |  7443577634481.656 |  7252716669494.947
    24 |  3785300 |  23072496009900.81 | 22559773876347.457
    25 |  3930867 |  20779584044953.27 | 20307320771204.332
    26 |  6866566 | 37215743834431.336 |   36181973172363.8
    27 |  6676741 |  46676006374227.07 |  45509106214871.39
    28 |  5110188 |  18633264973532.18 |  18012156141081.11
    29 |  6224177 | 23723775390464.617 |  22845117042669.63
    30 |  7061858 |   29253707311827.5 | 28278583734766.582
    31 |  8511396 |  51411244177164.07 |  49074369441838.43
    32 |  7716958 |  55522406348186.13 |  51251452013710.28
    33 |  3930739 |  18959867656133.08 | 17605591394980.715
    34 |  7606030 | 31956804968680.668 |   28761124471812.6
    35 |  3461739 |  5591759623731.643 | 4892789670765.1875
    36 |  2238119 | 2402689863606.2666 |   2162420877245.64
    37 | 12777778 |    114814811851852 |  76543207901234.67
    38 |  1840041 | 2239993117998.6665 |      1679994838499
    39 |  2517872 |    4930720062924.5 |   2465360031462.25
    40 |  4666916 | 17267521020833.332 | 11511680680555.555
