.. _data_types:

####################
Data Types
####################

SQream DB supports the following types:

****************
Supported types
****************

.. list-table:: Values
   :widths: 30 70
   :header-rows: 1
   
   * - Item
     - Further information
   * - ``tinyint``
     - Unsigned 1 byte integer (0 - 255)
   * - ``smallint``
     - 2 byte integer (-32,768 - 32,767)
   * - ``int``
     - 4 byte integer (-2,147,483,648 - 2,147,483,647)
   * - ``bigint``
     - 8 byte integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
   * - ``real``
     - 4 byte floating point (inexact)
   * - ``double``, ``float``
     - 8 byte floating point (inexact)
   * - ``varchar``
     - Variable length string - ASCII only
   * - ``nvarchar``
     - Variable length string - UTF-8 encoded
   * - ``date``
     - Date
   * - ``datetime``, ``timestamp``
     - Date and time pairing in UTC


************************
Converting and casting
************************

SQream DB supports explicit and implicit casting and type conversion.
Implicit casts may be added automatically by the system when mixing different data types in the same expression. In many cases, the details of this are not important. However, these can affect the results of a query. When necessary, an explicit cast can be used to override the automatic cast added by SQream DB.

For example, the ANSI standard defines a ``SUM()`` aggregation over an ``INT`` column as an ``INT``. However, when dealing with large amounts of data this could cause an overflow. 
To rectify this, cast the value to a larger data type: ``SUM(some_int_column :: BIGINT)``.

SQream DB supports three types of data conversion:

* ``CAST(<value> TO <data type>)``, to convert a value from one type to another. For example, ``CAST('1997-01-01' TO DATE)``, ``CAST(3.45 TO SMALLINT)``, ``CAST(some_column TO VARCHAR(30))``.
* ``<value>::<data type>``, a shorthand for the ``CAST`` syntax. For example, ``'1997-01-01' :: DATE``, ``3.45 :: SMALLINT``, ``(3+5) :: BIGINT``.
* See the :ref:`SQL functions reference <sql_functions>` for additional functions that convert from a specific value which is not an SQL type, such as ``from_unixts``, etc.