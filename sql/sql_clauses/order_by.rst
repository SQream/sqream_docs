:orphan:

.. _order_by:

********
ORDER BY
********

The ``OREDER BY`` clause sorts the result set of a query by one or more columns.

Syntax
======

.. code-block:: postgres


   OREDER BY <column_name> [ ASC | DESC ] [, ...]
   
   column_name ::= identifier


Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column_name``
     - The column by which to order the result set
   * - ``ASC``
     - Order the result set in ascending order
   * - ``DESC``
     - Order the result set in descending order

Usage Notes
===========

The ``ORDER BY`` clause may be used in your main query. When used within a subquery, the :ref:`CBO<cost_based_optimizer>` ignores it to improve performance.


Example
=======

.. code-block:: psql

	SELECT
	  employee_id,
	  employee_name,
	  salary
	FROM
	  employees
	ORDER BY
	  salary DESC;


