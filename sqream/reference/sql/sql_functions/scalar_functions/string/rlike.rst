.. _rlike:

**************************
RLIKE
**************************

Tests if a string matches a given regular expression pattern.

``RLIKE`` and :ref:`like` are similar, but ``RLIKE`` uses POSIX regular expressions instead of the SQL patterns.

See also: :ref:`like`, :ref:`regexp_count`, :ref:`regexp_instr`, :ref:`regexp_substr`.

Syntax
==========

.. code-block:: postgres

   string_expr [ NOT ] RLIKE string_test_expr

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

``TRUE`` if the test string matches the pattern, or ``FALSE`` otherwise.

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
      Name varchar(40),
      Team varchar(40),
      Number tinyint,
      Position varchar(2),
      Age tinyint,
      Height varchar(4),
      Weight real,
      College varchar(40),
      Salary float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Match the beginning of a string
----------------------------------

This form is equivalent to ``... LIKE "Portland%"``

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" RLIKE '^(Portland)+' LIMIT 5;
   Name            | Age | Salary  | Team                  
   ----------------+-----+---------+-----------------------
   Cliff Alexander |  20 |  525093 | Portland Trail Blazers
   Al-Farouq Aminu |  25 | 8042895 | Portland Trail Blazers
   Pat Connaughton |  23 |  625093 | Portland Trail Blazers
   Allen Crabbe    |  24 |  947276 | Portland Trail Blazers
   Ed Davis        |  27 | 6980802 | Portland Trail Blazers


Negate with ``NOT``
----------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" NOT RLIKE '^(Portland)+' LIMIT 5;
   Name          | Age | Salary  | Team          
   --------------+-----+---------+---------------
   Avery Bradley |  25 | 7730337 | Boston Celtics
   Jae Crowder   |  25 | 6796117 | Boston Celtics
   John Holland  |  27 |         | Boston Celtics
   R.J. Hunter   |  22 | 1148640 | Boston Celtics
   Jonas Jerebko |  29 | 5000000 | Boston Celtics


Match the middle of a string
------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" RLIKE '(zz)' LIMIT 5;
   Name           | Age | Salary  | Team             
   ---------------+-----+---------+------------------
   Jordan Adams   |  21 | 1404600 | Memphis Grizzlies
   Tony Allen     |  34 | 5158539 | Memphis Grizzlies
   Chris Andersen |  37 | 5000000 | Memphis Grizzlies
   Matt Barnes    |  36 | 3542500 | Memphis Grizzlies
   Vince Carter   |  39 | 4088019 | Memphis Grizzlies

Find players with a Roman numeral suffix
---------------------------------------------

Use ``$`` to match only the end of the string

.. code-block:: psql

   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Name" RLIKE '[XCLVMI]$';
   Name                | Age | Salary  | Team             
   --------------------+-----+---------+------------------
   Glenn Robinson III  |  22 | 1100000 | Indiana Pacers   
   Johnny O'Bryant III |  23 |  845059 | Milwaukee Bucks  
   Frank Kaminsky III  |  23 | 2612520 | Charlotte Hornets


Find players with just one middle name
----------------------------------------

.. code-block:: psql

   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Name" RLIKE '^[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+$';
   Name                 | Age | Salary  | Team                 
   ---------------------+-----+---------+----------------------
   James Michael McAdoo |  23 |  845059 | Golden State Warriors
   Metta World Peace    |  36 |  947276 | Los Angeles Lakers   
   Glenn Robinson III   |  22 | 1100000 | Indiana Pacers       
   Frank Kaminsky III   |  23 | 2612520 | Charlotte Hornets    
