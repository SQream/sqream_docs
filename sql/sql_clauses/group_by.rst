:orphan:

.. _group_by:

********
GROUP BY
********

The ``GROUP BY`` groups rows that have the same values in specified columns into summary rows, like aggregating data.

Syntax
======

.. code-block:: postgres

	SELECT <column1>, [ aggregate_function <column2> ]
	FROM <table_name>
	[ WHERE <condition> ]
	GROUP BY <column_name>


Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column1``
     - The column by which you want to group the data
   * - ``column2``
     - The columns to retrieve
   * - ``table_name``
     - The table from which to retrieve the data
   * - ``condition``
     - Filters the rows before grouping them
   * - ``GROUP BY column1``
     - Groups the rows by the values in column1

Examples
========

.. code-block:: psql

	SELECT
	  department_id,
	  COUNT(*)
	FROM
	  employees
	GROUP BY
	  department_id;