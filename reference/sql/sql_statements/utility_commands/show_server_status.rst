.. _show_server_status:

********************
SHOW_SERVER_STATUS
********************

``SHOW_SERVER_STATUS`` returns a list of active sessions across the cluster.

To list active statements on the current worker only, see :ref:`show_connections`.

Permissions
=============

The role must have the ``SUPERUSER`` permissions.

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
     - The worker ID
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

.. include from here: 66


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
   * - ``Stopping``
     - Statement is in the process of stopping


.. include until here 86

Notes
===========

* This utility shows the active sessions. Some sessions may be actively connected, but not running any statements.

Examples
===========

Using ``SHOW_SERVER_STATUS`` to get statement IDs
----------------------------------------------------


.. code-block:: psql

   t=> SELECT SHOW_SERVER_STATUS();
   service | instanceid | connection_id | serverip      | serverport | database_name | user_name        | clientip      | statementid | statement                                                                                             | statementstarttime  | statementstatus | statementstatusstart
   --------+------------+---------------+---------------+------------+---------------+------------------+---------------+-------------+-------------------------------------------------------------------------------------------------------+---------------------+-----------------+---------------------
   sqream  | sqream_2   |  19           | 192.168.0.111 |       5000 | master        | etl              | 192.168.0.011 |2484923      | SELECT t1.account, t1.msisd from table a t1 join table b t2 on t1.id = t2.id where t1.msid='123123';  | 17-01-2022 16:19:31 | Executing       | 17-01-2022 16:19:32
   sqream  | sqream_1   |  2            | 192.168.1.112 |       5000 | master        | etl              | 192.168.1.112 |2484924      | select show_server_status();                                                                          | 17-01-2022 16:19:39 | Executing       | 17-01-2022 16:19:39
   sqream  | None       |  248          | 192.168.1.112 |       5007 | master        | maintenance_user | 192.168.1.112 |2484665      | select * from  sqream_catalog.tables;                                                                 | 17-01-2022 15:55:01 | In Queue        | 17-01-2022 15:55:02

The statement ID is ``128``, running on worker ``192.168.1.91``.