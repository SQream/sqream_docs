.. _current_timestamp2:

**************************
CURRENT_TIMESTAMP2
**************************

Returns the current date and time of the system.

.. note:: This function has a special ANSI SQL form and can be called without parentheses.

Syntax
==========

.. code-block:: postgres

   CURRENT_TIMESTAMP2() --> DATETIME2
   
   CURRENT_TIMESTAMP2 --> DATETIME2

Arguments
============

None

Returns
============

The current system date and time, with type ``DATETIME2``.

Notes
========

* This function has a special ANSI SQL form and can be called without parentheses.

* Aliases to this function include :ref:`SYSDATE2<sysdate2>` and :ref:`GETDATE2<getdate2>`.

* To get the date only, see :ref:`CURRENT_DATE<current_date>`.

Examples
===========

Get the current system date and time
----------------------------------------

.. code-block:: psql

   master=> SELECT CURRENT_TIMESTAMP2, CURRENT_TIMESTAMP2(), SYSDATE2, GETDATE2();
   getdate0                             | getdate1                             | getdate2                             | getdate3                            
   -------------------------------------+--------------------------------------+--------------------------------------+-------------------------------------
   2019-12-07 23:04:26.300032671 +02:00 | 2019-12-07 23:04:26.300032671 +02:00 | 2019-12-07 23:04:26.300032671 +02:00 | 2019-12-07 23:04:26.300032671 +02:00


Find events that happen before this month
--------------------------------------------

We will use :ref:`TRUNC<date_trunc>` to get the date at the beginning of this month, and then filter.

.. code-block:: psql

   master=> SELECT COUNT(*) FROM cool_dates WHERE dt <= TRUNC(CURRENT_TIMESTAMP2, month);
   count
   -----
    5
