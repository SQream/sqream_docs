.. _from_unixts:

****************************
FROM_UNIXTS, FROM_UNIXTSMS
****************************

Converts a ``BIGINT`` representing a UNIX timestamp to a ``DATETIME`` value.

Syntax
==========

.. code-block:: postgres

   FROM_UNIXTS( expr ) --> DATETIME
   
   FROM_UNIXTSMS( expr ) --> DATETIME

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - An integer containing a UNIX timestamp in seconds/milliseconds from EPOCH

Returns
============

* ``FROM_UNIXTS`` returns a ``DATETIME`` from a UNIX timestamp in seconds since EPOCH

* ``FROM_UNIXTSMS`` returns ``DATETIME`` from a UNIX timestamp in milliseconds since EPOCH.

Notes
==========

To convert a ``DATETIME`` to a UNIX timestamp, see :ref:`TO_UNIXTS<to_unixts>`.

Examples
===========

Convert a UNIX timestamp to ``DATETIME``
-----------------------------------------

.. code-block:: psql

   master=> SELECT FROM_UNIXTS(0), FROM_UNIXTS(1575636057);
   to_unixtsms   | to_unixts 
   --------------+-----------
   1575642811562 | 1575642811
