.. _describe_tables_extended:

*****************
DESCRIBE TABLES EXTENDED
*****************
.. note::  The **DESCRIBE TABLES EXTENDED** command is not relevant to Alpha, and will be implemented in Beta.

The ``DESCRIBE TABLES EXTENDED`` command lets you list all the tables in your database, including information about storage and deleted data. You can define the ``DESCRIBE TABLES EXTENDED`` command as either ``EXTERNAL`` or ``INTERNAL``.

Syntax
==========
The following is the correct syntax for the ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres

   DESCRIBE TABLES [SCHEMA <schema_name>] [DATABASE <database_name>] EXTERNAL | INTERNAL

Parameters
============
The following parameters can be used with the ``DESCRIBE TABLES EXTENDED`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``database_name``
     - Displays the name of the database.
     - Text
   * - ``schema_name``
     - Displays the name of the table.
     - Text	 
	 
Examples
==============
The following is an example of an **internal** ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres

   DESCRIBE TABLES DATABASE master SCHEMA public INTERNAL;
   
The following is an example of an **external** ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres
   
   DESCRIBE TABLES DATABASE master SCHEMA public EXTERNAL;
   
Output
=============
Using the **internal** ``DESCRIBE_TABLES_EXTENDED`` command generates the following output:

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
   * - ``table_id``
     - Displays the ID of the table.
     - Integer
     - 0	 
   * - ``schema_name``
     - Displays the name of the schema.
     - Text
     - public
   * - ``table_name``
     - Displays the name of the table.
     - Text
     - t5
   * - ``row_count_valid``
     - Indicates whether the row count is valid or invalid.
     - Boolean
     - true
   * - ``row_count_valid``
     - Displays whether the row count is valid or invalid.
     - Boolean
     - 1
   * - ``row_count``
     - Displays the amount of rows in the table.
     - Integer
     - 0

Using the **external** ``DESCRIBE_TABLES_EXTENDED`` command generates the following output:

master,3,public,t4,0,2022-05-02 15:25:57

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
   * - ``table_id``
     - Displays the ID of the table.
     - Integer
     - 3	 
   * - ``schema_name``
     - Displays the name of the schema.
     - Text	
     - public
   * - ``table_name``
     - Displays the name of the table.
     - Text
     - t4	 
   * - ``format``
     - Indicates whether the table is formatted or not.
     - Boolean
     - 0	 
   * - ``created``
     - Displays the table's creation date and timestamp.
     - Date
     - 2022-05-02 15:25:57	 

Examples
===========
The following is an example of the generated output for the **internal** ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres

   master,0,public,t5,true,1,0

The following is an example of the generated output for the **external** ``DESCRIBE TABLES EXTENDED`` command:

.. code-block:: postgres

   master,3,public,t4,0,2022-05-02 15:25:57

Permissions
=============
**Comment** - *What are the permissions?*