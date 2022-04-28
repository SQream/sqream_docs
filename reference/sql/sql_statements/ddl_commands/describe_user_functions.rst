.. _describe_user_functions:

*****************
DESCRIBE USER FUNCTIONS
*****************
The ``DESCRIBE USER FUNCTIONS`` command lets you list all user-defined functions.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE USER FUNCTIONS [ DATABASE <database_name>] [ LIKE '<pattern>' ] [ HISTORY ]

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE USER FUNCTIONS** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``database_name``
     - Displays the name of the database.
   * - ``table type``
     - Lets you select EXTERNAL, INTERNAL, or ALL tables.
   * - ``column_name_pattern``
     - Outputs pre-defined information related to the table.
   * - ``HISTORY``
     - **Comment** - *What does HISTORY output?*
	 
Examples
==============
The following is an example of the **DESCRIBE USER FUNCTIONS** command:

.. code-block:: postgres

   DESCRIBE USER FUNCTIONS [ DATABASE <master>] [ LIKE '<pattern>' ] [ HISTORY ] 
   
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
     - Displays the date and time when the user function was created.
     - Date
   * - ``function_name``
     - Displays the name of the function.
     - Text	 
   * - ``function_id``
     - Displays the ID of the function.
     - Integer		 
   * - ``database``
     - Displays the name of the database.
     - Text	 
   * - ``arguments``
     - Displays the data types of the arguments and of the returned value.
     - Text
	 
**Comment** - *Source doc said, "V1 R&D catalog documentation for reference - functions return values should be the same as V1 catalog functions," and linked to this page: https://sqream.atlassian.net/wiki/spaces/RD/pages/1974894634/Catalog+Documentation

*Should that page be converted to a public page? What is the difference in function between the page above and this public page:* https://docs.sqream.com/en/2022.3_preview/reference/catalog_reference.html#
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*