.. _converting_and_casting_types:

*********************
Casts and Conversions
*********************

BLUE supports explicit and implicit casting and type conversion. The system may automatically add implicit casts when combining different data types in the same expression. In many cases, while the details related to this are not important, they can affect the results of a query. When necessary, an explicit cast can be used to override the automatic cast added by BLUE.

For example, the ANSI standard defines a ``SUM()`` aggregation over an ``INT`` column as an ``INT``. However, when dealing with large amounts of data this could cause an overflow. 

You can rectify this by casting the value to a larger data type, as shown below:

.. code-block:: sql

   SUM(some_int_column :: BIGINT)

Conversion Methods
==================

BLUE supports the following data conversion methods:

* ``CAST(<value> AS <data type>)``, to convert a value from one type to another. 

  For example: 
  
  .. code-block:: postgres
	
	CAST('1997-01-01' AS DATE)
	CAST(3.45 AS SMALLINT)
	CAST(some_column AS TEXT)
  
* ``<value> :: <data type>``, a shorthand for the ``CAST`` syntax. 

  For example: 
  
  .. code-block:: postgres
  
	'1997-01-01' :: DATE 
	3.45 :: SMALLINT 
	(3+5) :: BIGINT
  
* See the :ref:`SQL functions reference <sql_functions>` for additional functions that convert from a specific value which is not an SQL type, such as :ref:`from_unixts`, etc.

.. _supported_casts_table:

Supported Casts
===============

The listed table of supported casts also applies to the :ref:`Array <sql_data_type_array>` data type. 
For instance, you can cast a NUMERIC[] array to a TEXT[] array.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - **TO/FROM**
     - **BOOL**
     - **TINYINT**/**SMALLINT**/**INT**/**BIGINT**	
     - **REAL/FLOAT**
     - **NUMERIC**
     - **DATE**/**DATETIME**
     - **VARCHAR**/**TEXT**
   * - **BOOL**
     - N/A
     - |:white_check_mark:|
     - |:no_entry:|
     - |:no_entry:|
     - |:no_entry:|
     - |:white_check_mark:|
   * - **TINYINT**/**SMALLINT**/**INT**/**BIGINT**
     - |:white_check_mark:|
     - N/A
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:no_entry:|
     - |:white_check_mark:|
   * - **REAL/FLOAT**
     - |:no_entry:|
     - |:white_check_mark:|
     - N/A
     - |:white_check_mark:|
     - |:no_entry:|
     - |:white_check_mark:|
   * - **NUMERIC**
     - |:no_entry:|
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:no_entry:|
     - |:white_check_mark:|
   * - **DATE**/**DATETIME**
     - |:no_entry:|
     - |:no_entry:|
     - |:no_entry:|
     - |:no_entry:|
     - N/A
     - |:white_check_mark:|
   * - **VARCHAR**/**TEXT**
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
     - N/A
	 
Value Dependent Conversions
---------------------------

Conversions between certain data types may be value-dependent, as the outcome can vary based on the specific values being converted and their compatibility with the target data type's range or precision.

For example:

.. code-block:: postgres

	CREATE OR REPLACE TABLE t(xint INT, xtext TEXT);
	INSERT INTO t VALUES(1234567, 'abc');

	-- yields cast overflow:
	SELECT xint::TINYINT FROM t;

	-- yields Unsupported conversion attempt from string to number - not all strings are numbers:
	SELECT xtext::INT FROM t;
	
	
	CREATE OR REPLACE TABLE t(xint INT, xtext TEXT);
	INSERT INTO t VALUES(12, '12');

	-- yields 12 in both cases:
	SELECT xint::TINYINT FROM t;
	
	SELECT xtext::INT FROM t;