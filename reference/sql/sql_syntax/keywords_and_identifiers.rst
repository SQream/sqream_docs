.. _keywords_and_identifiers:

***************************
Identifiers
***************************
**Identifiers** are names given to SQL entities, such as tables, columns, databases, and variables. Identifiers must be unique so that entities can be correctly identified during the execution of a program. Identifiers can also be used to change a column name in the result (column alias) in a  ``SELECT`` statement. Identifiers can be either quoted or unquoted and a maximum 128 characters long.

Identifiers are sometimes referred to as "names".

Regular identifiers must follow these rules:

* Must not contain any special characters except for underscores (``_``).
* Must be case-insensitive. SQream converts all identifiers to lowercase unless quoted.
* Does not equal any keywords, such as ``SELECT``, ``OR``, or ``AND``, etc.

To bypass the rules above you can surround an identifier with double quotes (``"``).

Quoted identifiers must follow these rules:

* Must be surrounded with double quotes (``"``).
* May contain any ASCII character except ``@``, ``$`` or ``"``.
* Must be case-sensitive and referenced with double quotes (``"``).

Identifiers are different than **keywords**, which are predefined words reserved with specific meanings in a statement. Some examples of keywords are ``SELECT``, ``CREATE``, and ``WHERE``. Note that keywords **cannot** be used as identifiers.

The following table shows a full list of the reserved keywords:

+-------------------------------------------------------------------------------------------------+
| **Keywords**                                                                                    |
+-------------------+---------------------+--------------------+------------------+---------------+
| **A - C**         | **C - G**           | **H - N**          | **N - S**        | **S - W**     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ALL``           | ``CURRENT_CATALOG`` | ``HASH``           | ``NOT``          | ``SIMILAR``   |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ANALYSE``       | ``CURRENT_ROLE``    | ``HAVING``         | ``NOTNULL``      | ``SOME``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ANALYZE``       | ``CURRENT_TIME``    | ``ILIKE``          | ``NULL``         | ``SYMMETRIC`` |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AND``           | ``CURRENT_USER``    | ``IN``             | ``OFFSET``       | ``TABLE``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ANY``           | ``DEFAULT``         | ``INITIALLY``      | ``ON``           | ``THEN``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ARRAY``         | ``DEFERRABLE``      | ``INNER``          | ``ONLY``         | ``TO``        |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AS``            | ``DESC``            | ``INTERSECT``      | ``OPTION``       | ``TRAILING``  |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``ASC``           | ``DISTINCT``        | ``INTO``           | ``OR``           | ``TRUE``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AUTHORIZATION`` | ``DO``              | ``IS``             | ``ORDER``        | ``UNION``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BINARY``        | ``ELSE``            | ``ISNULL``         | ``OUTER``        | ``UNIQUE``    |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BOTH``          | ``END``             | ``JOIN``           | ``OVER``         | ``USER``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CASE``          | ``EXCEPT``          | ``LEADING``        | ``OVERLAPS``     | ``USING``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CAST``          | ``FALSE``           | ``LEFT``           | ``PLACING``      | ``VARIADIC``  |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CHECK``         | ``FETCH``           | ``LIKE``           | ``PRIMARY``      | ``VERBOSE``   |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``COLLATE``       | ``FOR``             | ``LIMIT``          | ``REFERENCES``   | ``WHEN``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``COLUMN``        | ``FREEZE``          | ``LOCALTIME``      | ``RETURNING``    | ``WHERE``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CONCURRENTLY``  | ``FROM``            | ``LOCALTIMESTAMP`` | ``RIGHT``        | ``WINDOW``    |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CONSTRAINT``    | ``FULL``            | ``LOOP``           | ``RLIKE``        | ``WITH``      |
+-------------------+---------------------+--------------------+------------------+               | 
| ``CREATE``        | ``GRANT``           | ``MERGE``          | ``SELECT``       |               |
+-------------------+---------------------+--------------------+------------------+               |  
| ``CROSS``         | ``GROUP``           | ``NATURAL``        | ``SESSION_USER`` |               |  
+-------------------+---------------------+--------------------+------------------+---------------+
