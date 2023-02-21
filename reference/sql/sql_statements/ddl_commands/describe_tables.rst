.. _describe_tables:

*****************
DESCRIBE TABLES
*****************
The ``DESCRIBE TABLES`` command lets you list information about tables in your database.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
==========
The following is the syntax for the ``DESCRIBE TABLES`` command:

.. code-block:: postgres

   DESCRIBE TABLES:

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
   * - ``ALL``, ``EXTERNAL``, ``INTERNAL``
     - ``ALL``, ``EXTERNAL``, or ``INTERNAL``.
     - You may define the ``DESCRIBE TABLES`` command to show information related to all tables, external tables, or internal tables. The default value is ``ALL``.
     - Text	
	 
Examples
==============
Listing internal tables:

.. code-block:: postgres

   DESCRIBE TABLES DATABASE master SCHEMA public INTERNAL;
   
Listing external tables:

.. code-block:: postgres
   
   DESCRIBE TABLES DATABASE master SCHEMA public EXTERNAL;
   
Output
=============
When the set to ``ALL``, the ``DESCRIBE_TABLES`` command returns the following parameters:

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
	 
Output Examples
~~~~~~~~~~~~~~~
Listing all tables:


.. code-block:: postgres

   database_name|schema_name|table_name  |table_type|row_count|created_on         |Additional details                           |
   -------------+-----------+------------+----------+---------+-------------------+---------------------------------------------+
   master       |public     |nba         |Internal  |914      |2022-06-14 13:14:45|     		                                |
   master       |public     |cool_animals|Internal  |5        |2022-06-20 12:09:40|                                             |
   master       |public     |users	 |External  |         |2022-06-22 15:05:12|Format:parquet, Path:/var/mounts/nfsshare...     |		
 
Listing internal tables:

.. code-block:: postgres

   database_name|schema_name|table_name  |table_type|row_count|created_on         |Additional details	                       |
   -------------+-----------+------------+----------+---------+-------------------+--------------------------------------------+
   master       |public     |nba         |Internal  |914      |2022-06-14 13:14:45|                                            |
   master       |public     |cool_animals|Internal  |5        |2022-06-20 12:09:40|                                            |
   	 
Listing external tables:

.. code-block:: postgres

   database_name|schema_name|table_name  |table_type|row_count|created_on          |Additional details                          |
  --------------+-----------+------------+----------+---------+--------------------+--------------------------------------------+
   master       |public     |users	 |External  |         |2022-06-22 15:05:12 |Format:parquet, Path:/var/mounts/nfsshare...|

Permissions
=============
Using the ``DESCRIBE TABLES`` command requires ``USAGE`` permissions.