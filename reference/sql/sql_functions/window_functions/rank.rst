.. _rank:

**************************
RANK
**************************

Returns the rank of each row within the partition of a result set.

The rank of a row is defined as ``1 + the number of ranks that come before the row``.

While :ref:`row_number` numbers all rows sequentially, ``RANK`` provides the same value for identical consecutive rows (e.g. 1, 2, 2, 4, 4, 6).

Syntax
==========

.. code-block:: postgres

   RANK( )
      OVER (   
            [ PARTITION BY partition_expr [, ...] ]  
            [ ORDER BY order [ ASC | DESC ] [, ...]]   
         )

Arguments
============

None

Returns
============

The rank of the row, with data type ``BIGINT``.

Notes
=======

* The ``ORDER BY`` clause that is used determines the order in which the rows appear in a result set, and thus the rank.

* Rank is non-deterministic. It may return different results each time it is called with a specific set of input values even if there has been no change in the table contents.


Examples
===========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      "Name" text,
      "Team" text,
      "Number" tinyint,
      "Position" text,
      "Age" tinyint,
      "Height" text,
      "Weight" real,
      "College" text,
      "Salary" float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

``RANK`` vs. :ref:`row_number`
-------------------------------------

.. code-block:: psql

   t=> SELECT ROW_NUMBER () OVER (PARTITION BY "Age" ORDER BY "Height") FROM nba;
   row_number
   ----------
            1
            2
            1
            2
            3
            4
            5
            6
            7
            8
            9
           10
           11
           12
           13
           14
           15
           16
           17
           18
           19
            1
            2
            3
            4
   [...]


   t=> SELECT RANK () OVER (PARTITION BY "Age" ORDER BY "Height") FROM nba;
   rank
   ----
      1
      1
      1
      2
      2
      2
      5
      6
      6
      8
      8
     10
     10
     10
     13
     14
     14
     14
     14
     18
     19
      1
      2
      2
      2
   [...]
