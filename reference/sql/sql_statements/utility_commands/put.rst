:orphan:

.. _put:

***
PUT
***

The ``PUT`` function addresses the need to transfer data files stored in a user's local file system to the database's internal staging area.


Syntax
======

.. code-block:: postgres

	PUT <'local-file-path'> INTO <'SQDB-cluster-relative-file-path'> [OVERWRITE]

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``local-file-path``
     - Source File path - on the executing client machine.
   * - ``SQDB-cluster-relative-file-path``
     - Destination File path - relative to the defined SQDB cluster staging area.
   * - ``OVERWRITE``
     - When used existing files will be overridden.
   

Important Considerations
========================
	* File size may be up to 25MB.
	* The SQDB cluster staging area's root path is configured using the ``stagingAreaRootPath`` flag. By default, this area is created within the defined ``storageClusterPath`` as a subdirectory named staging_area. This ``staging_area`` directory contains two subdirectories: ``content``, intended for user-uploaded data, and ``temp``, reserved for internal system operations.
	* The command is limited to a single file copy per execution.
	* File extensions are limited to supported FDWs.
	* The command execution is CPU based and does not use GPU Workers.
	* Up to 50 concurrent ``PUT`` / ``GET`` / ``REMOVE`` operation are supported per SQDB cluster.

	




Permissions
=============

The role must have the ``SUPERUSER`` privilege.