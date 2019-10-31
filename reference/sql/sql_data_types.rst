.. _data_types:

*************************
Data Types
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
   * - ``DOUBLE``, ``FLOAT``
     - Floating point (inexact)
     - 8 bytes
     - ``0.000003``
   * - ``VARCHAR (n)``
     - Variable length string - ASCII only
     - ``n`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``
   * - ``NVARCHAR (n)``
     - Variable length string - UTF-8 encoded
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``
   * - ``DATE``
     - Date
     - 4 bytes
     - ``'1955-11-05'``
   * - ``DATETIME``, ``TIMESTAMP``
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


BOOL
-----
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
   * - ``DOUBLE``, ``FLOAT``
     - Double precision floating point (inexact)
     - 8 bytes
     - ``0.000003``


Syntax
^^^^^^^^

A double precision floating point can be entered as a regular literal, such as ``3.14``, ``2.718``.

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
