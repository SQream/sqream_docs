.. _eomonth:

**************************
EOMONTH
**************************

Returns a ``DATE`` or ``DATETIME`` value, reset to midnight on the last day of the month.

.. note:: This function is provided for SQL Server compatability.

Syntax
==========

.. code-block:: postgres

   EOMONTH( date_expr )
   

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``date_expr``
     - A ``DATE`` or ``DATETIME`` expression


Returns
============

The return type is the same as the argument supplied.

Notes
========

* The time value will be set to midnight on the last day of the month,

* See also :ref:`TRUNC<date_trunc>` to find the first day of the month.

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


Find last day of the month for a ``DATE``
------------------------------------------

.. code-block:: psql

   master=> SELECT name, d AS date, EOMONTH(d) FROM cool_dates;
   name                               | date       | eomonth   
   -----------------------------------+------------+-----------
   Marty McFly goes back to this time | 1955-11-05 | 1955-11-30
   Marty McFly came from this time    | 1985-10-26 | 1985-10-31
   Vesuvius erupts                    | 0079-08-24 | 0079-08-31
   1997 begins                        | 1997-01-01 | 1997-01-31
   1997 ends                          | 1997-12-31 | 1997-12-31



Find the last day of the month for a ``DATETIME``
---------------------------------------------------

.. note:: The time value is reset to midnight, regardless of the original time value.

.. code-block:: psql

   master=> SELECT name, dt AS datetime, EOMONTH(dt) FROM cool_dates;
   name                               | datetime            | eomonth            
   -----------------------------------+---------------------+--------------------
   Marty McFly goes back to this time | 1955-11-05 01:21:00 | 1955-11-30 00:00:00
   Marty McFly came from this time    | 1985-10-26 01:22:00 | 1985-10-31 00:00:00
   Vesuvius erupts                    | 0079-08-24 13:00:00 | 0079-08-31 00:00:00
   1997 begins                        | 1997-01-01 00:00:00 | 1997-01-31 00:00:00
   1997 ends                          | 1997-12-31 23:59:59 | 1997-12-31 00:00:00
