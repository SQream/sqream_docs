.. _get_ddl:

*******
GET DDL
*******

The ``GET DDL`` function retrieves the Data Definition Language (DDL) statement used to create a table. It may include additional information that was added by SQreamDB (e.g., explicit ``NULL`` constraints). 

See also: :ref:`GET_VIEW_DDL<get_view_ddl>`, :ref:`DUMP_DATABASE_DDL<dump_database_ddl>`, :ref:`GET_FUNCTION_DDL<get_function_ddl>`

Syntax
======

.. code-block:: postgres

	SELECT
	  GET_DDL(['<schema_name>'.]'<table_name>')

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema
   * - ``table_name``
     - The name of the table

Examples
========


.. code-block:: postgres

	-- Create a table:
	CREATE TABLE
	  cool_animals (
	    id INT NOT NULL,
	    name TEXT NOT NULL,
	    weight FLOAT,
	    is_agressive BOOL DEFAULT false NOT NULL
	  );

	-- Get table ddl:
	SELECT
	  GET_DDL('cool_animals');

	-- Result:
	CREATE TABLE
	  'public'.'cool_animals' (
	    'id' INT NOT NULL,
	    'name' TEXT NOT NULL,
	    'weight' DOUBLE NULL,
	    'is_agressive' BOOL DEFAULT FALSE NOT NULL
	  );

Exporting table DDL to a file
-----------------------------

.. code-block:: postgres

	COPY
	  (
	    SELECT
	      GET_DDL('cool_animals')
	  ) TO
	WRAPPER
	  csv_fdw
	OPTIONS
	  (LOCATION = 's3://sqream-docs/cool_animals_ddl.csv');

Permissions
=============

The role must have the ``CONNECT`` permission at the database level.