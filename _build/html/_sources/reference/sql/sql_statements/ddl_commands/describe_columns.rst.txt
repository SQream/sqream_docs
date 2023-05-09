.. _describe_columns:

*****************
DESCRIBE COLUMNS
*****************
The ``DESCRIBE COLUMNS`` command lets you list information about columns in an internal or external table.

Syntax
==========
The following is the syntax for the ``DESCRIBE COLUMNS`` command:

.. code-block:: postgres

   DESCRIBE COLUMNS [ SCHEMA <schema_name> ] [ DATABASE  <database_name> ] TABLE <table_name>

Parameters
============
The following parameters can be used with the ``DESCRIBE COLUMNS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``DATABASE``
     - ``database_name``
     - Optional - The name of the database.
     - Text
   * - ``SCHEMA``
     - ``schema_name``
     - Optional - The name of the schema.
     - Text
   * - ``TABLE``
     - ``table_name``
     - The name of the table.
     - Text
	 
Examples
==============
The following is an example of the ``DESCRIBE COLUMNS`` command:

.. code-block:: postgres

   DESCRIBE COLUMNS DATABASE master SCHEMA public TABLE t1;
   	 
Output
=============
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
     - Text
     - master
   * - ``schema_name``
     - Displays the name of the schema.
     - Text
     - public
   * - ``table_name``
     - Displays the name of the table.
     - Text
     - cool_animals
   * - ``is_nullable``
     - Displays whether the column can contain ``null`` values.
     - Text
     - false	 
   * - ``table_id``
     - Displays the ID of the table.
     - Integer
     - 2		 
   * - ``column_name``
     - Displays the name of the column.
     - Text
     - id
   * - ``type_name``
     - Displays the data type of the column.
     - Text
     - INT
   * - ``default_value``
     - Displays the column default value if one exists.
     - Integer
     - 0
   * - ``created``
     - Displays the table's creation date and timestamp.
     - Date
     - 2022-06-09 05:06:6:33	 
   * - ``column_size``
     - Displays the size of the column in bytes.
     - Integer
     - 4 	 

The following is an example of the generated output in Studio:

.. image:: /_static/images/describe_columns.png

Permissions
=============
Using the ``DESCRIBE COLUMNS`` command requires ``USAGE`` permissions.