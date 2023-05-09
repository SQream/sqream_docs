.. _current_date:

**************************
CURRENT_DATE
**************************

Returns the current date of the system.

.. note:: This function has a special ANSI SQL form and can be called without parentheses.

Syntax
==========

.. code-block:: postgres

   CURRENT_DATE() --> DATE
   
   CURRENT_DATE --> DATE

Arguments
============

None

Returns
============

The current system date, with type ``DATE``.

Notes
========

* This function has a special ANSI SQL form and can be called without parentheses.

* This function is equivalent to :ref:`CURDATE<curdate>`.

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

