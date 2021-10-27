.. _data_types:

*************************
Data Types
*************************

This topic describes the data types that SQream DB supports, and how to convert between them. 

.. contents:: In this topic:
   :local:
   :depth: 2

Supported Types
=================

The following table shows the supported data types.

.. list-table::
   :widths: 20 15 20 55
   :header-rows: 1
   
   * - Name
     - Description
     - Data Size (Not Null, Uncompressed)
     - Example
   * - ``BOOL``
     - Boolean values (``true``, ``false``)
     - 1 byte
     - ``true``
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
   * - ``REAL``
     - Floating point (inexact)
     - 4 bytes
     - ``3.141``
   * - ``DOUBLE`` (``FLOAT``)
     - Floating point (inexact)
     - 8 bytes
     - ``0.000003``
   * - ``TEXT [(n)]``, ``NVARCHAR (n)``
     - Variable length string - UTF-8 unicode
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``
   * - ``NUMERIC``, ``DECIMAL``
     -  38 digits
     - 16 bytes
     - ``0.123245678901234567890123456789012345678``
   * - ``VARCHAR (n)``
     - Variable length string - ASCII only
     - ``n`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``
   * - ``DATE``
     - Date
     - 4 bytes
     - ``'1955-11-05'``
   * - ``DATETIME`` (``TIMESTAMP``)
     - Date and time pairing in UTC
     - 8 bytes
     - ``'1955-11-05 01:24:00.000'``

.. note:: SQream DB compresses all columns and types. The data size noted is the maximum data size allocation for uncompressed data.

.. _cast:

Converting and Casting Types
==============================

SQream DB supports explicit and implicit casting and type conversion.
The system may automatically add implicit casts when combining different data types in the same expression. In many cases, while the details related to this are not important, they can affect the query results of a query. When necessary, an explicit cast can be used to override the automatic cast added by SQream DB.

For example, the ANSI standard defines a ``SUM()`` aggregation over an ``INT`` column as an ``INT``. However, when dealing with large amounts of data this could cause an overflow. 

You can rectify this by casting the value to a larger data type:

.. code-block:: postgres

   SUM(some_int_column :: BIGINT)

SQream DB supports the following three data conversion types:

* ``CAST(<value> AS <data type>)``, to convert a value from one type to another. For example, ``CAST('1997-01-01' AS DATE)``, ``CAST(3.45 AS SMALLINT)``, ``CAST(some_column AS VARCHAR(30))``.
* ``<value> :: <data type>``, a shorthand for the ``CAST`` syntax. For example, ``'1997-01-01' :: DATE``, ``3.45 :: SMALLINT``, ``(3+5) :: BIGINT``.
* See the :ref:`SQL functions reference <sql_functions>` for additional functions that convert from a specific value which is not an SQL type, such as :ref:`from_unixts`, etc.

The **Data Type Reference** section below provides more details about the supported casts for each type.

Data Type Reference
======================

.. _numeric:

Numeric (``NUMERIC``, ``DECIMAL``)
-----------------------------------
The **Numeric** data type (also known as **Decimal**) is recommended for values that tend to occur as exact decimals, such as in Finance. While Numeric has a fixed precision of ``38``, higher than ``REAL`` (``9``) or ``DOUBLE`` (``17``), it runs calculations more slowly. For operations that require faster performance, using :ref:`Floating Point <floating_point>` is recommended.

The correct syntax for Numeric is ``numeric(p, s)``), where ``p`` is the total number of digits (``38`` maximum), and ``s`` is the total number of decimal digits.

Numeric Examples
^^^^^^^^^^^^^^^^^^^^

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
   


Boolean (``BOOL``)
-------------------
The following table describes the Boolean data type.

.. list-table::
   :widths: 30 30 30
   :header-rows: 1
   
   * - Values
     - Syntax
     - Data Size (Not Null, Uncompressed)	 
   * - ``true``, ``false`` (case sensitive)
     - When loading from CSV, ``BOOL`` columns can accept ``0`` as ``false`` and ``1`` as ``true``.
     - 1 byte, but resulting average data sizes may be lower after compression.
	 
Boolean Examples
^^^^^^^^^^^^^^^^^^^^

The following is an example of the Boolean syntax:

.. code-block:: postgres
   
   CREATE TABLE animals (name TEXT, is_angry BOOL);
   
   INSERT INTO animals VALUES ('fox',true), ('cat',true), ('kiwi',false);
   
   SELECT name, CASE WHEN is_angry THEN 'Is really angry!' else 'Is not angry' END FROM animals;
   
The following is an example of the correct output:

.. code-block:: text

   "fox","Is really angry!"
   "cat","Is really angry!"
   "kiwi","Is not angry"

Boolean Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible Boolean value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``
     - ``true`` → ``1``, ``false`` → ``0``
   * - ``REAL``, ``DOUBLE``
     - ``true`` → ``1.0``, ``false`` → ``0.0``









Integers (``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``)
------------------------------------------------------------
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
^^^^^^^^^^^^^^^^^^^^
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible Integer value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``REAL``, ``DOUBLE``
     - ``1`` → ``1.0``, ``-32`` → ``-32.0``
   * - ``VARCHAR(n)`` (All numberic values must fit in the string length)
     - ``1`` → ``'1'``, ``2451`` → ``'2451'``
	 
.. _floating_point:

Floating Point (``REAL``, ``DOUBLE``)
------------------------------------------------   
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
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: postgres
   
   CREATE TABLE cool_numbers (a REAL NOT NULL, b DOUBLE);
   
   INSERT INTO cool_numbers VALUES (1,2), (3.14159265358979, 2.718281828459);
   
   SELECT * FROM cool_numbers;

.. code-block:: text

   1.0,2.0
   3.1415927,2.718281828459

.. note:: Most SQL clients control display precision of floating point numbers, and values may appear differently in some clients.

Floating Point Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
   * - ``VARCHAR(n)`` (n > 6 recommended)
     - ``1`` → ``'1.0000'``, ``3.14159265358979`` → ``'3.1416'``

.. note:: As shown in the above examples, when casting ``real`` to ``int``, we round down.

String (``TEXT``, ``VARCHAR``)
------------------------------------------------
``TEXT`` and ``VARCHAR`` are types designed for storing text or strings of characters.

SQream DB separates ASCII (``VARCHAR``) and UTF-8 representations (``TEXT``).

.. note:: The data type ``NVARCHAR`` has been deprecated by ``TEXT`` as of version 2020.1.

String Types
^^^^^^^^^^^^^^^^^^^^^^
The following table describes the String types.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data Size (Not Null, Uncompressed)
     - Example
   * - ``TEXT [(n)]``, ``NVARCHAR (n)``
     - Varaiable length string - UTF-8 unicode. ``NVARCHAR`` is synonymous with ``TEXT``.
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``
   * - ``VARCHAR (n)``
     - Variable length string - ASCII only
     - ``n`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``

Length
^^^^^^^^^

When using ``TEXT``, specifying a size is optional. If not specified, the text field carries no constraints. To limit the size of the input, use ``VARCHAR(n)`` or ``TEXT(n)``, where ``n`` is the permitted number of characters.

The following apply to setting the String type length:

* If the data exceeds the column length limit on ``INSERT`` or ``COPY`` operations, SQream DB will return an error.
* When casting or converting, the string has to fit in the target. For example, ``'Kiwis are weird birds' :: VARCHAR(5)`` will return an error. Use ``SUBSTRING`` to truncate the length of the string.
* ``VARCHAR`` strings are padded with spaces.

Syntax
^^^^^^^^

String types can be written with standard SQL string literals, which are enclosed with single quotes, such as
``'Kiwi bird'``.

To include a single quote in the string, use double quotations, such as ``'Kiwi bird''s wings are tiny'``.

String literals can also be dollar-quoted with the dollar sign ``$``, such as ``$$Kiwi bird's wings are tiny$$`` is the same as ``'Kiwi bird''s wings are tiny'``.

Size
^^^^^^

``VARCHAR(n)`` can occupy up to *n* bytes, whereas ``TEXT(n)`` can occupy up to *4*n* bytes.
However, the size of strings is variable and is compressed by SQream DB.

String Examples
^^^^^^^^^^^^^^^^^^^^
The following is an example of the String syntax: 

.. code-block:: postgres
   
   CREATE TABLE cool_strings (a TEXT NOT NULL, b TEXT);
   
   INSERT INTO cool_strings VALUES ('hello world', 'Hello to kiwi birds specifically');
   
   INSERT INTO cool_strings VALUES ('This is ASCII only', 'But this column can contain 中文文字');

   SELECT * FROM cool_strings;
   
The following is an example of the correct output:

.. code-block:: text

   hello world	,Hello to kiwi birds specifically
   This is ASCII only,But this column can contain 中文文字

.. note:: Most clients control the display precision of floating point numbers, and values may appear differently in some clients.

String Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following table shows the possible String value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``BOOL``
     - ``'true'`` → ``true``, ``'false'`` → ``false``
   * - ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``
     - ``'2'`` → ``2``, ``'-128'`` → ``-128``
   * - ``REAL``, ``DOUBLE``
     - ``'2.0'`` → ``2.0``, ``'3.141592'`` → ``3.141592``
   * - ``DATE``, ``DATETIME``
     - Requires a supported format, such as ``'1955-11-05`` → ``date '1955-11-05'``, ``'1955-11-05 01:24:00.000'`` → ``'1955-11-05 01:24:00.000'``



Date (``DATE``, ``DATETIME``)
------------------------------------------------
``DATE`` is a type designed for storing year, month, and day.

``DATETIME`` is a type designed for storing year, month, day, hour, minute, seconds, and milliseconds in UTC with 1 millisecond precision.


Date Types
^^^^^^^^^^^^^^^^^^^^^^
The following table describes the Date types.

.. list-table:: Date types
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

``DATETIME`` is also known as ``TIMESTAMP``.


Syntax
^^^^^^^^

``DATE`` values are formatted as string literals. For example, ``'1955-11-05'`` or ``date '1955-11-05'``.

``DATETIME`` values are formatted as string literals conforming to `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_, for example ``'1955-11-05 01:26:00'``.

SQream DB attempts to guess if the string literal is a date or datetime based on context, for example when used in date-specific functions.

Size
^^^^^^

A ``DATE`` column is 4 bytes in length, while a ``DATETIME`` column is 8 bytes in length.

However, the size of these values is compressed by SQream DB.

Date Examples
^^^^^^^^^^^^^^^^^^^^
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible ``DATE`` and ``DATETIME`` value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``VARCHAR(n)``
     - ``'1997-01-01'`` → ``'1997-01-01'``, ``'1955-11-05 01:24'`` → ``'1955-11-05 01:24:00.000'``
