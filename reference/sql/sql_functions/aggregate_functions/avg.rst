.. _avg:

**************************
AVG
**************************

Returns the average of numeric values.

Syntax
==========

.. code-block:: postgres

   AVG( expr )

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

Return type is dependant on the argument.

* For ``TINYINT``, ``SMALLINT`` and ``INT``, the return type is ``INT``.

* For ``BIGINT``, the return type is ``BIGINT``.

* For ``REAL``, the return type is ``REAL``

* For ``DOUBLE``, rhe return type is ``DOUBLE``

Notes
=======

* ``NULL`` values are ignored

* ``AVG`` relies on calculating the sum, which can very quickly overflow on large data sets. If the sum is over 2\ :sup:`31` for example, up-cast to a larger type like ``BIGINT``: ``AVG(expr :: BIGINT)``

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

Simple average
----------------

.. code-block:: psql

   t=> SELECT AVG("Age") FROM nba;
   avg
   ---
   26

.. note:: 
   The return type is the same as the input type. To get a fractional result, cast the argument:
   
   .. code-block:: psql

   t=> SELECT AVG("Age" :: REAL) FROM nba;
   avg    
   -------
   26.9387

Combine AVG with other aggregates
-------------------------------------

.. code-block:: psql

   t=> SELECT "Age", AVG("Salary") as "Average salary", COUNT(*) as "Number of players" FROM nba GROUP BY 1;
   Age | Average salary | Number of players
   ----+----------------+------------------
    19 |        1930440 |                 2
    20 |        2725790 |                19
    21 |        2067379 |                19
    22 |        2357963 |                26
    23 |        2034746 |                41
    24 |        3785300 |                47
    25 |        3930867 |                45
    26 |        6866566 |                36
    27 |        6676741 |                41
    28 |        5110188 |                31
    29 |        6224177 |                28
    30 |        7061858 |                31
    31 |        8511396 |                22
    32 |        7716958 |                13
    33 |        3930739 |                14
    34 |        7606030 |                10
    35 |        3461739 |                 9
    36 |        2238119 |                10
    37 |       12777778 |                 4
    38 |        1840041 |                 4
    39 |        2517872 |                 2
    40 |        4666916 |                 3

