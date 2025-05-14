:orphan:

.. _remove:

******
REMOVE
******

The ``REMOVE`` function addresses the need to remove files from the database's internal staging area.


Syntax
======

.. code-block:: postgres

	REMOVE <'SQDB-cluster-relative-file-path'>

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``SQDB-cluster-relative-file-path``
     - File path to remove - relative to the defined SQDB cluster staging area.
   

Important Considerations
========================
	* The SQDB cluster staging area is configured using the ``stagingAreaRootPath`` flag.
	* The command is limited to a single file deletion per execution.
	* File extensions are limited to supported FDWs.
	* The command execution is CPU based and does not use GPU Workers.
	* Up to 50 concurrent ''PUT`` / ``GET`` / ``REMOVE`` operation are supported per SQDB cluster.
	




Permissions
=============

The role must have the ``SUPERUSER`` privilege.