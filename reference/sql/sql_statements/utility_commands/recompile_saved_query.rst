.. _recompile_saved_query:

**************************
RECOMPILE_SAVED_QUERY
**************************

``RECOMPILE_SAVED_QUERY`` recompiles a saved query that has been invalidated due to a schema change.

Read more in the :ref:`saved_queries<saved_queries>` guide.

Permissions
=============

Recompiling a saved query requires no special permissions.

Syntax
==========

.. code-block:: postgres

   recompile_saved_query_statement ::=
       SELECT RECOMPILE_SAVED_QUERY(saved_query_name)
       ;

   saved_query_name ::= string_literal

Returns
==========

If saved query is recompiled successfully, returns nothing.

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``saved_query_name``
     - The name of the query to recompile

Examples
===========

Recreating a query that has been invalidated
-------------------------------------------------

.. code-block:: psql

   t=> SELECT SAVE_QUERY('select_by_weight_and_team',$$SELECT * FROM nba WHERE Weight > ? AND Team = ?$$);
   executed
   t=> SELECT EXECUTE_SAVED_QUERY('select_by_weight_and_team', 240, 'Toronto Raptors');
   Name              | Team            | Number | Position | Age | Height | Weight | College     | Salary 
   ------------------+-----------------+--------+----------+-----+--------+--------+-------------+--------
   Bismack Biyombo   | Toronto Raptors |      8 | C        |  23 | 6-9    |    245 |             | 2814000
   James Johnson     | Toronto Raptors |      3 | PF       |  29 | 6-9    |    250 | Wake Forest | 2500000
   Jason Thompson    | Toronto Raptors |      1 | PF       |  29 | 6-11   |    250 | Rider       |  245177
   Jonas Valanciunas | Toronto Raptors |     17 | C        |  24 | 7-0    |    255 |             | 4660482
   

To invalidate the original saved query, we will change the schema without affecting our original query text:

.. code-block:: psql

   t=> ALTER TABLE nba RENAME COLUMN age to "Age (as of 2015)";
   executed

However, because the query was compiled previously, this change invalidates the query and causes it to fail:

.. code-block:: psql

   t=> SELECT EXECUTE_SAVED_QUERY('select_by_weight_and_team', 240, 'Toronto Raptors');
   Error: column not found {Age@null}
   column not found {Age@null}

Recompiling the query will fix this issue

.. code-block:: psql
   
   t=> SELECT RECOMPILE_SAVED_QUERY('select_by_weight_and_team');
   executed
   t=> SELECT EXECUTE_SAVED_QUERY('select_by_weight_and_team', 240, 'Toronto Raptors');
   Name              | Team            | Number | Position | Age (as of 2015) | Height | Weight | College     | Salary 
   ------------------+-----------------+--------+----------+------------------+--------+--------+-------------+--------
   Bismack Biyombo   | Toronto Raptors |      8 | C        |               23 | 6-9    |    245 |             | 2814000
   James Johnson     | Toronto Raptors |      3 | PF       |               29 | 6-9    |    250 | Wake Forest | 2500000
   Jason Thompson    | Toronto Raptors |      1 | PF       |               29 | 6-11   |    250 | Rider       |  245177
   Jonas Valanciunas | Toronto Raptors |     17 | C        |               24 | 7-0    |    255 |             | 4660482
