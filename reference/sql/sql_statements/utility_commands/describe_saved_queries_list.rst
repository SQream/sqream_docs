.. _describe_saved_queries_list:

***************************
DESCRIBE SAVED QUERIES LIST
***************************

The ``DESCRIBE SAVED QUERIES LIST`` command creates a list of all of your saved queries.

See also: :ref:`save_query`, :ref:`execute_saved_query`, :ref:`drop_saved_query`, :ref:`recompile_saved_query`, and :ref:`describe_saved_query`

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE SAVED QUERIES LIST`` command:

.. code-block:: postgres

   DESC[RIBE] SAVED QUERIES LIST [ DATABASE <database_name>] [ LIKE '<pattern>' ]
   
Parameters
==========

The following parameters can be used with the ``DESCRIBE SAVED QUERIES LIST`` command:

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
   * - ``LIKE``
     - ``pattern``
     - Optional parameter for filtering by saved query name using wildcards 
     - TEXT
	 
	 
Output
======

Using the ``DESCRIBE SAVED QUERIES LIST`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``save_query_name``
     - Name of the saved query
     - TEXT
     - “select_all”


Examples
========

The following is the syntax for the ``DESCRIBE SAVED QUERIES LIST`` command:

.. code-block:: postgres

		DESCRIBE SAVED QUERIES LIST;

The following is an example of the ``DESCRIBE SAVED QUERIES LIST`` command output:

.. code-block:: postgres

		save_query_name   |
		------------------+
		cool_heavy_animals|
		select_all        |


The following is the syntax for the ``DESCRIBE SAVED QUERIES LIST LIKE`` command with a database specification:

.. code-block:: postgres

   DESCRIBE SAVED QUERIES LIST database master LIKE 'select%';
   
   
The following is an example of the ``DESCRIBE SAVED QUERIES LIST LIKE`` command output:

.. code-block:: postgres

	save_query_name|
	---------------+
	select_all     |



Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own saved queries.