.. _lower:

**************************
LOWER
**************************

Converts characters in a string to lower case

Syntax
==========


.. code-block:: postgres

   LOWER( expr )

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

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE jabberwocky(line VARCHAR(50));

   INSERT INTO jabberwocky VALUES 
      (''Twas brillig, and the slithy toves'), ('      Did gyre and gimble in the wabe:')
      ,('All mimsy were the borogoves,'), ('      And the mome raths outgrabe.')
      ,('"Beware the Jabberwock, my son!'), ('      The jaws that bite, the claws that catch!')
      ,('Beware the Jubjub bird, and shun'), ('      The frumious Bandersnatch!"');


Lower-casing a literal value
-------------------------------

.. code-block:: psql

   t=> SELECT LOWER('SQream DB');
   sqream db

Lower-casing a column of values
--------------------------------------

.. code-block:: psql

   
   t=> SELECT LOWER(line) FROM jabberwocky;
   lower                                    
   -----------------------------------------
   'twas brillig, and the slithy toves      
   did gyre and gimble in the wabe:         
   all mimsy were the borogoves,            
   and the mome raths outgrabe.             
   "beware the jabberwock, my son!          
   the jaws that bite, the claws that catch!
   beware the jubjub bird, and shun         
   the frumious bandersnatch!"              
