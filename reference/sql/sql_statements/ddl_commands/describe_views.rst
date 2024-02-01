.. _describe_views:

**************
DESCRIBE VIEWS
**************

The ``DESCRIBE VIEWS`` command enables creating a list of database views. 

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE VIEWS`` command:

.. code-block:: postgres

   DESC[RIBE] VIEWS [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] [ LIKE '<pattern>' ]

Parameters
==========

The following parameters can be used with the ``DESCRIBE VIEWS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``DATABASE``
     - ``database_name``
     - Optional parameter for specifying the name of the database to use, if not specified current database will be used
     - TEXT
   * - ``SCHEMA``
     - ``schema_name``
     - Optional parameter for specifying the name of the schema to use, if not specified current schema will be used
     - TEXT
   * - ``LIKE``
     - ``pattern``
     - Optional parameter for filtering by view name using wildcards
     - TEXT
	 
   
   
Output
======

Using the ``DESCRIBE_TABLES`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``created_on``
     - Displays the table creation timestamp
     - Date
     - 2022-06-14 13:14:45
   * - ``name``
     - Displays the name of the view
     - TEXT
     - nba  
   * - ``database``
     - Displays the name of the database
     - TEXT
     - master
   * - ``schema``
     - Displays the name of the schema
     - TEXT
     - public
   * - ``sql``
     - Displays the SQL statement used to create the view
     - TEXT
     - create view "public".nba_view as  select * from nba;	 


The following is the syntax for the ``DESCRIBE VIEWS`` command:

.. code-block:: postgres

		DESCRIBE VIEWS;
	 
The following is an example of the ``DESCRIBE VIEWS`` command output:

.. code-block:: postgres
 
		created_on         |name              |database|schema|sql                                                                                                   |
		-------------------+------------------+--------+------+------------------------------------------------------------------------------------------------------+
		2022-12-15 07:29:07|cool_animals_view |master  |public|create view "public".cool_animals_view as¶  select * from cool_animals;¶¶                             |
		2022-12-15 15:12:29|only_heavy_animals|master  |public|create view "public".only_heavy_animals as¶  select *¶  from cool_animals¶  where¶    weight > 1000;¶¶|
 
The following is the syntax for the ``DESCRIBE VIEWS LIKE`` command:

.. code-block:: postgres

		DESCRIBE VIEWS LIKE 'only%';
 
The following is an example of the ``DESCRIBE VIEWS LIKE`` command output:

.. code-block:: postgres
 
		created_on         |name                  |database|schema|sql                                                                                                       |
		-------------------+----------------------+--------+------+----------------------------------------------------------------------------------------------------------+
		2022-12-15 15:12:29|only_heavy_animals    |master  |public|create view "public".only_heavy_animals as¶  select *¶  from cool_animals¶  where¶    weight > 1000;¶¶    |
		2022-12-20 11:14:16|only_agressive_animals|master  |public|create view "public".only_agressive_animals as¶  select *¶  from cool_animals¶  where¶    weight > 1000;¶¶|
	 
Permissions
===========

This command requires a ``CONNECT`` permission on the database level and a ``USAGE`` permission on the schema level.