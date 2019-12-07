.. _datepart:

**************************
DATEPART
**************************

Extracts a date or time part from a ``DATE`` or ``DATETIME`` value.

Syntax
==========

.. code-block:: postgres

   DATEPART( interval, date_expr ) --> INT
   
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

* An integer representing the date part value

Notes
========

* All dateparts work on a ``DATETIME``.

* The ``hour``, ``minute``, ``second``, and ``millisecond`` dateparts work only on ``DATETIME``. Using them on ``DATE`` will result in an error.

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


Break up a ``DATE`` into components
-------------------------------------

.. code-block:: psql

   master=> SELECT DATEPART(year, d) AS  year, DATEPART(month, d) AS month, DATEPART(day,d) AS day, 
   .>              DATEPART(q,d) AS quarter FROM cool_dates;
   year | month | day | quarter
   -----+-------+-----+--------
   1955 |    11 |   5 |       4
   1985 |    10 |  26 |       4
     79 |     8 |  24 |       3
   1997 |     1 |   1 |       1
   1997 |    12 |  31 |       4

Break up a ``DATETIME`` into time components
----------------------------------------------

.. code-block:: psql

   master=> SELECT DATEPART(hour, dt) AS hour, DATEPART(minute, dt) AS minute, 
   .>              DATEPART(second,dt) AS seconds, DATEPART(millisecond,dt) AS milliseconds
   .>              FROM cool_dates;
   hour | minute | seconds | milliseconds
   -----+--------+---------+-------------
      1 |     21 |       0 |            0
      1 |     22 |       0 |            0
     13 |      0 |       0 |            0
      0 |      0 |       0 |            0
     23 |     59 |      59 |          999

Count number of rows grouped by quarter
-------------------------------------------

.. tip:: Use ordinal aliases to avoid having to write complex functions in the ``GROUP BY`` clause. See :ref:`Select lists<select_lists>` for more information.

.. code-block:: psql

   master=> SELECT COUNT(*), DATEPART(q, dt) AS quarter FROM cool_dates GROUP BY 2;
   
   count | quarter
   ------+--------
       1 |       1
       1 |       3
       3 |       4

