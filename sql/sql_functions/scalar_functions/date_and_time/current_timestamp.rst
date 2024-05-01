.. _current_timestamp:

**************************
CURRENT_TIMESTAMP
**************************

Returns the current date and time of the system.

.. note:: This function has a special ANSI SQL form and can be called without parentheses.

Syntax
==========

.. code-block:: postgres

   CURRENT_TIMESTAMP() --> DATETIME
   
   CURRENT_TIMESTAMP --> DATETIME

Arguments
============

None

Returns
============

The current system date and time, with type ``DATETIME``.

Notes
========

* This function has a special ANSI SQL form and can be called without parentheses.

* Aliases to this function include :ref:`SYSDATE<sysdate>` and :ref:`GETDATE<getdate>`.

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

   master=> SELECT COUNT(*) FROM cool_dates WHERE dt <= TRUNC(CURRENT_TIMESTAMP, month);
   count
   -----
    5
