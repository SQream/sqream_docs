.. _converting_and_casting_types:

*************************
Converting and Casting Types
*************************
SQream supports explicit and implicit casting and type conversion. The system may automatically add implicit casts when combining different data types in the same expression. In many cases, while the details related to this are not important, they can affect the query results of a query. When necessary, an explicit cast can be used to override the automatic cast added by SQream DB.

For example, the ANSI standard defines a ``SUM()`` aggregation over an ``INT`` column as an ``INT``. However, when dealing with large amounts of data this could cause an overflow. 

You can rectify this by casting the value to a larger data type, as shown below:

.. code-block:: postgres

   SUM(some_int_column :: BIGINT)

SQream supports the following three data conversion types:

* ``CAST(<value> TO <data type>)``, to convert a value from one type to another. For example, ``CAST('1997-01-01' TO DATE)``, ``CAST(3.45 TO SMALLINT)``, ``CAST(some_column TO TEXT)``.

   ::
  
* ``<value> :: <data type>``, a shorthand for the ``CAST`` syntax. For example, ``'1997-01-01' :: DATE``, ``3.45 :: SMALLINT``, ``(3+5) :: BIGINT``.

   ::
  
* See the :ref:`SQL functions reference <sql_functions>` for additional functions that convert from a specific value which is not an SQL type, such as :ref:`from_unixts`, etc.

.. note:: SQream interprets integer constants exceeding the maximum bigint value as float constants, which may cause precision loss.