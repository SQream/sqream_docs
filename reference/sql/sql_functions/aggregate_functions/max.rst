.. _max:

**************************
MAX
**************************

Returns the maximum values

Syntax
==========


.. code-block:: postgres

   -- As an aggregate
   
   MAX( expr )
   
   -- As a window function
   
   MAX ( expr ) OVER (   
            [ PARTITION BY partition_expr [, ...] ]  
            [ ORDER BY order [ ASC | DESC ] [, ...]]   
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


Combine MAX with GROUP BY
------------------------------

.. code-block:: psql

   t=> SELECT "Team", MAX("Salary") FROM nba GROUP BY 1 ORDER BY 2 DESC LIMIT 5;
   Team                | max     
   --------------------+---------
   Los Angeles Lakers  | 25000000
   Cleveland Cavaliers | 22970500
   New York Knicks     | 22875000
   Houston Rockets     | 22359364
   Miami Heat          | 22192730

