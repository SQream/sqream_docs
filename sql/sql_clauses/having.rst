:orphan:

.. _limit:

*****
LIMIT
*****

The ``LIMIT`` clause specifies the maximum number of rows that should be returned in the result set.

Syntax
======

.. code-block:: postgres

	SELECT <column_name> [ ,... ]
	FROM <table_name>
	LIMIT <number_of_rows>


Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column_name``
     - The column to retrieve
   * - ``table_name``
     - The table from which to retrieve the data
   * - ``number_of_rows``
     - The maximum number of rows to return


Examples
========

.. code-block:: psql

	SELECT
	  employee_id,
	  employee_name
	FROM
	  employees
	ORDER BY
	  employee_id ASC
	LIMIT
	  10 OFFSET 20;
