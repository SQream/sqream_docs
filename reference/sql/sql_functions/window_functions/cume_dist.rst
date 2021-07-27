.. _cume_dist:

**************************
CUME_DIST
**************************

The **CUME_DIST** function returns the cumulative distribution for each of your partitioned rows between the range of ``1/n`` (with ``n`` being the total number of rows), and ``1``. For example, in a table with ten rows, the cumulative distance for the first row is ``0.1`` and the second is ``0.2``, etc. The cumulative distance of the final row is always ``1``.

Syntax
-------
The following shows the correct syntax for the CUME_DIST function.

.. code-block:: postgres

   CUME_DIST ( ) OVER (...)  

Arguments
---------
None

Returns
---------
Returns the cumulative distribution for each of your partitioned rows.