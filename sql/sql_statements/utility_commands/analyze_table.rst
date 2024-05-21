:orphan:

.. _analyze_table:

*************
ANALYZE TABLE
*************

This command generates statistics for entire tables or a specific column within a table. The command is asynchronous, meaning you can continue processing other tasks without waiting for the command to complete. The processing duration depends on the table size. The output includes the session ID and query ID, which you can use to check the status of your statistics request and to abort the statistics operation if needed.

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

* ``TEXT``
* ``NUMERIC`` 

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