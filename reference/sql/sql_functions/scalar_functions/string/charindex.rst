.. _charindex:

**************************
CHARINDEX
**************************

Returns the starting position of a string inside another string.

See also :ref:`patindex`, :ref:`regexp_instr`.

Syntax
==========

.. code-block:: postgres

   CHARINDEX ( needle_string_expr , haystack_string_expr [ , start_location ] )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``needle_string_expr``
     - String to find
   * - ``haystack_string_expr``
     - String to search within
   * - ``start_location``
     - An integer at which the search starts. This value is optinoal and when not supplied, the search starts at the beggining of ``needle_string_expr``

Returns
============

Integer start position of a match, or 0 if no match was found.

Notes
=======

* If the value is NULL, the result is NULL.


Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE jabberwocky(line TEXT);

   INSERT INTO jabberwocky VALUES 
      ('''Twas brillig, and the slithy toves '), ('      Did gyre and gimble in the wabe: ')
      ,('All mimsy were the borogoves, '), ('      And the mome raths outgrabe. ')
      ,('"Beware the Jabberwock, my son! '), ('      The jaws that bite, the claws that catch! ')
      ,('Beware the Jubjub bird, and shun '), ('      The frumious Bandersnatch!" ');


Using ``CHARINDEX``
-----------------------------------------

.. code-block:: psql

   t=> SELECT line, CHARINDEX('the', line) FROM jabberwocky
   line                                            | charindex
   ------------------------------------------------+----------
   'Twas brillig, and the slithy toves             |        20
         Did gyre and gimble in the wabe:          |        30
   All mimsy were the borogoves,                   |        16
         And the mome raths outgrabe.              |        11
   "Beware the Jabberwock, my son!                 |         9
         The jaws that bite, the claws that catch! |        27
   Beware the Jubjub bird, and shun                |         8
         The frumious Bandersnatch!"               |         0
