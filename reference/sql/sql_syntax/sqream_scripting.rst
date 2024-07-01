.. _sqream_scripting:

****************
SQream Scripting
****************

The Java- based SQreamDB scripting enhances your interaction with SQL by providing conventions which allow dynamic generation, management, and automation of SQL code and database operations. 

Syntax
======

.. code-block:: postgres

	-- Double curly brackets
	
	{{ … }}

	-- Parallel:

	@@ Parallel $$ ... $$

	-- Declare:

	@@ Declare '<my_parameter>' = <value>

	-- SetResults:

	@@ SetResults <result_variable>

	-- SplitQueryByDateTime

	@@ SplitQueryByDateTime instances = <value>, from = <value>, to = <value>

	-- SplitQueryByDate

	@@ SplitQueryByDate instances = <value>, from = <value>, to = <value>

	-- SplitQueryByNumber

	@@ SplitQueryByNumber instances = <value>, from = <value>, to = <value>
	
	-- ${ ... }
	
.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``{{ … }}``
     - Double brackets can contain JavaScript code to be executed through the Editor
   * - ``Parallel``
     - Runs specified queries in parallel
   * - ``Declare``
     - Declares a variable value
   * - ``SetResults``
     - Saves specified query results as a variable
   * - ``SplitQueryByDateTime``
     - Splits query execution by a predefined number of instances and by specific ``DATETIME`` column values
   * - ``SplitQueryByDate``
     - Splits query execution by a predefined number of instances and by specific ``DATE`` column values
   * - ``SplitQueryByNumber``
     - Splits query execution by a predefined number of instances and by specific ``NUMERIC`` column values

Usage Notes
===========

.. glossary::

	**Execution**
		Metalanguage scripting is available only through the SQreamDB web interface and cannot be used via the CLI. 

Examples
========

Double Curly Brackets
---------------------

.. code-block:: console

	{{
	  return 1;
	}}

``Parallel``
------------

.. code-block:: console

	@@ Parallel
	$$
	SELECT * FROM my_table;
	SELECT * FROM our_table;
	SELECT * FROM that_table;
	$$;

``Declare``
-----------

.. code-block:: console

	@@ Declare myVar = 3;
	SELECT '${myVar}';

``SetResults``
--------------

.. code-block:: console

	@@ SetResults tableAverage
	SELECT AVG(col1) AS avg_salary FROM my_table;

	SELECT col1 FROM my_table WHERE col1 > ${tableAverage[0].avg_salary};


``SplitQueryByDateTime``
------------------------

.. code-block:: console

	@@ SplitQueryByDateTime instances = 4, from = '2021-01-01 00:00:00', to = '2022-01-01 00:00:00'
	SELECT ${from}, ${to};


``SplitQueryByDate``
--------------------

.. code-block:: console

	@@ SplitQueryByDateTime instances = 4, from = '2021-01-01', to = '2022-01-01'
	SELECT ${from}, ${to};


``SplitQueryByNumber``
----------------------

.. code-block:: console

	@@ SplitQueryByDateTime instances = 4, from = 0, to = 100
	SELECT ${from}, ${to};
