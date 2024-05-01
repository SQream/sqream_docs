.. _describe_columns:

****************
DESCRIBE COLUMNS
****************

The ``DESCRIBE COLUMNS`` command lets you list information about table columns.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: postgres

   DESC[RIBE] COLUMNS [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] TABLE <table_name> [LIKE 'pattern']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``DATABASE``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - Filters by a specific database
   * - ``SCHEMA``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - Filters by a specific schema
   * - ``TABLE``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - Identifies the specific table for which you want to retrieve column descriptions
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match
   
	 
Output
======

Using the ``DESCRIBE COLUMNS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``database_name``
     - ``TEXT``
     - Displays the name of the database
   * - ``schema_name``
     - ``TEXT``
     - Displays the name of the schema
   * - ``table_name``
     - ``TEXT``
     - Displays the name of the table
   * - ``is_nullable``
     - ``TEXT`` 
     - Displays whether the column can contain ``null`` values
   * - ``table_id``
     - ``INTEGER``
     - Displays the ID of the table 
   * - ``column_name``
     - ``TEXT``
     - Displays the name of the column
   * - ``type_name``
     - ``TEXT``
     - Displays the data type of the column
   * - ``default_value``
     - ``INTEGER``
     - Displays the column default value if one exists
   * - ``created``
     - ``DATE``
     - Displays the table's creation date and timestamp
   * - ``column_size``
     - ``INTEGER``	
     - Displays the size of the column in bytes
	 
Examples
========

.. code-block:: sql

	DESCRIBE COLUMNS DATABASE master SCHEMA public TABLE nba;

	database_name|schema_name|table_name|is_nullable|column_name|type_name|default_value|created            |column_size|
	-------------+-----------+----------+-----------+-----------+---------+-------------+-------------------+-----------+
	master       |public     |nba       |true       |name       |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |team       |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |number     |INT      |0            |2023-08-08 06:47:47|4          |
	master       |public     |nba       |true       |position   |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |age        |INT      |0            |2023-08-08 06:47:47|4          |
	master       |public     |nba       |true       |height     |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |weight     |INT      |0            |2023-08-08 06:47:47|4          |
	master       |public     |nba       |true       |college    |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |salary     |INT      |0            |2023-08-08 06:47:47|4          |
	master       |public     |nba       |true       |name0      |TEXT     |             |2023-08-08 06:47:47|0          |

.. code-block:: sql

	DESCRIBE COLUMNS DATABASE master SCHEMA public TABLE nba LIKE '%name%';

	database_name|schema_name|table_name|is_nullable|column_name|type_name|default_value|created            |column_size|
	-------------+-----------+----------+-----------+-----------+---------+-------------+-------------------+-----------+
	master       |public     |nba       |true       |name       |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |name0      |TEXT     |             |2023-08-08 06:47:47|0          |

Permissions
===========

This command requires ``USAGE`` permission on the schema level.
