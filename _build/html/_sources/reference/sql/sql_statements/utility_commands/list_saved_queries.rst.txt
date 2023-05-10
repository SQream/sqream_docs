.. _list_saved_queries:

********************
LIST_SAVED_QUERIES
********************

``LIST_SAVED_QUERIES`` lists the available :ref:`previously saved queries<save_query>`.

This is an alternative way to using the ``savedqueries`` catalog view.

Read more in the :ref:`saved_queries` guide.

See also: ref:`save_query`, :ref:`execute_saved_query`,  ref:`drop_saved_query`,  ref:`show_saved_query`.

Permissions
=============

Listing the saved queries requires no special permissions.

Syntax
==========

.. code-block:: postgres

   list_saved_queries_statement ::=
       SELECT LIST_SAVED_QUERIES()
       ;

Returns
==========

List of saved query names, one per row.

Parameters
============

None

Notes
=========

This statement returns an empty result set if no saved queries exist in the current database.

Examples
===========

Listing previously saved queries
---------------------------------------

.. code-block:: psql

   t=> SELECT LIST_SAVED_QUERIES();
   saved_query              
   -------------------------
   select_all               
   select_by_weight         
   select_by_weight_and_team

   t=> SELECT SHOW_SAVED_QUERY('select_by_weight_and_team');
   saved_query                                    
   -----------------------------------------------
   SELECT * FROM nba WHERE Weight > ? AND Team = ?


Listing saved queries with the catalog
---------------------------------------------

Using the :ref:`catalog<catalog_reference>` is also possible:

.. code-block:: psql

   t=> SELECT * FROM sqream_catalog.savedqueries;
   name                      | num_parameters
   --------------------------+---------------
   select_all                |              0
   select_by_weight          |              1
   select_by_weight_and_team |              2
