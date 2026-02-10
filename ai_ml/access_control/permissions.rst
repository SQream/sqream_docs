.. _Permissions:

***********
Permissions
***********

SQream’s Python Module allows users to integrate custom Python code and functions directly. This section describes the permissions required for the AI/ML features.
For all other permissions - you can find the full permissions details here `SQream documentation <https://docs.sqream.com/en/latest/operational_guides/access_control_permissions.html>`_.

Objects
=======

* Module - A Python module that contains custom Python code and functions that can be invoked from Sqream.

* Algorithm - A registered machine-learning recipe that defines how to train a model and run inference. Sqream provides native support for Linear Regression and XGBoost, and additional algorithms can be provided via register algorithm.

* Model - A trained machine learning artifact created from an algorithm and data. models can be used for inference.

+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Permission**       | **Description**                                                                                                         |
+======================+=========================================================================================================================+
| **Database**         |                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE MODULE``    | Ability to create a new module. The role that creates the module receives all permissions (EXECUTE, DDL)                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE ALGORITHM`` | Ability to register a new algorithm. The creator receives ``USAGE`` and ``DDL`` permissions                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Schema**           |                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``CREATE MODEL``     | Ability to create a new model in the schema                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Module**           |                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``          | Ability to execute any function within a specified module                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Ability to drop a module                                                                                                |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | Encapsulates both ``EXECUTE`` and ``DDL`` permissions                                                                   |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Algorithm**        |                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``USAGE``            | Ability to create a new Python model based on the algorithm                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Ability to unregister an algorithm                                                                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | Encapsulates both ``USAGE`` and ``DDL`` permissions                                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Model**            |                                                                                                                         |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``EXECUTE``          | Ability to use a specified model for inference with the ``model_predict`` function                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``DDL``              | Ability to remove a model from the database                                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``ALL``              | Ability to drop a model                                                                                                 |
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

GRANT
--------------

Grant create module on db database to role_name:

.. code-block:: sql

	GRANT CREATE MODULE ON DATABASE db TO role_name;
	
Grant execute/ddl/all on md module to role_name:

.. code-block:: postgres

	GRANT EXECUTE,DDL,ALL ON MODULE md TO role_name;

Grant create algorithm on db database to role_name:

.. code-block:: sql

	GRANT CREATE ALGORITHM ON DATABASE db TO role_name;
	
Grant usage/ddl/all on algo ALGORITHM to role_name:

.. code-block:: postgres

	GRANT USAGE,DDL,ALL ON ALGORITHM algo TO role_name;

Grant create model on s1 schema to role_name:

.. code-block:: sql

	GRANT CREATE MODEL ON SCHEMA s1 TO role_name;
	
Grant execute/ddl/all model mod1 to role_name:

.. code-block:: sql

	GRANT EXECUTE,DDL,ALL ON MODEL s1.mod1 TO role_name;

REVOKE
---------------

Revoke create module on db database from role_name:

.. code-block:: postgres

	REVOKE CREATE MODULE ON DATABASE db FROM role_name;
	
Revoke execute/ddl/all on md module from role_name

.. code-block:: postgres

	REVOKE EXECUTE,DDL,ALL ON MODULE md FROM role_name;
	
Revoke create algorithm on db database from role_name:

.. code-block:: sql

	REVOKE CREATE ALGORITHM ON DATABASE db FROM role_name;
	
Revoke usage/ddl/all on algo ALGORITHM from role_name:

.. code-block:: postgres

	REVOKE USAGE,DDL,ALL ON ALGORITHM algo FROM role_name;

Revoke create model on s1 schema from role_name:

.. code-block:: sql

	REVOKE CREATE MODEL ON SCHEMA s1 FROM role_name;

Revoke execute/ddl/all model mod1 from role_name:

.. code-block:: sql

	REVOKE EXECUTE,DDL,ALL ON MODEL s1.mod1 FROM role_name;