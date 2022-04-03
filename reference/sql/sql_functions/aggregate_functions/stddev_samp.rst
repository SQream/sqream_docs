.. _stddev_samp:

**************************
STDDEV_SAMP
**************************

Returns the sample standard deviation of values.

.. note:: Aliases to this function include ``STDDEV`` and ``STDEV`` for compatibility.

See also: :ref:`stddev_pop`

Syntax
==========

.. code-block:: postgres

   -- As an aggregate
   STDDEV_SAMP( expr )
   
   STDDEV( expr )
   
   STDEV( expr )
   
   -- As a window function
   STDDEV_SAMP ( expr ) OVER (   
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

Returns the standard deviation with type ``DOUBLE``.

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

Simple standard deviation
----------------------------

.. code-block:: psql

   t=> SELECT AVG("Age"), STDDEV_SAMP("Age") FROM nba;
   avg | stddev_samp
   ----+------------
    26 |       4.404


Combine ``stddev`` with other aggregates
-------------------------------------------

.. code-block:: psql

   t=> SELECT "Age", AVG("Salary"), STDDEV_SAMP("Salary"), STDDEV_POP("Salary") FROM nba GROUP BY 1;
   Age | avg      | stddev_samp  | stddev_pop  
   ----+----------+--------------+-------------
    19 |  1930440 |  279165.7572 |       197400
    20 |  2725790 | 1510913.4308 | 1470615.1437
    21 |  2067379 | 1412350.3607 | 1374680.8959
    22 |  2357963 |  1517378.326 | 1487911.8642
    23 |  2034746 | 2728292.0728 | 2693086.8292
    24 |  3785300 | 4803383.8083 | 4749713.0309
    25 |  3930867 | 4558462.9038 | 4506364.4739
    26 |  6866566 | 6100470.7879 |  6015145.316
    27 |  6676741 |  6831984.073 | 6746043.7454
    28 |  5110188 | 4316626.5733 | 4244073.0603
    29 |  6224177 | 4870705.8411 | 4779656.5821
    30 |  7061858 | 5408669.6434 | 5317761.1581
    31 |  8511396 | 7170163.4693 | 7005310.0889
    32 |  7716958 | 7451335.8768 |  7159011.944
    33 |  3930739 | 4354293.0145 |  4195901.738
    34 |  7606030 | 5653035.0228 | 5362939.9094
    35 |  3461739 |  2364690.175 | 2211965.1152
    36 |  2238119 | 1550061.2451 | 1470517.2142
    37 | 12777778 | 10715167.374 | 8748897.5249
    38 |  1840041 | 1496660.6556 | 1296146.1486
    39 |  2517872 | 2220522.4752 |    1570146.5
    40 |  4666916 | 4155420.6792 | 3392886.7769



