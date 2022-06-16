.. _regexp_count:

**************************
REGEXP_COUNT
**************************

Counts the number of occurences that a string matches a given regular expression pattern.

See also: :ref:`regexp_instr`, :ref:`regexp_substr`.

Syntax
==========

.. code-block:: postgres

   REGEXP_COUNT( string_expr, string_test_expr [, start_index ] ) --> INT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``string_expr``
     - String to test
   * - ``string_test_expr``
     - Test pattern
   * - ``start_index``
     - The character index offset to start counting from. Defaults to 1

Test patterns
==============

.. list-table::
   :widths: auto
   :header-rows: 1
   
   
   * - Pattern
     - Description
   * - ``^``
     - Match the beginning of a string

   * - ``$``
     - Match the end of a string

   * - ``.``
     - Match any character (including whitespace such as carriage return and newline)

   * - ``*``
     - Match the preceding pattern zero or more times

   * - ``+``
     - Match the preceding pattern at least once

   * - ``?``
     - Match the preceding pattern once at most

   * - ``de|abc``
     - Match either ``de`` or ``abc``

   * - ``(abc)*``
     - Match zero or more instances of the sequence ``abc``

   * - ``{2}``
     - Match the preceding pattern exactly two times

   * - ``{2,4}``
     - Match the preceding pattern between two and four times

   * - ``[a-dX]``, ``[^a-dX]``
     -
         Matches any character that is (or is not when negated with ``^``) either ``a``, ``b``, ``c``, ``d``, or ``X``.
         The ``-`` character between two other characters forms a range that matches all characters from the first character to the second. For example, [0-9] matches any decimal digit. 
         To include a literal ``]`` character, it must immediately follow the opening bracket [. To include a literal - character, it must be written first or last.
         Any character that does not have a defined special meaning inside a [] pair matches only itself.

Returns
============

Integer result of the number of times that a pattern occurs in a string.

Notes
=======

* The test pattern must be literal string. Column references or complex expressions are currently unsupported.

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      "Name" texT,
      "Team" text,
      "Number" tinyint,
      "Position" text
      "Age" tinyint,
      "Height" text,
      "Weight" real,
      "College" text,
      "Salary" float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Find players with at least 3 names (2 spaces)
-----------------------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+')>1;
   Name                    
   ------------------------ 
   James Michael McAdoo    
   Luc Richard Mbah a Moute
   Larry Nance Jr.         
   Metta World Peace       
   Glenn Robinson III      
   Johnny O'Bryant III     
   Tim Hardaway Jr.        
   Frank Kaminsky III      
   Kelly Oubre Jr.         
   Otto Porter Jr.         


Using the offset index
----------------------------------

Start finding spaces that appear 8 characters in

.. code-block:: psql
   
   nba=> SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1;
   Name                    
   ------------------------
   Luc Richard Mbah a Moute
