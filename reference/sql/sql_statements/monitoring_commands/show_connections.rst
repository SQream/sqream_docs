.. _show_connections:

********************
SHOW_CONNECTIONS
********************

``SHOW_CONNECTIONS`` returns a list of active sessions on the current worker.

To see sessions across the cluster, see :ref:`show_server_status`.

Permissions
=============

The role must have the ``SUPERUSER`` privileges.

Syntax
==========

.. code-block:: postgres

   show_connections_statement ::=
       SELECT SHOW_CONNECTIONS()
       ;

Parameters
============

None

Returns
=========

This function returns a list of active sessions. If no sessions are active on the worker, the result set will be empty.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1
   
   * - ``ip``
     - The worker hostname or IP
   * - ``conn_id``
     - Connection ID
   * - ``conn_start_time``
     - Connection start timestamp
   * - ``stmt_id``
     - Statement ID. Connections with no active statement display ``-1``.
   * - ``stmt_start_time``
     - Statement start timestamp
   * - ``stmt``
     - Statement text


Notes
===========

* This utility shows the active connections. Some sessions may be actively connected, but not currently running a statement.

* A connection is typically reused. There could be many statements under a single connection ID.

Examples
===========

Using ``SHOW_CONNECTIONS`` to get statement IDs
----------------------------------------------------


.. code-block:: psql

   t=> SELECT SHOW_CONNECTIONS();
   ip           | conn_id | conn_start_time     | stmt_id | stmt_start_time     | stmt                     
   -------------+---------+---------------------+---------+---------------------+--------------------------
   192.168.1.91 |     103 | 2019-12-24 00:01:27 |     129 | 2019-12-24 00:38:18 | SELECT GET_DATE(), * F...
   192.168.1.91 |      23 | 2019-12-24 00:01:27 |      -1 | 2019-12-24 00:01:27 |                          
   192.168.1.91 |      22 | 2019-12-24 00:01:27 |      -1 | 2019-12-24 00:01:27 |                          
   192.168.1.91 |      26 | 2019-12-24 00:01:28 |      -1 | 2019-12-24 00:01:28 |                          


The statement ID we're interested in is ``129``. We can see the connection started at 00:01:27, while the statement started at 00:38:18.