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

The Statistics operation does not support the following column data types:

* ``TEXT``
* ``NUMERIC`` 

Examples
========

Initiating Statistics Collection
--------------------------------

The command is asynchronous, meaning you can continue processing other tasks without waiting for the command to complete. The processing duration depends on the table size. The output includes the session ID and query ID, which you can use to check the status of your statistics request and to abort the statistics operation if needed.

.. code-block:: postgres

	ANALYZE TABLE nba COMPUTE STATISTICS FOR ALL COLUMNS;
	
Output:

.. code-block:: none

	session_id                          |query_id|
	------------------------------------+--------+
	1ebafa4a-c843-4133-8335-54d295bdfdd0|1       |
	
Retrieving Statistics Request Status
------------------------------------

This command returns information about your statistics collection request, including whether or not the collection is completed.

.. code-block:: postgres

	STATISTICS REQUEST STATUS queryId '1';

Output:

.. code-block:: none

	session_id                          |query_id|submission_time        |start_execution_time   |termination_time|status   |current_column|total_num_columns|error_message|
	------------------------------------+--------+-----------------------+-----------------------+----------------+---------+--------------+-----------------+-------------+
	1ebafa4a-c843-4133-8335-54d295bdfdd0|1       |2024-05-21 10:02:30.249|2024-05-21 10:02:30.249|                |EXECUTING|3             |4                |             |
		
Querying Statistics
-------------------

When querying for statistics of a specific column, note that for nullable columns, it's required to specify that you're querying for values using the ``@val`` suffix.

.. code-block:: postgres

	SELECT FETCH_COLUMN_HISTOGRAM("nba", "number");
	
	-- Using the @val suffix:
	SELECT FETCH_COLUMN_HISTOGRAM("nba", "number@val");

If the operation hasn't finished yet, the output will indicate that ``Column has no statistics``:

.. code-block:: none

	info                    |
	------------------------+
	Column has no statistics|

If the operation has finished, the output will show the requested histogram:

.. code-block:: none

	BucketLeft|BucketRight|BucketCount|
	----------+-----------+-----------+
	         0|          0|          2|
	         1|          1|          2|
	         3|          3|          2|
	         7|          7|          1|
	        12|         12|          1|
	        13|         13|          1|
	        23|         23|          1|
	        24|         24|          1|
	        35|         35|          1|

Aborting Statistics Operation
-----------------------------

.. code-block:: postgres

	STATISTICS REQUEST ABORT sessionId '1ebafa4a-c843-4133-8335-54d295bdfdd0' queryId '1';

Output:

.. code-block:: none

	Aborted

Deleting Statistics Operation
-----------------------------

.. code-block:: postgres

	ALTER TABLE "nba" DROP STATISTICS FOR COLUMNS "number";


Permissions
===========

The role must have the ``SUPERUSER`` permissions.


