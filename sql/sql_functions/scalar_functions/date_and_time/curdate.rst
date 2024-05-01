.. _curdate:

**************************
CURDATE
**************************

Returns the current date of the system.

.. note:: This function is provided for compatibility with MySQL, IBM DB2 and ODBC. 

Syntax
==========

.. code-block:: postgres

   CURDATE() --> DATE


Arguments
============

None

Returns
============

The current system date, with type ``DATE``.

Notes
========

* This function is equivalent to :ref:`CURRENT_DATE<current_date>`.

* To get the date and time, see :ref:`CURRENT_TIMESTAMP<current_timestamp>`.

Examples
===========

Get the current system date
------------------------------

.. code-block:: psql

   master=> SELECT CURRENT_DATE, CURRENT_DATE(), CURDATE();
   date       | date0      | date1     
   -----------+------------+-----------
   2019-12-07 | 2019-12-07 | 2019-12-07

