.. _cli_reference:

************************
Command Line Programs
************************

SQream contains several command line programs for using, starting, managing, and configuring SQream DB clusters.

This topic contains the reference for these programs, as well as flags and configuration settings.

.. list-table:: User CLIs
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`sqream sql<sqream_sql_cli_reference>`
     - Built-in SQL client

.. list-table:: SQream DB cluster components
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`sqreamd <sqreamd_cli_reference>`
     - Start a SQream DB worker
   * - :ref:`metadata_server <metadata_server_cli_reference>`
     - The cluster manager/coordinator that enables scaling SQream DB.
   * - :ref:`server_picker <server_picker_cli_reference>`
     - Load balancer end-point

.. list-table:: SQream DB utilities
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`SqreamStorage <sqream_storage_cli_reference>`
     - Initialize a cluster and set superusers
   * - :ref:`upgrade_storage <upgrade_storage_cli_reference>`
     - Upgrade metadata schemas when upgrading between major versions

.. list-table:: Docker utilities
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`sqream_console <sqream_console_cli_reference>`
     - Dockerized convenience wrapper for operations
   * - :ref:`sqream_installer <sqream_installer_cli_reference>`
     - Dockerized installer

.. toctree::
   :maxdepth: 1
   :hidden:
   
   metadata_server
   sqreamd
   sqream_console
   server_picker
   sqream_storage
   sqream sql<sqream_sql>
   upgrade_storage
