.. _describe_tables:

*****************
DESCRIBE TABLES
*****************
The ``DESCRIBE TABLES`` command lets you list information about tables in your database. You can define the ``DESCRIBE TABLES`` command as one of the following:

* **Internal** - list information regarding SQream native tables residing in the defined SQream database storage area.
* **Foreign/External** - list information about tables residing as files external to the SQream database.

Syntax
==========
The following is the syntax for the ``DESCRIBE TABLES`` command:

.. code-block:: postgres

   DESCRIBE TABLES [SCHEMA <schema_name>] [DATABASE <database_name>] EXTERNAL | INTERNAL

Parameters
============
The following parameters can be used with the ``DESCRIBE TABLES`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``DATABASE``
     - ``database_name``
     - The name of the database.
     - Text
   * - ``SCHEMA``
     - ``schema_name``
     - The name of the table.
     - Text
   * - ``EXTERNAL`` | ``INTERNAL``
     - Select ``EXTERNAL`` or ``INTERNAL``
     - Information belonging to either an external or internal table.
     - Text	
	 
Example
==============
The following is an example of an **internal** ``DESCRIBE TABLES`` command:

.. code-block:: postgres

   DESCRIBE TABLES DATABASE master SCHEMA public INTERNAL;
   
The following is an example of an **external** ``DESCRIBE TABLES`` command:

.. code-block:: postgres
   
   DESCRIBE TABLES DATABASE master SCHEMA public EXTERNAL;
   
Output
=============
Using the **internal** ``DESCRIBE_TABLES`` command generates the following output:

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
   * - ``table_type``
     - Displays whether the table is internal or external.
     - Text
     - Internal	 
   * - ``row_count``
     - Displays the amount of rows in the table.
     - Integer
     - 5
   * - ``created_on``
     - Displays the table creation timestamp.
     - Date
     - 2022-06-09 05:06:33
   * - ``Addtional details``
     - Displays additional table details.
     - Text
     - 

The following is an example of the generated output in Studio for the **internal** ``DESCRIBE TABLES`` command:

.. image:: /_static/images/describe_tables_internal.png

Using the **foreign/external** ``DESCRIBE_TABLES`` command generates the following output:

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
     - external_tables		 
   * - ``table_type``
     - Displays whether the table is internal or external.
     - Text
     - External
   * - ``row_count``
     - Displays the amount of rows in the table.
     - Integer
     - 
   * - ``created_on``
     - Displays the table creation timestamp.
     - Date
     - 2022-06-06 14:15:34
   * - ``Addtional details``
     - Displays additional table details.
     - Text
     - Format: parquet, Path: hdfs://hadoop-nn.piedpiper.com

The following is an example of the generated output for the **external** ``DESCRIBE TABLES`` command:

.. image:: /_static/images/describe_tables_external.png
   
Permissions
=============
No permissions are required for the ``DESCRIBE TABLES`` command.