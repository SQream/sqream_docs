.. _sqream_console_cli_reference:

*********************************
sqream-console
*********************************

``sqream-console`` is an interactive shell designed to help manage a dockerized SQream DB installation.

The console itself is a dockerized application.

This page serves as a reference for the options and parameters.

.. contents:: In this topic:
   :local:

Starting the console
======================

``sqream-console`` can be found in your SQream DB installation, under the name ``sqream-console``.

Start the console by executing it from the shell

.. code-block:: console
   
   $ ./sqream-console
   ....................................................................................................................

   ███████╗ ██████╗ ██████╗ ███████╗ █████╗ ███╗   ███╗     ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ███████╗
   ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗████╗ ████║    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║     ██╔════╝
   ███████╗██║   ██║██████╔╝█████╗  ███████║██╔████╔██║    ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     █████╗
   ╚════██║██║▄▄ ██║██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║    ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██╔══╝
   ███████║╚██████╔╝██║  ██║███████╗██║  ██║██║ ╚═╝ ██║    ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗███████╗
   ╚══════╝ ╚══▀▀═╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝

   ....................................................................................................................


   Welcome to SQream Console ver 1.7.6, type exit to log-out

   usage: sqream [-h] [--settings] {master,worker,client,editor} ...

   Run SQream Cluster

   optional arguments:
     -h, --help            show this help message and exit
     --settings            sqream environment variables settings

   subcommands:
     sqream services

     {master,worker,client,editor}
                           sub-command help
       master              start sqream master
       worker              start sqream worker
       client              operating sqream client
       editor              operating sqream statement editor
   sqream-console>

The console is now waiting for commands.

The console is a wrapper around a standard linux shell. It supports commands like ``ls``, ``cp``, etc.

All SQream DB-specific commands start with the keyword ``sqream``.


Operations and flag reference
===============================

Commands
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - ``sqream --help``
     - Shows the initial usage information
   * - ``sqream master``
     - Controls the master node's operations
   * - ``sqream worker``
     - Controls workers' operations
   * - ``sqream client``
     - Access to :ref:`sqream sql<sqream_sql_cli_reference>`
   * - ``sqream editor``
     - Controls the statement editor's operations (web UI)

.. _master_node:

Master
------------

The master node contains the :ref:`metadata server<metadata_server_cli_reference>` and the :ref:`load balancer<server_picker_cli_reference>`.

Syntax
^^^^^^^^^^

.. code-block:: console
   
   sqream master <flags>

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag/command
     - Description
   * - ``--start [ --single-host ]``
     - 
         Starts the master node.
         The ``--single-host`` modifier sets the mode to allow all containers to run on the same server.

   * - ``--stop [ --all ]``
     - 
         Stops the master node and all connected :ref:`workers<workers>`.
         The ``--all`` modifier instructs the ``--stop`` command to stop all running services related to SQream DB
   * - ``--list``
     - Shows a list of all active master nodes and their workers
   * - ``-p <port>``
     - Sets the port for the load balancer. Defaults to ``3108``
   * - ``-m <port>``
     - Sets the port for the metadata server. Defaults to ``3105``

Common usage
^^^^^^^^^^^^^^^

Start master node
********************

.. code-block:: console
   
   sqream-console> sqream master --start
   starting master server in single_host mode ...
   sqream_single_host_master is up and listening on ports:   3105,3108

Start master node on different ports
*******************************************

.. code-block:: console
   
   sqream-console> sqream master --start -p 4105 -m 4108
   starting master server in single_host mode ...
   sqream_single_host_master is up and listening on ports:   4105,4108

Listing active master nodes and workers
***************************************************

.. code-block:: console
   
   sqream-console> sqream master --list
   container name: sqream_single_host_worker_1, container id: de9b8aff0a9c
   container name: sqream_single_host_worker_0, container id: c919e8fb78c8
   container name: sqream_single_host_master, container id: ea7eef80e038

Stopping all SQream DB workers and master
*********************************************

.. code-block:: console
   
   sqream-console> sqream master --stop --all
     shutting down 2 sqream services ...
    sqream_editor    stopped
    sqream_single_host_worker_1    stopped
    sqream_single_host_worker_0    stopped
    sqream_single_host_master    stopped

.. _workers:

Workers
------------

Workers are :ref:`SQream DB daemons<sqreamd_cli_reference>`, that connect to the master node.

Syntax
^^^^^^^^^^

.. code-block:: console
   
   sqream worker <flags>

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag/command
     - Description
   * - ``--start [ options [ ...] ]``
     - Starts worker nodes. See options table below.
   * - ``--stop [ <worker name> | --all ]``
     - 
         Stops the specified worker name.
         The ``--all`` modifier instructs the ``--stop`` command to stop all running workers.

Start options are specified consecutively, separated by spaces.

.. list-table:: Start options
   :widths: auto
   :header-rows: 1
   
   * - Option
     - Description
   * - ``<n>``
     - Specifies the number of workers to start
   * - ``-j <config file> [ ...]``
     - Specifies configuration files to apply to each worker. When launching multiple workers, specify one file per worker, separated by spaces.
   * - ``-p <port> [ ...]``
     - Sets the ports to listen on. When launching multiple workers, specify one port per worker, separated by spaces. Defaults to 5000 - 5000+n.
   * - ``-g <gpu id> [ ...]``
     - Sets the GPU ordinal to assign to each worker. When launching multiple workers, specify one GPU ordinal per worker, separated by spaces. Defaults to automatic allocation.
   * - ``-m <spool memory>``
     - Sets the spool memory per node in gigabytes.
   * - ``--master-host``
     - Sets the hostname for the master node. Defaults to ``localhost``.
   * - ``--master-port``
     - Sets the port for the master node. Defaults to ``3105``.
   * - ``--stand-alone``
     - For testing only: Starts a worker without connecting to the master node.

Common usage
^^^^^^^^^^^^^^^

Start 2 workers
********************

After starting the master node, start workers:

.. code-block:: console
   
   sqream-console> sqream worker --start 2
   started sqream_single_host_worker_0 on port 5000, allocated gpu: 0
   started sqream_single_host_worker_1 on port 5001, allocated gpu: 1

Stop a single worker
*******************************************

To stop a single worker, find its name first:

.. code-block:: console
   
   sqream-console> sqream master --list
   container name: sqream_single_host_worker_1, container id: de9b8aff0a9c
   container name: sqream_single_host_worker_0, container id: c919e8fb78c8
   container name: sqream_single_host_master, container id: ea7eef80e038

Then, issue a stop command:

.. code-block:: console
   
   sqream-console> sqream worker --stop sqream_single_host_worker_1
   stopped sqream_single_host_worker_1

Start workers with a different spool size
**********************************************

If no spool size is specified, the RAM is equally distributed among workers.
Sometimes a system engineer may wish to specify the spool size manually.

This example starts two workers, with a spool size of 50GB per node:

.. code-block:: console
   
   sqream-console> sqream worker --start 2 -m 50

Starting multiple workers on non-dedicated GPUs
****************************************************

By default, SQream DB workers assign one worker per GPU. However, a system engineer may wish to assign multiple workers per GPU, if the workload permits it.

This example starts 4 workers on 2 GPUs, with 50GB spool each:

.. code-block:: console
   
   sqream-console> sqream worker --start 2 -g 0 -m 50
   started sqream_single_host_worker_0 on port 5000, allocated gpu: 0
   started sqream_single_host_worker_1 on port 5001, allocated gpu: 0
   sqream-console> sqream worker --start 2 -g 1 -m 50
   started sqream_single_host_worker_2 on port 5002, allocated gpu: 1
   started sqream_single_host_worker_3 on port 5003, allocated gpu: 1

Overriding default configuration files
*******************************************

It is possible to override default configuration settings by listing a configuration file for every worker. 

This example starts 2 workers on the same GPU, with modified configuration files:

.. code-block:: console
   
   sqream-console> sqream worker --start 2 -g 0 -j /etc/sqream/configfile.json /etc/sqream/configfile2.json

Client
------------

The client operation runs :ref:`sqream sql<sqream_sql_cli_reference>` in interactive mode.

.. note:: The dockerized client is useful for testing and experimentation. It is not the recommended method for executing analytic queries. See more about connecting a :ref:`third party tool to SQream DB <third_party_tools>` for data analysis.

Syntax
^^^^^^^^^^

.. code-block:: console
   
   sqream client <flags>

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag/command
     - Description
   * - ``--master``
     - Connects to the master node via the load balancer
   * - ``--worker``
     -  Connects to a worker directly
   * - ``--host <hostname>``
     - Specifies the hostname to connect to. Defaults to ``localhost``.
   * - ``--port <port>``, ``-p <port>``
     - Specifies the port to connect to. Defaults to ``3108`` when used with ``-master``.
   * - ``--user <username>``, ``-u <username>``
     - Specifies the role's username to use
   * - ``--password <password>``, ``-w <password>``
     - Specifies the password to use for the role
   * - ``--database <database>``, ``-d <database>``
     - Specifies the database name for the connection. Defaults to ``master``.

Common usage
^^^^^^^^^^^^^^^

Start a client
********************

Connect to default ``master`` database through the load balancer:

.. code-block:: console
   
   sqream-console> sqream client --master -u sqream -w sqream
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> _

Start a client to a specific worker
**************************************

Connect to database ``raviga`` directly to a worker on port 5000:

.. code-block:: console
   
   sqream-console> sqream client --worker -u sqream -w sqream -p 5000 -d raviga
   Interactive client mode
   To quit, use ^D or \q.
   
   raviga=> _

Start master node on different ports
*******************************************

.. code-block:: console
   
   sqream-console> sqream master --start -p 4105 -m 4108
   starting master server in single_host mode ...
   sqream_single_host_master is up and listening on ports:   4105,4108

Listing active master nodes and worker nodes
***************************************************

.. code-block:: console
   
   sqream-console> sqream master --list
   container name: sqream_single_host_worker_1, container id: de9b8aff0a9c
   container name: sqream_single_host_worker_0, container id: c919e8fb78c8
   container name: sqream_single_host_master, container id: ea7eef80e038

.. _start_editor:

Editor
------------

The editor operation runs the web UI for the :ref:`SQream DB Statement Editor<statement_editor>`.

The editor can be used to run queries from a browser.

Syntax
^^^^^^^^^^

.. code-block:: console
   
   sqream editor <flags>

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag/command
     - Description
   * - ``--start``
     - Start the statement editor
   * - ``--stop``
     - Shut down the statement editor
   * - ``--port <port>``, ``-p <port>``
     - Specify a different port for the editor. Defaults to ``3000``.

Common usage
^^^^^^^^^^^^^^^

Start the editor UI
**********************

.. code-block:: console
   
   sqream-console> sqream editor --start
   access sqream statement editor through Chrome http://192.168.0.100:3000

Stop the editor UI
**********************

.. code-block:: console
   
   sqream-console> sqream editor --stop
    sqream_editor    stopped


Using the console to start SQream DB
============================================

The console is used to start and stop SQream DB components in a dockerized environment.

Starting a SQream DB cluster for the first time
-------------------------------------------------------

To start a SQream DB cluster, start the master node, followed by workers.

The example below starts 2 workers, running on 2 dedicated GPUs.

.. code-block:: console

   sqream-console> sqream master --start
   starting master server in single_host mode ...
   sqream_single_host_master is up and listening on ports:   3105,3108
   
   sqream-console> sqream worker --start 2
   started sqream_single_host_worker_0 on port 5000, allocated gpu: 0
   started sqream_single_host_worker_1 on port 5001, allocated gpu: 1
   
   sqream-console> sqream editor --start
   access sqream statement editor through Chrome http://192.168.0.100:3000

SQream DB is now listening on port 3108 for any incoming statements.

A user can also access the web editor (running on port ``3000`` on the SQream DB machine) to connect and run queries.