.. _extract:

**************************
EXTRACT
**************************

Extracts a date or time part from a ``DATE`` or ``DATETIME`` value.

.. note:: SQream DB also supports the SQL Server :ref:`DATEPART<datepart>` Syntax, which contains more date parts for use.

Syntax
==========

.. code-block:: postgres

   EXTRACT( interval FROM date_expr ) --> DOUBLE
   
   interval ::= 
        YEAR
      | MONTH
      | WEEK
      | DOY
      | DAY
      | HOUR
      | MINUTE
      | SECOND
      | MILLISECONDS

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``interval``
     - An interval representing a date part. See the table below or the Syntax reference above for valid date parts
   * - ``date_expr``
     - A ``DATE`` or ``DATETIME`` expression


Valid date parts
-------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Date part
     - Definition
   * - ``YEAR``
     - Year (0.0 - 9999.0)
   * - ``MONTH``
     - Month (1.0-12.0)
   * - ``DOY``
     - Day of the year (1.0-365.0)
   * - ``DAY``
     - Day of the month (1.0-31.0)
   * - ``WEEK``
     - Week of the year (1.0-52.0)
   * - ``HOUR``
     - Hour (0.0-23.0)
   * - ``MINUTE``
     - Minute (0.0-59.0)
   * - ``SECOND``
     - Seconds (0.0-59.0)
   * - ``MILLISECONDS``
     - Milliseconds (0.0-999.0)

Returns
============

* A floating point representing the date part value

Notes
========

* The ``HOUR``, ``MINUTE``, ``SECOND``, and ``MILLISECOND`` date parts work only on ``DATETIME``. Using them on ``DATE`` will result in an error.

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

   master=> SELECT EXTRACT(YEAR FROM d) AS year, EXTRACT(MONTH FROM d) AS month, EXTRACT(DAY FROM d) AS day 
   .>              FROM cool_dates;
   year   | month | day 
   -------+-------+-----
   1955.0 |  11.0 |  5.0
   1985.0 |  10.0 | 26.0
     79.0 |   8.0 | 24.0
   1997.0 |   1.0 |  1.0
   1997.0 |  12.0 | 31.0


