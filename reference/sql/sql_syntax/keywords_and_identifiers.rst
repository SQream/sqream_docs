:orphan:

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

These are all valid examples when quoted, but are invalid when unquoted:

.. code-block:: postgres

	CREATE SCHEMA "my schema";
	
	CREATE SCHEMA "123schema";
	  
	CREATE SCHEMA my schema;   --invalid
	
	CREATE SCHEMA 123schema;   --invalid
	
Use of invalid characters, such as ``@``:

.. code-block:: postgres
	
	CREATE SCHEMA "my schema@master";
	
Provides the following error message:

.. code-block:: console

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
		``ABORT``, ``ADD``, ``ALL``, ``ALTER``, ``AND``, ``ANY``, ``AS``, ``ASC``, ``AUDITLOG``, ``AUTHORIZATION``

	B
		``BACKUP``, ``BEGIN``, ``BETWEEN``, ``BREAK``, ``BROWSE``, ``BULK``, ``BY``

	C
		``CASE``, ``CASCADE``, ``CHECK``, ``CHECKPOINT``, ``CLOSE``, ``CLUSTERED``, ``COLLATE``, ``COLUMN``, ``COMMIT``, ``COMPUTE``, ``CONSTRAINT``, ``CONTAINSTABLE``, ``CONTINUE``, ``CONVERT``, ``CREATE``, ``CROSS``, ``CURRENT``, ``CURRENT_TIME``, ``CURRENT_USER``, ``CURSOR``

	D
		``DATABASE``, ``DBCC``, ``DEALLOCATE``, ``DECLARE``, ``DEFAULT``, ``DELETE``, ``DENY``, ``DESC``, ``DISK``, ``DISTINCT``, ``DISTRIBUTED``, ``DROP``, ``DUMP``

	E
		``ELSE``, ``END``, ``ERRLVL``, ``ESCAPE``, ``EXEC``, ``EXECUTE``, ``EXCEPT``, ``EXISTS``, ``EXIT``, ``EXTERNAL``

	F
		``FETCH``, ``FILLFACTOR``, ``FILE``, ``FOR``, ``FOREIGN``, ``FREETEXT``, ``FREETEXTTABLE``, ``FROM``, ``FULL``, ``FUNCTION``

	G
		``GOTO``, ``GRANT``, ``GROUP``, ``HASH``, ``HAVING``, ``HOLDLOCK``

	H
		``HASH``, ``HAVING``, ``HOLDLOCK``

	I
		``IDENTITY``, ``IDENTITYCOL``, ``IDENTITY_INSERT``, ``IF``, ``IN``, ``INNER``, ``INDEX``, ``INSERT``, ``INTERSECT``, ``INTO``, ``IS``

	J
		``JOIN``

	K
		``KEY``, ``KILL``

	L
		``LEFT``, ``LIKE``, ``LIMIT``, ``LINENO``, ``LOAD``, ``LOOP``

	M
		``MERGE``

	N
		``NATIONAL``, ``NATURAL``, ``NOCHECK``, ``NONCLUSTERED``, ``NOT``, ``NULL``, ``NULLIF``

	O
		``OFF``, ``OFFSETS``, ``OF``, ``ON``, ``OPEN``, ``OPENDATASOURCE``, ``OPENQUERY``, ``OPENROWSET``, ``OPENXML``, ``OPTION``, ``OR``, ``ORDER``, ``OUTER``, ``OVER``

	P
		``PERCENT``, ``PIVOT``, ``PRECISION``, ``PRIMARY``, ``PRINT``, ``PROC``, ``PROCEDURE``

	R
		``RAISERROR``, ``READ``, ``READTEXT``, ``REFERENCES``, ``RECONFIGURE``, ``REPLICATION``, ``RESTORE``, ``RESTRICT``, ``RETURN``, ``REVERT``, ``REVOKE``, ``RIGHT``, ``ROLLBACK``, ``ROWCOUNT``, ``ROWGUIDCOL``, ``RULE``

	S
		``SAVE``, ``SCHEMA``, ``SECURITYAUDIT``, ``SELECT``, ``SESSION_USER``, ``SET``, ``SETUSER``, ``SHUTDOWN``, ``SOME``, ``STATISTICS``, ``SYSTEM_USER``

	T
		``TABLE``, ``TABLESAMPLE``, ``TEXTSIZE``, ``THEN``, ``TO``, ``TOP``, ``TRANSACTION``, ``TRAN``, ``TRIGGER``, ``TRUNCATE``, ``TSEQUAL``

	U
		``UNION``, ``UNIQUE``, ``UNPIVOT``, ``UPDATE``, ``UPDATETEXT``, ``USE``, ``USER``, ``USING``

	V
		``VIEW``, ``VALUES``, ``VARYING``

	W
		``WAITFOR``, ``WHEN``, ``WHERE``, ``WHILE``, ``WINDOW``, ``WITH``, ``WRITETEXT``


	




 
 
 
