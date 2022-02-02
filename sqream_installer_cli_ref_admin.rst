.. _sqream_installer_cli_ref_admin:

*********************************
SQream Installer
*********************************
``sqream-installer`` is an application that prepares and configures a dockerized SQream DB installation.

This page serves as a reference for the options and parameters. 

.. contents:: In this topic:
   :local:


Operations and flag reference
===============================

Command line flags
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Flag
     - Description
   * - ``-i``
     - Loads the docker images for installation
   * - ``-k``
     - Load new licenses from the ``license`` subdirectory
   * - ``-K``
     - Validate licenses
   * - ``-f``
     - Force overwrite any existing installation **and data directories currently in use**
   * - ``-c <path to read configuration from>``
     - Specifies a path to read and store configuration files in. Defaults to ``/etc/sqream``.
   * - ``-v <storage cluster path>``
     - Specifies a path to the storage cluster. The path is created if it does not exist.
   * - ``-l <startup log path>``
     - Specifies a path to store system startup logs. Defaults to ``/var/log/sqream``
   * - ``-d <path>``
     - Specifies a path to expose to SQream DB workers. To expose several paths, repeat the usage of this flag.
   * - ``-s``
     - Shows system settings
   * - ``-r``
     - Reset the system configuration. This flag can't be combined with other flags.

Usage
=============

Install SQream DB for the first time
----------------------------------------

Assuming license package tarball has been placed in the ``license`` subfolder.

* The path where SQream DB will store data is ``/home/rhendricks/sqream_storage``.

* Logs will be stored in /var/log/sqream

* Source CSV, Parquet, and ORC files can be accessed from ``/home/rhendricks/source_data``. All other directory paths are hidden from the Docker container.

.. code-block:: console
   
   # ./sqream-install -i -k -v /home/rhendricks/sqream_storage -l /var/log/sqream -c /etc/sqream -d /home/rhendricks/source_data

.. note:: Installation commands should be run with ``sudo`` or root access.

Modify exposed directories
-------------------------------

To expose more directory paths for SQream DB to read and write data from, re-run the installer with additional directory flags.

.. code-block:: console
   
   # ./sqream-install -d /home/rhendricks/more_source_data

There is no need to specify the initial installation flags - only the modified exposed directory paths flag.


Install a new license package
----------------------------------

Assuming license package tarball has been placed in the ``license`` subfolder.

.. code-block:: console
   
   # ./sqream-install -k

View system settings
----------------------------

This information may be useful to identify problems accessing directory paths, or locating where data is stored.

.. code-block:: console
   
   # ./sqream-install -s
   SQREAM_CONSOLE_TAG=1.7.4
   SQREAM_TAG=2020.1
   SQREAM_EDITOR_TAG=3.1.0
   license_worker_0=[...]
   license_worker_1=[...]
   license_worker_2=[...]
   license_worker_3=[...]
   SQREAM_VOLUME=/home/rhendricks/sqream_storage
   SQREAM_DATA_INGEST=/home/rhendricks/source_data
   SQREAM_CONFIG_DIR=/etc/sqream/
   LICENSE_VALID=true
   SQREAM_LOG_DIR=/var/log/sqream/
   SQREAM_USER=sqream
   SQREAM_HOME=/home/sqream
   SQREAM_ENV_PATH=/home/sqream/.sqream/env_file
   PROCESSOR=x86_64
   METADATA_PORT=3105
   PICKER_PORT=3108
   NUM_OF_GPUS=8
   CUDA_VERSION=10.1
   NVIDIA_SMI_PATH=/usr/bin/nvidia-smi
   DOCKER_PATH=/usr/bin/docker
   NVIDIA_DRIVER=418
   SQREAM_MODE=single_host


.. _upgrade_with_docker:

Upgrading to a new version of SQream DB
----------------------------------------------

When upgrading to a new version with Docker, most settings don't need to be modified.

The upgrade process replaces the existing docker images with new ones.

#. Obtain the new tarball, and untar it to an accessible location. Enter the newly extracted directory.

#. 
   Install the new images
   
   .. code-block:: console
   
      # ./sqream-install -i

#. The upgrade process will check for running SQream DB processes. If any are found running, the installer will ask to stop them in order to continue the upgrade process. Once all services are stopped, the new version will be loaded. 

#. After the upgrade, open :ref:`sqream_console_cli_reference` and restart the desired services.