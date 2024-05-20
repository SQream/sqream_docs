:orphan:

.. _drop_saved_query:

****************
DROP SAVED QUERY
****************

``DROP_SAVED_QUERY`` drops a :ref:`previously saved query<save_query>`.

Read more in the :ref:`saved_queries<saved_queries>` guide.

See also: :ref:`save_query`, :ref:`execute_saved_query`, :ref:`describe_saved_query`, :ref:`recompile_saved_query`, and :ref:`describe_saved_queries_list`.

Permissions
===========

Dropping a saved query requires no special permissions.

Syntax
======

.. code-block:: postgres

	SELECT DROP_SAVED_QUERY(saved_query_name)

Returns
=======

If saved query is dropped successfully, returns nothing.

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``saved_query_name``
     - :ref:`STRING literal<literals>`	
     - The name of the query to drop

Examples
========

.. code-block:: psql

	SELECT DROP_SAVED_QUERY(select_all);

