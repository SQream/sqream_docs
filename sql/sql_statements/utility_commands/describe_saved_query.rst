:orphan:

.. _describe_saved_query:

********************
DESCRIBE SAVED QUERY
********************

The ``DESCRIBE SAVED QUERY`` command returns the SQL syntax of a specific saved query.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

See also: :ref:`save_query`, :ref:`execute_saved_query`, :ref:`drop_saved_query`, :ref:`recompile_saved_query`, and :ref:`describe_saved_queries_list`

Syntax
======

.. code-block:: sql

   DESC[RIBE] SAVED QUERY [ DATABASE <database_name>] NAME "<saved_query_name>"
   
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
   * - ``NAME``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - The name of the saved query
 
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``sql``
     - ``TEXT``
     - The SQL syntax of the selected saved query

Example
=======

.. code-block:: sql

	DESCRIBE SAVED QUERY DATABASE master NAME "SelectAll";

	sql              
	-----------------
	SELECT * FROM nba


Permissions
===========

This command requires ``SUPERUSER`` permission, except when a role queries its own saved queries.