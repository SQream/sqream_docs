.. _describe_columns:

****************
DESCRIBE COLUMNS
****************

The ``DESCRIBE COLUMNS`` command lets you list information about table columns.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE COLUMNS`` command:

.. code-block:: postgres

   DESCRIBE COLUMNS [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] TABLE <table_name> [LIKE 'column_name']
   DESC COLUMNS [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] TABLE <table_name> [LIKE 'column_name']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``DATABASE``
     - ``database_name``
     - Optional - The name of the database.
   * - ``SCHEMA``
     - ``schema_name``
     - Optional - The name of the schema.
   * - ``TABLE``
     - ``table_name``
     - The name of the table.
   * - ``LIKE``
     - ``column_name``
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.
   
	 
Output
======

Using the ``DESCRIBE COLUMNS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``database_name``
     - Displays the name of the database.
     - TEXT
     - master
   * - ``schema_name``
     - Displays the name of the schema.
     - TEXT
     - public
   * - ``table_name``
     - Displays the name of the table.
     - TEXT
     - cool_animals
   * - ``is_nullable``
     - Displays whether the column can contain ``null`` values.
     - TEXT
     - false	 
   * - ``table_id``
     - Displays the ID of the table.
     - INTEGER
     - 2		 
   * - ``column_name``
     - Displays the name of the column.
     - TEXT
     - id
   * - ``type_name``
     - Displays the data type of the column.
     - TEXT
     - INT
   * - ``default_value``
     - Displays the column default value if one exists.
     - INTEGER
     - 0
   * - ``created``
     - Displays the table's creation date and timestamp.
     - DATE
     - 2022-06-09 05:06:6:33	 
   * - ``column_size``
     - Displays the size of the column in bytes.
     - Integer
     - 4 	
	 
Examples
========

The following is an example of the ``DESCRIBE COLUMNS`` command:

.. code-block:: sql

	DESCRIBE COLUMNS DATABASE master SCHEMA public TABLE nba;
   	 
 
Output:

.. code-block:: none

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
	
Output:

.. code-block:: none

	database_name|schema_name|table_name|is_nullable|column_name|type_name|default_value|created            |column_size|
	-------------+-----------+----------+-----------+-----------+---------+-------------+-------------------+-----------+
	master       |public     |nba       |true       |name       |TEXT     |             |2023-08-08 06:47:47|0          |
	master       |public     |nba       |true       |name0      |TEXT     |             |2023-08-08 06:47:47|0          |

Permissions
===========

This command requires ``USAGE`` permission on the schema level.
