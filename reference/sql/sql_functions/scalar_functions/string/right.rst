.. _right:

**************************
RIGHT
**************************

Returns the right part of a character string with the specified number of characters.

See also :ref:`left`.

Syntax
==========

.. code-block:: postgres

   RIGHT( expr , character_count )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - String expression
   * - ``character_count``
     - A positive integer that specifies how many characters to return.

Returns
============

Returns the same type as the argument supplied.

Notes
=======

* This function works on ``TEXT`` strings only.

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE jabberwocky(line TEXT(50));

   INSERT INTO jabberwocky VALUES 
      ('''Twas brillig, and the slithy toves '), ('      Did gyre and gimble in the wabe: ')
      ,('All mimsy were the borogoves, '), ('      And the mome raths outgrabe. ')
      ,('"Beware the Jabberwock, my son! '), ('      The jaws that bite, the claws that catch! ')
      ,('Beware the Jubjub bird, and shun '), ('      The frumious Bandersnatch!" ');


Using ``RIGHT``
-------------------------------

.. code-block:: psql

   t=> SELECT LEFT(line, 10), RIGHT(line, 10) FROM jabberwocky;
   left       | right     
   -----------+-----------
   'Twas bril | thy toves 
         Did  | the wabe: 
   All mimsy  | orogoves, 
         And  | outgrabe. 
   "Beware th | , my son! 
         The  | at catch! 
   Beware the |  and shun 
         The  | rsnatch!" 
