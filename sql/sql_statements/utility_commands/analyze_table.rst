:orphan:

.. _analyze_table:

*************
ANALYZE TABLE
*************

This command generates statistics for an entire table or for a specific column within a table.
The command is asynchronous by default, meaning you can continue processing other tasks without waiting for the command to complete.
The processing duration depends on the table size. The output includes the session ID and query ID, which you can use as input parameter for ``STATISTICS REQUEST STATUS`` to check the status of your statistics request or using ``STATISTICS REQUEST ABORT`` to abort the statistics operation if needed.
When you specify the NOSCAN option during an ``ANALYZE`` operation, a lightweight analysis is performed. This analysis only extracts the row count of columns in a foreign table from the metadata. This process is synchronous, meaning it will complete before proceeding to other tasks. Due to the fact that it doesn't involve reading actual data, the ``ANALYZE NOSCAN`` operation is expected to finish quickly.

More about statistics under :ref:`cost_based_optimizer`

Syntax
======

.. code-block:: postgres

	ANALYZE TABLE 
	  '<table_name>' 
	COMPUTE STATISTICS FOR 
	{
	COLUMNS '<column_name>' [, ...]
	| ALL COLUMNS 
	[ NOSCAN ]
	 }

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

Usage Note
==========

The Statistics operation does not support the following column data types:

* ``NUMERIC`` (``DECIMAL``)
* ``ARRAY``

Example
=======

.. code-block:: postgres

	ANALYZE TABLE nba COMPUTE STATISTICS FOR ALL COLUMNS;
	
Output:

.. code-block:: none

	session_id                          |query_id|
	------------------------------------+--------+
	1ebafa4a-c843-4133-8335-54d295bdfdd0|1       |

Permissions
===========

The role must have the ``SUPERUSER`` permissions.
