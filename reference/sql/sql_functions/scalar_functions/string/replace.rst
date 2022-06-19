.. _replace:

**************************
REPLACE
**************************

Replaces all occurrences of a specified string value with another string value.

Syntax
==========

.. code-block:: postgres

   REPLACE( expr, source_expr, replacement_expr )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - String expression
   * - ``source_expr``
     - String expression to be replaced
   * - ``replacement_expr``
     - String expression containing the replacement

Returns
============

Returns the same type as the argument supplied.

Notes
=======

* In ``TEXT`` strings, the ``source_expr`` and ``replacement_expr`` must be the same **byte length**. See :ref:`octet_length`.

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

Replacing single characters
--------------------------------

.. code-block:: psql

   t=> SELECT REPLACE('What is all of this about?', 'u', 'o');
   replace                   
   --------------------------
   What is all of this aboot?


Replacing words
----------------------------

.. code-block:: psql

   t=> SELECT REPLACE(line, 'the', 'þe') FROM jabberwocky;
   replace                                        
   -----------------------------------------------
   'Twas brillig, and þe slithy toves             
         Did gyre and gimble in þe wabe:          
   All mimsy were þe borogoves,                   
         And þe mome raths outgrabe.              
   "Beware þe Jabberwock, my son!                 
         The jaws that bite, þe claws that catch! 
   Beware þe Jubjub bird, and shun                
         The frumious Bandersnatch!"              
