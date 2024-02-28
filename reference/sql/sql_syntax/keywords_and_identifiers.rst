.. _keywords_and_identifiers:

************************
Identifiers and Keywords
************************

Identifiers
===========

**Identifiers** are names given to SQL entities, such as tables, columns, databases, and variables. Identifiers must be unique so that entities can be correctly identified during the execution of a program. Identifiers can also be used to change a column name in the result (column alias) in a  ``SELECT`` statement. Identifiers can be either quoted or unquoted and a maximum 128 characters long.

Identifiers are sometimes referred to as "names".

Unquoted identifiers must follow these rules:

* Must not contain a whitespace character or any special characters except for underscores (``_``)
* Must be case-insensitive. SQream converts all identifiers to lowercase unless quoted
* Does not equal any keywords, such as ``SELECT``, ``OR``, ``AND``, etc'

To bypass the rules above you can surround an identifier with double quotes (``"``).

Quoted identifiers must follow these rules:

* Must be enclosed with double quotes (``"``)
* May contain any ASCII character except ``@``, ``$`` or ``"``
* Must be case-sensitive

Examples
--------

Creating quoted and unquoted identifiers:

.. code-block:: sql

	--Quoted identifiers preserves case - will create "developer"
	CREATE ROLE "developer";
	
	--Quoted identifiers preserves case - will create "Developer"
	CREATE ROLE "Developer"; 
	
	--Unquoted identifiers ignores case - will create "developer"
	CREATE ROLE Developer;   

Valid and invalid use of identifiers:

.. code-block:: sql

	-- These are all valid examples when quoted:
	
	CREATE SCHEMA "my schema";
	CREATE SCHEMA "123schema";
	
	-- but are invalid when unquoted:
	
	CREATE SCHEMA my schema; --invalid
	CREATE SCHEMA 123schema; --invalid
	
	-- Use of invalid characters:
	
	CREATE SCHEMA "my schema@master";
	
	Status:  Ended with errorError preparing statement: Unsupported character '@'  in identifier: "my schema@master"
	Quoted identifiers cannot contain the character '@'.
	Quoted identifiers may contain any ASCII character with code between 32 and 126 except for:
	- @
	- $
	- "
	
	
Keywords
========

Identifiers are different than **keywords**, which are predefined words reserved with specific meanings in a statement. Some examples of keywords are ``SELECT``, ``CREATE``, and ``WHERE``. Note that keywords **cannot** be used as identifiers.

SQreamDB reserved keywords:



``ALL`` | ``ANALYSE`` | ``ANALYZE`` | ``AND`` | ``ANY`` | ``ARRAY`` | ``AS`` | ``ASC`` | ``AUTHORIZATION`` | ``BINARY`` | ``BIGINT`` | ``BOTH`` | ``CASE`` | ``CAST`` | ``CHECK`` | ``COLLATE`` | ``COLUMN`` | ``COMMENT`` | ``CONCURRENTLY`` | ``CONSTRAINT`` | ``CREATE`` | ``CROSS`` | ``CURRENT_CATALOG`` | ``CURRENT_ROLE`` | ``CURRENT_TIME`` | ``CURRENT_USER`` | ``DEFAULT`` | ``DEFERRABLE`` | ``DESC`` | ``DISTINCT`` | ``DO`` | ``ELSE`` | ``END`` | ``EXCEPT`` | ``FALSE`` | ``FETCH`` | ``FOR`` | ``FREEZE`` | ``FROM`` | ``FULL`` | ``FUNCTION`` | ``GRANT`` | ``GROUP`` | ``HASH`` | ``HAVING`` | ``ILIKE`` | ``IN`` | ``INITIALLY`` | ``INNER`` | ``INTERSECT`` | ``INTO`` | ``IS`` | ``ISNULL`` | ``JOIN`` | ``KEY`` | ``LEADING`` | ``LEFT`` | ``LIKE`` | ``LIMIT`` | ``LOCALTIME`` | ``LOCALTIMESTAMP`` | ``LOOP`` | ``MERGE`` | ``NATURAL`` | ``NOT`` | ``NOTNULL`` | ``NULL`` | ``OFF`` | ``OFFSET`` | ``OFFSETS`` | ``ON`` | ``ONLY`` | ``OPTION`` | ``OR`` | ``ORDER`` | ``OUTER`` | ``OVER`` | ``OVERLAPS`` | ``PERCENT`` | ``PLACING`` | ``PRIMARY`` | ``PRECISION`` | ``PROC`` | ``PROCEDURE`` | ``REFERENCES`` | ``RETURNING`` | ``RIGHT`` | ``RLIKE`` | ``RULE`` | ``SCHEMA`` | ``SELECT`` | ``SESSION_USER`` | ``SET`` | ``SIMILAR`` | ``SOME`` | ``STATISTICS`` | ``SYMMETRIC`` | ``TABLE`` | ``THEN`` | ``TO`` | ``TOP`` | ``TRAILING`` | ``TRAN`` | ``TRUE`` | ``UNION`` | ``UNIQUE`` | ``USER`` | ``USING`` | ``VARIADIC`` | ``VERBOSE`` | ``WHEN`` | ``WHERE`` | ``WINDOW`` | ``WITH`` | 


 
 
 
