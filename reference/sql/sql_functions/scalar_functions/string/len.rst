.. _len:

**************************
LEN
**************************

Calculates the number of characters in a string.

.. note::
   
   * This function is provided for SQL Server compatability.
   
   * For UTF-8 encoded ``TEXT`` strings, multi-byte characters are counted as a single character. To get the length in bytes, see :ref:`octet_length`. To get the length in characters, see :ref:`char_length`.

Syntax
==========


.. code-block:: postgres

   LEN( expr ) --> INT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - String expression

Returns
============

Returns an integer containing the number of characters in the string.

Notes
=======

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres
   
   CREATE TABLE jabberwocky(line TEXT);
   
   INSERT INTO jabberwocky VALUES 
      ($$'Twas brillig, and the slithy toves$$), ('      Did gyre and gimble in the wabe:')
      ,('All mimsy were the borogoves,'), ('      And the mome raths outgrabe.')
      ,('"Beware the Jabberwock, my son!'), ('      The jaws that bite, the claws that catch!')
      ,('Beware the Jubjub bird, and shun'), ('      The frumious Bandersnatch!"');

   CREATE TABLE alphabets(line TEXT(50));
   
   INSERT INTO alphabets VALUES 
      ('abcdefghijklmnopqrstuvwxyz'), ('กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯ')
      , ('אבגדהוזחטיכלמנסעפצקרשת');

Length in characters and bytes of strings
--------------------------------------------------

ASCII characters take up 1 byte per character, while Thai takes up 3 bytes and Hebrew takes up 2 bytes.

.. code-block:: psql

   t=> SELECT LEN(line), OCTET_LENGTH(line) FROM alphabets;
   len | octet_length
   ----+-------------
    26 |           26
    47 |          141
    22 |           44


Length of an ASCII string
----------------------------

.. note:: SQream DB does not count trailing spaces, but does keep leading spaces.

.. code-block:: psql

   t=> SELECT LEN('Trailing spaces are not counted            ');
   len
   ---
    31
   
   t=> SELECT LEN('            Leading spaces are counted');
   len
   ---
    38



Absolute value on integer and floating point
-----------------------------------------------

.. code-block:: psql

   
   numbers=> SELECT LEN(line) FROM jabberwocky;
   len
   ---
    35
    38
    29
    34
    31
    47
    32
    33


