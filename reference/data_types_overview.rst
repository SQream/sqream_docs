.. _data_types_overview:

*************************
Overview
*************************
This page describes the following:

.. contents::
   :local:
   :depth: 2
   
Supported Data Types
======================
The **Supported Data Types** page describes SQream's supported data types:

.. list-table::
   :widths: 20 15 20 30 20
   :header-rows: 1
   
   * - Name
     - Description
     - Data Size (Not Null, Uncompressed)
     - Example
     - Alias
   * - ``BOOL``
     - Boolean values (``true``, ``false``)
     - 1 byte
     - ``true``
     - ``BIT``
   * - ``TINYINT``
     - Unsigned integer (0 - 255)
     - 1 byte
     - ``5``
     - NA
   * - ``SMALLINT``
     - Integer (-32,768 - 32,767)
     - 2 bytes
     - ``-155``
     - NA
   * - ``INT``
     - Integer (-2,147,483,648 - 2,147,483,647)
     - 4 bytes
     - ``1648813``
     - ``INTEGER``
   * - ``BIGINT``
     - Integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
     - 8 bytes
     - ``36124441255243``
     - ``NUMBER``
   * - ``REAL``
     - Floating point (inexact)
     - 4 bytes
     - ``3.141``
     - NA
   * - ``DOUBLE``
     - Floating point (inexact)
     - 8 bytes
     - ``0.000003``
     - ``FLOAT``/``DOUBLE PRECISION``
   * - ``TEXT [(n)]``, ``NVARCHAR (n)``
     - Variable length string - UTF-8 unicode
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``
     - ``CHAR VARYING``, ``CHAR``, ``CHARACTER VARYING``, ``CHARACTER``, ``NATIONAL CHARACTER VARYING``, ``NATIONAL CHARACTER``, ``NCHAR VARYING``, ``NCHAR``, ``NVARCHAR``
   * - ``NUMERIC``
     -  38 digits
     - 16 bytes
     - ``0.123245678901234567890123456789012345678``
     - ``DECIMAL``
   * - ``VARCHAR (n)``
     - Variable length string - ASCII only
     - ``n`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``
     - ``SQL VARIANT``
   * - ``DATE``
     - Date
     - 4 bytes
     - ``'1955-11-05'``
     - NA
   * - ``DATETIME``
     - Date and time pairing in UTC
     - 8 bytes
     - ``'1955-11-05 01:24:00.000'``
     -  ``TIMESTAMP``, ``DATETIME2``

.. note:: SQream compresses all columns and types. The data size noted is the maximum data size allocation for uncompressed data.

Converting and Casting Types
==============================
SQream supports explicit and implicit casting and type conversion. The system may automatically add implicit casts when combining different data types in the same expression. In many cases, while the details related to this are not important, they can affect the query results of a query. When necessary, an explicit cast can be used to override the automatic cast added by SQream DB.

For example, the ANSI standard defines a ``SUM()`` aggregation over an ``INT`` column as an ``INT``. However, when dealing with large amounts of data this could cause an overflow. 

You can rectify this by casting the value to a larger data type, as shown below:

.. code-block:: postgres

   SUM(some_int_column :: BIGINT)

SQream supports the following three data conversion types:

* ``CAST(<value> TO <data type>)``, to convert a value from one type to another. For example, ``CAST('1997-01-01' TO DATE)``, ``CAST(3.45 TO SMALLINT)``, ``CAST(some_column TO VARCHAR(30))``.

   ::
  
* ``<value> :: <data type>``, a shorthand for the ``CAST`` syntax. For example, ``'1997-01-01' :: DATE``, ``3.45 :: SMALLINT``, ``(3+5) :: BIGINT``.

   ::
  
* See the :ref:`SQL functions reference <sql_functions>` for additional functions that convert from a specific value which is not an SQL type, such as :ref:`from_unixts`, etc.

The **Data Type Reference** section below provides more details about the supported casts for each type.

.. toctree::
   :maxdepth: 5
   :caption: In this section:
   :glob:

   sql_data_types_numeric