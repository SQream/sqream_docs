.. _describe_tables:

*****************
DESCRIBE TABLES
*****************
The ``DESCRIBE TABLES`` command lets you list information about tables in your database. You can define the ``DESCRIBE TABLES`` command as one of the following:

* **All** - list information regarding both internal and external tables.

   ::
   
* **Internal** - list information regarding SQream native tables residing in the defined SQream database storage area.

   ::
   
* **External** - list information about tables residing as files external to the SQream database.

   ::
   
* **View** - list information regarding database views.

Syntax
==========
The following is the syntax for the ``DESCRIBE TABLES`` command:

.. code-block:: postgres

   DESCRIBE TABLES [SCHEMA <schema_name>] [DATABASE <database_name>] ALL | EXTERNAL | INTERNAL | VIEW

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
   * - ``ALL`` | ``EXTERNAL`` | ``INTERNAL`` | ``VIEW``
     - Select ``ALL``, ``EXTERNAL``, ``INTERNAL``, or ``VIEW``.
     - Information belonging to all tables, an external or internal table ,or displays information related to databases views.
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
Using the **ALL** ``DESCRIBE_TABLES`` command generates the following output:

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
     - nba	 
   * - ``table_type``
     - Displays whether the table is internal or external.
     - Text
     - Internal	 
   * - ``row_count``
     - Displays the amount of rows in the table.
     - Integer
     - 914
   * - ``created_on``
     - Displays the table creation timestamp.
     - Date
     - 2022-06-14 13:14:45
   * - ``Addtional details``
     - Displays additional table details.
     - Text
     - 
	 
The following is an example of the generated output in Studio for the **ALL** ``DESCRIBE TABLES`` command:

.. code-block:: postgres
 
   DESCRIBE TABLES SCHEMA public DATABASE master ALL;

   database_name|schema_name|table_name  |table_type|row_count|created_on         |Additional details                           |
   -------------+-----------+------------+----------+---------+-------------------+---------------------------------------------+
   master       |public     |nba         |Internal  |914      |2022-06-14 13:14:45|     		                        |
   master       |public     |cool_animals|Internal  |5        |2022-06-20 12:09:40|                                             |
   master       |public     |users	 |External  |         |2022-06-22 15:05:12|Format:parquet, Path:/var/mounts/nfsshare... |		
 
The following is an example of the generated output in Studio for the **INTERNAL** ``DESCRIBE TABLES`` command:

.. code-block:: postgres
 
   DESCRIBE TABLES SCHEMA public DATABASE master INTERNAL;

   database_name|schema_name|table_name  |table_type|row_count|created_on         |Additional details	                       |
   -------------+-----------+------------+----------+---------+-------------------+--------------------------------------------+
   master       |public     |nba         |Internal  |914      |2022-06-14 13:14:45|                                            |
   master       |public     |cool_animals|Internal  |5        |2022-06-20 12:09:40|                                            |
   	 
The following is an example of the generated output in Studio for the **EXTERNAL** ``DESCRIBE TABLES`` command:

.. code-block:: postgres

   DESCRIBE TABLES SCHEMA public DATABASE master EXTERNAL;

   database_name|schema_name|table_name  |table_type|row_count|created_on          |Additional details                          |
  --------------+-----------+------------+----------+---------+--------------------+--------------------------------------------+
   master       |public     |users	 |External  |         |2022-06-22 15:05:12 |Format:parquet, Path:/var/mounts/nfsshare...|

Permissions
=============
Using the ``DESCRIBE TABLES`` command requires ``USAGE`` permissions.