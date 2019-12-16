.. _reverse:

**************************
REVERSE
**************************

Returns a reversed order of a character string.


Syntax
==========

.. code-block:: postgres

   REVERSE( expr )

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

.. * This function works on ``NVARCHAR`` strings only.

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE jabberwocky(line NVARCHAR(50));

   INSERT INTO jabberwocky VALUES 
      ('''Twas brillig, and the slithy toves '), ('      Did gyre and gimble in the wabe: ')
      ,('All mimsy were the borogoves, '), ('      And the mome raths outgrabe. ')
      ,('"Beware the Jabberwock, my son! '), ('      The jaws that bite, the claws that catch! ')
      ,('Beware the Jubjub bird, and shun '), ('      The frumious Bandersnatch!" ');


Using ``REVERSE``
-------------------------------

.. code-block:: psql

   t=> SELECT line, REVERSE(line) FROM jabberwocky;
   line                                             | reverse                                         
   -------------------------------------------------+-------------------------------------------------
   'Twas brillig, and the slithy toves              |  sevot yhtils eht dna ,gillirb sawT'            
         Did gyre and gimble in the wabe:           |  :ebaw eht ni elbmig dna eryg diD               
   All mimsy were the borogoves,                    |  ,sevogorob eht erew ysmim llA                  
         And the mome raths outgrabe.               |  .ebargtuo shtar emom eht dnA                   
   "Beware the Jabberwock, my son!                  |  !nos ym ,kcowrebbaJ eht eraweB"                
         The jaws that bite, the claws that catch!  |  !hctac taht swalc eht ,etib taht swaj ehT      
   Beware the Jubjub bird, and shun                 |  nuhs dna ,drib bujbuJ eht eraweB               
         The frumious Bandersnatch!"                |  "!hctansrednaB suoimurf ehT                    
