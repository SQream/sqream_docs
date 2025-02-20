.. _sql_data_types_date:

*************************
DateTime2
*************************

``DATETIME2`` is a type designed for storing year, month, day, hour, minute, seconds, milliseconds, microseconds, nanoseconds and UTC offset with 1 nanosecond precision.


Aliases
^^^^^^^^^^

NA


Syntax
^^^^^^^^

``DATETIME2`` values are formatted as string literals. 

The following is an example of the DATETIME2 syntax:

.. code-block:: console
     
   ``1955-11-05 01:24:00.000000000 +00:00:00``


``DATETIME2`` values are formatted as string literals conforming to `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.

SQream attempts to guess if the string literal is a datetime2 based on context, for example when used in date-specific functions.

Size
^^^^^^

A ``DATETIME2`` column is 16 bytes.

However, the size of these values is compressed by SQream DB.

Date Examples
^^^^^^^^^^^^^

The following is an example of the Date syntax:

.. code-block:: postgres
   
   CREATE TABLE important_dates (a DATETIME2);

   INSERT INTO important_dates VALUES ('1955-11-05 01:24:00.000000000 -08:00:00');

   SELECT * FROM important_dates;
   
The following is an example of the correct output:

.. code-block:: text

   1955-11-05 01:24:00.000000000 -08:00:00
   


Date Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible ``DATETIME2`` value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``TEXT``
     - ``'1997-01-01'`` → ``'1997-01-01 00:00:00.000000 +00:00:00'``, ``'1955-11-05 01:24'`` → ``'1955-11-05 01:24:00.000000 +00:00:00'``
	 * - Type
     - Details
   * - ``DATE``
     - ``'1997-01-01'`` → ``'1997-01-01 00:00:00.000000 +00:00:00'``
	 * - Type
     - Details
   * - ``DATETIME``
     - ``'1955-11-05 01:24'`` → ``'1955-11-05 01:24:00.000000 +00:00:00'``