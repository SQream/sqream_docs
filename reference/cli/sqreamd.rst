.. _sqreamd_cli_reference:

*************************
sqreamd (CLI) Reference
*************************

SQream DB's main worker is called *sqreamd*. 

In general, you should not need to run ``sqreamd`` manually, but it is sometimes useful for testing. 

This page serves as a reference for the options and parameters.

Starting SQream DB
====================

Start SQream DB temporarily
-----------------------------

.. code-block:: console

   $ nohup sqreamd -config ~/.sqream/sqream_config.json &
   $ SQREAM_PID=$!

Using ``nohup`` and ``&`` sends SQream DB to run in the background.

To stop the active instance:

.. code-block:: console

   $ kill -9 $SQREAM_PID

.. tip:: It is safe to stop SQream DB at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.

Command line arguments
==========================

**sqreamd** supports the following command line arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``--version``
     - None
     - Outputs the version of SQream DB and immediately exits.
   * - ``-config``
     - ``$HOME/.sqream/sqream_config.json``
     - Specifies the configuration file to use
   * - ``--port_ssl``
     - Don't use SSL
     - When specified, tells SQream DB to listen for SSL connections

Positional command arguments
------------------------------

**sqreamd** also supports positional arguments, when not using a configuration file.

This method can be used to temporarily start a SQream DB instance for testing.

.. code-block:: console

   $ sqreamd <Storage path> <GPU ordinal> <TCP listen port (unsecured)> <License path>

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Required
     - Description
   * - Storage path
     - ✓
     - Full path to a valid SQream DB persistant storage
   * - GPU Ordinal
     - ✓
     - Number representing the GPU to use. Check GPU ordinals with `nvidia-smi -L`
   * - TCP listen port (unsecured)
     - ✓
     - TCP port SQream DB should listen on. Recommended: 5000
   * - License path
     - ✓
     - Full path to a SQream DB license file
