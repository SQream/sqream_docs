.. _count:

**************************
COUNT
**************************

Returns the count of numeric values, or only the distinct values.

Syntax
==========


.. code-block:: postgres

   COUNT( { [ DISTINCT ] expr | * } ) --> INT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Any value expression
   * - ``*``
     - Specifies that ``COUNT`` should count all rows. It does not use information about any particular column, and preserves duplicate rows and ``NULL`` values.
   * - ``DISTINCT``
     - Specifies that the operation should operate only on unique values

Returns
============

Return type is dependant on the argument.

* Count returns ``INT`` for all types except ``BIGINT``.

* For ``BIGINT``, the return type is ``BIGINT``.

Notes
=======

* ``NULL`` values are *not* ignored by ``COUNT``

* When all rows contain ``NULL`` values, the function returns ``NULL``.


* ``COUNT`` can very quickly overflow on large data sets. If the count is over 2\ :sup:`31`, up-cast to a larger type like ``BIGINT``: ``COUNT(expr :: BIGINT)``

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

Count rows in a table
---------------------------

.. code-block:: psql

   t=> SELECT COUNT(*) FROM nba;
   count
   -----
   457

Count distinct values in a table
----------------------------------

These two forms are equivalent:

.. code-block:: psql

   t=> SELECT COUNT(distinct "Age") FROM nba;
   count
   -----
   22
   
   t=> SELECT COUNT(*) FROM (SELECT "Age" FROM nba GROUP BY 1);
   count
   -----
   22


Combine COUNT with other aggregates
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

