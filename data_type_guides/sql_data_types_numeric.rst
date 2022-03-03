.. _sql_data_types_numeric:

*************************
Numeric
*************************
The **Numeric** data type (also known as **Decimal**) is recommended for values that tend to occur as exact decimals, such as in Finance. While Numeric has a fixed precision of ``38``, higher than ``REAL`` (``9``) or ``DOUBLE`` (``17``), it runs calculations more slowly. For operations that require faster performance, using :ref:`Floating Point <floating_point>` is recommended.

The correct syntax for Numeric is ``numeric(p, s)``), where ``p`` is the total number of digits (``38`` maximum), and ``s`` is the total number of decimal digits.

Numeric Examples
^^^^^^^^^^

The following is an example of the Numeric syntax:

.. code-block:: postgres

   $ create or replace table t(x numeric(20, 10), y numeric(38, 38));
   $ insert into t values(1234567890.1234567890, 0.123245678901234567890123456789012345678);
   $ select x + y from t;
   
The following table shows information relevant to the Numeric data type:

.. list-table::
   :widths: 30 30 30
   :header-rows: 1
   
   * - Description
     - Data Size (Not Null, Uncompressed)
     - Example	 
   * - 38 digits
     - 16 bytes
     - ``0.123245678901234567890123456789012345678``

Numeric supports the following operations:

   * All join types.
   * All aggregation types (not including Window functions).
   * Scalar functions (not including some trigonometric and logarithmic functions).