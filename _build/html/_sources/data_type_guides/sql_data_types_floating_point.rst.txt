.. _sql_data_types_floating_point:

*************************
Floating Point
*************************
The **Floating Point** data types (``REAL`` and ``DOUBLE``) store extremely close value approximations, and are therefore recommended for values that tend to be inexact, such as Scientific Notation. While Floating Point generally runs faster than Numeric, it has a lower precision of ``9`` (``REAL``) or ``17`` (``DOUBLE``) compared to Numeric's ``38``. For operations that require a higher level of precision, using :ref:`Numeric <numeric>` is recommended.

The floating point representation is based on `IEEE 754 <https://en.wikipedia.org/wiki/IEEE_754>`_.

Floating Point Types
^^^^^^^^^^^^^^^^^^^^^^
The following table describes the Floating Point data types.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data Size (Not Null, Uncompressed)
     - Example
   * - ``REAL``
     - Single precision floating point (inexact)
     - 4 bytes
     - ``3.141``
   * - ``DOUBLE``
     - Double precision floating point (inexact)
     - 8 bytes
     - ``0.000003``
	 
The following table shows information relevant to the Floating Point data types.

.. list-table::
   :widths: 30 30 30
   :header-rows: 1
   
   * - Aliases
     - Syntax
     - Data Size (Not Null, Uncompressed)	 
   * - ``DOUBLE`` is also known as ``FLOAT``.
     - A double precision floating point can be entered as a regular literal, such as ``3.14``, ``2.718``, ``.34``, or ``2.71e-45``. To enter a ``REAL`` floating point number, cast the value. For example, ``(3.14 :: REAL)``.
     - Floating point types are either 4 or 8 bytes, but size could be lower after compression.

Floating Point Examples
^^^^^^^^^^
The following are examples of the Floating Point syntax:

.. code-block:: postgres
   
   CREATE TABLE cool_numbers (a REAL NOT NULL, b DOUBLE);
   
   INSERT INTO cool_numbers VALUES (1,2), (3.14159265358979, 2.718281828459);
   
   SELECT * FROM cool_numbers;

.. code-block:: text

   1.0,2.0
   3.1415927,2.718281828459

.. note:: Most SQL clients control display precision of floating point numbers, and values may appear differently in some clients.

Floating Point Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^
The following table shows the possible Floating Point value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``BOOL``
     - ``1.0`` → ``true``, ``0.0`` → ``false``
   * - ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``
     - ``2.0`` → ``2``, ``3.14159265358979`` → ``3``, ``2.718281828459`` → ``2``, ``0.5`` → ``0``, ``1.5`` → ``1``


.. note:: As shown in the above examples, casting ``real`` to ``int`` rounds down.