:orphan:

.. _union:

***********
UNION [ALL]
***********

The ``UNION`` set operation clause combines the result sets of two or more ``SELECT`` statements, removing duplicates.

The ``UNION ALL`` set operation clause combines the result sets of two or more ``SELECT`` statements, allowing duplicates.

Syntax
======

.. code-block:: postgres

	SELECT <column_name> [ ,... ]
	FROM <table1>
	UNION [ ALL ]
	SELECT <column_name> [ ,... ]
	FROM <table2>

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``column_name``
     - The columns to retrieve
   * - ``table1``
     - The table from which to retrieve the data
   * - ``table2``
     - The table from which to retrieve the data
   * - ``ALL``
     - Allows the ``UNION`` to return duplicate rows in the result set


Examples
========

``UNION``
---------

.. code-block:: psql

	SELECT 
	  city 
	FROM 
	  customers
	UNION ALL
	SELECT 
	  city 
	FROM 
	  suppliers;

``UNION ALL``
-------------

.. code-block:: psql

	SELECT 
	  city 
	FROM 
	  customers
	UNION ALL
	SELECT 
	  city 
	FROM 
	  suppliers;




















