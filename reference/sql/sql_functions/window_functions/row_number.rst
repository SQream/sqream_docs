.. _row_number:

**************************
ROW_NUMBER
**************************

Returns the row number of each row within the partition of a result set.

``ROW_NUMBER`` numbers all rows sequentially. 

See also :ref:`rank`, which provides the same value for identical consecutive rows (e.g. 1, 2, 2, 4, 4, 6).

Syntax
==========

.. code-block:: postgres

   ROW_NUMBER( ) --> BIGINT

Arguments
============

None

Returns
============

The row number, with data type ``BIGINT``.

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
