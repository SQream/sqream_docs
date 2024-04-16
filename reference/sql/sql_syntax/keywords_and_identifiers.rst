.. _keywords_and_identifiers:

************************
Identifiers and Keywords
************************

Identifiers
===========

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

Examples
--------

Creating quoted and unquoted identifiers:

.. code-block:: postgres

	CREATE ROLE "developer"; --quoted identifiers preserves case - will create "developer"
	CREATE ROLE "Developer"; --quoted identifiers preserves case - will create "Developer"
	CREATE ROLE Developer;   --unquoted identifiers ignores case - will create "developer"

Valid and invalid use of identifiers:

.. code-block:: postgres

	-- these are all valid examples when quoted:
	
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

.. glossary::

	A
		``ABORT``, ``ADD``, ``ALL``, ``ALTER``, ``ANALYSE``, ``ANALYZE``, ``AND``, ``ANY``, ``ARRAY``, ``AS``, ``ASC``, ``AUDITLOG``, ``AUTHORIZATION``

	B
		``BACKUP``, ``BEGIN``, ``BETWEEN``, ``BIGINT``, ``BINARY``<, ``BOTH``, ``BREAK``, ``BROWSE``, ``BULK``, ``BY``

	C
		``CASE``, ``CAST``, ``CASCADE``, ``CHECK``, ``CHECKPOINT``, ``CLOSE``, ``CLUSTERED``, ``COLLATE``, ``COLUMN``, ``COMMENT``<, ``COMPUTE``, ``CONCURRENTLY``, ``CONSTRAINT``, ``CONTAINSTABLE``, ``CONTINUE``, ``CONVERT``, ``CREATE``, ``CROSS``, ``CURRENT``, ``CURRENT_CATALOG``, ``CURRENT_ROLE``, ``CURRENT_TIME``, ``CURRENT_USER``, ``CURSOR``

	D
		``DATABASE``, ``DBCC``, ``DEALLOCATE``, ``DECLARE``, ``DEFAULT``, ``DEFERRABLE``, ``DELETE``, ``DENY``, ``DESC``, ``DISTINCT``, ``DISTRIBUTED``, ``DO``<, ``DROP``, ``DUMP``

	E
		``ELSE``, ``END``, ``ERRLVL``, ``ESCAPE``, ``EXEC``, ``EXECUTE``, ``EXCEPT``, ``EXISTS``, ``EXIT``, ``EXTERNAL``

	F
		``FALSE``, ``FETCH``, ``FILLFACTOR``, ``FILE``, ``FOR``, ``FOREIGN``, ``FREEZE``, ``FREETEXT``, ``FREETEXTTABLE``, ``FROM``, ``FULL``, ``FUNCTION``

	G
		``GOTO``, ``GRANT``, ``GROUP``, ``HASH``, ``HAVING``, ``HOLDLOCK``

	H
		``HASH``, ``HAVING``, ``HOLDLOCK``

	I
		``IDENTITY``, ``IDENTITYCOL``, ``IDENTITY_INSERT``, ``IF``, ``ILIKE``, ``IN``, ``INITIALLY``, ``INNER``, ``INDEX``, ``INSERT``, ``IS``, ``ISCASTABLE``, ``ISNULL``<

	J
		``JOIN``

	K
		``KEY``, ``KILL``

	L
		``LEFT``, ``LEADING``, ``LIKE``, ``LIMIT``, ``LINENO``, ``LOAD``, ``LOCALTIME``, ``LOCALTIMESTAMP``, ``LOOP``

	M
		``MERGE``

	N
		``NATIONAL``, ``NATURAL``, ``NOCHECK``, ``NONCLUSTERED``, ``NOT``, ``NOTNULL``<, ``NULL``, ``NULLIF``

	O
		``OFF``, ``OFFSET``, ``OFFSETS``, ``OF``, ``ON``, ``ONLY``, ``OPEN``, ``OPENDATASOURCE``, ``OPENQUERY``, ``OPENROWSET``, ``OPENXML``, ``OPTION``, ``OR``, ``ORDER``, ``OUTER``, ``OVER``, ``OVERLAPS``

	P
		``PERCENT``, ``PLACING``, ``PLAIN``, ``PLAINS``, ``PLAINTEXT``, ``PLB``, ``PLI``, ``PLM``, ``PLP``, ``PLSQL``, ``PRECISION``<<, ``PRIMARY``, ``PRINT``, ``PROC``, ``PROCEDURE``, ``PUBLICATION``, ``PUBLISH``, ``PUBLICIZE``

	R
		``RAISEERROR``, ``READ``, ``READTEXT``, ``REFERENCES``, ``RECONFIGURE``, ``REPLICATION``, ``RESTORE``, ``RESTRICT``, ``RETURN``, ``RETURNING``, ``REVERT``, ``REVOKE``, ``RIGHT``, ``RLIKE``, ``ROLLBACK``, ``ROWCOUNT``, ``ROWGUIDCOL``, ``RULE``

	S
		``SAVE``, ``SCHEMA``, ``SECURITYAUDIT``, ``SELECT``, ``SESSION_USER``, ``SET``, ``SETUSER``, ``SHUTDOWN``, ``SIMILAR``, ``SOME``, ``STATISTICS``, ``SYMMETRIC``

	T
		``TABLE``, ``TABLESAMPLE``, ``TEXTSIZE``, ``THEN``, ``TO``, ``TOP``, ``TRANSACTION``, ``TRAN``, ``TRIGGER``, ``TRUNCATE``, ``TRUE``

	U
		``UNION``, ``UNIQUE``, ``UNPIVOT``, ``UPDATE``, ``UPDATETEXT``, ``USE``, ``USER``, ``USING``

	V
		``VARIADIC``, ``VERBOSE``, ``VIEW``, ``VALUES``, ``VARYING``

	W
		``WAITFOR``, ``WHEN``, ``WHERE``, ``WHILE``, ``WINDOW``, ``WITH``, ``WRITETEXT``


	




 
 
 
