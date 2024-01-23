.. _describe_schemas:

****************
DESCRIBE SCHEMAS
****************

The ``DESCRIBE SCHEMAS`` command lets you list information about schemas in your cluster.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE SCHEMAS`` command:

.. code-block:: postgres

   DESC[RIBE] SCHEMAS [DATABASE <database_name>] [LIKE 'schema_name']

Parameters
==========

The following parameters can be used with the ``DESCRIBE SCHEMAS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``DATABASE``
     - ``database_name``
     - The name of the database to search within
   * - ``LIKE``
     - ``pattern``
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.
   
	
Output
======

Using the ``DESCRIBE SCHEMAS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``schema_id``
     - Displays the schema ID.
     - Integer
     - 0
   * - ``schema_name``
     - Displays the schema name.
     - Text
     - public
   * - ``schema_owner``
     - Displays the schema owner.
     - Text
     - sqream
	
Examples
========

.. code-block:: sql

	DESCRIBE SCHEMAS DATABASE master;
   	 
.. code-block:: none
	 
	schema_id|schema_name|schema_owner|
	---------+-----------+------------+
	0        |public     |sqream      |
	1        |staging_new|            |
	4        |stage      |            |
	5        |staging_1  |            |
	6        |staging_2  |            |
     
.. code-block:: sql

	DESCRIBE SCHEMAS DATABASE master LIKE '%stag%';

.. code-block:: none

	schema_id|schema_name|schema_owner|
	---------+-----------+------------+
	1        |staging_new|            |
	4        |stage      |            |
	5        |staging_1  |            |
	6        |staging_2  |            |

Permissions
===========

This command requires ``CONNECT`` permission on the database level.
