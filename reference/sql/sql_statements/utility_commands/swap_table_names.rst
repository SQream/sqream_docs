.. _swap_table_names:

****************
SWAP TABLE NAMES
****************

The ``SWAP_TABLE_NAMES`` command enables you to swap the names of two tables contained within a schema. 

Syntax
======

.. code-block:: postgres

	SELECT SWAP_TABLE_NAMES (<schema_name>, <table1_name>, <table2_name>)	

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema both tables are contained within
   * - ``table_name``
     - The table name you wish to swap names for

Notes
=====

Operations like views that are pointing to table name will continue to work on the name table that renamed to the old table, depending on same properties like columns  etc.. 

Examples
========

.. code-block:: postgres


Permissions
===========