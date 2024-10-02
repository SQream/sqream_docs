:orphan:

.. _where:

*****
WHERE
*****

The ``WHERE`` clause filters records that meet a specified condition.

Syntax
======

.. code-block:: postgres

	WHERE <condition>
   
Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``condition``
     - The condition to be met for a row to be included in the result set

Examples
========

.. code-block:: psql

	SELECT
	  *
	FROM
	  employees
	WHERE
	  salary > 50000;



