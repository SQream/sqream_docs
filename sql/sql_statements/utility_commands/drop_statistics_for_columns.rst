.. _drop_statistics_for_columns:

***************************
DROP STATISTICS FOR COLUMNS
***************************



Syntax
======

.. code-block:: postgres

	ALTER TABLE 
	  '<table_name>' 
	DROP STATISTICS FOR COLUMNS 
	  '<column_name>' [, ...]

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


Examples
========



Permissions
===========
