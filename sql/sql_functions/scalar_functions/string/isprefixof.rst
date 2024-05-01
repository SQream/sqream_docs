.. _isprefixof:

**************************
ISPREFIXOF
**************************

Checks if one string is a prefix of the other.

This is a more peformant way to write ``y LIKE (x || '%')``

See also: :ref:`like`.

Syntax
==========

.. code-block:: postgres

   ISPREFIXOF(needle_string_expr , haystack_string_expr) --> BOOL

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``needle_string_expr``
     - String to locate
   * - ``haystack_string_expr``
     - String to search within

Returns
============

``TRUE`` if ``needle_string_expr`` is a prefix of ``haystack_string_expr``, or ``FALSE`` otherwise.

Notes
=======

* This function is supported on ``TEXT`` strings only.

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


Filtering using ``ISPREFIXOF``
-----------------------------------------

.. code-block:: psql

   t=> SELECT line FROM jabberwocky WHERE ISPREFIXOF('And',TRIM(line));
   line                               
   -----------------------------------
      And the mome raths outgrabe. 

.. tip:: Use :ref:`trim` to avoid leading and trailing whitespace issues
