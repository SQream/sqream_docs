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

.. code-block:: 

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

**A**
    ``ABORT``, ``ALL``, ``ALLOCATE``, ``ALLOW``, ``ALTER``, ``ANALYZE``, ``AND``, ``ANY``, ``ARE``, ``ARRAY``, ``ARRAY_MAX_CARDINALITY``, ``AS``, ``ASENSITIVE``, ``ASYMMETRIC``, ``ATOMIC``, ``AUTHORIZATION``

**B**
   ``BEGIN``, ``BEGIN_FRAME``, ``BEGIN_PARTITION``, ``BETWEEN``, ``BIGINT``, ``BLOB``, ``BOOL``, ``BOOLEAN``, ``BOTH``, ``BY``

**C**
   ``CALL``, ``CALLED``, ``CASCADED``, ``CASE``, ``CAST``, ``CHAR``, ``CHARACTER``, ``CHECK``, ``CLASSIFIER``, ``CLOB``, ``CLOSE``, ``CLUSTERADMIN``, ``COLLATE``, ``COLUMN``, ``COMMIT``, ``COMPUTE``, ``CONDITION``, ``CONSTRAINT``, ``CONTAINS``, ``CONVERT``, ``CORRESPONDING``, ``CREATE``, ``CROSS``, ``CUBE``, ``CURRENT``, ``CURRENT_CATALOG``, ``CURRENT_DEFAULT_TRANSFORM_GROUP``, ``CURRENT_PATH``, ``CURRENT_ROLE``, ``CURRENT_ROW``, ``CURRENT_SCHEMA``, ``CURRENT_TIME``, ``CURRENT_TRANSFORM_GROUP_FOR_TYPE``, ``CURRENT_USER``, ``CURSOR``

**D**
   ``DATEDIFF``, ``DATETIME``, ``DDL``, ``DEALLOCATE``, ``DECIMAL``, ``DECLARE``, ``DEFAULT``, ``DEFINE``, ``DELETE``, ``DEREF``, ``DETERMINISTIC``, ``DISALLOW``, ``DISCONNECT``, ``DISTINCT``, ``DOT``, ``DOUBLE``, ``DROP``, ``DYNAMIC``

**E**
   ``EACH``, ``ELSE``, ``END``, ``END-EXEC``, ``END_FRAME``, ``END_PARTITION``, ``EQUALS``, ``ESCAPE``, ``EXCEPT``, ``EXEC``, ``EXECUTE``, ``EXISTS``, ``EXPLAIN``, ``EXTEND``, ``EXTERNAL``, ``EXTRACT``

**F**
   ``FALSE``, ``FETCH``, ``FILTER``, ``FLOAT``, ``FOR``, ``FOREIGN``, ``FRAME_ROW``, ``FREE``, ``FRIDAY``, ``FROM``, ``FULL``, ``FUNCTION``

**G**
   ``GET``, ``GLOBAL``, ``GRANT``, ``GROUP``, ``GROUPS``

**H**
   ``HAVING``, ``HOLD``

**I**
   ``IDENTITY``, ``IMPORT``, ``IN``, ``INDICATOR``, ``INITIAL``, ``INNER``, ``INOUT``, ``INSENSITIVE``, ``INSERT``, ``INT``, ``INTEGER``, ``INTERSECT``, ``INTERVAL``, ``INTO``, ``IS``

**J**
   ``JOIN``, ``JSON_ARRAY``, ``JSON_ARRAYAGG``, ``JSON_EXISTS``, ``JSON_OBJECT``, ``JSON_OBJECTAGG``, ``JSON_QUERY``, ``JSON_SCOPE``, ``JSON_VALUE``

**L**
   ``LAG``, ``LARGE``, ``LATERAL``, ``LEADING``, ``LEFT``, ``LIKE``, ``LIKE_REGEX``, ``LIMIT``, ``LOCAL``, ``LOCALTIME``, ``LOCALTIMESTAMP``, ``LOOP``

**M**
   ``MATCH``, ``MATCHES``, ``MATCH_NUMBER``, ``MATCH_RECOGNIZE``, ``MEASURES``, ``MERGE``, ``MINUS``, ``MODIFIES``, ``MODULE``, ``MONDAY``, ``MORE``, ``MULTISET``

**N**
   ``NATIONAL``, ``NATURAL``, ``NCHAR``, ``NCLOB``, ``NEW``, ``NEXT``, ``NO``, ``NOINHERIT``, ``NONE``, ``NORMALIZE``, ``NOT``, ``NULL``, ``NUMERIC``, ``NVARCHAR``

**O**
   ``OCCURRENCES_REGEX``, ``OF``, ``OFFSET``, ``OLD``, ``OMIT``, ``ON``, ``ONLY``, ``OPEN``, ``OR``, ``ORDER``, ``ORDINAL``, ``OUTER``, ``OVER``, ``OVERLAPS``, ``OVERLAY``

**P**
   ``PARAMETER``, ``PARTITION``, ``PATTERN``, ``PER``, ``PERCENT``, ``PERIOD``, ``PERMISSION``, ``PERMUTE``, ``PORTION``, ``POSITION_REGEX``, ``PRECEDES``, ``PRECISION``, ``PREPARE``, ``PREV``, ``PRIMARY``, ``PROCEDURE``

**Q**
   ``QUALIFY``

**R**
   ``RANGE``, ``READS``, ``REAL``, ``RECURSIVE``, ``REFERENCES``, ``REFERENCING``, ``REGR_AVGX``, ``REGR_AVGY``, ``REGR_INTERCEPT``, ``REGR_R2``, ``REGR_SLOPE``, ``REGR_SXY``, ``RELEASE``, ``RESET``, ``RESOURCE``, ``RETURN``, ``RETURNS``, ``REVOKE``, ``RIGHT``, ``ROLLBACK``, ``ROLLUP``, ``ROW``, ``ROWS``

**S**
   ``SAFE_CAST``, ``SAFE_OFFSET``, ``SAFE_ORDINAL``, ``SATURDAY``, ``SAVEPOINT``, ``SCROLL``, ``SEARCH``, ``SEEK``, ``SELECT``, ``SENSITIVE``, ``SESSION_USER``, ``SET``, ``SHOW``, ``SIMILAR``, ``SKIP``, ``SMALLINT``, ``SOME``, ``SPECIFIC``, ``SPECIFICTYPE``, ``SQL``, ``SQLEXCEPTION``, ``SQLSTATE``, ``SQLWARNING``, ``STATIC``, ``STREAM``, ``SUBMULTISET``, ``SUBSET``, ``SUBSTRING``, ``SUBSTRING_REGEX``, ``SUCCEEDS``, ``SUNDAY``, ``SYMMETRIC``, ``SYSTEM``, ``SYSTEM_TIME``, ``SYSTEM_USER``

**T**
   ``TABLE``, ``TABLESAMPLE``, ``TEXT``, ``THEN``, ``THURSDAY``, ``TIMEZONE_HOUR``, ``TIMEZONE_MINUTE``, ``TINYINT``, ``TO``, ``TOP``, ``TRAILING``, ``TRANSLATE``, ``TRANSLATE_REGEX``, ``TRANSLATION``, ``TREAT``, ``TRIGGER``, ``TRIM_ARRAY``, ``TRUE``, ``TRY_CAST``, ``TUESDAY``

**U**
   ``UESCAPE``, ``UNION``, ``UNIQUE``, ``UNKNOWN``, ``UNNEST``, ``UPDATE``, ``UPSERT``, ``USAGE``, ``USER``, ``USING``

**V**
   ``VALUES``, ``VALUE_OF``, ``VARBINARY``, ``VARCHAR``, ``VARYING``, ``VERSIONING``

**W**
   ``WEDNESDAY``, ``WHEN``, ``WHENEVER``, ``WHERE``, ``WIDTH_BUCKET``, ``WINDOW``, ``WITH``, ``WITHIN``, ``WITHOUT``

	
	