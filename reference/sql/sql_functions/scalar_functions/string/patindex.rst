.. _patindex:

**************************
PATINDEX
**************************
 
Returns the starting position of a pattern inside a string.

See also :ref:`charindex`, :ref:`regexp_instr`.

``PATINDEX`` works like :ref:`like`, so the standard wildcards are supported. You do not have to enclose the pattern between percents. 

.. note:: This function is provided for SQL Server compatability.

Syntax
==========

.. code-block:: postgres

   PATINDEX ( string_test_expr , string_expr ) --> INT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``string_test_expr``
     - Pattern to find
   * - ``string_expr``
     - String to search within


Test patterns
==============

.. list-table::
   :widths: auto
   :header-rows: 1
   
   
   * - Pattern
     - Description
   * - ``%``
     - match zero or more characters
   * - ``_``
     - match exactly one character
   * - ``[A-Z]``
     - match any character between ``A`` and ``Z`` inclusive. The ``-`` character between two other characters forms a range that matches all characters from the first character to the second. For example, [A-Z] matches all ASCII capital letters.
   * - ``[^A-Z]``
     - match any character *not* between ``A`` and ``Z``
   * - ``[abcde]``
     - match any one of ``a`` ``b`` ``c`` ``d`` and ``e``
   * - ``[^abcde]``
     - match any character that is *not* one of ``a`` ``b`` ``c`` ``d`` or ``e``
   * - ``[abcC-F]``
     - match ``a`` ``b`` ``c`` or any character between ``C`` and ``F``

Returns
============

Integer start position of a match, or 0 if no match was found.

Notes
=======

* If the value is NULL, the result is NULL.

* PATINDEX works on ``VARCHAR`` text types only.

* PATINDEX does not work on all literal values - only on column values.
   
   (i.e. ``PATINDEX('%mimsy%', 'All mimsy were the borogoves')`` will not work, but ``PATINDEX('%mimsy%', line)`` will)



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


Simple patterns
-----------------------------------------

.. code-block:: psql

   t=> SELECT line, PATINDEX('%mimsy%', line) as "Position of mimsy" FROM jabberwocky;
   line                                             | Position of mimsy
   -------------------------------------------------+------------------
   'Twas brillig, and the slithy toves              |                 0
         Did gyre and gimble in the wabe:           |                 0
   All mimsy were the borogoves,                    |                 5
         And the mome raths outgrabe.               |                 0
   "Beware the Jabberwock, my son!                  |                 0
         The jaws that bite, the claws that catch!  |                 0
   Beware the Jubjub bird, and shun                 |                 0
         The frumious Bandersnatch!"                |                 0


Complex wildcards expressions
--------------------------------

The following example uses the ``^`` negation operator to find the position of a character that is neither a number, a letter, or a space.

.. code-block:: psql

   t=> SELECT PATINDEX('%[^ 0-9A-z]%', line), line FROM jabberwocky;
   
   patindex | line                                           
   ---------+------------------------------------------------
          1 | 'Twas brillig, and the slithy toves            
         38 |       Did gyre and gimble in the wabe:         
         29 | All mimsy were the borogoves,                  
         34 |       And the mome raths outgrabe.             
          1 | "Beware the Jabberwock, my son!                
         25 |       The jaws that bite, the claws that catch!
         23 | Beware the Jubjub bird, and shun               
         32 |       The frumious Bandersnatch!"              
