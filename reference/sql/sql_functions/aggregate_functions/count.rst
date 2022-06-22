.. _count:

**************************
COUNT
**************************

The ``COUNT`` function returns the count of numeric values, or only the distinct values.

Syntax
==========
The following is the correct syntax for using the ``COUNT`` function as an **aggregate**:

.. code-block:: postgres

   COUNT( { [ DISTINCT ] expr | * } ) --> BIGINT
   
The following is the correct syntax for using the ``COUNT`` function as a **window function**:

.. code-block:: postgres
   
   COUNT ( { [ DISTINCT ] expr | * } ) OVER (   
            [ PARTITION BY value_expression [, ...] ]
            [ ORDER BY value_expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] ]
            [ frame_clause ]
         )

Arguments
============
The following table describes the ``COUNT`` arguments:

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
* The ``COUNT`` function returns ``BIGINT``.


Notes
=======
The following notes apply to the ``COUNT`` function:

* When all rows contain ``NULL`` values, the function returns ``NULL``.

* ``COUNT(*)`` returns the number of items in a group, including duplicates and ``NULL`` values.

* ``COUNT(ALL expression)`` evaluates expressions for each row in a group, returning the number of non-null values.

* ``COUNT(DISTINCT expression)`` evaluates expressions for each row in a group, returning the number of unique, non-null values.


Examples
===========
The examples in this section are based on a table named ``nba``, structured as follows:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name varchar(40),
      Team varchar(40),
      Number tinyint,
      Position varchar(2),
      Age tinyint,
      Height varchar(4),
      Weight real,
      College varchar(40),
      Salary float
    );

The following table is a preview of the source :download:`nba.csv </_static/samples/nba.csv>` table shown below:

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1
   
This section includes the following examples:

.. contents::
   :local:
   :depth: 1

Counting Rows in a Table
---------------------------
This example shows how to count rows in a table:

.. code-block:: psql

   t=> SELECT COUNT(*) FROM nba;
   count
   -----
   457

Counting Distinct Values in a Table
----------------------------------
This example shows how to count distinct values in a table:

The following structures generate the same result:

.. code-block:: psql

   t=> SELECT COUNT(distinct "Age") FROM nba;
   count
   -----
   22
   
.. code-block:: psql
   
   t=> SELECT COUNT(*) FROM (SELECT "Age" FROM nba GROUP BY 1);
   count
   -----
   22


Combining COUNT with Other Aggregates
-------------------------------------
This example shows how to combine the ``COUNT`` function with other aggregates:

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
