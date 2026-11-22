:orphan:

.. _dump_database_ddl:

*****************
DUMP_DATABASE_DDL
*****************

``DUMP_DATABASE_DDL()`` is a function that shows the ``CREATE`` statements for database objects including views and tables.

Syntax
======

.. code-block:: postgres

	SELECT DUMP_DATABASE_DDL()

Output
======

``DUMP_DATABASE_DDL`` returns a single column, ``ddl``, and includes UDFs. The statements are returned in the following order:

#. ``CREATE SCHEMA`` statements, except for the ``public`` schema
#. ``CREATE TABLE`` statements, including foreign tables
#. ``CREATE VIEW`` statements, in dependency order
#. ``SELECT SAVE_QUERY(...)`` statements for saved queries
#. ``CREATE FUNCTION`` statements for UDFs

Examples
========

.. code-block:: postgres

	SELECT
	  DUMP_DATABASE_DDL();

Exporting database DDL to a file
--------------------------------

.. code-block:: postgres

	COPY
	  (
	    SELECT 
	      DUMP_DATABASE_DDL()
	  ) TO
	WRAPPER
	  csv_fdw
	OPTIONS
	  (LOCATION = 's3://sqream-docs/database.ddl');
 
Permissions
===========

The role must have the ``CONNECT`` permission at the database level.