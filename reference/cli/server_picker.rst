.. _server_picker_cli_reference:

*************************
Server Picker
*************************

SQreamDB's load balancer is called ``server_picker``.

Command Line Arguments
========================

Parameters
------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``--metadata_server_port``
     - ``3105``
     - The metadata server listening port
   * - ``--metadata_server_ip``
     - ``127.0.0.1``
     - The metadata server IP
   * - ``--port``
     - ``3108``
     - The server picker port
   * - ``--ssl_port``
     - ``3109``
     - The server picker ssl port
   * - ``--log4_config``
     - ``/home/sqream/sqream3/etc/server_picker_log_properties``
     - The server picker log4 configuration file to use
   * - ``--refresh_interval``
     - ``15``
     - Refresh interval time to check available nodes
   * - ``--services``
     - None
     -  Lists services separated by comma
   * - ``--help``
     - None
     - Used to display a help message or documentation for a particular program or command
	 
Example
---------

.. code-block:: console

	server_picker --metadata_ip=127.0.0.1 --metadata_server_port=3105 --port=3118 --ssl_port=3119 --services=sqream23,sqream0 --log4_config=/home/sqream/metadata_log_properties --refresh_interval=10

Starting server picker
============================

Starting temporarily
-----------------------------

In general, you should not need to run ``server_picker`` manually, but it is sometimes useful for testing. 

Assuming we have a :ref:`metadata server<metadata_server_cli_reference>` listening on the localhost, on port 3105:

.. code-block:: console

	nohup server_picker --metadata_server_ip=127.0.0.1 metadata_server_port=3105 &
	SP_PID=$!

Using ``nohup`` and ``&`` sends server picker to run in the background.

Starting temporarily with non-default port
------------------------------------------------

Tell server picker to listen on port 2255 for unsecured connections, and port 2266 for SSL connections.

.. code-block:: console

	nohup server_picker --metadata_server_ip=127.0.0.1 --metadata_server_port=3105 --port=2255 --ssl_port=2266 &
	SP_PID=$!

Using ``nohup`` and ``&`` sends server picker to run in the background.

Stopping server picker
----------------------------

.. code-block:: console

	kill -9 $SP_PID

.. tip:: It is safe to stop any SQream DB component at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.
