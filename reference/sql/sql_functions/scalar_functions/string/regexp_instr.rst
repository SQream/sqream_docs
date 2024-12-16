.. _regexp_instr:

**************************
REGEXP_INSTR
**************************

The ``REGEXP_INSTR`` function returns the start position of a regex match and searches a string for a POSIX-style regular expression. This function returns the position within the string where the match was located.

See also: :ref:`regexp_count`, :ref:`regexp_substr`.

Syntax
==========

.. code-block:: postgres

   REGEXP_INSTR( string_expr, string_test_expr [, start_index [, occurence [, return_position ]] ) --> INT

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
   * - ``occurence``
     - Which occurence to search for. Defaults to 1
   * - ``return_position``
     - Specifies the location within the string to return. Using 0, the function returns the string position of the first character of the substring that matches the pattern. 
       A value greater than 0 returns will return the position of the first character following the end of the pattern. Defaults to 0

Supported RegEx Patterns
========================

.. list-table::
   :widths: auto
   :header-rows: 1
   
   
   * - Pattern
     - Description
   
   * - ``^``
     - Match the beginning of a string

   * - ``[^]``
     - Characters that do not match the speciifed string
	 
   * - ``$``
     - Match the end of a string

   * - ``.``
     - Match any character (including whitespace such as carriage return and newline)

   * - ``*``
     - Match the preceding pattern zero or more times

   * - ``+``
     - Match the preceding pattern at least once

   * - ``?``
     - Match the preceding pattern once at most (``0`` or ``1`` time)

   * - ``(abc)*``
     - Match zero or more instances of the sequence ``abc``

   * - ``{m}``
     - Match the preceding pattern exactly ``m`` times

   * - ``{m,n}``
     - Match the preceding pattern at least ``m`` times but no more than ``n`` times

   * - ``[...]``
     - Match any sing character from the list within the parentheses
	 
   * - ``|``
     - ``OR`` clause
	 
   * - ``(abc)*``
     - Treating the expression within the parentheses as a single unit

   * - ``\``
     - Treating the subsequent characters in the expression as ordinary characters rather than metacharacters
   
   * - ``\n``
     - Matching the nth (``1``-``9``) preceding subexpression grouped within parentheses
	 
   * - ``*?``
     - Occurs zero or more times
	 
   * - ``+?``
     - Occurs one or more times
	 
   * - ``??``
     - Occurs zero or one times

Returns
============

Integer start position of a regex match, or 0 if no match was found.

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
      "Name" text(40),
      "Team" text(40),
      "Number" tinyint,
      "Position" text(2),
      "Age" tinyint,
      "Height" text(4),
      "Weight" real,
      "College" text(40),
      "Salary" float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Find players with 'ow' in their name
-----------------------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name", REGEXP_INSTR("Name", 'ow') FROM nba WHERE REGEXP_COUNT("Name", 'ow')>0;
   Name               | regexp_instr
   -------------------+-------------
   Jae Crowder        |            7
   Markel Brown       |           10
   Langston Galloway  |           14
   Kyle Lowry         |            7
   Norman Powell      |            9
   Anthony Brown      |           11
   Cameron Bairstow   |           15
   Lorenzo Brown      |           11
   Dirk Nowitzki      |            7
   Dwight Powell      |            9
   Dwight Howard      |            9
   Justise Winslow    |           14
   Karl-Anthony Towns |           15
   Anthony Morrow     |           13



Using the ``return_position`` argument
----------------------------------------

Get the second occurence of the letter 'k' in a player's name.
We set ``start_index`` to ``1`` (the default)

.. code-block:: psql
   
   nba=> SELECT "Name", REGEXP_INSTR("Name", 'k', 1, 2)  FROM nba WHERE REGEXP_INSTR("Name", 'k', 1, 2)>0;
   Name               | regexp_instr
   -------------------+-------------
   Nik Stauskas       |           10
   Tarik Black        |           11
   Dirk Nowitzki      |           12
   Sam Dekker         |            8
   Kendrick Perkins   |           13
   Frank Kaminsky III |           13
   Nikola Jokic       |           10
   Nikola Pekovic     |           10
