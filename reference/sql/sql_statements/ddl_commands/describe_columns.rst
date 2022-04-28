.. _describe_columns:

*****************
DESCRIBE COLUMNS
*****************
The ``DESCRIBE COLUMNS`` command lets you list all columns in an internal or external table.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE COLUMNS [ SCHEMA <schema_name> ] [ DATABASE  <database_name> ] TABLE <table_name> [ LIKE '<column_name_pattern>' ][ HISTORY ]

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE COLUMNS** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``schema_name``
     - Displays the name of the schema.
   * - ``database_name``
     - Displays the name of the database.
   * - ``table``
     - Displays the name of the table.
   * - ``table type``
     - Lets you select EXTERNAL, INTERNAL, or ALL tables.
   * - ``column_name_pattern``
     - Outputs pre-defined information related to the table.
   * - ``HISTORY``
     - **Comment** - *What does HISTORY output?*
	 
Examples
==============
The following is an example of the **DESCRIBE COLUMNS** command:

.. code-block:: postgres

   DESCRIBE COLUMNS [ SCHEMA <customers> ] [ DATABASE  <public> ] TABLE <local> [ LIKE '<column_name_pattern>' ][ HISTORY ]
   
**Comment** - *Please confirm if the example above is correct. I don't know what goes in the "column_name_pattern" variable.*
	 
Output
=============
Using the **DESCRIBE COLUMNS** command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
	 - Type
   * - ``created_on``
     - Displays the date and time when the table was created.
     - Date
   * - ``table``
     - Displays the name of the table.
     - Text
   * - ``database``
     - Displays the name of the database.
     - Text	   	 
   * - ``schema``
     - Displays the name of the schema.
     - Text	 
   * - ``column_name``
     - Displays the name of the column.
     - Text		 
   * - ``data_type``
     - Displays the data type.
     - Text	
   * - ``null``
     - Displays whether the column can contain ``null`` values.
     - Text	
   * - ``default_value``
     - Displays the columns default value if one exists.
     - Text	
   * - ``auto-increment``
     - Auto-increments start values if they exist. **Comment** - *See Shachar's comment.*
     - 	
   * - ``dropped-on``
     - Returned if the HISTORY variable is used, returning ``NULL`` when no columns have been dropped.
     - Date
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*