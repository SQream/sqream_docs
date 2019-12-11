.. _octet_length:

**************************
OCTET_LENGTH
**************************

Calculates the number of bytes in a string.

.. note::
   
   * This function is supported on ``NVARCHAR`` strings only.
   
   * To get the length in characters, see :ref:`char_length`.
   
   * For ``VARCHAR`` strings, the octet length is the number of characters. Use :ref:`len` instead.

Syntax
==========


.. code-block:: postgres

   OCTET_LEN( nvarchar_expr ) --> INT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``nvarchar_expr``
     - ``NVARCHAR`` expression

Returns
============

Returns an integer containing the number of bytes in the string.

Notes
=======

* To get the length in characters, see :ref:`char_length`

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres
   
   CREATE TABLE alphabets(line NVARCHAR(50));
   
   INSERT INTO alphabets VALUES 
      ('abcdefghijklmnopqrstuvwxyz'), ('กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯ')
      , ('אבגדהוזחטיכלמנסעפצקרשת');

Length in characters and bytes of strings
--------------------------------------------------

ASCII characters take up 1 byte per character, while Thai takes up 3 bytes and Hebrew takes up 2 bytes.

.. code-block:: psql

   t=> SELECT LEN(line), CHAR_LENGTH(line), OCTET_LENGTH(line) FROM alphabets;
   len | char_length | octet_length
   ----+-------------+-------------
    26 |          26 |           26
    47 |          47 |          141
    22 |          22 |           44



