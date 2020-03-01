.. _workload_manager:

***********************
Workload manager
***********************

The workload manager (WLM) allows SQream DB workers to identify their availability to clients with specific service names. The load balancer will then use that information to route statements to specific workers.

Why use the workload manager?
===============================

The workload manager allows a system engineer or database administrator to allocate specific workers and compute resoucres for various tasks.

For example:

#. Creating a service queue named ``ETL`` and allocating two workers exclusively to this service prevents non-``ETL`` statements from utilizing these compute resources.

#. Creating a service for the company's leadership during working hours for dedicated access, and disabling this service at night to allow maintenance operations to use the available compute.

Setting up service queues
==========================

By default, every worker subscribes to the ``sqream`` service queue.

Additional service names are configured in the configuration file for every worker, but can also be :ref:`set on a per-session basis<subscribe_service>`.

Example - Allocating resources for ETL
========================================

We want to allocate resources for ETL to ensure a good quality of service, but we also have management users who don't like waiting.

The configuration in this example allocates resources as follows:

* 1 worker for ETL work
* 3 workers for general queries
* All workers assigned to queries from management

.. list-table:: 
   :widths: auto
   :header-rows: 1
   :stub-columns: 1
   
   * - Service / Worker
     - Worker #1
     - Worker #2
     - Worker #3
     - Worker #4
   * - ETL
     - ✓
     - ✗
     - ✗
     - ✗
   * - Query service
     - ✗
     - ✓
     - ✓
     - ✓
   * - Management
     - ✓
     - ✓
     - ✓
     - ✓

This configuration gives the ETL queue dedicated access to two workers, one of which can't be used by regular queries.

Queries from management will use any available worker.

Creating this configuration
-----------------------------------

The persistent configuration for this setup is listed in these four configuration files:

.. code-block:: json
   :caption: Worker #1
   :emphasize-lines: 7

   {
       "compileFlags": {
       },
       "runtimeFlags": {
       },
       "runtimeGlobalFlags": {
          "initialSubscribedServices" : "etl,management"
       },
       "server": {
           "gpu": 0,
           "port": 5000,
           "cluster": "/home/rhendricks/raviga_database",
           "licensePath": "/home/sqream/.sqream/license.enc"
       }
   }

.. code-block:: json
   :caption: Workers #2, #3, #4
   :emphasize-lines: 7

   {
       "compileFlags": {
       },
       "runtimeFlags": {
       },
       "runtimeGlobalFlags": {
          "initialSubscribedServices" : "query,management"
       },
       "server": {
           "gpu": 1,
           "port": 5001,
           "cluster": "/home/rhendricks/raviga_database",
           "licensePath": "/home/sqream/.sqream/license.enc"
       }
   }

This configuration can be created temporarily (for the current session only) by using the :ref:`subscribe_service` and :ref:`unsubscribe_service` statements.

Verifying the configuration
-----------------------------------

Use :ref:`show_subscribed_instances` to view service subscriptions for each worker. Use ref:`show_server_status` to see the statement queues.

.. code-block:: psql
   
   t=> SELECT SHOW_SUBSCRIBED_INSTANCES();
   service    | servernode | serverip      | serverport
   -----------+------------+---------------+-----------
   management | node_9383  | 192.168.0.111 |       5000
   etl        | node_9383  | 192.168.0.111 |       5000
   query      | node_9384  | 192.168.0.111 |       5001
   management | node_9384  | 192.168.0.111 |       5001
   query      | node_9385  | 192.168.0.111 |       5002
   management | node_9385  | 192.168.0.111 |       5002
   query      | node_9551  | 192.168.1.91  |       5000
   management | node_9551  | 192.168.1.91  |       5000

Configuring a client to connect to a specific service
===========================================================

Using :ref:`sqream_sql_cli_reference`
--------------------------------------------

Add ``--service=<service name>`` to the command line.

.. code-block:: psql

   $ sqream sql --port=3108 --clustered --username=mjordan --databasename=master --service=etl
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_

Using :ref:`JDBC<java_jdbc>`
--------------------------------------------

Add ``--service=<service name>`` to the command line.

.. code-block:: none
   :caption: JDBC connection string
   
   jdbc:Sqream://127.0.0.1:3108/raviga;user=rhendricks;password=Tr0ub4dor&3;service=etl;cluster=true;ssl=false;

Using :ref:`odbc`
--------------------------------------------

On Linux, modify the :ref:`DSN parameters<dsn_params>` in ``odbc.ini``.

For example, ``Service="etl"``:

.. code-block:: none
   :caption: odbc.ini
   :emphasize-lines: 7
   
      [sqreamdb]
      Description=64-bit Sqream ODBC
      Driver=/home/rhendricks/sqream_odbc64/sqream_odbc64.so
      Server="127.0.0.1"
      Port="3108"
      Database="raviga"
      Service="etl"
      User="rhendricks"
      Password="Tr0ub4dor&3"
      Cluster=true
      Ssl=false

On Windows, change the parameter in the :ref:`DSN editing window<create_windows_odbc_dsn>`.

Using :ref:`pysqream`
--------------------------------------------

In Python, set the ``service`` parameter in the connection command:

.. code-block:: python
   :caption: Python
   :emphasize-lines: 3

   con = pysqream.connect(host='127.0.0.1', port=3108, database='raviga'
                          , username='rhendricks', password='Tr0ub4dor&3'
                          , clustered=True, use_ssl = False, service='etl')

Using :ref:`nodejs`
--------------------------------------------

Add the service to the connection settings:

.. code-block:: javascript
   :caption: Node.JS
   :emphasize-lines: 5
   
   const Connection = require('sqreamdb');
   const config = {
      host: '127.0.0.1',
      port: 3108,
      username: 'rhendricks',
      password: 'Tr0ub4dor&3',
      connectDatabase: 'raviga',
      cluster: 'true',
      service: 'etl'
   };
