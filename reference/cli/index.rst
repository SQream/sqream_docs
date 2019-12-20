.. _cli_reference:

************************
Command line programs
************************

SQream contains several command line programs for starting, managing, and configuring SQream DB clusters.

This topic contains the reference for these programs, as well as flags and configuration settings.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`SQream SQL <sqream_sql_cli_reference>`
     - Built-in SQL client
   * - :ref:`sqreamd <sqreamd_cli_reference>`
     - Start a SQream DB worker
   * - :ref:`SqreamStorage <sqream_storage_cli_reference>`
     - Initialize a cluster and set superusers
   * - :ref:`metadata_server <metadata_server_cli_reference>`
     - The cluster manager/coordinator that enables scaling SQream DB.
   * - :ref:`server_picker <server_picker_cli_reference>`
     - Load balancer end-point
   * - :ref:`sqream_console <sqream_console_cli_reference>`
     - Dockerized convenience wrapper for operations
   * - :ref:`upgrade_storage <upgrade_storage_cli_reference>`
     - Upgrade metadata schemas when upgrading between major versions

.. toctree::
   :maxdepth: 1
   :hidden:
   
   sqream_sql
   sqreamd
   sqream_storage
   metadata_server
   server_picker
   sqream_console
   upgrade_storage
