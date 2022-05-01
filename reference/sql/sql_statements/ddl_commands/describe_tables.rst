.. _describe_tables:

*****************
DESCRIBE TABLES
*****************
The ``DESCRIBE TABLES`` command lets you list all the tables in your database. This command includes an argument for listing external tables.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE TABLES [DATABASE <database_name>] [SCHEMA <schema_name>] EXTERNAL | INTERNAL | VIEW | ALL(default)

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE TABLES** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``schema_name``
     - Displays the name of the schema.
   * - ``database_name``
     - Displays the database_name.
   * - ``table type``
     - Lets you select EXTERNAL, INTERNAL, or ALL tables.
	 
Examples
==============
The following is an example of the **DESCRIBE TABLES** command:

.. code-block:: postgres

   DESCRIBE TABLES DATABASE master SCHEMA customers EXTERNAL | INTERNAL | VIEW | ALL (default)   
	 
Output
=============
Using the **DESCRIBE SCHEMAS** command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
	 - Type
   * - ``created_on``
     - Displays the date and time when the table was created.
     - Date
   * - ``name``
     - Displays the name of the table.
     - Text
   * - ``type``
     - Displays the type of table (internal/external/all).
     - Text	 
   * - ``database``
     - Displays the name of the database.
     - Text	    
   * - ``schema``
     - Displays the name of the schema.
     - Text	 
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*