:orphan:

.. _show_saved_query:

********************
SHOW SAVED QUERY
********************

``SHOW_SAVED_QUERY`` shows the query text for a previously :ref:`saved query<save_query>`.

Read more in the :ref:`saved_queries` guide.

See also: :ref:`save_query`, :ref:`execute_saved_query`,  :ref:`drop_saved_query`,  :ref:`list_saved_queries`.

Syntax
==========

.. code-block:: sql

   show_saved_query_statement ::=
       SELECT SHOW_SAVED_QUERY(saved_query_name)

   saved_query_name ::= string_literal

Returns
==========

A single row result containing the saved query string.

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``saved_query_name``
     - The name of the query to show


Examples
===========

Showing a previously saved query
---------------------------------------

.. code-block:: sql

   SELECT SAVE_QUERY('select_by_weight_and_team',$$SELECT * FROM nba WHERE Weight > ? AND Team = ?$$);
   
   SELECT SHOW_SAVED_QUERY('select_by_weight_and_team');
   saved_query                                    
   -----------------------------------------------
   SELECT * FROM nba WHERE Weight > ? AND Team = ?

Permissions
=============

Showing a saved query requires ``SELECT`` permissions on the saved query.
