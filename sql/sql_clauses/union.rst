:orphan:

.. _union:

***********
UNION [ALL]
***********

The ``UNION`` and ``UNION ALL``clauses 

Syntax
======

.. code-block:: postgres



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


