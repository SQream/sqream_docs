.. _cost_based_optimizer:

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
	SELECT FETCH_COLUMN_HISTOGRAM("<table_name>", "<column_name>")

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

Initiating Statistics Collection
--------------------------------

.. code-block:: postgres

	ANALYZE TABLE lineitem COMPUTE STATISTICS FOR COLUMNS l_orderkey;
	
Output:

.. code-block:: none

	session_id                          |query_id|
	------------------------------------+--------+
	bda37dc1-8917-4e76-bcee-c139a7864948|23      |
	
Analyzing Statistics Request Status
-----------------------------------

.. code-block:: postgres

	STATISTICS REQUEST STATUS queryId '23';

Output:

.. code-block:: none

	session_id                          |query_id|submission_time        |start_execution_time|termination_time|status   |current_column|total_num_columns|error_message|
	------------------------------------+--------+-----------------------+--------------------+----------------+---------+--------------+-----------------+-------------+
	bda37dc1-8917-4e76-bcee-c139a7864948|23      |2024-05-06 11:12:55.121|NULL                |NULL            |SUBMITTED|0             |0                |NULL         |
	
Querying Statistics
-------------------

.. code-block:: postgres

	SELECT FETCH_COLUMN_HISTOGRAM("lineitem", "l_orderkey");
	
Output:
	
.. code-block:: none



Deleting Statistics Operation
-----------------------------

.. code-block:: postgres

	ALTER TABLE
	  "lineitem"
	DROP STATISTICS FOR COLUMNS
	  "l_orderkey";

Output:

.. code-block:: none



Aborting Statistics Operation
-----------------------------

.. code-block:: postgres

	STATISTICS REQUEST ABORT sessionId 'bda37dc1-8917-4e76-bcee-c139a7864948' queryId '23';

Output:

.. code-block:: none


Permissions
===========


   

