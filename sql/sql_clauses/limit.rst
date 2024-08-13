:orphan:

.. _offset:

******
OFFSET
******

The ``OFFSET`` clause skips a specified number of rows before returning the result set.

Syntax
======

.. code-block:: postgres

	SELECT <column_name>
	FROM <table_name>
	OFFSET <number_of_rows>


Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column_name``
     - The columns to retrieve
   * - ``table_name``
     - The table from which to retrieve the data
   * - ``number_of_rows``
     - The number of rows to skip before starting to return rows


Examples
========

.. code-block:: psql

	SELECT
	  employee_id,
	  employee_name
	FROM
	  employees
	ORDER BY
	  employee_id
	LIMIT
	  10 OFFSET 20;
