:orphan:

.. _analyze_table:

*************
ANALYZE TABLE
*************



Syntax
======

.. code-block:: postgres

	ANALYZE TABLE 
	  '<table_name>' 
	COMPUTE STATISTICS FOR 
	{
	COLUMNS '<column_name>' [, ...]
	| ALL COLUMNS 
	 }

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
     - Parameter Type
   * - ``table_name``
     - :ref:`Identifier<keywords_and_identifiers>`
     - Identifies the table for which to apply statistics
   * - ``column_name``
     - :ref:`Identifier<keywords_and_identifiers>`
     - Identifies the column for which to apply statistics

Example
=======


Permissions
===========