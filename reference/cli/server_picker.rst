.. _server_picker_cli_reference:

*************************
server_picker
*************************

SQream DB's load balancer is called ``server_picker``.

This page serves as a reference for the options and parameters.

Positional command line arguments
===================================

.. code-block:: console

   $ server_picker [ <Metadata server address> <Metadata server port> [ <TCP listen port> [ <SSL listen port> ] ]

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``Metadata server address``
     - 
     - IP or hostname to an active :ref:`metadata server<metadata_server_cli_reference>`
   * - ``Metadata server port``
     - 
     - TCP port to an active  :ref:`metadata server<metadata_server_cli_reference>`
   * - ``TCP listen port``
     - ``3108``
     - TCP port for server picker to listen on
   * - ``Metadata server port``
     - ``3109``
     - SSL port for server picker to listen on

Starting server picker
============================

Starting temporarily
-----------------------------

In general, you should not need to run ``server_picker`` manually, but it is sometimes useful for testing. 

Assuming we have a :ref:`metadata server<metadata_server_cli_reference>` listening on the localhost, on port 3105:

.. code-block:: console

   $ nohup server_picker 127.0.0.1 3105 &
   $ SP_PID=$!

Using ``nohup`` and ``&`` sends server picker to run in the background.

Starting temporarily with non-default port
------------------------------------------------

Tell server picker to listen on port 2255 for unsecured connections, and port 2266 for SSL connections.

.. code-block:: console

   $ nohup server_picker 127.0.0.1 3105 2255 2266 &
   $ SP_PID=$!

Using ``nohup`` and ``&`` sends server picker to run in the background.

Stopping server picker
----------------------------

.. code-block:: console

   $ kill -9 $SP_PID

.. tip:: It is safe to stop any SQream DB component at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.
