.. _saved_queries:

***********************
Saved Queries
***********************

The ``save_query`` command serves to both generate and store an execution plan, offering time savings for the execution of frequently used complex queries. It's important to note that the saved execution plan is closely tied to the structure of its underlying tables. Consequently, if any of the objects mentioned in the query undergo modification, the saved query must be recreated.

Saved queries undergo compilation during their creation. When executed, these queries utilize the precompiled query plan instead of compiling a new plan at query runtime.

Syntax
======

Saved queries related syntax:

.. code-block:: sql

	-- Saving a query
	SELECT SAVE_QUERY("<saved_query_name>", '<parameterized_query_string>')
	
	-- Showing a saved query
	DESCRIBE SAVED QUERY NAME "<saved_query_name>"

	-- Listing saved queries 
	DESCRIBE SAVED QUERIES LIST
		   
	-- Executing a saved query	   
	SELECT EXECUTE_SAVED_QUERY("<saved_query_name>")
	   
	-- Dropping a saved query
	SELECT DROP_SAVED_QUERY("<saved_query_name>")

	saved_query_name ::= identifier
	parameterized_query_string ::= string_literal
	argument ::= string_literal | number_literal

Parameter Support
------------------

Query parameters can be used as substitutes for constants expressions in queries.

* Parameters cannot be used to substitute identifiers like column names and table names.

* Query parameters of a string datatype must be of a fixed length and may be used in equality checks but not with patterns such as :ref:`like` and :ref:`rlike`.

Permissions
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Statement / Function
     - Permission
   * - :ref:`save_query`
     - Saving queries requires no special permissions per se, however, it does require from the user to have permissions to access the tables referenced in the query and other query element permissions. The user who saved the query is granted all permissions on the saved query.
   * - :ref:`describe_saved_query`
     - Showing a saved query requires ``SELECT`` permissions on the saved query.
   * - :ref:`describe_saved_queries_list`
     - Listing saved queries requires no special permissions. 
   * - :ref:`execute_saved_query`
     - Executing a saved query requires ``USAGE`` permissions on the saved query and ``SELECT`` permissions to access the tables referenced in the query.
   * - :ref:`drop_saved_query`
     - Dropping a saved query requires ``DDL`` permissions on the saved query and ``SELECT`` permissions to access the tables referenced in the query.

Parameterized Query
====================

Parameterized queries, also known as prepared statements, enable the usage of parameters which may be replaced by actual values when executing the query. They are created and managed in application code, primarily to optimize query execution, enhance security, and allow for the reuse of query templates with different parameter values.

.. code-block:: sql

   SELECT SAVE_QUERY('select_by_weight_and_team','SELECT * FROM nba WHERE Weight > ? AND Team = ?');


