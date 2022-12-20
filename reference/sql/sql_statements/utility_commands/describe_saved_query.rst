.. _describe_saved_query:

********************
DESCRIBE SAVED QUERY
********************
The ``DESCRIBE SAVED QUERY`` command returns the SQL syntax of a specific saved query.

.. note:: ``DESCRIBE`` commands use CPU.

.. tip:: You may use the :ref:`DESCRIBE_SAVED_QUERIES_LIST<describe_saved_queries_list>` command to locate any saved queries.

Syntax
==========
The following is the syntax for the ``DESCRIBE SAVED QUERY`` command:

.. code-block:: postgres

   DESCRIBE SAVED QUERY [ DATABASE <database_name>] NAME <saved_query_name>
   
Parameters
============
The following parameters can be used with the ``DESCRIBE SAVED QUERY`` command:

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
   * - ``NAME``
     - ``Saved query name``
     - Mandatory parameter for specifying the saved query name - note that this must be an exact match
     - TEXT
	 
	 
Output
=============
Using the ``DESCRIBE SAVED QUERY`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``sql``
     - The SQL syntax of the selected saved query
     - TEXT
     - “SELECT * FROM nba”





The following is the syntax for the ``DESCRIBE SAVED QUERY`` command:

.. code-block:: postgres

   DESCRIBE SAVED QUERY database master NAME 'select_all';
   
   
The following is an example of the ``DESCRIBE SAVED QUERY`` command output:

.. code-block:: postgres

	sql              
	-----------------
	SELECT * FROM nba


Permissions
=============

The role must have the ``CONNECT`` permission.