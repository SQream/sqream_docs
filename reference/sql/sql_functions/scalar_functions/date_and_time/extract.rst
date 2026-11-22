.. _extract:

**************************
EXTRACT
**************************

Extracts a date or time part from a ``DATE`` , ``DATETIME` or ``DATETIME2`` value.

.. note:: SQream DB also supports the SQL Server :ref:`DATEPART<datepart>` syntax, which contains more date parts for use.

Syntax
==========

.. code-block:: postgres

   EXTRACT( interval FROM date_expr ) --> INT
   
   interval ::= 
        YEAR
      | MONTH
      | WEEK
      | DOY
      | DAY
      | HOUR
      | MINUTE
      | SECOND
      | MILLISECOND | MS
      | MICROSECOND | MU
      | NANOSECOND | NS

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
     - A ``DATE`` , ``DATETIME`` or ``DATETIME2`` expression


Valid date parts
-------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Date part
     - Definition
   * - ``YEAR``
     - Year (0 - 9999)
   * - ``MONTH``
     - Month (1-12)
   * - ``DOY``
     - Day of the year (1-365)
   * - ``DAY``
     - Day of the month (1-31)
   * - ``WEEK``
     - Week of the year (1-52)
   * - ``HOUR``
     - Hour (0-23)
   * - ``MINUTE``
     - Minute (0-59)
   * - ``SECOND``
     - Seconds (0-59)
   * - ``MILLISECOND`` (``MS``)
     - Milliseconds (0-999)
   * - ``MICROSECOND``
     - ``MU``
     - Microseconds (0-999)
   * - ``NANOSECOND``
     - ``NS``
     - Nanoseconds (0-999)

Returns
============

* An integer representing the date part value

Notes
========

* The ``HOUR``, ``MINUTE``, ``SECOND``, and ``MILLISECOND`` date parts work on ``DATETIME`` or ``DATETIME2``. Using them on ``DATE`` will result in an error.
* The ``MICROSECOND`` and ``NANOSECOND`` date parts work only on ``DATETIME2``. Using them on ``DATE`` or ``DATETIME`` will result in an error.


Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE cool_dates(name TEXT(40), d DATE, dt DATETIME);
   
   INSERT INTO cool_dates VALUES ('Marty McFly goes back to this time','1955-11-05','1955-11-05 01:21:00.000')
       , ('Marty McFly came from this time', '1985-10-26', '1985-10-26 01:22:00.000')
       , ('Vesuvius erupts', '79-08-24', '79-08-24 13:00:00.000')
       , ('1997 begins', '1997-01-01', '1997-01-01')
       , ('1997 ends', '1997-12-31','1997-12-31 23:59:59.999');


Break up a ``DATE`` into components
-------------------------------------

.. code-block:: psql

   master=> SELECT EXTRACT(YEAR FROM d) AS year, EXTRACT(MONTH FROM d) AS month, EXTRACT(DAY FROM d) AS day 
   .               FROM cool_dates;
   year | month | day
   -----+-------+-----
   1955 |    11 |   5
   1985 |    10 |  26
     79 |     8 |  24
   1997 |     1 |   1
   1997 |    12 |  31


