.. _stop_statement:

********************
STOP_STATEMENT
********************

``STOP_STATEMENT`` stops or aborts an active statement.

To find a statement by ID, see :ref:`show_server_status` and :ref:`show_connections`.

Permissions
=============

The role must have the ``SUPERUSER`` permissions.

Syntax
==========

.. code-block:: postgres

   stop_statement_statement ::=
       SELECT STOP_STATEMENT(stmt_id)
       ;
   
   stmt_id ::= bigint

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``stmt_id``
     - The statement ID to stop

Returns
=========

This utility does not return any value, and always succeeds even if the statement does not exist, or has already stopped.


Notes
===========

* This utility always succeeds even if the statement does not exist, or has already stopped.

Examples
===========

Using :ref:`show_connections` to get statement IDs
----------------------------------------------------

.. tip:: Use :ref:`show_server_status` to find statments from across the entire cluster, or :ref:`show_connections` to show statements from the current worker the client is connected to.

.. code-block:: psql

   t=> SELECT SHOW_CONNECTIONS();
   ip           | conn_id | conn_start_time     | stmt_id | stmt_start_time     | stmt                     
   -------------+---------+---------------------+---------+---------------------+--------------------------
   192.168.1.91 |     103 | 2019-12-24 00:01:27 |     129 | 2019-12-24 00:38:18 | SELECT GET_DATE(), * F...
   192.168.1.91 |      23 | 2019-12-24 00:01:27 |      -1 | 2019-12-24 00:01:27 |                          
   192.168.1.91 |      22 | 2019-12-24 00:01:27 |      -1 | 2019-12-24 00:01:27 |                          
   192.168.1.91 |      26 | 2019-12-24 00:01:28 |      -1 | 2019-12-24 00:01:28 |                          


The statement ID we're interested in is ``129``. We can now stop this statement:

.. code-block:: psql

   t=> SELECT STOP_STATEMENT(129)
   executed

