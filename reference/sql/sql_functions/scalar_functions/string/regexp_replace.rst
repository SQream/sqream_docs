.. _regexp_replace:

**************************
REGEXP_REPLACE
**************************
The ``REGEXP_REPLACE`` function finds and replaces text column substrings using constant regexp-based patterns with constant replacement strings. 

For related information, see the following:

* `REGEXP_COUNT <https://docs.sqream.com/en/latest/reference/sql/sql_functions/scalar_functions/string/regexp_count.html>`_
* `REGEXP_INSTR <https://docs.sqream.com/en/latest/reference/sql/sql_functions/scalar_functions/string/regexp_instr.html>`_
* `REGEXP_SUBSTR <https://docs.sqream.com/en/latest/reference/sql/sql_functions/scalar_functions/string/regexp_substr.html>`_




Syntax
--------------
The following is a syntactic example of the ``REGEXP_REPLACE`` function:

.. code-block:: postgres
   
   REGEXP_REPLACE(input, pattern [, replacement [, position [, occurrence]]])

Arguments
--------------
The following table shows the ``REGEXP_REPLACE`` arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``input``
     - The replaced input value.
   * - ``pattern``
     - The pattern that identifies which substrings to replace.
   * - ``replacement``
     - The replacement string.
   * - ``position``
     - Indicates the 1-based offset where the pattern search starts.
   * - ``occurrence``
     - (Optional) Sets a specific occurrence to replace. Using ``0`` replaces all occurrences.

Test Patterns
--------------
The following table shows the ``REGEXP_REPLACE`` test patterns:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   
   * - Test Pattern
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
------------
The ``REGEXP_REPLACE`` function returns the replaced input value.
	 
Notes
--------------
The test pattern must be a literal string.

Example
--------------
The following is an example of the ``REGEXP_REPLACE`` function:

.. code-block::

   CREATE TABLE test(country_name TEXT); 
   INSERT INTO test values('SWEDEN');
   SELECT REGEXP_REPLACE(country_name, 'WEDE', 'PAI') FROM test;

   SELECT * FROM test;

The output generated from the example above is ``SPAIN``.


