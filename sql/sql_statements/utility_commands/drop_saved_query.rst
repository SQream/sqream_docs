:orphan:

.. _drop_saved_query:

********************
DROP SAVED QUERY
********************

``DROP_SAVED_QUERY`` drops a :ref:`previously saved query<save_query>`.

Read more in the :ref:`saved_queries<saved_queries>` guide.

See also: :ref:`save_query`, :ref:`execute_saved_query`, :ref:`describe_saved_query`, :ref:`recompile_saved_query`, and :ref:`describe_saved_queries_list`.

Permissions
=============

Dropping a saved query requires no special permissions.

Syntax
==========

.. code-block:: postgres

   drop_saved_query_statement ::=
       SELECT DROP_SAVED_QUERY(saved_query_name)
       ;

   saved_query_name ::= string_literal

Returns
==========

If saved query is dropped successfully, returns nothing.

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``saved_query_name``
     - The name of the query to drop

Examples
===========

Dropping a previously saved query
---------------------------------------

.. code-block:: psql

   t=> SELECT DROP_SAVED_QUERY('select_all');
   executed
