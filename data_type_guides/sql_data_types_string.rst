.. _sql_data_types_string:

*************************
String
*************************
The ``TEXT`` type is designed for storing text or strings of characters.

.. note:: The data type ``NVARCHAR`` has been deprecated by ``TEXT`` as of version 2020.1.

String Types
^^^^^^^^^^^^^^^^^^^^^^
The following table describes the String types:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Name
     - Details
     - Data Size (Not Null, Uncompressed)
     - Example
   * - ``TEXT [(n)]``
     - Varaiable length string - UTF-8 unicode. ``NVARCHAR`` is synonymous with ``TEXT``.
     - Up to ``4*n`` bytes
     - ``'キウイは楽しい鳥です'``

Length
^^^^^^^^^
When using ``TEXT``, specifying a size is optional. If not specified, the text field carries no constraints. To limit the size of the input, use ``TEXT(n)``, where ``n`` is the permitted number of characters.

The following apply to setting the String type length:

* If the data exceeds the column length limit on ``INSERT`` or ``COPY`` operations, SQream DB will return an error.
* When casting or converting, the string has to fit in the target. For example, ``'Kiwis are weird birds' :: TEXT`` will return an error. Use ``SUBSTRING`` to truncate the length of the string.
* ``TEXT`` strings are padded with spaces.

Syntax
^^^^^^^^
String types can be written with standard SQL string literals, which are enclosed with single quotes, such as
``'Kiwi bird'``. To include a single quote in the string, use double quotations, such as ``'Kiwi bird''s wings are tiny'``. String literals can also be dollar-quoted with the dollar sign ``$``, such as ``$$Kiwi bird's wings are tiny$$`` is the same as ``'Kiwi bird''s wings are tiny'``.

Size
^^^^^^
``VARCHAR(n)`` can occupy up to *n* bytes, whereas ``TEXT(n)`` can occupy up to *4*n* bytes. However, the size of strings is variable and is compressed by SQream.

String Examples
^^^^^^^^^^
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
^^^^^^^^^^^^^^^^^^^^^^^
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