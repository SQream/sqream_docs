.. _describe_saved_queries_list:

***************************
DESCRIBE SAVED QUERIES LIST
***************************

The ``DESCRIBE SAVED QUERIES LIST`` command creates a list of all of your saved queries.

See also: :ref:`save_query`, :ref:`execute_saved_query`, :ref:`drop_saved_query`, :ref:`recompile_saved_query`, and :ref:`describe_saved_query`

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] SAVED QUERIES LIST [ DATABASE <database_name>] [ LIKE '<pattern>' ]
   
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
     - Data Type
   * - ``save_query_name``
     - Name of the saved query
     - ``TEXT``


Examples
========

.. code-block:: sql

	DESCRIBE SAVED QUERIES LIST;

	save_query_name   |
	------------------+
	cool_heavy_animals|
	select_all        |

.. code-block:: sql

	DESCRIBE SAVED QUERIES LIST database master LIKE 'select%';

	save_query_name|
	---------------+
	select_all     |



Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own saved queries.