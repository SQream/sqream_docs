:orphan:

.. _get:

***
GET
***

The ``GET`` function addresses the need to transfer data files stored within the database's internal staging area to a user's local file system.


Syntax
======

.. code-block:: postgres

	GET <'SQDB-cluster-relative-file-path'> TO <'local-file-path'>;

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``SQDB-cluster-relative-file-path``
     - Source File path - relative to the defined SQDB cluster staging area.
   * - ``local-file-path``
     - Destination File path - on the executing client machine.

Important Considerations
========================
    * File size may be up to 25MB.
	* The SQDB cluster staging area's root path is configured using the ``stagingAreaRootPath`` flag. By default, this area is created within the defined ``storageClusterPath`` as a subdirectory named staging_area. This ``staging_area`` directory contains two subdirectories: ``content``, intended for user-uploaded data, and ``temp``, reserved for internal system operations.
	* The command is limited to a single file copy per execution.
	* File extensions are limited to supported FDWs.
	* The command execution is CPU based and does not use GPU Workers.
	* Up to 50 concurrent ``PUT`` / ``GET`` / ``REMOVE`` operation are supported per SQDB cluster.
	* The feature is supported for the following drivers: PySQream, JDBC, ODBC
	

Permissions
=============

The role must have the ``SUPERUSER`` privilege.