.. _window_functions:

********************
Window Functions
********************

Window functions are functions applied over a subset (known as a window) of the rows returned by a :ref:`select` query.  


Syntax
========

.. code-block:: postgres

   window_expr ::= 
      window_fn ( [ value_expr [, ...] ] )
         OVER (   
            [ PARTITION BY value_expression [, ...] ]
            [ ORDER BY value_expression [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] ]
            [ frame_clause ]
         )
      
   window_fn ::= 
      | AVG
      | COUNT
      | LAG
      | LEAD
      | MAX
      | MIN
      | RANK
      | ROW_NUMBER
      | SUM
      | FIRST_VALUE
      | LAST_VALUE
      | NTH_VALUE
      | DENSE_RANK
      | PERCENT_RANK
      | CUME_DIST
      | NTILE


   frame_clause ::= 
      { RANGE | ROWS } frame_start [ frame_exclusion ]
      | { RANGE | ROWS } BETWEEN frame_def AND frame_def [ frame_exclusion ]

   frame_def ::= 
      UNBOUNDED PRECEDING
      offset PRECEDING
      CURRENT ROW
      offset FOLLOWING
      UNBOUNDED FOLLOWING

   offset ::=
      EXCLUDE CURRENT ROW
      | EXCLUDE GROUP
      | EXCLUDE TIES
      | EXCLUDE NO OTHERS
      
   row_offset ::= numeric literal

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``window_fn``
     - Window function, like ``AVG``, ``MIN``, etc.
   * - ``PARTITION BY partition_expr``
     - An expression or column reference to partition by
   * - ``ORDER BY order``
     - An expression or column reference to order by


Supported Window Functions
===========================

.. list-table:: Window Aggregation Functions
   :widths: 16 200
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`avg`
     - Returns the average of numeric values.
   * - :ref:`count`
     - Returns the count of numeric values, or only the distinct values.
   * - :ref:`max`
     - Returns the maximum values.
   * - :ref:`min`
     - Returns the minimum values.
   * - :ref:`sum`
     - Returns the sum of numeric values, or only the distinct values.



   
.. list-table:: Ranking Functions
   :widths: 15 200
   :header-rows: 1
   
   * - Function
     - Description
   * - :ref:`lag`
     - Returns a value from a previous row within the partition of a result set.
   * - :ref:`lead`
     - Returns a value from a subsequent row within the partition of a result set.
   * - :ref:`row_number`
     - Returns the row number of each row within the partition of a result set.
   * - :ref:`rank`
     - Returns the rank of each row within the partition of a result set.
   * - :ref:`first_value`
     - Returns the value in the first row of a window.
   * - :ref:`last_value`
     - Returns the value in the last row of a window.	 
   * - :ref:`nth_value`
     - Returns the value in a specified (``n``) row of a window.	 
   * - :ref:`dense_rank`
     - Returns the rank of the current row with no gaps.	 
   * - :ref:`percent_rank`
     - Returns the relative rank of the current row.
   * - :ref:`cume_dist`
     - Returns the cumulative distribution of rows.
   * - :ref:`ntile`
     - Returns an integer ranging between ``1`` and the argument value, dividing the partitions as equally as possible.




How Window Functions Work
============================

A window function operates on a subset ("window") of rows.

Each time a window function is called, it gets the current row for processing, as well as the window of rows that contains the current row.

The window function returns one result row for each input.

The result depends on the individual row and the order of the rows. Some window functions are order-sensitive, such as :ref:`rank`.

.. note::
   In general, a window frame will include all rows of a partition.

   If an ``ORDER BY`` clause is applied, the rows will become ordered which can change the order of the function calls. The function will be applied to the subset between the first row and the current row, instead of the whole frame.

   Boundaries for the frames may need to be applied to get the correct results.

Window frame functions allows a user to perform rolling operations, such as calculate moving averages, longest standing customers, identifying churn, find movers and shakers, etc.

``PARTITION BY``
------------------
The ``PARTITION BY`` clause groups the rows of the query into partitions, which are processed separately by the window function. 

``PARTITION BY`` works similarly to a query-level ``GROUP BY`` clause, but expressions are always just expressions and cannot be output-column names or numbers. 

Without ``PARTITION BY``, all rows produced by the query are treated as a single partition.

``ORDER BY``
----------------------

The ``ORDER BY`` clause determines the order in which the rows of a partition are processed by the window function. It works similarly to a query-level ``ORDER BY`` clause, but cannot use output-column names or numbers.

Without ``ORDER BY``, rows are processed in an unspecified order.

Frames 
-------



.. note:: Frames and frame exclusions have been tested extensively, but are a complex feature. They are released as a preview in v2020.1 pending longer-term testing.

The ``frame_clause`` specifies the set of rows constituting the window frame, which is a subset of the current partition, for those window functions that act on the frame instead of the whole partition.

The set of rows in the frame can vary depending on which row is the current row. The frame can be specified in ``RANGE`` or ``ROWS`` mode; in each case, it runs from the ``frame_start`` to the ``frame_end``. If ``frame_end`` is omitted, the end defaults to ``CURRENT ROW``.

A ``frame_start`` of ``UNBOUNDED PRECEDING`` means that the frame starts with the first row of the partition, and similarly a ``frame_end`` of ``UNBOUNDED FOLLOWING`` means that the frame ends with the last row of the partition.

In ``RANGE`` mode, a frame_start of ``CURRENT ROW`` means the frame starts with the current row's first peer row (a row that the window's ``ORDER BY`` clause sorts as equivalent to the current row), while a ``frame_end`` of ``CURRENT ROW`` means the frame ends with the current row's last peer row. In ``ROWS`` mode, ``CURRENT ROW`` simply means the current row.

In the ``offset PRECEDING`` and ``offset FOLLOWING`` frame options, the offset must be an expression not containing any variables, aggregate functions, or window functions. The meaning of the ``offset`` depends on the frame mode:

* In ``ROWS`` mode, the offset must yield a non-null, non-negative integer, and the option means that the frame starts or ends the specified number of rows before or after the current row.

* In ``RANGE`` mode, these options require that the ``ORDER BY`` clause specify exactly one column. The offset specifies the maximum difference between the value of that column in the current row and its value in preceding or following rows of the frame. This option is restricted to integer types, date and datetime. The offset is required to be a non-null non-negative integer value.

* With a ``DATE`` or ``DATETIME`` column, the offset indicates a number of days.

In any case, the distance to the end of the frame is limited by the distance to the end of the partition, so that for rows near the partition ends the frame might contain fewer rows than elsewhere.

The default framing option is ``RANGE UNBOUNDED PRECEDING``, which is the same as ``RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW``. With ``ORDER BY``, this sets the frame to be all rows from the partition start up through the current row's last ``ORDER BY`` peer. Without ``ORDER BY``, this means all rows of the partition are included in the window frame, since all rows become peers of the current row.

Restrictions
^^^^^^^^^^^^^^^^^^^^^

* ``frame_start`` cannot be ``UNBOUNDED FOLLOWING``
* ``frame_end`` cannot be ``UNBOUNDED PRECEDING``
* ``frame_end`` choice cannot appear earlier in the above list of ``frame_start`` and ``frame_end`` options than the ``frame_start`` choice does.

For example ``RANGE BETWEEN CURRENT ROW AND 7 PRECEDING`` is not allowed. However, while ``ROWS BETWEEN 7 PRECEDING AND 8 PRECEDING`` is allowed, it would never select any rows.

Frame Exclusion
-----------------

The ``frame_exclusion`` option allows rows around the current row to be excluded from the frame, even if they would be included according to the frame start and frame end options. ``EXCLUDE CURRENT ROW`` excludes the current row from the frame. ``EXCLUDE GROUP`` excludes the current row and its ordering peers from the frame. ``EXCLUDE TIES`` excludes any peers of the current row from the frame, but not the current row itself. ``EXCLUDE NO OTHERS`` simply specifies explicitly the default behavior of not excluding the current row or its peers.

Limitations
==================
Window functions do not support the Numeric data type.



Examples
==========

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

Window Function Application
-----------------------------------

.. code-block:: psql

   t=> SELECT SUM("Salary") OVER (PARTITION BY "Team" ORDER BY "Age") FROM nba;
   sum      
   ---------
     1763400
     5540289
     5540289
     5540289
     5540289
     7540289
    18873622
    18873622
    30873622
    60301531
    60301531
    60301531
    64301531
    72902950
    72902950
    [...]

Ranking Results
-----------------

See :ref:`rank`.

.. code-block:: psql

   t=> SELECT n.Name, n.Age, n.Height ,RANK() OVER 
   .       (PARTITION BY n.Age ORDER BY n.Height DESC) AS Rank 
   .        FROM nba_2 n;
   name                     | age | height | rank
   -------------------------+-----+--------+-----
   Devin Booker             |  19 | 6-6    |    1
   Rashad Vaughn            |  19 | 6-6    |    1
   Kristaps Porzingis       |  20 | 7-3    |    1
   Karl-Anthony Towns       |  20 | 7-0    |    2
   Bruno Caboclo            |  20 | 6-9    |    3
   Kevon Looney             |  20 | 6-9    |    3
   Aaron Gordon             |  20 | 6-9    |    3
   Noah Vonleh              |  20 | 6-9    |    3
   Cliff Alexander          |  20 | 6-8    |    7
   Stanley Johnson          |  20 | 6-7    |    8
   Justise Winslow          |  20 | 6-7    |    8
   Kelly Oubre Jr.          |  20 | 6-7    |    8
   James Young              |  20 | 6-6    |   11
   Dante Exum               |  20 | 6-6    |   11
   D'Angelo Russell         |  20 | 6-5    |   13
   Emmanuel Mudiay          |  20 | 6-5    |   13
   Tyus Jones               |  20 | 6-2    |   15
   Jahlil Okafor            |  20 | 6-11   |   16
   Christian Wood           |  20 | 6-11   |   16
   Myles Turner             |  20 | 6-11   |   16
   Trey Lyles               |  20 | 6-10   |   19
   [...]
   

Using ``LEAD`` to Access Following Rows Without a Join
-----------------------------------------------------------


The :ref:`lead` function is used to return data from rows further down the result set. 
The :ref:`lag` function returns data from rows further up the result set.

This example calculates the salary between two players, starting from the highest salary.


.. code-block:: psql
   
   t=> SELECT "Name",
   .          "Salary",
   .          LEAD("Salary", 1) OVER (ORDER BY "Salary" DESC) AS "Salary - next",
   .          ABS(LEAD("Salary", 1) OVER (ORDER BY "Salary" DESC) - "Salary") AS "Salary - diff"
   .          FROM nba
   .          LIMIT 11 ;
   Name            | Salary   | Salary - next | Salary - diff
   ----------------+----------+---------------+--------------
   Kobe Bryant     | 25000000 |      22970500 |       2029500
   LeBron James    | 22970500 |      22875000 |         95500
   Carmelo Anthony | 22875000 |      22359364 |        515636
   Dwight Howard   | 22359364 |      22192730 |        166634
   Chris Bosh      | 22192730 |      21468695 |        724035
   Chris Paul      | 21468695 |      20158622 |       1310073
   Kevin Durant    | 20158622 |      20093064 |         65558
   Derrick Rose    | 20093064 |      20000000 |         93064
   Dwyane Wade     | 20000000 |      19689000 |        311000
   Brook Lopez     | 19689000 |      19689000 |             0
   DeAndre Jordan  | 19689000 |      19689000 |             0


