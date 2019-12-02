.. _keywords_and_identifiers:

***************************
Keywords and Identifiers
***************************

SQL statements are made up of three components:

* Keywords: Keywords have specific meaning in SQL, like ``SELECT``, ``CREATE``, ``WHERE``, etc.
* Identifiers: Names for things like tables, columns, databases, etc.

.. _keywords:

Keywords
===========

Keywords are special words that make up SQream's SQL syntax, and have a meaning in a statement.

Keywords are not allowed as identifiers. :ref:`A full list of reserved keywords <reserved_keywords>` can be found at the end of this document.

.. _identifiers:

Identifiers
=============

Identifiers are typically used as database objects names, such as databases, tables, views or columns. Because of their use, these are also often also called "names".

Identifiers can also be used to change a column name in the result (column alias) in a  ``SELECT`` statement.

Identifier rules
------------------

An identifier can be either quoted or unquoted, and are maximum 128 characters long.

Regular identifiers follow these rules:

#. Does not contain any special characters, apart for an underscore (``_``)
#. Case insensitive. SQream DB converts all identifiers to lowercase unless quoted.
#. Does not equal any :ref:`keyword <keywords>`, like ``SELECT``, ``OR``, ``AND``, etc.


To bypass these limitations, use a quoted identifier by surrounding the identifier with double quotes (``"``).

Quoted identifiers follow these rules:

* Surrounded with double quotes (").
* May contain any ASCII character, except ``@``, ``$`` or ``"``.
* Quoted identifiers are stored case-sensitive and must be referenced with double quotes.

.. _reserved_keywords:

Reserved keywords
==================

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Keyword
   * - ``ALL``
   * - ``ANALYSE``
   * - ``ANALYZE``
   * - ``AND``
   * - ``ANY``
   * - ``ARRAY``
   * - ``AS``
   * - ``ASC``
   * - ``AUTHORIZATION``
   * - ``BINARY``
   * - ``BOTH``
   * - ``CASE``
   * - ``CAST``
   * - ``CHECK``
   * - ``COLLATE``
   * - ``COLUMN``
   * - ``CONCURRENTLY``
   * - ``CONSTRAINT``
   * - ``CREATE``
   * - ``CROSS``
   * - ``CURRENT_CATALOG``
   * - ``CURRENT_ROLE``
   * - ``CURRENT_TIME``
   * - ``CURRENT_USER``
   * - ``DEFAULT``
   * - ``DEFERRABLE``
   * - ``DESC``
   * - ``DISTINCT``
   * - ``DO``
   * - ``ELSE``
   * - ``END``
   * - ``EXCEPT``
   * - ``FALSE``
   * - ``FETCH``
   * - ``FOR``
   * - ``FREEZE``
   * - ``FROM``
   * - ``FULL``
   * - ``GRANT``
   * - ``GROUP``
   * - ``HASH``
   * - ``HAVING``
   * - ``ILIKE``
   * - ``IN``
   * - ``INITIALLY``
   * - ``INNER``
   * - ``INTERSECT``
   * - ``INTO``
   * - ``IS``
   * - ``ISNULL``
   * - ``JOIN``
   * - ``LEADING``
   * - ``LEFT``
   * - ``LIKE``
   * - ``LIMIT``
   * - ``LOCALTIME``
   * - ``LOCALTIMESTAMP``
   * - ``LOOP``
   * - ``MERGE``
   * - ``NATURAL``
   * - ``NOT``
   * - ``NOTNULL``
   * - ``NULL``
   * - ``OFFSET``
   * - ``ON``
   * - ``ONLY``
   * - ``OPTION``
   * - ``OR``
   * - ``ORDER``
   * - ``OUTER``
   * - ``OVER``
   * - ``OVERLAPS``
   * - ``PLACING``
   * - ``PRIMARY``
   * - ``REFERENCES``
   * - ``RETURNING``
   * - ``RIGHT``
   * - ``RLIKE``
   * - ``SELECT``
   * - ``SESSION_USER``
   * - ``SIMILAR``
   * - ``SOME``
   * - ``SYMMETRIC``
   * - ``SYMMETRIC``
   * - ``TABLE``
   * - ``THEN``
   * - ``TO``
   * - ``TRAILING``
   * - ``TRUE``
   * - ``UNION``
   * - ``UNIQUE``
   * - ``USER``
   * - ``USING``
   * - ``VARIADIC``
   * - ``VERBOSE``
   * - ``WHEN``
   * - ``WHERE``
   * - ``WINDOW``
   * - ``WITH``