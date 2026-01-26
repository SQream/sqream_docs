.. _Permissions:

***********
Permissions
***********

SQream’s Python Module allows users to integrate custom Python code and functions directly. This section describes the permissions required for the AI/ML features.
For all other permissions - you can find the full permissions details here `SQream documentation <https://docs.sqream.com/en/latest/operational_guides/access_control_permissions.html>`.

Objects
=======

* Module - Python Module enables users to integrate custom Python code and functions directly

* Algorithm - SQream algorithms are machine learning models that run directly in SQream’s GPU-accelerated environment, with native support for Linear Regression and XGBoost and extensibility via Python modules.

* Model - Models are trained machine-learning artifacts that learn patterns from data and can make predictions or decisions.

+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Permission**       | **Description**                                                                                                         |
+======================+=========================================================================================================================+
|**Module**                                                                                                                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``           | Ability to create a new module, the role that create the module receives all permissions for this module (Execute, DDL) |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``          | The ability to execute any function within a specified module                                                           |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | The ability to remove a module from the database                                                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | This option encapsulates both ``EXECUTE`` and ``DDL`` permissions                                                       |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Algorithm**                                                                                                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``           | The ability to register a new algorithm , the role that create the algorithm receives all permissions - Usage and DDL   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE````          | The ability to create a new Python model based on the algorithm                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | The ability to drop an algorithm                   																	 |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | This option encapsulates both ``USAGE`` and ``DDL`` permissions.     					             					 |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Model**                                                                                                                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE``           | The ability to register a new model                                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``          | The ability to use a specified model for inference with a PREDICT function                                              |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | The ability to remove a model from the database                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | This option encapsulates both ``EXECUTE`` and ``DDL`` permissions.                                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+

Syntax
======

Permissions may be granted or revoked using the following syntax.

GRANT
------

.. code-block:: postgres

	-- Grant create module permissions to a role:
	GRANT {
	CREATE MODULE
	ON DATABASE <database> [, ...]
	TO <role> [, ...]

	-- Grant execute/ddl/all on module:
	GRANT {
	EXECUTE 
	| DDL
	| ALL
	ON MODULE <module> [, ...]
	TO <role> [, ...]

	-- Grant create algorithm permissions to a role:
	GRANT {
	CREATE ALGORITHM
	ON DATABASE <database> [, ...]
	TO <role> [, ...]

	-- Grant usage/ddl/all on algorithm:
	GRANT {
	USAGE 
	| DDL
	| ALL
	ON ALGORITHM <algorithm> [, ...]
	TO <role> [, ...]
	
	-- Grant create model at the schema level:
	GRANT {
	CREATE MODEL
	ON SCHEMA <schema> [, ...]
	TO <role> [, ...]
	
	-- Grant execute/ddl/all on model:
	GRANT {
	EXECUTE 
	| DDL
	| ALL
	ON MODEL <schema>.<model> [, ...]
	TO <role> [, ...]

REVOKE
------

.. code-block:: postgres

	-- Revoke create module permissions from a role:
	REVOKE {
	CREATE MODULE
	ON DATABASE <database> [, ...]
	FROM <role> [, ...]

	-- Revoke execute/ddl/all permissions on module:
	REVOKE {
	EXECUTE 
	| DDL
	| ALL
	ON MODULE <module> [, ...]
	FROM <role> [, ...]


	-- Revoke create algorithm permissions to a role:
	REVOKE {
	CREATE ALGORITHM
	ON DATABASE <database> [, ...]
	FROM <role> [, ...]

	-- Revoke usage/ddl/all on algorithm:
	REVOKE {
	USAGE 
	| DDL
	| ALL
	ON ALGORITHM <algorithm> [, ...]
	FROM <role> [, ...]
	
	-- Revoke create model at the schema level:
	REVOKE {
	CREATE MODEL
	ON SCHEMA <schema> [, ...]
	FROM <role> [, ...]
	
	-- Revoke execute/ddl/all on model:
	REVOKE {
	EXECUTE 
	| DDL
	| ALL
	ON MODEL <schema>.<model> [, ...]
	FROM <role> [, ...]
	
	
Examples
========

Examples
========

GRANT
--------------

Grant create module on db database to role_name:

.. code-block:: sql

	GRANT CREATE MODULE ON DATABASE db TO role_name;
	
Grant execute/ddl/all on md module to role_name:

.. code-block:: postgres

	GRANT EXECUTE,DDL,ALL ON MODULE md TO role_name;
	

REVOKE
---------------

Revoke create module on db database from role_name:

.. code-block:: postgres

	REVOKE CREATE MODULE ON DATABASE db FROM role_name;
	
Revoke execute/ddl/all on md module from role_name

.. code-block:: postgres

	REVOKE EXECUTE,DDL,ALL ON MODULE md FROM role_name;
	



