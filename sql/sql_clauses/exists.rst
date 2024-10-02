:orphan:

.. _exists:

******
EXISTS
******

The ``exists`` clause tests for the existence of any rows in a subquery.

Syntax
======

.. code-block:: postgres

	SELECT <column_name> [ ,... ]
	FROM <table_name>
	WHERE EXISTS (<subquery>)

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
     - The table from which to retrieve the data.

Returns
=======

Returns ``TRUE`` if the subquery returns one or more rows, and ``FALSE`` if the subquery returns no rows

Examples
========

.. code-block:: psql

	SELECT
	  employee_id,
	  employee_name
	FROM
	  employees
	WHERE
	  EXISTS (
	    SELECT
	      1
	    FROM
	      departments
	    WHERE
	      departments.department_id = employees.department_id
	  );




