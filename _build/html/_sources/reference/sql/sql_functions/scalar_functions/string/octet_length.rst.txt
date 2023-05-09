.. _octet_length:

**************************
OCTET_LENGTH
**************************

Calculates the number of bytes in a string.

.. note::   
 
   * To get the length in bytes, see :ref:`octet_length`.
   
Syntax
==========
The following is the correct syntax for the ``OCTET_LENGTH`` function:

.. code-block:: postgres

   OCTET_LEN( text_expr ) --> INT

Arguments
============
The following table describes the ``OCTET_LENGTH`` arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``text_expr``
     - ``TEXT`` expression

Returns
============
The ``OCTET_LENGTH`` function returns an integer containing the number of bytes in the string.

Notes
=======
The following notes are applicable to the ``OCTET_LENGTH`` function:

* To get the length in characters, see :ref:`char_length`

* If the value is NULL, the result is NULL.

Length in Characters and Bytes of Strings
===========
The **Length in characters and bytes of strings** example is based on the following table and contents:

.. code-block:: postgres
   
   CREATE TABLE alphabets(line TEXT(50));
   
   INSERT INTO alphabets VALUES 
      ('abcdefghijklmnopqrstuvwxyz'), ('กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯ')
      , ('אבגדהוזחטיכלמנסעפצקרשת');

ASCII characters take up 1 byte per character, while Thai takes up 3 bytes and Hebrew takes up 2 bytes, as shown below:

.. code-block:: psql

   t=> SELECT LEN(line), CHAR_LENGTH(line), OCTET_LENGTH(line) FROM alphabets;
   len | char_length | octet_length
   ----+-------------+-------------
    26 |          26 |           26
    47 |          47 |          141
    22 |          22 |           44
