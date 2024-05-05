.. _index:

********************
Cost-Based Optimizer
********************

The Cost-Based Optimizer (CBO) evaluates and compares the potential costs associated with different query execution plans to determine the most efficient one. The "cost" in this context refers to the estimated resource requirements and performance metrics (such as GPU usage) that each candidate query plan would entail when executed.

Before You Begin
================

It is essential that you enable Cost-Based Optimizer (CBO) using the BLUE web interface.

Syntax
======

.. code-block:: postgres

	-- Initiating statistics collection:
	ANALYZE TABLE 
	  '<table_name>' 
	COMPUTE STATISTICS FOR 
	{
	COLUMNS '<column_name>' [, ...]
	| ALL COLUMNS 
	 }

	-- Querying statistics:
	DESCRIBE COLUMNS TABLE '<table_name>'

	SELECT fetch_column_histogram('<table_name>', '<column_name>')

	-- Saving statistics:
	ALTER TABLE STORE STATISTICS

	-- Analyzing statistics status:
	STATISTICS REQUEST STATUS [sessionId '<session_id>'] queryId '<query_id>'

	-- Deleting statistics:
	ALTER TABLE 
	  '<table_name>' 
	DROP STATISTICS FOR COLUMNS 
	  '<column_name>' [, ...]

	-- Aborting Statistics:
	STATISTICS REQUEST ABORT [sessionId '<session_id>'] queryId '<query_id>'



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
   * - ``session_id``
     - :ref:`String literal<literals>`
     - Specifies the session ID
   * - ``query_id``
     - :ref:`String literal<literals>`
     - Specifies the query ID


Examples
========



Permissions
===========


   

