.. _show_server_status:

********************
SHOW_SERVER_STATUS
********************

``SHOW_SERVER_STATUS`` returns a list of active sessions across the cluster.

To see sessions on the current worker, see :ref:`show_server_status`.

Permissions
=============

The role must have the ``SUPERUSER`` privileges.

Syntax
==========

.. code-block:: postgres

   show_server_status_statement ::=
       SELECT SHOW_SERVER_STATUS()
       ;

Parameters
============

None

Returns
=========

This function returns a list of active sessions. If no sessions are active across the cluster, the result set will be empty.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1
   
   * - ``service``
     - The service name for the statement
   * - ``instance``
     - Instance ID
   * - ``connection_id``
     - Connection ID
   * - ``serverip``
     - Worker end-point IP
   * - ``serverport``
     - Worker end-point port
   * - ``database_name``
     - Database name for the statement
   * - ``user_name``
     - Username running the statement
   * - ``clientip``
     - Client IP
   * - ``statementid``
     - Statement ID
   * - ``statement``
     - Statement text
   * - ``statementstarttime``
     - Statement start timestamp
   * - ``statementstatus``
     - Statement status (see table below)
   * - ``statementstatusstart``
     - Last updated timestamp


.. list-table:: Statement status values
   :widths: auto
   :header-rows: 1
   
   * - Status
     - Description
   * - ``Preparing``
     - Statement is being prepared
   * - ``In queue``
     - Statement is waiting for execution
   * - ``Initializing``
     - Statement has entered execution checks
   * - ``Executing``
     - Statement is executing

Notes
===========

* This utility shows the active sessions. Some sessions may be actively connected, but not currently running a statement.

Examples
===========

Using ``SHOW_SERVER_STATUS`` to get statement IDs
----------------------------------------------------


.. code-block:: psql

   t=> SELECT SHOW_SERVER_STATUS();
   service | instanceid | connection_id | serverip     | serverport | database_name | user_name  | clientip    | statementid | statement                   | statementstarttime  | statementstatus | statementstatusstart
   --------+------------+---------------+--------------+------------+---------------+------------+-------------+-------------+-----------------------------+---------------------+-----------------+---------------------
   sqream  |            |           102 | 192.168.1.91 |       5000 | t             | rhendricks | 192.168.0.1 |         128 | SELECT SHOW_SERVER_STATUS() | 24-12-2019 00:14:53 | Executing       | 24-12-2019 00:14:53 

The statement ID is ``128``, running on worker ``192.168.1.91``.