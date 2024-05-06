:orphan:

.. _truncate:

********
TRUNCATE
********

``TRUNCATE`` effectively removes all rows from a table, rendering it empty. In terms of functionality, it is equivalent to executing a ``DELETE`` statement without specifying a ``WHERE`` clause.

Syntax
======

.. code-block:: postgres

	TRUNCATE [ TABLE ] 
	  [ "<schema_name>". ]"<table_name>" [ RESTART IDENTITY | CONTINUE IDENTITY ]

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema for the table.
   * - ``table_name``
     - The name of the table to truncate.
   * - ``RESTART IDENTITY``
     - Automatically restart sequences owned by columns of the truncated table.
   * - ``CONTINUE IDENTITY``
     - Do not change the values of sequences. This is the default.

Example
=======

.. code-block:: psql
   
	TRUNCATE TABLE cool_animals CONTINUE IDENTITY;
   
Permissions
=============

The role must have the ``DELETE`` permission at the table level.