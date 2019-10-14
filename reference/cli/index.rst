.. _cli_reference:

CLI reference overview
=====================================

SQream contains several command line utilities for starting, managing, and configuring SQream DB clusters.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`sqreamd <sqreamd>`
     - Start a SQream DB worker
   * - :ref:`SqreamStorage <sqream_storage>`
     - Initialize a cluster and manage superusers
   * - :ref:`metadata_server <metadata_server>`
     - The cluster manager/coordinator that enables scaling SQream DB.
   * - :ref:`server_picker <server_picker>`
     - Load balancer end-point
   * - :ref:`sqream_console <sqream_console>`
     - Dockerized convenience wrapper for operations
   * - :ref:`upgrade_storage <upgrade_storage>`
     - Upgrade metadata schemas when upgrading between major versions

.. toctree::
   :maxdepth: 1
   :hidden:
   
   sqream_sql
   sqream_storage
   sqreamd
   metadata_server
   server_picker
   upgrade_storage
