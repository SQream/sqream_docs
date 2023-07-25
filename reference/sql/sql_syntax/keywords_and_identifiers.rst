.. _keywords_and_identifiers:

***********
Identifiers
***********

**Identifiers** are names given to SQL entities, such as tables, columns, databases, and variables. Identifiers must be unique so that entities can be correctly identified during the execution of a program. Identifiers can also be used to change a column name in the result (column alias) in a  ``SELECT`` statement. Identifiers can be either quoted or unquoted and a maximum 128 characters long.

Identifiers are sometimes referred to as "names".

Regular identifiers must follow these rules:

* Must not contain a whitespace character or any special characters except for underscores (``_``)
* Must be case-insensitive. SQream converts all identifiers to lowercase unless quoted
* Does not equal any keywords, such as ``SELECT``, ``OR``, or ``AND``, etc

To bypass the rules above you can surround an identifier with double quotes (``"``).

Quoted identifiers must follow these rules:

* Must be surrounded with double quotes (``"``)
* May contain any ASCII character except ``@``, ``$`` or ``"``.
* Must be case-sensitive and referenced with double quotes (``"``)

Identifiers are different than **keywords**, which are predefined words reserved with specific meanings in a statement. Some examples of keywords are ``SELECT``, ``CREATE``, and ``WHERE``. Note that keywords **cannot** be used as identifiers.

SQreamDB reserved keywords:


     - ``ALL``
     - ``ANALYSE``
     - ``ANALYZE``
     - ``AND``
     - ``ANY``
     - ``ARRAY``
     - ``AS`` 
     - ``ASC``
     - ``AUTHORIZATION``
     - ``BINARY``
     - ``BIGINT``
     - ``BOTH``
     - ``CASE``
     - ``CAST``
     - ``CHECK``
     - ``COLLATE``
     - ``COLUMN``
     - ``CONCURRENTLY``
     - ``CONSTRAINT``
     - ``CREATE``
     - ``CROSS``
     - ``CURRENT_CATALOG``
     - ``CURRENT_ROLE``
     - ``CURRENT_TIME``
     - ``CURRENT_USER``
     - ``DEFAULT``
     - ``DEFERRABLE``
     - ``DESC``
     - ``DISTINCT``
     - ``DO``
     - ``ELSE``
     - ``END``
     - ``EXCEPT``
     - ``FALSE``
     - ``FETCH``
     - ``FOR``
     - ``FREEZE``
     - ``FROM``
     - ``FULL``
     - ``FUNCTION``
     - ``GRANT``
     - ``GROUP``
     - ``HASH``
     - ``HAVING``
     - ``ILIKE``
     - ``IN``
     - ``INITIALLY``
     - ``INNER``
     - ``INTERSECT``
     - ``INTO``
     - ``IS``
     - ``ISNULL``
     - ``JOIN``
     - ``KEY``
     - ``LEADING``
     - ``LEFT``
     - ``LIKE``
     - ``LIMIT``
     - ``LOCALTIME``
     - ``LOCALTIMESTAMP``
     - ``LOOP``
     - ``MERGE``
     - ``NATURAL``
     - ``NOT``
     - ``NOTNULL``
     - ``NULL``
     - ``OFFSET``
     - ``ON``
     - ``ONLY``
     - ``OPTION``
     - ``OR``
     - ``ORDER``
     - ``OUTER``
     - ``OVER``
     - ``OVERLAPS``
     - ``PERCENT``
     - ``PLACING``
     - ``PRIMARY``
     - ``PRECISION``
     - ``PROC``
     - ``REFERENCES``
     - ``RETURNING``
     - ``RIGHT``
     - ``RLIKE``
     - ``SELECT``
     - ``SESSION_USER``
     - ``SET``
     - ``SIMILAR``
     - ``SOME``
     - ``SYMMETRIC``
     - ``TABLE``
     - ``THEN``
     - ``TO``
     - ``TRAILING``
     - ``TRAN``
     - ``TRUE``
     - ``UNION``
     - ``UNIQUE``
     - ``USER``
     - ``USING``
     - ``VARIADIC``
     - ``VERBOSE``
     - ``WHEN``
     - ``WHERE``
     - ``WINDOW``
     - ``WITH``


 
 
 
