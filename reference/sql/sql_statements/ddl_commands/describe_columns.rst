.. _describe_columns:

*****************
DESCRIBE COLUMNS
*****************
The ``DESCRIBE COLUMNS`` command lets you list all columns in an internal or external table.

Syntax
==========
The following is the correct syntax for the ``DESCRIBE COLUMNS`` command:

.. code-block:: postgres

   DESCRIBE COLUMNS [SCHEMA <schema_name>] [DATABASE <database_name>][TABLE <table_name>]

Parameters
============
The following parameters can be used with the ``DESCRIBE COLUMNS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``database_name``
     - The name of the database.
   * - ``schema_name``
     - The name of the schema.
   * - ``table``
     - The name of the table.
	 
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
   * - ``table_id``
     - Displays the ID of the table.
     - Integer
     - 2		 
   * - ``table_name``
     - Displays the name of the table.
     - Text
     - t1	
   * - ``is_nullable``
     - Displays whether the column can contain ``null`` values.
     - Text
     - true
   * - ``column_id``
     - Displays the ID of the column.
     - Integer
     - 1
   * - ``column_name``
     - Displays the name of the column.
     - Text
     - xint		 
   * - ``type_name``
     - Displays the name of the type.
     - Text
     - INT
   * - ``column_size``
     - Displays the size of the column.
     - Integer
     - 4 	 
   * - ``has_default``
     - Indicates whether the column has a default value or not.
     - Boolean
     - 1		 
   * - ``default_value``
     - Displays the column default value if one exists.
     - Integer
     - 0		 
   * - ``compression_strategy``
     - Displays the column's default strategy.
     - Text
     - default
   * - ``created``
     - Displays the table's creation date and timestamp.
     - Date
     - 2022-04-28 08:00:36
   * - ``altered``
     - Displays the table's creation date and timestamp.
     - Date
     - 2022-04-28 08:00:36
	      
Example
===========
The following is an example of the generated output:

.. code-block:: postgres

   master,public,2,t1,true,1,xint,INT,4,1,0,default,2022-04-28 08:00:36,2022-04-28 08:00:36

Permissions
=============
**Comment** - *What are the permissions?*