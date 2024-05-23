:orphan:

.. _fetch_column_histogram:

**********************
FETCH COLUMN HISTOGRAM
**********************

This command displays the results of an :ref:`analyze_table` operation.

More about statistics under :ref:`cost_based_optimizer`

Syntax
======

.. code-block:: postgres

	SELECT FETCH_COLUMN_HISTOGRAM('<table_name>', '<column_name>')

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

Examples
========

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

Permissions
===========

The role must have the ``SUPERUSER`` permissions.