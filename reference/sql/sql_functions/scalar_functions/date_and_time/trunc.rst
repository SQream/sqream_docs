.. _date_trunc:

**************************
TRUNC
**************************

Truncates a ``DATE`` or ``DATETIME`` value to a specified resolution.

For example, truncating a ``DATE`` down to the nearest month returns the date of the first day of the month.

.. note:: This function is overloaded. The function :ref:`TRUNC<trunc>` can also round numbers towards zero.

Syntax
==========

.. code-block:: postgres

   TRUNC( date_expr [ , interval ])
   
   interval ::= 
        YEAR | YYYY | YY
      | QUARTER | QQ | Q
      | MONTH | MM | M
      | DAY | DD | D
      | WEEK | WK | WW
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
   * - ``date_expr``
     - A ``DATE`` or ``DATETIME`` expression
   * - ``interval``
     - An interval representing a date part. See the table below or the Syntax reference above for valid date parts. If not specified, sets the value to to midnight and returns a ``DATETIME``.


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
   * - ``DAY``
     - ``DD``, ``D``
     - Day of the month (1-31)
   * - ``WEEK``
     - ``WK``, ``WW``
     - Week of the year (1-52)
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

Returns
============

If no date part is specified, the return type is ``DATETIME``. Otherwise, the return type is the same as the argument supplied.

Notes
========

* All date parts work on a ``DATETIME``.

* The ``HOUR``, ``MINUTE``, ``SECOND``, and ``MILLISECOND`` date parts work only on ``DATETIME``. Using them on ``DATE`` will result in an error.

* If no date part is specified, the ``DATE`` or ``DATETIME`` value will be set to midnight on the date value. See examples below

* See also :ref:`EOMONTH<eomonth>` to find the last day of the month.

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


Set all ``DATE`` columns to ``DATETIME`` at midnight
---------------------------------------------------------

.. code-block:: psql

   master=> SELECT name, d AS date, trunc(d) FROM cool_dates;
   name                               | date       | trunc              
   -----------------------------------+------------+--------------------
   Marty McFly goes back to this time | 1955-11-05 | 1955-11-05 00:00:00
   Marty McFly came from this time    | 1985-10-26 | 1985-10-26 00:00:00
   Vesuvius erupts                    | 0079-08-24 | 0079-08-24 00:00:00
   1997 begins                        | 1997-01-01 | 1997-01-01 00:00:00
   1997 ends                          | 1997-12-31 | 1997-12-31 00:00:00


Find the first day of the month for dates
----------------------------------------------

.. code-block:: psql

   master=> SELECT name, d AS date, trunc(d, MONTH) FROM cool_dates;
   name                               | date       | trunc     
   -----------------------------------+------------+-----------
   Marty McFly goes back to this time | 1955-11-05 | 1955-11-01
   Marty McFly came from this time    | 1985-10-26 | 1985-10-01
   Vesuvius erupts                    | 0079-08-24 | 0079-08-01
   1997 begins                        | 1997-01-01 | 1997-01-01
   1997 ends                          | 1997-12-31 | 1997-12-01


Calculate number of hours from New Years
-------------------------------------------

Combine ``TRUNC`` with :ref:`DATEDIFF<datediff>` to calculate the number of hours since New Years.

.. code-block:: psql

   master=> SELECT name, dt AS datetime,
   .>              , DATEDIFF(HOUR, trunc(dt, YEAR), dt) AS "Hours since New Years" 
   .>       FROM cool_dates;
   name                               | datetime            | Hours since New Years
   -----------------------------------+---------------------+----------------------
   Marty McFly goes back to this time | 1955-11-05 01:21:00 |                  7393
   Marty McFly came from this time    | 1985-10-26 01:22:00 |                  7153
   Vesuvius erupts                    | 0079-08-24 13:00:00 |                  5653
   1997 begins                        | 1997-01-01 00:00:00 |                     0
   1997 ends                          | 1997-12-31 23:59:59 |                  8759


