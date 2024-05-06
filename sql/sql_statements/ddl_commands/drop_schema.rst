:orphan:

.. _drop_schema:

**********************
DROP SCHEMA
**********************

``DROP SCHEMA`` can be used to remove a schema.

The schema has to be empty before removal. 

SQream DB does not support dropping a schema with objects.

See also: :ref:`create_schema`, :ref:`alter_default_schema`, and :ref:`rename_schema`.

Permissions
=============

The role must have the ``DDL`` permission at the database level.

Syntax
==========

.. code-block:: sql

	DROP SCHEMA <schema_name>

	schema_name ::= identifier  


Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema to drop

Examples
===========

Dropping a schema:

.. code-block:: sql

	DROP SCHEMA sales;

Dropping a schema if it's not empty:

If a schema contains several tables, BLUE will alert you that these tables need to be dropped first. This prevents accidental dropping of full schemas.

.. code-block:: sql
   
	DROP SCHEMA sales;
	Schema 'sales' contains the following objects:
	Tables - 'sales.foo' , 'sales.bar'
	Please drop its content and then try again.
   
To drop the schema, drop the schema's tables first, and then drop the schema:

.. code-block:: sql
   
	DROP TABLE sales.foo;

	DROP TABLE sales.bar;

	DROP SCHEMA sales;

