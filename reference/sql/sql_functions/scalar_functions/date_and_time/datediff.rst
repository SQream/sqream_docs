.. _datediff:

**************************
DATEDIFF
**************************

Calculates the difference between to ``DATE`` or ``DATETIME`` expressions, in terms of a specific date part.

.. note:: Results are given in integers, rather than ``INTERVAL``, which SQream DB does not support.

Syntax
==========

.. code-block:: postgres

   DATEDIFF( interval, date_expr1, date_expr2 ) --> INT
   
   interval ::= 
        year | yyyy | yy
      | quarter | qq | q
      | month | mm | m
      | dayofyear | doy | dy | y
      | day | dd | d
      | week | wk | ww
      | weekday | dw
      | hour | hh
      | minute | mi | n
      | second | ss | s
      | millisecond | ms

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``interval``
     - An interval representing a date part. See the table below or the syntax reference above for valid date parts
   * - ``date_expr1``, ``date_expr2``
     - A ``DATE`` or ``DATETIME`` expression. The function calculates ``date_expr1 - date_expr2``.


Valid date parts
-------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Date part
     - Shorthand
     - Definition
   * - ``year``
     - ``yyyy``, ``yy``
     - Year (0 - 9999)
   * - ``quarter``
     - ``qq``, ``q``
     - Quarter (1-4)
   * - ``month``
     - ``mm``, ``m``
     - Month (1-12)
   * - ``dayofyear``
     - ``doy``, ``dy``, ``y``
     - Day of the year (1-365)
   * - ``day``
     - ``dd``, ``d``
     - Day of the month (1-31)
   * - ``week``
     - ``wk``, ``ww``
     - Week of the year (1-52)
   * - ``weekday``
     - ``dw``
     - Weekday / Day of week (1-7)
   * - ``hour``
     - ``hh``
     - Hour (0-23)
   * - ``minute``
     - ``mi``, ``n``
     - Minute (0-59)
   * - ``second``
     - ``ss``, ``s``
     - Seconds (0-59)
   * - ``millisecond``
     - ``ms``
     - Milliseconds (0-999)

.. note::
 * The first day of the week is Sunday, when used with ``weekday``.

Returns
============

An integer representing the number of date part units (e.g. years, days, months, hours, etc.) between ``date_expr1`` and ``date_expr2``.

Notes
========

* Only the selected date part is used to calculate the difference. For example, the difference between ``'1997-12-31'`` and ``'1997-01-01'`` in years is 0, even though they are 364 days apart.

* Negative values means that ``date_expr1`` is after ``date_expr2``.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE cool_dates(name VARCHAR(40), d DATE, dt DATETIME);
   
   INSERT INTO cool_dates VALUES ('Marty McFly goes back to this time','1955-11-05','1955-11-05 01:21:00.000')
       , ('Marty McFly came from this time', '1985-10-26', '1985-10-26 01:22:00.000')
       , ('Vesuvius erupts', '79-08-24', '79-08-24 13:00:00.000')
       , ('1997 begins', '1997-01-01', '1997-01-01')
       , ('1997 ends', '1997-12-31','1997-12-31 23:59:59.999');


Find out how far past events are
-------------------------------------

In years
^^^^^^^^^^^^^

.. code-block:: psql

   master=> SELECT d AS original_date, DATEDIFF(year, CURRENT_DATE, d) AS "was ... years ago" FROM cool_dates;
   original_date | was ... years ago
   --------------+------------------
   1955-11-05    |               -64
   1985-10-26    |               -34
   0079-08-24    |             -1940
   1997-01-01    |               -22
   1997-12-31    |               -22

In days
^^^^^^^^^^^^^

.. code-block:: psql

   master=> SELECT d AS original_date, DATEDIFF(day, CURRENT_DATE, d) AS "was ... days ago" FROM cool_dates;
   original_date | was ... days ago
   --------------+-----------------
   1955-11-05    |           -23408
   1985-10-26    |           -12460
   0079-08-24    |          -708675
   1997-01-01    |            -8375
   1997-12-31    |            -8011

In hours
^^^^^^^^^^^

.. note:: 
   * We use the :ref:`CURRENT_TIMESTAMP<current_timestamp>` instead of :ref:`CURRENT_DATE<current_date>`, to include the current time as well as date.
   
   * In this example, we will use ``dt`` which is a ``DATETIME`` column

.. code-block:: psql

   master=> SELECT CURRENT_TIMESTAMP as "Now", dt AS "Original datetime", DATEDIFF(hour, CURRENT_TIMESTAMP, dt) AS "was ... hours ago" FROM cool_dates;
   Now                 | Original datetime   | was ... hours ago
   --------------------+---------------------+------------------
   2019-12-07 22:35:50 | 1955-11-05 01:21:00 |           -561813
   2019-12-07 22:35:50 | 1985-10-26 01:22:00 |           -299061
   2019-12-07 22:35:50 | 0079-08-24 13:00:00 |         -17008209
   2019-12-07 22:35:50 | 1997-01-01 00:00:00 |           -201022
   2019-12-07 22:35:50 | 1997-12-31 23:59:59 |           -192263
