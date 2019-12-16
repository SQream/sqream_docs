.. _window_functions:

********************
Window functions
********************

Window functions are funcitons applied over a subset (known as a window frame) of the rows returned by a :ref:`select` query. 

Syntax
========

.. code-block:: postgres

   window_expr ::= 
      window_fn ( [ value_expr [, ...] ] )
         OVER (   
            [ PARTITION BY partition_expr [, ...] ]  
            [ ORDER BY order [ ASC | DESC ] [, ...]]   
         )
      
   window_fn ::= 
      AVG
      | COUNT
      | MAX
      | MIN
      | STDDEV
      | SUM

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


.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:
   
   row_number
   rank
   
Supported window functions
===========================

* :ref:`avg`
* :ref:`max`
* :ref:`min`
* :ref:`rank`
* :ref:`row_number`
* :ref:`sum`


How window functions work
============================

Things to notice
===================

In general, a window frame will include all rows of a partition.

If an ``ORDER BY`` clause is applied, the rows will become ordered which can change the order of the function calls. The function will be applied to the subset between the first row and the current row, instead of the whole frame.

Boundaries for the frames may need to be applied to get the correct results.

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

Window function application
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

Ranking results
-----------------

See :ref:`rank`.

.. code-block:: psql

   t=> SELECT n.Name, n.Age, n.Height ,RANK() OVER 
   .>      (PARTITION BY n.Age ORDER BY n.Height DESC) AS Rank 
   .>       FROM nba_2 n;
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