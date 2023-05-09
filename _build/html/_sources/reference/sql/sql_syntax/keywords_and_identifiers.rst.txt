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

To bypass the rules above you can surround an identifier with double quotes (``"``) or square brackets (``[]``).

Quoted identifiers must follow these rules:

* Must be surrounded with double quotes (``"``) or square brackets (``[]``).
* May contain any ASCII character except ``@``, ``$`` or ``"``.
* Must be case-sensitive and referenced with double quotes or square brackets (``[]``).

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
| ``ASC``           | ``DISTINCT``        | ``INTO``           | ``OR``           | ``TRAN``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``AUTHORIZATION`` | ``DO``              | ``IS``             | ``ORDER``        | ``TRUE``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BINARY``        | ``ELSE``            | ``ISNULL``         | ``OUTER``        | ``UNION``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BIGINT``        | ``END``             | ``JOIN``           | ``OVER``         | ``UNIQUE``    |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``BOTH``          | ``EXCEPT``          | ``LEADING``        | ``OVERLAPS``     | ``USER``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CASE``          | ``FALSE``           | ``LEFT``           | ``PLACING``      | ``USING``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CAST``          | ``FETCH``           | ``LIKE``           | ``PRIMARY``      | ``VARIADIC``  |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CHECK``         | ``FOR``             | ``LIMIT``          | ``REFERENCES``   | ``VERBOSE``   |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``COLLATE``       | ``FREEZE``          | ``LOCALTIME``      | ``RETURNING``    | ``WHEN``      |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``COLUMN``        | ``FROM``            | ``LOCALTIMESTAMP`` | ``RIGHT``        | ``WHERE``     |
+-------------------+---------------------+--------------------+------------------+---------------+
| ``CONCURRENTLY``  | ``FULL``            | ``LOOP``           | ``RLIKE``        | ``WINDOW``    |
+-------------------+---------------------+--------------------+------------------+---------------+ 
| ``CONSTRAINT``    | ``FUNCTION``        | ``MERGE``          | ``SELECT``       | ``WITH``      |
+-------------------+---------------------+--------------------+------------------+               | 
| ``CREATE``        | ``GRANT``           | ``NATURAL``        | ``SESSION_USER`` |               |  
+-------------------+---------------------+--------------------+------------------+               |
| ``CROSS``         | ``GROUP``           |                    |                  |               |
+-------------------+---------------------+--------------------+------------------+---------------+
