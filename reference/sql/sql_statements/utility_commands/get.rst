:orphan:

.. _get:

***
GET
***

The ``GET`` function addresses the need to transfer data files stored within the database's internal staging areas to a user's local file system.


Syntax
======

.. code-block:: postgres

	GET <'SQDB-cluster-relative-file-path'> TO <'local-file-path'>

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
	* The SQDB cluster staging area is configured using the ``stagingAreaRootPath`` flag.
	* The command is limited to a single file copy per execution.
	* File extensions are limited to supported FDWs.
	* The command execution is CPU based and does not use GPU Workers.
	* Up to 50 concurrent ''PUT`` / ``GET`` / ``REMOVE`` operation are supported per SQDB cluster.
	




Permissions
=============

The role must have the ``SUPERUSER`` privilege.