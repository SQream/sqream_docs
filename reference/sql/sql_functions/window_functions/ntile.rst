.. _ntile:

**************************
NTILE
**************************

The **NTILE** function returns an integer ranging between ``1`` and the argument value, and divides a table's rows into ``n`` ranked buckets according to the following:

* The selected column.
* The selected positive, literal ``n``.

Selecting an ``n`` that exceeds the number of rows in a table outputs a result identical to the RANK function. When this happens, each ranked bucket is populated with a single value and any bucket numbered higher than the number of rows not even being created.

Additionally, if the number of rows in a bucket is not exactly divisible by ``n``, the function gives precedence to values at the top. For example, if ``n`` is ``6`` for 63 values, the top three buckets each have 11 values, and the bottom three each have 10.

Syntax
-------
The following shows the correct syntax for the NTILE function.

.. code-block:: postgres

   NTILE(n) OVER (...)
