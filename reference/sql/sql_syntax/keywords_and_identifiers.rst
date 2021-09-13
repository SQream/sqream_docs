.. _keywords_and_identifiers:

***************************
Keywords and Identifiers
***************************

SQL statements are made up of three components:

* **Keywords:** Keywords have specific meaning in SQL, like ``SELECT``, ``CREATE``, ``WHERE``, etc.
* **Identifiers:** Names for things like tables, columns, databases, etc.

.. _keywords:

Keywords
===========

Keywords are special words that make up SQream DB's SQL syntax, and have a meaning in a statement.

Keywords are not allowed as identifiers. :ref:`A full list of reserved keywords <reserved_keywords>` can be found at the end of this document.

.. _identifiers:

Identifiers
=============

Identifiers are typically used as database objects names, such as databases, tables, views or columns. Because of their use, these are also often also called "names".

Identifiers can also be used to change a column name in the result (column alias) in a  ``SELECT`` statement.

Identifier Rules
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

Reserved Keywords
==================

The following table shows the reserved keywords:

+-------------------+---------------------+--------------------+------------------+---------------+
|                  **Reserved Keywords**                                                          |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ALL``           | ``CURRENT_CATALOG`` | ``HASH``           | ``NOT``          | ``SIMILAR``   |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ANALYSE``       | ``CURRENT_ROLE``    | ``HAVING``         | ``NOTNULL``      | ``SOME``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ANALYZE``       | ``CURRENT_TIME``    | ``ILIKE``          | ``NULL``         | ``SYMMETRIC`` |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AND``           | ``CURRENT_USER``    | ``IN``             | ``OFFSET``       | ``SYMMETRIC`` |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ANY``           | ``DEFAULT``         | ``INITIALLY``      | ``ON``           | ``TABLE``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ARRAY``         | ``DEFERRABLE``      | ``INNER``          | ``ONLY``         | ``THEN``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AS``            | ``DESC``            | ``INTERSECT``      | ``OPTION``       | ``TO``        |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ASC``           | ``DISTINCT``        | ``INTO``           | ``OR``           | ``TRAILING``  |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AUTHORIZATION`` | ``DO``              | ``IS``             | ``ORDER``        | ``TRUE``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BINARY``        | ``ELSE``            | ``ISNULL``         | ``OUTER``        | ``UNION``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BOTH``          | ``END``             | ``JOIN``           | ``OVER``         | ``UNIQUE``    |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CASE``          | ``EXCEPT``          | ``LEADING``        | ``OVERLAPS``     | ``USER``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CAST``          | ``FALSE``           | ``LEFT``           | ``PLACING``      | ``USING``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CHECK``         | ``FETCH``           | ``LIKE``           | ``PRIMARY``      | ``VARIADIC``  |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``COLLATE``       | ``FOR``             | ``LIMIT``          | ``REFERENCES``   | ``VERBOSE``   |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``COLUMN``        | ``FREEZE``          | ``LOCALTIME``      | ``RETURNING``    | ``WHEN``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CONCURRENTLY``  | ``FROM``            | ``LOCALTIMESTAMP`` | ``RIGHT``        | ``WHERE``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CONSTRAINT``    | ``FULL``            | ``LOOP``           | ``RLIKE``        | ``WINDOW``    |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CREATE``        | ``GRANT``           | ``MERGE``          | ``SELECT``       | ``WITH``      |
+-------------------+---------------------+--------------------+------------------+               +
| ``CROSS``         | ``GROUP``           | ``NATURAL``        | ``SESSION_USER`` |               |
+-------------------+---------------------+--------------------+------------------+---------------+
