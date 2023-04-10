.. _bitwise_not:

***************************
``~`` (bitwise NOT)
***************************

The bitwise NOT operator (``~``) is a unary operator used to invert the bits of a binary value. It converts each 0 to a 1 and each 1 to a 0, resulting in the ones' complement of the original value.

Syntax
==========

.. code-block:: postgres

   ~ expr --> integer

   expr ::= integer
   


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Integer expression

Returns
============

Returns an integer that is the bitwise ``NOT`` of the input and preserves the data type of the argument supplied.

Notes
=======

* If the value is ``NULL``, the result is ``NULL``.

Examples
===========

.. code-block:: psql

   master=> SELECT ~16, ~24;
   -17,-25
   
   master=> SELECT ~101, ~110;
   -102,-111
   
   master=> SELECT ~32, ~64;
   -33,-65


.. code-block:: psql


   master=> CREATE OR REPLACE TABLE t (xtinyInt tinyInt, xsmallInt smallInt, xint int, xbigInt bigInt);

   master=> INSERT INTO t VALUES (1,1,1,1);

   master=> SELECT ~xtinyInt, ~xsmallInt, ~xint, ~xbigInt from t;
   
   ?column? | ?column?0 | ?column?1 | ?column?2 |
   ---------+-----------+-----------+-----------+
        254 |        -2 |        -2 |        -2 |


