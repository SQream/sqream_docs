:orphan:

.. _distinct:

********
DISTINCT
********

The ``DISTINCT`` clause returns only unique (distinct) values from a column or a set of columns, eliminating duplicate rows in the result set.

Syntax
======

.. code-block:: postgres

	SELECT DISTINCT <column_name> [ ,... ]
	FROM <table_name>
   
Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column_name``
     - The columns from which to retrieve distinct values
   * - ``table_name``
     - The table from which to retrieve the data

Examples
========

.. code-block:: psql

	SELECT
	  COUNT(DISTINCT department_id)
	FROM
	  employees;



