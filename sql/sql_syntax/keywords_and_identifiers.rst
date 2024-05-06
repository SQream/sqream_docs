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
* Must be case-insensitive. BLUE converts all identifiers to lowercase unless quoted
* Does not equal any keywords, such as ``SELECT``, ``OR``, ``AND``, etc'

To bypass the rules above you can surround an identifier with double quotes (``"``).

Quoted identifiers must follow these rules:

* Must be enclosed with double quotes (``"``)
* May contain any ASCII character except ``@``, ``$`` or ``"``
* Must be case-sensitive

Examples
--------

Creating quoted and unquoted identifiers:

.. code-block:: postgres

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

BLUE reserved keywords:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Reserved Word
     - Description
   * - :kbd:`ALL`
     - ANSI
   * - :kbd:`ALLOCATE`
     - ANSI
   * - :kbd:`ANALYSE`
     - ANSI
   * - :kbd:`ANALYZE`
     - ANSI
   * - :kbd:`AND`
     - ANSI
   * - :kbd:`ANY`
     - ANSI
   * - :kbd:`ARRAY`
     - ANSI
   * - :kbd:`AS`
     - ANSI
   * - :kbd:`ASC`
     - ANSI
   * - :kbd:`AUTHORIZATION`
     - ANSI
   * - :kbd:`BINARY`
     - ANSI
   * - :kbd:`BIGINT`
     - ANSI
   * - :kbd:`BOTH`
     - ANSI
   * - :kbd:`CASE`
     - ANSI
   * - :kbd:`CAST`
     - ANSI
   * - :kbd:`CHECK`
     - ANSI
   * - :kbd:`COLLATE`
     - ANSI
   * - :kbd:`COLUMN`
     - ANSI
   * - :kbd:`COMMENT`
     - ANSI
   * - :kbd:`CONCURRENTLY`
     - ANSI
   * - :kbd:`CONSTRAINT`
     - ANSI
   * - :kbd:`CREATE`
     - ANSI
   * - :kbd:`CROSS`
     - ANSI
   * - :kbd:`CURRENT_CATALOG`
     - ANSI
   * - :kbd:`CURRENT_ROLE`
     - ANSI
   * - :kbd:`CURRENT_TIME`
     - ANSI
   * - :kbd:`CURRENT_USER`
     - ANSI
   * - :kbd:`DEFAULT`
     - ANSI
   * - :kbd:`DEFERRABLE`
     - ANSI
   * - :kbd:`DESC`
     - ANSI
   * - :kbd:`DISTINCT`
     - ANSI
   * - :kbd:`DO`
     - ANSI
   * - :kbd:`ELSE`
     - ANSI
   * - :kbd:`END`
     - ANSI
   * - :kbd:`EXCEPT`
     - ANSI
   * - :kbd:`FALSE`
     - ANSI
   * - :kbd:`FETCH`
     - ANSI
   * - :kbd:`FOR`
     - ANSI
   * - :kbd:`FREEZE`
     - ANSI
   * - :kbd:`FROM`
     - ANSI
   * - :kbd:`FULL`
     - ANSI
   * - :kbd:`FUNCTION`
     - ANSI
   * - :kbd:`GRANT`
     - ANSI
   * - :kbd:`GROUP`
     - ANSI
   * - :kbd:`HASH`
     - ANSI
   * - :kbd:`HAVING`
     - ANSI
   * - :kbd:`ILIKE`
     - ANSI
   * - :kbd:`IN`
     - ANSI
   * - :kbd:`INITIALLY`
     - ANSI
   * - :kbd:`INNER`
     - ANSI
   * - :kbd:`INTERSECT`
     - ANSI
   * - :kbd:`INTO`
     - ANSI
   * - :kbd:`IS`
     - ANSI
   * - :kbd:`ISNULL`
     - ANSI
   * - :kbd:`JOIN`
     - ANSI
   * - :kbd:`KEY`
     - ANSI
   * - :kbd:`LEADING`
     - ANSI
   * - :kbd:`LEFT`
     - ANSI
   * - :kbd:`LIKE`
     - ANSI
   * - :kbd:`LIMIT`
     - ANSI
   * - :kbd:`LOCALTIME`
     - ANSI
   * - :kbd:`LOCALTIMESTAMP`
     - ANSI
   * - :kbd:`LOOP`
     - ANSI
   * - :kbd:`MERGE`
     - ANSI
   * - :kbd:`NATURAL`
     - 	 ANSI
   * - :kbd:`NOT`
     - ANSI	 
   * - :kbd:`NOTNULL`
     - ANSI	 
   * - :kbd:`NULL`
     - ANSI	 
   * - :kbd:`OFF`
     - ANSI	 
   * - :kbd:`OFFSET`
     - ANSI	 
   * - :kbd:`OFFSETS`
     - ANSI	 
   * - :kbd:`ON`
     - ANSI	 
   * - :kbd:`ONLY`
     - ANSI	 
   * - :kbd:`OPTION`
     - ANSI	 
   * - :kbd:`OR`
     - ANSI	 
   * - :kbd:`ORDER`
     - ANSI	 
   * - :kbd:`OUTER`
     - ANSI	 
   * - :kbd:`OVER`
     - ANSI	 	 
   * - :kbd:`OVERLAPS`
     - ANSI	 
   * - :kbd:`PERCENT`
     - ANSI	
   * - :kbd:`PLACING`
     - ANSI	 
   * - :kbd:`PRIMARY`
     - ANSI	 
   * - :kbd:`PRECISION`
     - ANSI	 
   * - :kbd:`PROC`
     - ANSI	 
   * - :kbd:`PROCEDURE`
     - ANSI	 
   * - :kbd:`REFERENCES`
     - ANSI	 
   * - :kbd:`RETURNING`
     - ANSI	 
   * - :kbd:`RIGHT`
     - ANSI	 
   * - :kbd:`RLIKE`
     - ANSI	 
   * - :kbd:`RULE`
     - ANSI	 
   * - :kbd:`SCHEMA`
     - ANSI	 
   * - :kbd:`SELECT`
     - ANSI	 
   * - :kbd:`SESSION_USER`
     - ANSI	 
   * - :kbd:`SET`
     - ANSI	 
   * - :kbd:`SIMILAR`
     - ANSI	 
   * - :kbd:`SOME`
     - ANSI	 
   * - :kbd:`STATISTICS`
     - ANSI	 
   * - :kbd:`SYMMETRIC`
     - ANSI	 
   * - :kbd:`TABLE`
     - ANSI
   * - :kbd:`THEN`
     - ANSI	 
   * - :kbd:`TO`
     - ANSI	 
   * - :kbd:`TOP`
     - ANSI	 
   * - :kbd:`TRAILING`
     - ANSI	 
   * - :kbd:`TRAN`
     - ANSI	 
   * - :kbd:`TRUE`
     - ANSI	 
   * - :kbd:`UNION`
     - ANSI	 
   * - :kbd:`UNIQUE`
     - ANSI	 
   * - :kbd:`USER`
     - ANSI	 
   * - :kbd:`USING`
     - ANSI	 	 
   * - :kbd:`VARIADIC`
     - ANSI	 	
   * - :kbd:`VERBOSE`
     - ANSI	 	
   * - :kbd:`WHEN`
     - ANSI	 	
   * - :kbd:`WHERE`
     - ANSI	 	
   * - :kbd:`WINDOW`
     - ANSI	 	
   * - :kbd:`WITH`
     - ANSI	 	


 
 
 
