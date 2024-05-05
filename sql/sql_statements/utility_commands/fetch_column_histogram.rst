.. _fetch_column_histogram:

**********************
FETCH COLUMN HISTOGRAM
**********************



Syntax
======

.. code-block:: postgres

	SELECT FETCH_COLUMN_HISTOGRAM('<table_name>', '<column_name>')

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