.. _metadata_server_cli_reference:

*************************
metadata_server
*************************

SQream DB's cluster manager/coordinator is called ``metadata_server``.

In general, you should not need to run ``metadata_server`` manually, but it is sometimes useful for testing. 

This page serves as a reference for the options and parameters.

Command Line Arguments
==================================

.. list-table:: 
   :widths: 2 3 5 
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``--config``
     - ``/home/omert/.sqream/metadata_server_config.json``
     - The configuration file to use
   * - ``--port``
     - ``3105``
     - The metadata server listening port	 
   * - ``--log_path``
     - ``./metadata_server_log``
     - The ``metadata_server`` log file output contains information about the activities and events related to the metadata server of a system.
   * - ``--log4_config``
     - None
     - Specifies the location of the configuration file for the ``Log4cxx`` logging library.
   * - ``--num_deleters``
     - 1
     - Specifies the number of threads to use for the file reaper in a system or program.
   * - ``--metadata_path``
     - ``<...sqreamd/leveldb>``
     - Specifies the path to the directory where metadata files are stored for a system or program.
   * - ``--help``
     - None
     - Used to display a help message or documentation for a particular program or command.
	 

Starting metadata server
============================

Starting temporarily
---------------------

.. code-block:: console

	nohup metadata_server -config ~/.sqream/metadata_server_config.json &
	MS_PID=$!

Using ``nohup`` and ``&`` sends metadata server to run in the background.

.. note::
   * Logs are saved to the current directory, under ``metadata_server_logs``.
   * The default listening port is 3105

Starting temporarily with non-default port
------------------------------------------------

To use a non-default port, specify the logging path as well.

.. code-block:: console

	nohup metadata_server --log_path=/home/rhendricks/metadata_logs --port=9241 &
	MS_PID=$!

Using ``nohup`` and ``&`` sends metadata server to run in the background.

.. note::
   * Logs are saved to the ``/home/rhendricks/metadata_logs`` directory.
   * The listening port is 9241
   
Stopping metadata server
----------------------------

To stop metadata server:

.. code-block:: console

	kill -9 $MS_PID

.. tip:: It is safe to stop any SQream DB component at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.
