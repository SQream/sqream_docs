.. _data_types:

*************************
SQL Data Types
*************************

This topic describes the data types that SQream DB supports, and how to convert between them.

.. contents:: In this topic:
   :local:
   :depth: 2

Supported types
=================

.. list-table:: Data types
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Description
     - Data size (not null, uncompressed)
     - Example
   * - ``BOOL``
     - Boolean values (``true``,``false``)
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
   * - ``VARCHAR (n)``
     - Variable length string - ASCII only
     - ``n`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``
   * - ``NVARCHAR (n)``
     - Variable length string - UTF-8 unicode
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``
   * - ``DATE``
     - Date
     - 4 bytes
     - ``'1955-11-05'``
   * - ``DATETIME`` (``TIMESTAMP``)
     - Date and time pairing in UTC
     - 8 bytes
     - ``'1955-11-05 01:24:00.000'``

.. note:: SQream DB compresses all columns and types. The data size noted is the maximum data size allocation for uncompressed data.

Converting and casting
=========================

SQream DB supports explicit and implicit casting and type conversion.
Implicit casts may be added automatically by the system when mixing different data types in the same expression. In many cases, the details of this are not important. However, these can affect the results of a query. When necessary, an explicit cast can be used to override the automatic cast added by SQream DB.

For example, the ANSI standard defines a ``SUM()`` aggregation over an ``INT`` column as an ``INT``. However, when dealing with large amounts of data this could cause an overflow. 

To rectify this, cast the value to a larger data type:

.. code-block:: postgres

   SUM(some_int_column :: BIGINT)

SQream DB supports three types of data conversion:

* ``CAST(<value> TO <data type>)``, to convert a value from one type to another. For example, ``CAST('1997-01-01' TO DATE)``, ``CAST(3.45 TO SMALLINT)``, ``CAST(some_column TO VARCHAR(30))``.
* ``<value>::<data type>``, a shorthand for the ``CAST`` syntax. For example, ``'1997-01-01' :: DATE``, ``3.45 :: SMALLINT``, ``(3+5) :: BIGINT``.
* See the :ref:`SQL functions reference <sql_functions>` for additional functions that convert from a specific value which is not an SQL type, such as ``from_unixts``, etc.

Data type reference
======================


Boolean (``BOOL``)
-------------------
A ``BOOL`` datatype is designed to store Boolean values of ``true`` or ``false``.

Syntax
^^^^^^^^

A ``BOOL`` type can accept either ``true`` or ``false`` (case insensitive).

When loading from CSV, ``BOOL`` columns can accept ``0`` as ``false`` and ``1`` as ``true``.

Size
^^^^^^

A ``BOOL`` type is 1 byte, but resulting average data sizes could be lower after compression.

Examples
^^^^^^^^^^

.. code-block:: postgres
   
   CREATE TABLE animals (name VARCHAR(15), is_angry BOOL);
   
   INSERT INTO animals VALUES ('fox',true), ('cat',true), ('kiwi',false);
   
   SELECT name, CASE WHEN is_angry THEN 'Is really angry!' else 'Is not angry' END FROM animals;

.. code-block:: text

   "fox","Is really angry!"
   "cat","Is really angry!"
   "kiwi","Is not angry"

Casts and conversions
^^^^^^^^^^^^^^^^^^^^^^^

A ``BOOL`` value can be converted to:

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
Integer datatypes are designed to store whole numbers.

For information about sequences (sometimes called auto-increment or auto-numbers), see :ref:`SEQUENCE <sequence>`.

Integer types
^^^^^^^^^^^^^^^^^^^
.. list-table:: Integer types
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data size (not null, uncompressed)
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

Syntax
^^^^^^^^

An integer can be entered as a regular literal, such as ``12``, ``-365``.

Size
^^^^^^

Integer types range between 1, 2, 4, and 8 bytes - but resulting average data sizes could be lower after compression.

Examples
^^^^^^^^^^

.. code-block:: postgres
   
   CREATE TABLE cool_numbers (a INT NOT NULL, b TINYINT, c SMALLINT, d BIGINT);
   
   INSERT INTO cool_numbers VALUES (1,2,3,4), (-5, 127, 32000, 45000000000);
   
   SELECT * FROM cool_numbers;

.. code-block:: text

   1,2,3,4
   -5,127,32000,45000000000

Casts and conversions
^^^^^^^^^^^^^^^^^^^^^^^

Integer values can be converted to:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``REAL``, ``DOUBLE``
     - ``1`` → ``1.0``, ``-32`` → ``-32.0``
   * - ``VARCHAR(n)`` (All numberic values must fit in the string length)
     - ``1`` → ``'1'``, ``2451`` → ``'2451'``


Floating point (``REAL``, ``DOUBLE``)
------------------------------------------------
``REAL`` and ``DOUBLE`` are inexact floating point data types, designed to store up to 9 or 17 digits of precision respectively.

The floating point representation is based on `IEEE 754 <https://en.wikipedia.org/wiki/IEEE_754>`_.

For information about sequences (sometimes called auto-increment or auto-numbers), see :ref:`SEQUENCE <sequence>`.

Floating point types
^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: Floating point types
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data size (not null, uncompressed)
     - Example
   * - ``REAL``
     - Single precision floating point (inexact)
     - 4 bytes
     - ``3.141``
   * - ``DOUBLE``
     - Double precision floating point (inexact)
     - 8 bytes
     - ``0.000003``

Aliases
^^^^^^^^^^

``DOUBLE`` is also known as ``FLOAT``.


Syntax
^^^^^^^^

A double precision floating point can be entered as a regular literal, such as ``3.14``, ``2.718``, ``.34``, ``2.71e-45``.

To enter a ``REAL`` floating point number, cast the value. For example, ``(3.14 :: REAL)``. 

Size
^^^^^^

Floating point types are either 4 or 8 bytes, but size could be lower after compression.

Examples
^^^^^^^^^^

.. code-block:: postgres
   
   CREATE TABLE cool_numbers (a REAL NOT NULL, b DOUBLE);
   
   INSERT INTO cool_numbers VALUES (1,2), (3.14159265358979, 2.718281828459);
   
   SELECT * FROM cool_numbers;

.. code-block:: text

   1.0,2.0
   3.1415927,2.718281828459

.. note:: Most clients control display precision of floating point numbers, and values may appear differently in some clients.

Casts and conversions
^^^^^^^^^^^^^^^^^^^^^^^

Floating point values can be converted to:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``BOOL``
     - ``1.0`` → ``true``, ``0.0`` → ``false``
   * - ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``
     - ``2.0`` → ``2``, ``3.14159265358979`` → ``3``, ``2.718281828459`` → ``2``
   * - ``VARCHAR(n)`` (n > 6 recommended)
     - ``1`` → ``'1.0000'``, ``3.14159265358979`` → ``'3.1416'``


String types (``VARCHAR``, ``NVARCHAR``)
------------------------------------------------
``VARCHAR`` and ``NVARCHAR`` are types designed for storing text or strings of characters.

In this release, SQream DB separates ASCII (``VARCHAR``) and UTF-8 representations (``NVARCHAR``).


String types
^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: String types
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data size (not null, uncompressed)
     - Example
   * - ``VARCHAR (n)``
     - Variable length string - ASCII only
     - ``n`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``
   * - ``NVARCHAR (n)``
     - Variable length string - UTF-8 unicode
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``

Length
^^^^^^^^^

Unlike some other types, the string types can be limited in length. To limit the length, use ``VARCHAR(n)`` or ``NVARCHAR(n)``, where n is the number of characters allowed.

* If the data exceeds the column length limit on ``INSERT`` or ``COPY`` operations, SQream DB will return an error.

* When casting or converting, the string has to fit in the target. For example, ``'Kiwis are weird birds' :: VARCHAR(5)`` will return an error. Use ``SUBSTRING`` to truncate the length of the string.

* ``VARCHAR`` strings are padded with spaces.

Syntax
^^^^^^^^

String types can be written with standard SQL string literals, which are enclosed with single quotes, such as
``'Kiwi bird'``. To include a single quote in the string, repeat the quote twice: ``'Kiwi bird''s wings are tiny'``.

String literals can also be dollar-quoted with the dollar sign ``$``. For example: ``$$Kiwi bird's wings are tiny$$`` is the same as ``'Kiwi bird''s wings are tiny'``.

Size
^^^^^^

``VARCHAR(n)`` can occupy up to *n* bytes, whereas ``NVARCHAR(n)`` can occupy up to *4*n* bytes.
However, the size of strings is variable and is compressed by SQream DB.

Examples
^^^^^^^^^^

.. code-block:: postgres
   
   CREATE TABLE cool_strings (a VARCHAR(25) NOT NULL, b NVARCHAR(40));
   
   INSERT INTO cool_strings VALUES ('hello world', 'Hello to kiwi birds specifically');
   
   INSERT INTO cool_strings VALUES ('This is ASCII only', 'But this column can contain 中文文字');

   SELECT * FROM cool_strings;

.. code-block:: text

   hello world	,Hello to kiwi birds specifically
   This is ASCII only,But this column can contain 中文文字

.. note:: Most clients control display precision of floating point numbers, and values may appear differently in some clients.

Casts and conversions
^^^^^^^^^^^^^^^^^^^^^^^

String values can be converted to:

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



Date types (``DATE``, ``DATETIME``)
------------------------------------------------

``DATE`` is a type designed for storing year, month, and day.

``DATETIME`` is a type designed for storing year, month, day, hour, minute, seconds, and milliseconds in UTC with 1 millisecond precision.


Date types
^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: Date types
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data size (not null, uncompressed)
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

SQream DB will attempt to guess if the string literal is a date or datetime based on context, for example when used in date-specific functions.

Size
^^^^^^

A ``DATE`` column is 4 bytes in length, while a ``DATETIME`` column is 8 bytes in length.

However, the size of these values is compressed by SQream DB.

Examples
^^^^^^^^^^

.. code-block:: postgres
   
   CREATE TABLE important_dates (a DATE, b DATETIME);

   INSERT INTO important_dates VALUES ('1997-01-01', '1955-11-05 01:24');

   SELECT * FROM important_dates;

.. code-block:: text

   1997-01-01,1955-11-05 01:24:00.0

.. code-block:: postgres
   
   SELECT a :: DATETIME, b :: DATE FROM important_dates;

.. code-block:: text

   1997-01-01 00:00:00.0,1955-11-05
   

.. warning:: Some client applications may alter the ``DATETIME`` value by modifying the timezone.

Casts and conversions
^^^^^^^^^^^^^^^^^^^^^^^

``DATE`` and ``DATETIME`` values can be converted to:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``VARCHAR(n)``
     - ``'1997-01-01'`` → ``'1997-01-01'``, ``'1955-11-05 01:24'`` → ``'1955-11-05 01:24:00.000'``
