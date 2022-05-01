.. _describe_user_functions:

*****************
DESCRIBE USER FUNCTIONS
*****************
The ``DESCRIBE USER FUNCTIONS`` command lets you list all user-defined functions.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE USER FUNCTIONS [DATABASE <database_name>]

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
	 
Examples
==============
The following is an example of the **DESCRIBE USER FUNCTIONS** command:

.. code-block:: postgres

   DESCRIBE USER FUNCTIONS DATABASE master
   
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
    
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*