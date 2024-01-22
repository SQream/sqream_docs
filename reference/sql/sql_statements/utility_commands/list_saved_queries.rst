.. _list_saved_queries:

********************
LIST SAVED QUERIES
********************

``LIST_SAVED_QUERIES`` lists the available previously :ref:`saved queries<save_query>`.

This is an alternative way to using the ``savedqueries`` catalog view.

Read more in the :ref:`saved_queries` guide.

See also: :ref:`save_query`, :ref:`execute_saved_query`, :ref:`drop_saved_query`, :ref:`show_saved_query`

Syntax
==========

.. code-block:: sql

   list_saved_queries_statement ::=
       SELECT LIST_SAVED_QUERIES()

Returns
==========

A list of saved queries the user has ``SELECT`` permissions on.

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

.. code-block:: sql

   SELECT LIST_SAVED_QUERIES();
   saved_query              
   -------------------------
   select_all               
   select_by_weight         
   select_by_weight_and_team

   SELECT SHOW_SAVED_QUERY('select_by_weight_and_team');
   saved_query                                    
   -----------------------------------------------
   SELECT * FROM nba WHERE Weight > ? AND Team = ?


Listing saved queries with the catalog
---------------------------------------------

Using the :ref:`catalog<catalog_reference>` is also possible:

.. code-block:: sql

   SELECT * FROM sqream_catalog.savedqueries;
   name                      | num_parameters
   --------------------------+---------------
   select_all                |              0
   select_by_weight          |              1
   select_by_weight_and_team |              2

Permissions
=============

Listing saved queries requires no special permissions. 