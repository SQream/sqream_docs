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
        year | yyyy | yy
      | quarter | qq | q
      | month | mm | m
      | day | dd | d
      | week | wk | ww
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
   * - ``date_expr``
     - A ``DATE`` or ``DATETIME`` expression
   * - ``interval``
     - An interval representing a date part. See the table below or the syntax reference above for valid date parts. If not specified, sets the value to to midnight and returns a ``DATETIME``.


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
   * - ``day``
     - ``dd``, ``d``
     - Day of the month (1-31)
   * - ``week``
     - ``wk``, ``ww``
     - Week of the year (1-52)
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

Returns
============

If no date part is specified, the return type is ``DATETIME``. Otherwise, the return type is the same as the argument supplied.

Notes
========

* All date parts work on a ``DATETIME``.

* The ``hour``, ``minute``, ``second``, and ``millisecond`` date parts work only on ``DATETIME``. Using them on ``DATE`` will result in an error.

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

   master=> SELECT name, d as date, trunc(d) FROM cool_dates;
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

   master=> SELECT name, d as date, trunc(d, month) FROM cool_dates;
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

   master=> SELECT name, dt as datetime,
   .>              , DATEDIFF(hour, trunc(dt, year), dt) as "Hours since New Years" 
   .>       FROM cool_dates;
   name                               | datetime            | Hours since New Years
   -----------------------------------+---------------------+----------------------
   Marty McFly goes back to this time | 1955-11-05 01:21:00 |                  7393
   Marty McFly came from this time    | 1985-10-26 01:22:00 |                  7153
   Vesuvius erupts                    | 0079-08-24 13:00:00 |                  5653
   1997 begins                        | 1997-01-01 00:00:00 |                     0
   1997 ends                          | 1997-12-31 23:59:59 |                  8759


