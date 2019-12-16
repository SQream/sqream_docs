.. _charindex:

**************************
CHARINDEX
**************************

Returns the starting position of a string inside another string.

See also :ref:`patindex`, :ref:`regexp_instr`.

Syntax
==========

.. code-block:: postgres

   CHARINDEX ( needle_string_expr , haystack_string_expr ) --> INT

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

Returns
============

Integer start position of a match, or 0 if no match was found.

Notes
=======

   * This function is supported on ``VARCHAR`` strings only.

* If the value is NULL, the result is NULL.


Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE jabberwocky(line VARCHAR(50));

   INSERT INTO jabberwocky VALUES 
      ('''Twas brillig, and the slithy toves '), ('      Did gyre and gimble in the wabe: ')
      ,('All mimsy were the borogoves, '), ('      And the mome raths outgrabe. ')
      ,('"Beware the Jabberwock, my son! '), ('      The jaws that bite, the claws that catch! ')
      ,('Beware the Jubjub bird, and shun '), ('      The frumious Bandersnatch!" ');


Using ``CHARINDEX``
-----------------------------------------

.. code-block:: psql

   t=> SELECT line, PATINDEX('%J_b%', line) FROM jabberwocky;
   line                                      | patindex
   ------------------------------------------+---------
   'Twas brillig, and the slithy toves       |        0
   Did gyre and gimble in the wabe:          |        0
   All mimsy were the borogoves,             |        0
   And the mome raths outgrabe.              |        0
   "Beware the Jabberwock, my son!           |       13
   The jaws that bite, the claws that catch! |        0
   Beware the Jubjub bird, and shun          |       12
   The frumious Bandersnatch!"               |        0