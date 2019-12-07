.. _getdate:

**************************
GETDATE
**************************

Returns the current date and time of the system.

.. note:: This function is provided for SQL Server compatability.

Syntax
==========

.. code-block:: postgres

   GETDATE() --> DATETIME

Arguments
============

None

Returns
============

The current system date and time, with type ``DATETIME``.

Notes
========

* Aliases to this function include :ref:`CURRENT_TIMESTAMP<current_timestamp>` and :ref:`SYSDATE<sysdate>`.

* To get the date only, see :ref:`CURRENT_DATE<current_date>`.

Examples
===========

Get the current system date and time
----------------------------------------

.. code-block:: psql

   master=> SELECT CURRENT_TIMESTAMP, CURRENT_TIMESTAMP(), SYSDATE, GETDATE();
   getdate             | getdate0            | getdate1            | getdate2           
   --------------------+---------------------+---------------------+--------------------
   2019-12-07 23:04:26 | 2019-12-07 23:04:26 | 2019-12-07 23:04:26 | 2019-12-07 23:04:26


Find events that happen before this month
--------------------------------------------

We will use :ref:`TRUNC<date_trunc>` to get the date at the beginning of this month, and then filter.

.. code-block:: psql

   master=> SELECT COUNT(*) FROM cool_dates WHERE dt <= TRUNC(GETDATE(), month);
   count
   -----
    5
