.. _sql_data_types_integer:

*************************
Integer
*************************
Integer data types are designed to store whole numbers.

For more information about identity sequences (sometimes called auto-increment or auto-numbers), see :ref:`identity`.

Integer Types
^^^^^^^^^^^^^^^^^^^
The following table describes the Integer types.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data Size (Not Null, Uncompressed)
     - Example
   * - ``TINYINT``
     - Unsigned integer (0 - 255)
     - 1 byte
     - ``5``
   * - ``SMALLINT``
     - Integer (-32,768 - 32,767)
     - 2 bytes
     - ``-155``
   * - ``INT``
     - Integer (-2,147,483,648 - 2,147,483,647)
     - 4 bytes
     - ``1648813``
   * - ``BIGINT``
     - Integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
     - 8 bytes
     - ``36124441255243``	 
	 
The following table describes the Integer data type.
	 
.. list-table::
   :widths: 25 25
   :header-rows: 1
   
   * - Syntax
     - Data Size (Not Null, Uncompressed)	 
   * - An integer can be entered as a regular literal, such as ``12``, ``-365``.
     - Integer types range between 1, 2, 4, and 8 bytes - but resulting average data sizes could be lower after compression.

Integer Examples
^^^^^^^^^^
The following is an example of the Integer syntax:

.. code-block:: postgres
   
   CREATE TABLE cool_numbers (a INT NOT NULL, b TINYINT, c SMALLINT, d BIGINT);
   
   INSERT INTO cool_numbers VALUES (1,2,3,4), (-5, 127, 32000, 45000000000);
   
   SELECT * FROM cool_numbers;
   
The following is an example of the correct output:

.. code-block:: text

   1,2,3,4
   -5,127,32000,45000000000

Integer Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible Integer value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``REAL``, ``DOUBLE``
     - ``1`` → ``1.0``, ``-32`` → ``-32.0``
   * - ``TEXT`` (All numeric values must fit in the string length)
     - ``1`` → ``'1'``, ``2451`` → ``'2451'``