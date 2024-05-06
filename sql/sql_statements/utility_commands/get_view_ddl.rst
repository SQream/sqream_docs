:orphan:

.. _get_view_ddl:

************
GET VIEW DDL
************

``GET_VIEW_DDL`` is a function that shows the :ref:`CREATE VIEW<create_view>` statement for a view.

Syntax
======

.. code-block:: postgres

	SELECT GET_VIEW_DDL(["<schema_name>".]"<view_name>")

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema
   * - ``view_name``
     - The name of the view

Examples
========

.. code-block:: postgres

	CREATE VIEW
	  angry_animals AS
	SELECT
	  *
	FROM
	  cool_animals
	WHERE
	  is_agressive = false;

   
	SELECT
	  GET_VIEW_DDL("angry_animals");
	  
	CREATE VIEW "public".angry_animals AS
	  SELECT
	     "cool_animals"."id" as "id",
	     "cool_animals"."name" as "name",
	     "cool_animals"."weight" as "weight",
	     "cool_animals"."is_agressive" as "is_agressive"
	   FROM
	     "public".cool_animals as cool_animals
	   WHERE
	     "cool_animals"."is_agressive" = false;

Exporting view DDL to a file
----------------------------

.. code-block:: postgres

	COPY
	  (
	    SELECT
	      GET_VIEW_DDL("angry_animals")
	  ) TO
	WRAPPER
	  csv_fdw
	OPTIONS
	  (LOCATION = 's3://sqream-docs/cool_animals_ddl.csv');

Permissions
===========

The role must have the ``CONNECT`` permission at the database level.
