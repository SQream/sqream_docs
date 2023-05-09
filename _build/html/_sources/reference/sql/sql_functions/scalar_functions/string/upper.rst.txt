.. _upper:

**************************
UPPER
**************************

Converts characters in a string to upper case

See also: :ref:`lower`

Syntax
==========


.. code-block:: postgres

   UPPER( expr )

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

   CREATE TABLE jabberwocky(line TEXT(50));

   INSERT INTO jabberwocky VALUES 
      ('''Twas brillig, and the slithy toves'), ('      Did gyre and gimble in the wabe:')
      ,('All mimsy were the borogoves,'), ('      And the mome raths outgrabe.')
      ,('"Beware the Jabberwock, my son!'), ('      The jaws that bite, the claws that catch!')
      ,('Beware the Jubjub bird, and shun'), ('      The frumious Bandersnatch!"');


Upper-casing a literal value
-------------------------------

.. code-block:: psql

   t=> SELECT UPPER('SQream DB');
   SQREAM DB

Upper-casing a column of values
--------------------------------------

.. code-block:: psql

   
   t=> SELECT UPPER(line) FROM jabberwocky;
   upper                                    
   -----------------------------------------
   'TWAS BRILLIG, AND THE SLITHY TOVES      
   DID GYRE AND GIMBLE IN THE WABE:         
   ALL MIMSY WERE THE BOROGOVES,            
   AND THE MOME RATHS OUTGRABE.             
   "BEWARE THE JABBERWOCK, MY SON!          
   THE JAWS THAT BITE, THE CLAWS THAT CATCH!
   BEWARE THE JUBJUB BIRD, AND SHUN         
   THE FRUMIOUS BANDERSNATCH!"              

