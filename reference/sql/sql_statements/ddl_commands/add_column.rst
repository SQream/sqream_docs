.. _add_column:

**********
ADD COLUMN
**********

The ``ADD COLUMN`` command is used to add columns to an existing table.

Syntax
======

.. code-block:: postgres

	ALTER TABLE [schema_name.]table_name ADD COLUMN column_def [, ADD COLUMN column_def ...]

	schema_name ::= identifier
	
	table_name ::= identifier
	
	column_def ::= 
	  { column_name type_name [ default ] [ column_constraint ] CHECK('CS "compression_type"') }

	column_name ::= identifier
	
	column_constraint ::=
	  { NOT NULL | NULL }
	  
	default ::=
	  DEFAULT default_value

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified
   * - ``table_name``
     - The table name to apply the change to
   * - ``ADD COLUMN column_def``
     - A comma separated list of ADD COLUMN commands
   * - ``column_def``
     - A column definition. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally
   
Usage Notes
=========== 

When adding an empty column, the default values for that column will be set to ``NULL``.

Each column needs its own ``ADD COLUMN``, as shown in the "Adding Several Columns in One Command" example. ``ADD COLUMN a INT, b INT`` is a parse error.

Examples
========
   
Adding a Simple Column with a Default Value
-------------------------------------------

.. code-block:: postgres

	ALTER TABLE
	  cool_animals
	ADD
	  COLUMN number_of_eyes INT DEFAULT 2 NOT NULL;   

Adding Several Columns in One Command
-------------------------------------

.. code-block:: postgres

	ALTER TABLE
	  cool_animals
	ADD
	  COLUMN number_of_eyes INT DEFAULT 2 NOT NULL,
	ADD
	  COLUMN date_seen DATE DEFAULT '2019-08-01';
	 
Adding Compressed Column
------------------------

.. code-block::

	ALTER TABLE
	  coo_animals
	ADD
	  COLUMN animal_salary INT CHECK('CS "dict"');

Follow SQreamDB :ref:`compression guide<compression>` for compression types and methods.

Permissions
===========

The role must have the ``DDL`` permission on the table (or ``SUPERUSER`` on the table's schema or database), and ``USAGE`` on the table's schema. ``DDL`` granted at the database level does not satisfy this.