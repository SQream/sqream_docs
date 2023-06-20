.. _supported_data_types:

********************
Supported Data Types
********************

The following table shows the supported data types.

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
   * - ``TEXT (n)``
     - Variable length string - UTF-8 unicode
     - Up to ``4`` bytes
     - ``'Kiwis have tiny wings, but cannot fly.'``
     - ``CHAR VARYING``, ``CHAR``, ``CHARACTER VARYING``, ``CHARACTER``, ``NATIONAL CHARACTER VARYING``, ``NATIONAL CHARACTER``, ``NCHAR VARYING``, ``NCHAR``, ``NATIONAL CHAR``, ``NATIONAL CHAR VARYING``
   * - ``NUMERIC``
     -  38 digits
     - 16 bytes
     - ``0.123245678901234567890123456789012345678``
     - ``DECIMAL``
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
   * - ``ARRAY``
     - Array of values
     - Variable
     - ``[1,2,3]``
     -  NA

.. note:: SQream compresses all columns and types. The data size noted is the maximum data size allocation for uncompressed data.