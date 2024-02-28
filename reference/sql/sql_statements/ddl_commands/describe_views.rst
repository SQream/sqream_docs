.. _describe_views:

**************
DESCRIBE VIEWS
**************

The ``DESCRIBE VIEWS`` command enables creating a list of database views. 

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] VIEWS [ DATABASE  <database_name> ] [ SCHEMA <schema_name> ] [ LIKE '<pattern>' ]

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``DATABASE``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - The name of the database to search within
   * - ``SCHEMA``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - The name of the schema to search within
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match


   
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``created_on``
     - ``DATE``
     - Displays the table creation timestamp
   * - ``name``
     - ``TEXT``
     - Displays the name of the view
   * - ``database``
     - ``TEXT``
     - Displays the name of the database
   * - ``schema``
     - ``TEXT``
     - Displays the name of the schema
   * - ``sql``
     - ``TEXT``
     - Displays the SQL statement used to create the view

Examples
========

.. code-block:: sql

	DESCRIBE VIEWS;
 
	created_on         |name              |database|schema|sql                                                                                             |
	-------------------+------------------+--------+------+------------------------------------------------------------------------------------------------+
	2022-12-15 07:29:07|cool_animals_view |master  |public|create view "public".cool_animals_view as  select * from cool_animals;                          |
	2022-12-15 15:12:29|only_heavy_animals|master  |public|create view "public".only_heavy_animals as  select *  from cool_animals  where    weight > 1000;|

.. code-block:: sql

	DESCRIBE VIEWS LIKE 'only%';
 
	created_on         |name                  |database|schema|sql                                                                                                 |
	-------------------+----------------------+--------+------+----------------------------------------------------------------------------------------------------+
	2022-12-15 15:12:29|only_heavy_animals    |master  |public|create view "public".only_heavy_animals as  select *  from cool_animals  where    weight > 1000;    |
	2022-12-20 11:14:16|only_agressive_animals|master  |public|create view "public".only_agressive_animals as  select *  from cool_animals  where    weight > 1000;|
	 
Permissions
===========

This command requires a ``CONNECT`` permission on the database level and a ``USAGE`` permission on the schema level.