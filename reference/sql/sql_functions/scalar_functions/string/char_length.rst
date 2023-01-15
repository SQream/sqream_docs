.. _char_length:

**************************
CHARACTER_LENGTH / CHAR_LENGTH
**************************

Calculates the number of characters in a string.

.. note::
     
   * To get the length in bytes, see :ref:`octet_length`.
   
Syntax
==========

.. code-block:: postgres

   CHAR_LEN( text_expr ) --> INT
   CHARACTER_LEN( text_expr ) --> INT

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

Return an integer containing the number of characters in the string.

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

Unlike :ref:`len`, ``CHARACTER_LENGTH`` and ``CHAR_LENGTH`` preserve the trailing white spaces.

.. code-block:: psql

   t=> SELECT LEN(line), CHAR_LENGTH(line), OCTET_LENGTH(line) FROM alphabets;
   len | char_length | octet_length
   ----+-------------+-------------
    26 |          26 |           26
    47 |          47 |          141
    22 |          22 |           44



