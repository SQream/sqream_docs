.. _cost_based_optimizer:

********************
Cost-Based Optimizer
********************

The Cost-Based Optimizer (CBO) evaluates and compares the potential costs associated with different query execution plans to determine the most efficient one. The "cost" in this context refers to the estimated resource requirements and performance metrics (such as GPU usage) that each candidate query plan would entail when executed.

After adding or deleting data from a table on which we executed ``ANALYZE``, we must execute ANALYZE once more in terms of updating the statistics.  

Before You Begin
================

It is essential that you enable Cost-Based Optimizer (CBO) using the BLUE web interface.

Syntax
======

.. code-block:: postgres

	-- Initiating statistics collection:
	ANALYZE TABLE '<table_name>' COMPUTE STATISTICS FOR { COLUMNS '<column_name>' [, ...] | ALL COLUMNS }

	-- Analyzing statistics status:
	STATISTICS REQUEST STATUS [sessionId '<session_id>'] queryId '<query_id>'

	-- Querying statistics:
	SELECT FETCH_COLUMN_HISTOGRAM("<table_name>", "<column_name>")

	-- Aborting Statistics:
	STATISTICS REQUEST ABORT [sessionId '<session_id>'] queryId '<query_id>'

	-- Deleting statistics:
	ALTER TABLE '<table_name>' DROP STATISTICS FOR COLUMNS '<column_name>' [, ...]

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


Usage Note
==========

The Statistics operation does not support ``TEXT`` and ``NUMERIC`` columns. 

Best Practice
=============

A best practice of following statistics is:

1. Executing ``ANALYZE TABLE`` 

Examples
========

Initiating Statistics Collection
--------------------------------
The command is asynchronous 
Depending on the tale size, this command may take a while to process. 

The output is the session ID + query ID

.. code-block:: postgres

	ANALYZE TABLE nba COMPUTE STATISTICS FOR COLUMNS number;
	
Output:

.. code-block:: none

	session_id                          |query_id|
	------------------------------------+--------+
	ba0cc085-35a3-48f3-8c97-fedc636dccc8|26      |
	
Analyzing Statistics Request Status
-----------------------------------

To determine whether or not the collection of your statistics request is completed.

.. code-block:: postgres

	STATISTICS REQUEST STATUS queryId '26';

Output:

.. code-block:: none

	session_id                          |query_id|submission_time        |start_execution_time   |termination_time       |status             |current_column|total_num_columns|error_message|
	------------------------------------+--------+-----------------------+-----------------------+-----------------------+-------------------+--------------+-----------------+-------------+
	ba0cc085-35a3-48f3-8c97-fedc636dccc8|26      |2024-05-20 10:37:25.747|2024-05-20 10:37:25.748|2024-05-20 10:37:28.885|EXECUTION_SUCCEEDED|0             |0                |             |
		
Querying Statistics
-------------------

Nullable columns require @val

.. code-block:: postgres

	SELECT FETCH_COLUMN_HISTOGRAM("lineitem", "l_orderkey");

Output:

.. code-block:: none

	info                                 |
	-------------------------------------+
	Table is empty (has no non-null data)|

Aborting Statistics Operation
-----------------------------

.. code-block:: postgres

	STATISTICS REQUEST ABORT sessionId 'bda37dc1-8917-4e76-bcee-c139a7864948' queryId '23';

Output:

.. code-block:: none

	Error: Aborted.

Deleting Statistics Operation
-----------------------------

.. code-block:: postgres

	ALTER TABLE "lineitem" DROP STATISTICS FOR COLUMNS "l_orderkey";


Permissions
===========

The role must have the ``SUPERUSER`` permissions.
   

