.. _describe_schemas:

****************
DESCRIBE SCHEMAS
****************

The ``DESCRIBE SCHEMAS`` command lets you list information about schemas in your cluster.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] SCHEMAS [DATABASE <database_name>] [LIKE 'pattern']

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
     - Filters by a specific database
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match
   
	
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``schema_id``
     - Displays the schema ID
     - ``INTEGER``
   * - ``schema_name``
     - Displays the schema name
     - ``TEXT``
   * - ``schema_owner``
     - Displays the schema owner
     - ``TEXT``
	
Examples
========

.. code-block:: sql

	DESCRIBE SCHEMAS DATABASE master;
	 
	schema_id|schema_name|schema_owner|
	---------+-----------+------------+
	0        |public     |sqream      |
	1        |staging_new|            |
	4        |stage      |            |
	5        |staging_1  |            |
	6        |staging_2  |            |
     
.. code-block:: sql

	DESCRIBE SCHEMAS DATABASE master LIKE '%stag%';

	schema_id|schema_name|schema_owner|
	---------+-----------+------------+
	1        |staging_new|            |
	4        |stage      |            |
	5        |staging_1  |            |
	6        |staging_2  |            |

Permissions
===========

This command requires ``CONNECT`` permission on the database level.
