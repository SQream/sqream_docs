.. _min:

**************************
MIN
**************************

Returns the minimum values

Syntax
==========


.. code-block:: postgres

   -- As an aggregate
   MIN( expr )
   
   -- As a window function
   MIN ( expr ) OVER (   
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
     - Value expression

Returns
============

Return type is dependant on the argument.

Notes
=======

* ``NULL`` values are ignored

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

Simple Minimum, Maximum on numeric columns
--------------------------------------------

.. code-block:: psql

   t=> SELECT MIN("Age"), MAX("Age") FROM nba;
   min | max
   ----+----
    19 |  40

Minimum and maximum on text columns
----------------------------------------

.. code-block:: psql

   t=> SELECT MIN("Name"), MAX("Name") FROM nba;
   min          | max          
   -------------+--------------
   Aaron Brooks | Zaza Pachulia


Combine MIN with GROUP BY
------------------------------

.. code-block:: psql

   t=> SELECT "Team", MIN("Salary") FROM nba GROUP BY 1 ORDER BY 2 DESC LIMIT 5;
   Team                   | min    
   -----------------------+--------
   Boston Celtics         | 1148640
   Minnesota Timberwolves |  947276
   Utah Jazz              |  900000
   Orlando Magic          |  845059
   Memphis Grizzlies      |  700902


