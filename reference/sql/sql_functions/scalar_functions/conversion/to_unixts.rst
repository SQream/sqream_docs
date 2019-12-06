.. _to_unixts:

**************************
TO_UNIXTS, TO_UNIXTSMS
**************************

Converts a ``DATETIME`` value to a ``BIGINT`` representing a UNIX timestamp.

Syntax
==========

.. code-block:: postgres

   TO_UNIXTS( expr ) --> BIGINT
   
   TO_UNIXTSMS( expr ) --> BIGINT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - A ``DATE`` or ``DATETIME`` expression

Returns
============

* ``TO_UNIXTS`` returns the UNIX timestamp in seconds since EPOCH

* ``TO_UNIXTSMS`` returns the UNIX timestamp in milliseconds since EPOCH.

Notes
==========

To convert a UNIX timestamp to a ``DATE`` or ``DATETIME``, see :ref:`FROM_UNIXTS<from_unixts>`.

Examples
===========

Get the current UNIX timestamp
-------------------------------------

.. code-block:: psql

   master=> SELECT TO_UNIXTSMS(GETDATE()), TO_UNIXTS(GETDATE());
   to_unixtsms   | to_unixts 
   --------------+-----------
   1575642811562 | 1575642811

Filter on a range of UNIX timestamps
------------------------------------------

Get the amount of users that signed up during 2019

.. code-block:: psql

   master=> SELECT COUNT(*) FROM users 
   .>          WHERE signup_ts BETWEEN TO_UNIXTS('2019-01-01') AND TO_UNIXTS('2019-12-31');
   
   count 
   ------
   523428



