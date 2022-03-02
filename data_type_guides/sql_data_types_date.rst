.. _sql_data_types_date:

*************************
Date
*************************
``DATE`` is a type designed for storing year, month, and day. ``DATETIME`` is a type designed for storing year, month, day, hour, minute, seconds, and milliseconds in UTC with 1 millisecond precision.


Date Types
^^^^^^^^^^^^^^^^^^^^^^
The following table describes the Date types:

.. list-table:: Date Types
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data Size (Not Null, Uncompressed)
     - Example
   * - ``DATE``
     - Date
     - 4 bytes
     - ``'1955-11-05'``
   * - ``DATETIME``
     - Date and time pairing in UTC
     - 8 bytes
     - ``'1955-11-05 01:24:00.000'``

Aliases
^^^^^^^^^^

``DATETIME`` is also known as ``TIMESTAMP`` or ``DATETIME2``.


Syntax
^^^^^^^^
``DATE`` values are formatted as string literals. 

The following is an example of the DATETIME syntax:

.. code-block:: console
     
   '1955-11-05'

.. code-block:: console
     
   date '1955-11-05'

``DATETIME`` values are formatted as string literals conforming to `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.

The following is an example of the DATETIME syntax:


.. code-block:: console
     
   '1955-11-05 01:26:00'

SQream attempts to guess if the string literal is a date or datetime based on context, for example when used in date-specific functions.

Size
^^^^^^
A ``DATE`` column is 4 bytes in length, while a ``DATETIME`` column is 8 bytes in length.

However, the size of these values is compressed by SQream DB.

Date Examples
^^^^^^^^^^
The following is an example of the Date syntax:

.. code-block:: postgres
   
   CREATE TABLE important_dates (a DATE, b DATETIME);

   INSERT INTO important_dates VALUES ('1997-01-01', '1955-11-05 01:24');

   SELECT * FROM important_dates;
   
The following is an example of the correct output:

.. code-block:: text

   1997-01-01,1955-11-05 01:24:00.0
   
The following is an example of the Datetime syntax:

.. code-block:: postgres
   
   SELECT a :: DATETIME, b :: DATE FROM important_dates;
   
The following is an example of the correct output:

.. code-block:: text

   1997-01-01 00:00:00.0,1955-11-05
   

.. warning:: Some client applications may alter the ``DATETIME`` value by modifying the timezone.

Date Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible ``DATE`` and ``DATETIME`` value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``VARCHAR(n)``
     - ``'1997-01-01'`` → ``'1997-01-01'``, ``'1955-11-05 01:24'`` → ``'1955-11-05 01:24:00.000'``