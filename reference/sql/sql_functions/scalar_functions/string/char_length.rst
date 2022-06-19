.. _char_length:

**************************
CHAR_LENGTH
**************************

Calculates the number of characters in a string.

.. note::
   
   * This function is supported on ``TEXT`` only.
   
   * To get the length in bytes, see :ref:`octet_length`.
   
   * For ``TEXT`` strings, the octet length is the number of characters. Use :ref:`len` instead.

Syntax
==========

.. code-block:: postgres

   CHAR_LEN( text_expr ) --> INT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``text_expr``
     - ``TEXT`` expression

Returns
============

Returns an integer containing the number of characters in the string.

Notes
=======

* To get the length in bytes, see :ref:`octet_length`

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres
   
   CREATE TABLE alphabets(line TEXT(50));
   
   INSERT INTO alphabets VALUES 
      ('abcdefghijklmnopqrstuvwxyz'), ('กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯ')
      , ('אבגדהוזחטיכלמנסעפצקרשת');

Length in characters and bytes of strings
--------------------------------------------------

ASCII characters take up 1 byte per character, while Thai takes up 3 bytes and Hebrew takes up 2 bytes.

Unlike :ref:`len`, ``CHAR_LENGTH`` preserves the trailing whitespaces.

.. code-block:: psql

   t=> SELECT LEN(line), CHAR_LENGTH(line), OCTET_LENGTH(line) FROM alphabets;
   len | char_length | octet_length
   ----+-------------+-------------
    26 |          26 |           26
    47 |          47 |          141
    22 |          22 |           44



