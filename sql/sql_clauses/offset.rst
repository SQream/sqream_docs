:orphan:

.. _having:

******
HAVING
******

The ``HAVING`` clause filters groups of rows created by the ``GROUP BY`` clause. Unlike the :ref:`where` clause, which filters rows before grouping, ``HAVING`` filters groups after the aggregation has been performed.

Syntax
======

.. code-block:: postgres

	SELECT <column1>, [ aggregate_function <column2> ]
	FROM <table_name>
	[ WHERE <condition1> ]
	GROUP BY <column1>
	HAVING <condition2>

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column1``
     - The columns to retrieve
   * - ``table_name``
     - The table from which to retrieve the data
   * - ``condition1``
     - Filters the rows before grouping them
   * - ``GROUP BY column1``
     - Groups the rows by the values in column1
   * - ``condition2``
     - Filters the groups based on the condition

Examples
========

.. code-block:: psql

	SELECT
	  department_id,
	  COUNT(*)
	FROM
	  employees
	GROUP BY
	  department_id
	HAVING
	  COUNT(*) > 5;
