.. _regexp_substr:

**************************
REGEXP_SUBSTR
**************************

Returns the occurence of a regex match.


See also: :ref:`regexp_instr`, :ref:`regexp_count`.

Syntax
==========

.. code-block:: postgres

   REGEXP_SUBSTR( string_expr, string_test_expr [ , start_index [ , occurence ] ] ) --> INT

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
     - Setes the position within the string to return. Using 0, the function returns the string position of the first character of the substring that matches the pattern. Defaults to 0

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
     - Match zero or more instances of the sequence ``abc``, treating the expression within the parentheses as a single unit

   * - ``{m}``
     - Match the preceding pattern exactly ``m`` times

   * - ``{m,n}``
     - Match the preceding pattern at least ``m`` times but no more than ``n`` times

   * - ``[...]``
     - Match any sing character from the list within the parentheses
	 
   * - ``|``
     - ``OR`` clause

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

Returns the same type as the argument supplied, or Integer start position of a regex match, or an empty string (``''``) if no match was found.

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

Find players with 'o' in their name
-----------------------------------------------

.. code-block:: psql
   
   nba=> SELECT "Name", REGEXP_SUBSTR("Name", '([a-zA-Z]+o[a-zA-Z]+)+') FROM nba ORDER BY 2 DESC LIMIT 10;
   Name               | regexp_substr
   -------------------+--------------
   James Young        | Young        
   Thaddeus Young     | Young        
   Nick Young         | Young        
   Metta World Peace  | World        
   Christian Wood     | Wood         
   Justise Winslow    | Winslow      
   Wilson Chandler    | Wilson       
   C.J. Wilcox        | Wilcox       
   Shayne Whittington | Whittington  
   Russell Westbrook  | Westbrook    

Using the ``return_position`` argument
----------------------------------------

Get the last name (or middle name) for players with 'o' in their first and last name.
We set ``start_index`` to ``1`` (the default)

.. code-block:: psql
   
   nba=> SELECT "Name", REGEXP_SUBSTR("Name", '([a-zA-Z]+o[a-zA-Z]+)+', 1, 2) FROM nba ORDER BY 2 DESC LIMIT 10;
   Name               | regexp_substr
   -------------------+--------------
   Joe Young          | Young        
   Tony Wroten        | Wroten       
   Noah Vonleh        | Vonleh       
   Karl-Anthony Towns | Towns        
   Anthony Tolliver   | Tolliver     
   Hollis Thompson    | Thompson     
   Jason Thompson     | Thompson     
   Donald Sloan       | Sloan        
   Jonathon Simmons   | Simmons      
   Ramon Sessions     | Sessions     

