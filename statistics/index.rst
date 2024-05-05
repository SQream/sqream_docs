.. _index:

**********
Statistics
**********



Before You Begin
================

It is essential that you enable Cost-Based Optimizer (CBO) using the BLUE web interface.

Syntax
======

.. code-block:: postgres

	-- Initiating statistics collection

	ANALYZE TABLE 
	  <table_name> 
	COMPUTE STATISTICS FOR 
	{
	COLUMNS <column_name> [, ...]
	| ALL COLUMNS }

	-- Deleting statistics

	ALTER TABLE 
	  <table_name> 
	DROP STATISTICS FOR COLUMNS 
	  <olumn_name> [, ...]

	-- Querying statistics

	DESCRIBE COLUMNS TABLE <table_name>

	SELECT fetch_column_histogram(<table_name>, <column_name)

	-- Saving statistics

	ALTER TABLE STORE STATISTICS

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
     - Parameter Type
   * - ``table_name``
     - :ref:`Identifier<keywords_and_identifiers>`
     - Identifies the table for which to apply statistics
   * - ``column_name``
     - :ref:`Identifier<keywords_and_identifiers>`
     - Identifies the column for which to apply statistics

Examples
========

Permissions
===========


   

