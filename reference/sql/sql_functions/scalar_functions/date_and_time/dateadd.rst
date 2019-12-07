.. _dateadd:

**************************
DATEADD
**************************

Adds or subtracts an interval to ``DATE`` or ``DATETIME`` value.

.. note:: SQream DB does not support the ``INTERVAL`` ANSI syntax. Use ``DATEADD`` to add or subtract date intervals.

Syntax
==========

.. code-block:: postgres

   DATEADD( interval, number, date_expr )
   
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
   * - ``number``
     - An integer expression
   * - ``date_expr``
     - A ``DATE`` or ``DATETIME`` expression


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

* If ``hour``, ``minute``, ``second``, or ``millisecond`` are added to a ``DATE``, the return type will be ``DATETIME``.

* For all other date parts, the return type is the same as the argument supplied.

Notes
========

* Use negative numbers to subtract from a date

* Use ``DATEADD`` instead of manually figuring out dates. For example, adding a day to February 28th 2020 should result in February 29th 2020. Adding another day should result in March 1st, not February 30th.

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


Add a quarter to each date
-------------------------------------

.. code-block:: psql

   master=> SELECT d as original_date, DATEADD(quarter, 1, d) as next_quarter FROM cool_dates;
   original_date | next_quarter
   --------------+-------------
   1955-11-05    | 1956-02-05  
   1985-10-26    | 1986-01-26  
   0079-08-24    | 0079-11-24  
   1997-01-01    | 1997-04-01  
   1997-12-31    | 1998-03-31  


Getting next month's date
----------------------------

.. code-block:: psql

   master=> SELECT CURRENT_DATE,DATEADD(month, 1, CURRENT_DATE);
   date       | dateadd   
   -----------+-----------
   2019-12-07 | 2020-01-07


Filtering +- 50 years from a specific date
----------------------------------------------

.. code-block:: psql

   master=> SELECT name, dt as datetime FROM cool_dates 
  .>         WHERE dt BETWEEN DATEADD(year,-50,'1955-06-01') AND DATEADD(year,50,'1955-06-01');
   
   name                               | datetime           
   -----------------------------------+--------------------
   Marty McFly goes back to this time | 1955-11-05 01:21:00
   Marty McFly came from this time    | 1985-10-26 01:22:00
   1997 begins                        | 1997-01-01 00:00:00
   1997 ends                          | 1997-12-31 23:59:59


Check if a year is a leap year
-----------------------------------

Returns ``TRUE`` if this is a leap year - because adding a day to February 28th is February 29th on a leap year.
.. code-block:: psql

   -- Should return true for 2020:
   master=> SELECT DATEPART(month, DATEADD(day,1,'2020-02-28')) = 2 AS "2020 is a leap year";
   2020 is a leap year
   -------------------
   true               

   -- Should return false for 2021:
   master=> SELECT DATEPART(month, DATEADD(day,1,'2021-02-28')) = 2 AS "2021 is a leap year";
   2021 is a leap year
   -------------------
   false               

