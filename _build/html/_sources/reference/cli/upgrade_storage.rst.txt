.. _upgrade_storage_cli_reference:

*************************
upgrade_storage
*************************

``upgrade_storage`` is used to upgrade metadata schemas, when upgrading between major versions.

This page serves as a reference for the options and parameters.

Running upgrade_storage
=========================

``upgrade_storage`` can be found in the ``bin`` directory of your SQream DB installation.


Command line arguments
==========================

``upgrade_storage`` contains one positional argument:

.. code-block:: console

   $ upgrade_storage <storage path>

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Required
     - Description
   * - Storage path
     - ✓
     - Full path to a valid storage cluster

Results and error codes
========================

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Result
     - Message
     - Description
   * - Success
     - ``storage has been upgraded successfully to version 26``
     - Storage has been successfully upgraded
   * - Success
     - ``no need to upgrade``
     - Storage doesn't need an upgrade
   * - Failure: can't read storage
     - ``RocksDB is in use by another application``
     - Check permissions, and ensure no SQream DB workers or :ref:`metadata_server <metadata_server_cli_reference>` are running when performing this operation.


Examples
=============

Upgrade SQream DB's storage cluster
--------------------------------------

.. code-block:: console

   $ ./upgrade_storage /home/rhendricks/raviga_database
   get_rocksdb_version path{/home/rhendricks/raviga_database}
   current storage version 23
   upgrade_v24
   upgrade_storage to 24
   upgrade_storage to 24 - Done
   upgrade_v25
   upgrade_storage to 25
   upgrade_storage to 25 - Done
   upgrade_v26
   upgrade_storage to 26
   upgrade_storage to 26 - Done
   validate_rocksdb
   storage has been upgraded successfully to version 26

This message confirms that the cluster has already been upgraded correctly.
