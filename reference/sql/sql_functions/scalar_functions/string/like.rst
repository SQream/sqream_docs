.. _like:

**************************
LIKE
**************************

Tests if a string matches a given pattern.

``LIKE`` and :ref:`rlike` are similar. ``LIKE`` uses SQL patterns, whereas :ref:`rlike` uses POSIX regular expressions.

See also: :ref:`rlike`, :ref:`regexp_count`, :ref:`regexp_instr`, :ref:`regexp_substr`, :ref:`isprefixof`.

Syntax
==========

.. code-block:: postgres

   string_expr [ NOT ] LIKE string_test_expr

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

``TRUE`` if the test string matches the pattern, or ``FALSE`` otherwise.

Notes
=======

* The test pattern must be literal string. Column references or complex expressions are currently unsupported. If matching just the beginning of the string, use :ref:`isprefixof` which supports column references.

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

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" LIKE 'Portland%' LIMIT 5;
   Name            | Age | Salary  | Team                  
   ----------------+-----+---------+-----------------------
   Cliff Alexander |  20 |  525093 | Portland Trail Blazers
   Al-Farouq Aminu |  25 | 8042895 | Portland Trail Blazers
   Pat Connaughton |  23 |  625093 | Portland Trail Blazers
   Allen Crabbe    |  24 |  947276 | Portland Trail Blazers
   Ed Davis        |  27 | 6980802 | Portland Trail Blazers

.. tip::
   :ref:`isprefixof` is a more performant way to match the beginning of a string, especially
   This example can be written as 
   
   .. code-block:: postgres
   
      SELECT "Name","Age","Salary","Team" FROM nba WHERE ISPREFIXOF('Portland',"Team") LIMIT 5;

Negate with ``NOT``
----------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" NOT LIKE 'Portland%' LIMIT 5;
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
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Team" LIKE '%zz%' LIMIT 5;
   Name           | Age | Salary  | Team             
   ---------------+-----+---------+------------------
   Jordan Adams   |  21 | 1404600 | Memphis Grizzlies
   Tony Allen     |  34 | 5158539 | Memphis Grizzlies
   Chris Andersen |  37 | 5000000 | Memphis Grizzlies
   Matt Barnes    |  36 | 3542500 | Memphis Grizzlies
   Vince Carter   |  39 | 4088019 | Memphis Grizzlies

Find players with a middle name or suffix
---------------------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name","Age","Salary","Team" FROM nba WHERE "Name" LIKE '% % %';
   Name                     | Age | Salary  | Team                 
   -------------------------+-----+---------+----------------------
   James Michael McAdoo     |  23 |  845059 | Golden State Warriors
   Luc Richard Mbah a Moute |  29 |  947276 | Los Angeles Clippers 
   Larry Nance Jr.          |  23 | 1155600 | Los Angeles Lakers   
   Metta World Peace        |  36 |  947276 | Los Angeles Lakers   
   Glenn Robinson III       |  22 | 1100000 | Indiana Pacers       
   Johnny O'Bryant III      |  23 |  845059 | Milwaukee Bucks      
   Tim Hardaway Jr.         |  24 | 1304520 | Atlanta Hawks        
   Frank Kaminsky III       |  23 | 2612520 | Charlotte Hornets    
   Kelly Oubre Jr.          |  20 | 1920240 | Washington Wizards   
   Otto Porter Jr.          |  23 | 4662960 | Washington Wizards   