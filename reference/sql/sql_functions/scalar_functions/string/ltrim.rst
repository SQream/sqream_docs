.. _ltrim:

**************************
LTRIM
**************************

Trims leading whitespace from a string.

See also :ref:`trim`, :ref:`rtrim`.

Syntax
==========


.. code-block:: postgres

   LTRIM( expr )

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

Returns the same type as the argument supplied.

Notes
=======

* This function is equivalent to the ANSI form ``TRIM( LEADING FROM expr )``

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE jabberwocky(line TEXT(50));

   INSERT INTO jabberwocky VALUES 
      ('''Twas brillig, and the slithy toves'), ('      Did gyre and gimble in the wabe:')
      ,('All mimsy were the borogoves,'), ('      And the mome raths outgrabe.')
      ,('"Beware the Jabberwock, my son!'), ('      The jaws that bite, the claws that catch!')
      ,('Beware the Jubjub bird, and shun'), ('      The frumious Bandersnatch!"');


Trimming a literal value
-------------------------------

.. code-block:: psql

   t=> SELECT LTRIM('            SQream DB');
   ltrim    
   ---------
   SQream DB


Trimming a column of values
--------------------------------------

In this example we use :ref:`concat` to show the leading spaces.

.. code-block:: psql

   
   t=> SELECT ('Line: ' || line) as untrimmed, ('Line: ' || LTRIM(line)) as trimmed FROM jabberwocky;
   untrimmed                                             | trimmed                                        
   ------------------------------------------------------+------------------------------------------------
   Line: 'Twas brillig, and the slithy toves             | Line: 'Twas brillig, and the slithy toves      
   Line:       Did gyre and gimble in the wabe:          | Line: Did gyre and gimble in the wabe:         
   Line: All mimsy were the borogoves,                   | Line: All mimsy were the borogoves,            
   Line:       And the mome raths outgrabe.              | Line: And the mome raths outgrabe.             
   Line: "Beware the Jabberwock, my son!                 | Line: "Beware the Jabberwock, my son!          
   Line:       The jaws that bite, the claws that catch! | Line: The jaws that bite, the claws that catch!
   Line: Beware the Jubjub bird, and shun                | Line: Beware the Jubjub bird, and shun         
   Line:       The frumious Bandersnatch!"               | Line: The frumious Bandersnatch!"              


