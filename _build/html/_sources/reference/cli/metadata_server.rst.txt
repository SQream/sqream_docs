.. _metadata_server_cli_reference:

*************************
metadata_server
*************************

SQream DB's cluster manager/coordinator is called ``metadata_server``.

In general, you should not need to run ``metadata_server`` manually, but it is sometimes useful for testing. 

This page serves as a reference for the options and parameters.

Positional command line arguments
===================================

.. code-block:: console

   $ metadata_server [ <logging path> [ <listen port> ] ]

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - Logging path
     - Current directory
     - Path to store metadata logs into
   * - Listen port
     - ``3105``
     - TCP listen port. If used, log path must be specified beforehand.

Starting metadata server
============================

Starting temporarily
-----------------------------

.. code-block:: console

   $ nohup metadata_server &
   $ MS_PID=$!

Using ``nohup`` and ``&`` sends metadata server to run in the background.

.. note::
   * Logs are saved to the current directory, under ``metadata_server_logs``.
   * The default listening port is 3105

Starting temporarily with non-default port
------------------------------------------------

To use a non-default port, specify the logging path as well.

.. code-block:: console

   $ nohup metadata_server /home/rhendricks/metadata_logs 9241 &
   $ MS_PID=$!

Using ``nohup`` and ``&`` sends metadata server to run in the background.

.. note::
   * Logs are saved to the ``/home/rhendricks/metadata_logs`` directory.
   * The listening port is 9241

Stopping metadata server
----------------------------

To stop metadata server:

.. code-block:: console

   $ kill -9 $MS_PID

.. tip:: It is safe to stop any SQream DB component at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.
