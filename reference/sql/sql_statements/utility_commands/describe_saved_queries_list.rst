.. _describe_saved_queries_list:

*****************
DESCRIBE SAVED QUERIES LIST
*****************
The ``DESCRIBE SAVED QUERIES LIST`` command creates a list of all of your saved queries.

.. note:: ``DESCRIBE`` commands use CPU.

Syntax
==========
The following is the syntax for the ``DESCRIBE SAVED QUERIES LIST`` command:

.. code-block:: postgres

   DESCRIBE SAVED QUERIES LIST [ DATABASE <database_name>] [ LIKE '<pattern>' ]
   
Parameters
============
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
=============
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


The following is the syntax for the ``DESCRIBE SAVED QUERIES LIST LIKE`` command:

.. code-block:: postgres

   DESCRIBE SAVED QUERIES LIST database master LIKE 'select%';
   
   
The following is an example of the ``DESCRIBE SAVED QUERIES LIST LIKE`` command output:

.. code-block:: postgres

	save_query_name|
	---------------+
	select_all     |



Permissions
=============

The role must have the ``CONNECT`` permission.