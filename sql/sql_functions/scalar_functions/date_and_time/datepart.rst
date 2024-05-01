.. _datepart:

**************************
DATEPART
**************************

Extracts a date or time part from a ``DATE`` or ``DATETIME`` value.

.. note:: SQream DB also supports the ANSI :ref:`EXTRACT<extract>` syntax.

Syntax
==========

.. code-block:: postgres

   DATEPART( interval, date_expr ) --> INT
   
   interval ::= 
        YEAR | YYYY | YY
      | QUARTER | QQ | Q
      | MONTH | MM | M
      | DAYOFYEAR | DOY | DY | Y
      | DAY | DD | D
      | WEEK | WK | WW
      | WEEKDAY | DW
      | HOUR | HH
      | MINUTE | MI | N
      | SECOND | SS | S
      | MILLISECOND | MS

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
   * - ``YEAR``
     - ``YYYY``, ``YY``
     - Year (0 - 9999)
   * - ``QUARTER``
     - ``QQ``, ``Q``
     - Quarter (1-4)
   * - ``MONTH``
     - ``MM``, ``M``
     - Month (1-12)
   * - ``DAYOFYEAR``
     - ``DOY``, ``DY``, ``Y``
     - Day of the year (1-365)
   * - ``DAY``
     - ``DD``, ``D``
     - Day of the month (1-31)
   * - ``WEEK``
     - ``WK``, ``WW``
     - Week of the year (1-52)
   * - ``WEEKDAY``
     - ``DW``
     - Weekday / Day of week (1-7)
   * - ``HOUR``
     - ``HH``
     - Hour (0-23)
   * - ``MINUTE``
     - ``MI``, ``N``
     - Minute (0-59)
   * - ``SECOND``
     - ``SS``, ``S``
     - Seconds (0-59)
   * - ``MILLISECOND``
     - ``MS``
     - Milliseconds (0-999)

.. note::
 * The first day of the week is Sunday, when used with ``WEEKDAY``.

Returns
============

* An integer representing the date part value

Notes
========

* All date parts work on a ``DATETIME``.

* The ``HOUR``, ``MINUTE``, ``SECOND``, and ``MILLISECOND`` date parts work only on ``DATETIME``. Using them on ``DATE`` will result in an error.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE cool_dates(name TEXT, d DATE, dt DATETIME);
   
   INSERT INTO cool_dates VALUES ('Marty McFly goes back to this time','1955-11-05','1955-11-05 01:21:00.000')
       , ('Marty McFly came from this time', '1985-10-26', '1985-10-26 01:22:00.000')
       , ('Vesuvius erupts', '79-08-24', '79-08-24 13:00:00.000')
       , ('1997 begins', '1997-01-01', '1997-01-01')
       , ('1997 ends', '1997-12-31','1997-12-31 23:59:59.999');


Break up a ``DATE`` into components
-------------------------------------

.. code-block:: psql

   master=> SELECT DATEPART(YEAR, d) AS  year, DATEPART(MONTH, d) AS month, DATEPART(DAY,d) AS day, 
   .               DATEPART(Q,d) AS quarter FROM cool_dates;
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

   master=> SELECT DATEPART(HOUR, dt) AS hour, DATEPART(MINUTE, dt) AS minute, 
   .               DATEPART(SECOND,dt) AS seconds, DATEPART(MILLISECOND,dt) AS milliseconds
   .               FROM cool_dates;
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

   master=> SELECT COUNT(*), DATEPART(Q, dt) AS quarter FROM cool_dates GROUP BY 2;
   
   count | quarter
   ------+--------
       1 |       1
       1 |       3
       3 |       4

