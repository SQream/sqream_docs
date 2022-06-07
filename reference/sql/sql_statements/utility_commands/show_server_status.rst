.. _show_server_status:

********************
SHOW_SERVER_STATUS
********************
``SHOW_SERVER_STATUS`` returns a list of active sessions across the cluster.

To list active statements on the current worker only, see :ref:`show_connections`.

Syntax
==========
The following is the correct syntax when showing your server status:

.. code-block:: postgres

   show_server_status_statement ::=
       SELECT SHOW_SERVER_STATUS()
       ;

Parameters
============
The Parameters section is not relevant for the ``SHOW_SERVER_STATUS`` statement.

Returns
=========
The ``SHOW_SERVER_STATUS`` function returns a list of active sessions. If no sessions are active across the cluster, the result set will be empty.

The following table shows the ``SHOW_SERVER_STATUS`` result columns;

.. list-table:: Result Columns
   :widths: auto
   :header-rows: 1
   
   * - service
     - Statement Service Name
   * - ``instance``
     - Shows the worker ID.
   * - ``connection_id``
     - Shows the connection ID.
   * - ``serverip``
     - Shows the worker end-point IP.
   * - ``serverport``
     - Shows the worker end-point port.
   * - ``database_name``
     - Shows the statement's database name.
   * - ``user_name``
     - Shows the username running the statement.
   * - ``clientip``
     - Shows the client IP.
   * - ``statementid``
     - Shows the statement ID.
   * - ``statement``
     - Shows the statement text.
   * - ``statementstarttime``
     - Shows the statement start timestamp.
   * - ``statementstatus``
     - Shows the statement status (see table below).
   * - ``statementstatusstart``
     - Shows the most recently updated timestamp.

.. include from here: 66

The following table shows the statement status values:

.. list-table:: Statement Status Values
   :widths: auto
   :header-rows: 1
   
   * - Status
     - Description
   * - ``Preparing``
     - The statement is being prepared.
   * - ``In queue``
     - The statement is waiting for execution.
   * - ``Initializing``
     - The statement has entered execution checks.
   * - ``Executing``
     - The statement is executing.
   * - ``Stopping``
     - The statement is in the process of stopping.

.. include until here 86

Notes
===========
This utility shows the active sessions. Some sessions may be actively connected, but not running any statements.

Example
===========

Using SHOW_SERVER_STATUS to Get Statement IDs
----------------------------------------------------
The following example shows how to use the ``SHOW_SERVER_STATUS`` statement to get statement IDs:

.. code-block:: psql

   t=> SELECT SHOW_SERVER_STATUS();
   service | instanceid | connection_id | serverip      | serverport | database_name | user_name        | clientip      | statementid | statement                                                                                             | statementstarttime  | statementstatus | statementstatusstart
   --------+------------+---------------+---------------+------------+---------------+------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------+---------------------+-----------------+---------------------
   sqream  | sqream_2   |  19           | 192.168.0.111 |       5000 | master        | etl              | 192.168.0.011 |2484923      | SELECT t1.account, t1.msisd from table a t1 join table b t2 on t1.id = t2.id where t1.msid='123123';  | 17-01-2022 16:19:31 | Executing       | 17-01-2022 16:19:32
   sqream  | sqream_1   |  2            | 192.168.1.112 |       5000 | master        | etl              | 192.168.1.112 |2484924      | select show_server_status();                                                                          | 17-01-2022 16:19:39 | Executing       | 17-01-2022 16:19:39
   sqream  | None       |  248          | 192.168.1.112 |       5007 | master        | maintenance_user | 192.168.1.112 |2484665      | select * from  sqream_catalog.tables;                                                                 | 17-01-2022 15:55:01 | In Queue        | 17-01-2022 15:55:02

The statement ID is ``128``, running on worker ``192.168.1.91``.

Permissions
=============
The role must have the ``SUPERUSER`` permissions.