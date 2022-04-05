.. _var_pop:

**************************
VAR_POP
**************************

Returns the population variance of values. 

.. note:: Aliases to this function include ``VARP`` for compatibility.

See also: :ref:`stddev_samp`

Syntax
==========

.. code-block:: postgres

   -- As an aggregate
   VAR_POP( expr )
   
   VARP( expr )

   -- As a window function
   VAR_POP ( expr ) OVER (   
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

Returns the population variance with type ``DOUBLE``.

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

Simple variance
----------------------------

.. code-block:: psql

   t=> SELECT "Team", VAR_POP("Age") FROM nba GROUP BY 1 LIMIT 10;
   Team                  | var_pop
   ----------------------+--------
   Atlanta Hawks         | 16.6933
   Boston Celtics        |  7.5289
   Brooklyn Nets         |  8.5067
   Charlotte Hornets     |  9.3156
   Chicago Bulls         | 16.3733
   Cleveland Cavaliers   | 15.8489
   Dallas Mavericks      | 12.8622
   Denver Nuggets        | 20.9956
   Detroit Pistons       | 18.4267
   Golden State Warriors | 13.8222


Combine ``VARP`` with other aggregates
-------------------------------------------

.. code-block:: psql

   t=> SELECT "Age", AVG("Salary"), VARP("Salary"), STDDEV_POP("Salary") FROM nba GROUP BY 1;
   Age | avg      | var_pop            | stddev_pop  
   ----+----------+--------------------+-------------
    19 |  1930440 |        38966760000 |       197400
    20 |  2725790 | 2162708900784.4473 | 1470615.1437
    21 |  2067379 | 1889747565514.0222 | 1374680.8959
    22 |  2357963 |  2213881715652.018 | 1487911.8642
    23 |  2034746 |  7252716669494.947 | 2693086.8292
    24 |  3785300 | 22559773876347.457 | 4749713.0309
    25 |  3930867 | 20307320771204.332 | 4506364.4739
    26 |  6866566 |   36181973172363.8 |  6015145.316
    27 |  6676741 |  45509106214871.39 | 6746043.7454
    28 |  5110188 |  18012156141081.11 | 4244073.0603
    29 |  6224177 |  22845117042669.63 | 4779656.5821
    30 |  7061858 | 28278583734766.582 | 5317761.1581
    31 |  8511396 |  49074369441838.43 | 7005310.0889
    32 |  7716958 |  51251452013710.28 |  7159011.944
    33 |  3930739 | 17605591394980.715 |  4195901.738
    34 |  7606030 |   28761124471812.6 | 5362939.9094
    35 |  3461739 | 4892789670765.1875 | 2211965.1152
    36 |  2238119 |   2162420877245.64 | 1470517.2142
    37 | 12777778 |  76543207901234.67 | 8748897.5249
    38 |  1840041 |      1679994838499 | 1296146.1486
    39 |  2517872 |   2465360031462.25 |    1570146.5
    40 |  4666916 | 11511680680555.555 | 3392886.7769




