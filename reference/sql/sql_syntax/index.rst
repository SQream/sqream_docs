.. _sql_syntax:

**********************
SQL Syntax Features
**********************

SQreamDB supports SQL from the ANSI 92 syntax.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Features
     - Description
   * - :ref:`keywords_and_identifiers`
     - Keywords are reserved words with specific meanings, while identifiers are used to name database objects like tables and columns.
   * - :ref:`literals`
     - Literals are fixed values representing specific data types, such as numbers or strings, used directly in SQL statements.
   * - :ref:`scalar_expressions`
     - Scalar expressions are single-value computations that operate on one or more values to produce a single result.
   * - :ref:`cross_database_query`  
     - Cross-database queries involve accessing and manipulating data from multiple databases within a single SQL statement or operation.
   * - :ref:`joins`
     - Joins combine rows from two or more tables based on a related column to retrieve data from multiple sources in a single result set.
   * - :ref:`common_table_expressions`
     - Common Table Expressions (CTEs) are named temporary result sets that simplify complex queries by allowing the definition of subqueries for better readability and reusability.
   * - :ref:`window_functions`
     - Window Functions perform calculations across a specified range of rows related to the current row, offering advanced analytics and aggregation within result sets.
   * - :ref:`subqueries`
     - Subqueries are nested queries that are embedded within a larger query to retrieve data, perform calculations, or filter results based on the outcome of the inner query.
   * - :ref:`null_handling`
     - Null handling involves managing and evaluating the presence of null values, representing unknown or undefined data, to avoid unexpected results in queries and expressions.
   * - :ref:`sqream_scripting`
     - Metalanguage scripting enhances your interaction with SQL by providing conventions which allow dynamic generation, management, and automation of SQL code.
	 * - :ref:`pivot_unpivot`
     - convert row-level data into columnar representation.



.. toctree::
   :caption:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:
   
   keywords_and_identifiers
   literals
   scalar_expressions
   cross_database_query
   joins
   common_table_expressions
   window_functions
   subqueries
   null_handling
   sqream_scripting
   pivot_unpivot
   
   




 









