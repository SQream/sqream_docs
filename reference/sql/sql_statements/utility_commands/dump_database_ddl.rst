.. _dump_database_ddl:

*****************
DUMP_DATABASE_DDL
*****************

``DUMP_DATABASE_DDL()`` is a function that shows the ``CREATE`` statements for database objects including views and tables.

Syntax
======

.. code-block:: postgres

	SELECT DUMP_DATABASE_DDL()

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
 
Showing the ``CREATE`` Statements for UDFs
------------------------------------------
 
``DUMP_DATABASE_DDL`` does not show UDFs. 

To list available UDFs:

#. Retrieve UDFs from catalog:
   
   .. code-block:: postgres

	SELECT
	  *
	FROM
	  sqream_catalog.user_defined_functions;

   Output:

   .. code-block:: console

	database_name|function_id|function_name|
	-------------+-----------+-------------+
	master       |          0|add_months   |
	master       |          2|my_distance  |
   
#. Export UDFs one-by-one using :ref:`GET_FUNCTION_DDL<get_function_ddl>`.

Permissions
===========

The role must have the ``CONNECT`` permission at the database level.