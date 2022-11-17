.. _saved_queries:

***********************
Saved Queries
***********************


Using the SAVE_QUERY command allows you to save time by easily running frequently used complex queries which once saved, do not require execution plan compilation. You may also use saved queries to implement 'parameterized views'. 


Parameters support
===========================

* Query parameters can be used as substitutes for literal expressions in queries.

* Parameters cannot be used to substitute things like column names and table names.

* Query parameters of a string datatype (like ``TEXT``) must be of a fixed length, and can be used in equality checks, but not patterns (e.g. :ref:`like`, :ref:`rlike`, etc.)

Creating a saved query
======================

A saved query is created using the :ref:`save_query` utility command.

Saving a simple query
---------------------------

.. code-block:: psql

   t=> SELECT SAVE_QUERY('select_all','SELECT * FROM nba');
   executed

Saving a parametrized query
------------------------------------------

Use parameters to replace them later at execution time. 



.. code-block:: psql

   t=> SELECT SAVE_QUERY('select_by_weight_and_team','SELECT * FROM nba WHERE Weight > ? AND Team = ?');
   executed

.. TODO tip Use dollar quoting (`$$`) to avoid escaping strings.
.. this makes no sense unless you have a query which would otherwise need escaping
..   t=> SELECT SAVE_QUERY('select_by_weight_and_team',$$SELECT * FROM nba WHERE Weight > ? AND Team = ?$$);
..   executed


Listing and executing saved queries
======================================

Saved queries are saved as a database objects. They can be listed in one of two ways:

Using the :ref:`catalog<catalog_reference>`:

.. code-block:: psql

   t=> SELECT * FROM sqream_catalog.savedqueries;
   name                      | num_parameters
   --------------------------+---------------
   select_all                |              0
   select_by_weight          |              1
   select_by_weight_and_team |              2

Using the :ref:`list_saved_queries` utility function:

.. code-block:: psql

   t=> SELECT LIST_SAVED_QUERIES();
   saved_query              
   -------------------------
   select_all               
   select_by_weight         
   select_by_weight_and_team

Executing a saved query requires calling it by it's name in a :ref:`execute_saved_query` statement. A saved query with no parameter is called without parameters.

.. code-block:: psql

   t=> SELECT EXECUTE_SAVED_QUERY('select_all');
   Name                     | Team                   | Number | Position | Age | Height | Weight | College               | Salary  
   -------------------------+------------------------+--------+----------+-----+--------+--------+-----------------------+---------
   Avery Bradley            | Boston Celtics         |      0 | PG       |  25 | 6-2    |    180 | Texas                 |  7730337
   Jae Crowder              | Boston Celtics         |     99 | SF       |  25 | 6-6    |    235 | Marquette             |  6796117
   John Holland             | Boston Celtics         |     30 | SG       |  27 | 6-5    |    205 | Boston University     |         
   R.J. Hunter              | Boston Celtics         |     28 | SG       |  22 | 6-5    |    185 | Georgia State         |  1148640
   [...]

Executing a saved query with parameters requires specifying the parameters in the order they appear in the query:

.. code-block:: psql

   t=> SELECT EXECUTE_SAVED_QUERY('select_by_weight_and_team', 240, 'Toronto Raptors');
   Name              | Team            | Number | Position | Age | Height | Weight | College     | Salary 
   ------------------+-----------------+--------+----------+-----+--------+--------+-------------+--------
   Bismack Biyombo   | Toronto Raptors |      8 | C        |  23 | 6-9    |    245 |             | 2814000
   James Johnson     | Toronto Raptors |      3 | PF       |  29 | 6-9    |    250 | Wake Forest | 2500000
   Jason Thompson    | Toronto Raptors |      1 | PF       |  29 | 6-11   |    250 | Rider       |  245177
   Jonas Valanciunas | Toronto Raptors |     17 | C        |  24 | 7-0    |    255 |             | 4660482


Dropping a saved query
=============================

When you're done with a saved query, or would like to replace it with another, you can drop it with :ref:`drop_saved_query`:

.. code-block:: psql

   t=> SELECT DROP_SAVED_QUERY('select_all');
   executed
   t=> SELECT DROP_SAVED_QUERY('select_by_weight_and_team');
   executed
   
   t=> SELECT LIST_SAVED_QUERIES();
   saved_query              
   -------------------------
   select_by_weight         
