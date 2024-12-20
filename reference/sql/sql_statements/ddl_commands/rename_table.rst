.. _rename_table:

************
RENAME TABLE
************
 
``RENAME TABLE`` can be used to rename a table. 

.. warning:: Renaming a table can void existing views that use this table. See more about :ref:`recompiling views <recompile_view>`.

Syntax
======

.. code-block:: postgres

	ALTER TABLE [schema_name.]current_name RENAME TO new_name

	schema_name ::= identifier
	
	current_name ::= identifier

	new_name ::= identifier

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified
   * - ``current_name``
     - The table name to apply the change to
   * - ``new_name``
     - The new table name
     
Examples
========

Renaming a Table
----------------

.. code-block:: postgres

	ALTER TABLE
	  public.users RENAME TO former_users;

Permissions
===========

The role must have the ``DDL`` permission at the database or table level.
