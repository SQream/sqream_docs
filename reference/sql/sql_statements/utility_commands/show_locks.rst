:orphan:

.. _show_locks:

**********
SHOW LOCKS
**********

``SHOW_LOCKS`` returns a list of locks from across the cluster.

Read more about locks in :ref:`concurrency_and_locks`.

Syntax
======

.. code-block:: postgres

	SELECT SHOW_LOCKS()

Output
======

This function returns a list of active locks. If no locks are active in the cluster, the result set will be empty.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description   
   * - ``stmt_id``
     - Statement ID that caused the lock.
   * - ``stmt_string``
     - Statement text
   * - ``username``
     - The role that executed the statement
   * - ``server``
     - The worker node's IP
   * - ``port``
     - The worker node's port
   * - ``locked_object``
     - The full qualified name of the object being locked, separated with ``$`` (e.g. ``table$t$public$nba2`` for table ``nba2`` in schema ``public``, in database ``t``
   * - ``lockmode``
     - The locking mode (:ref:`inclusive<locking_modes>` or :ref:`exclusive<locking_modes>`).
   * - ``statement_start_time``
     - Timestamp the statement started
   * - ``lock_start_time``
     - Timestamp the lock was obtained
   * - ``is_statement_active``
     - Is the statement causing the lock running or not
   * - ``is_snapshot_active``
     - Is the snapshot of the metadata keys, created by the statement, still active or not	 


Examples
========

.. code-block:: postgres

	SELECT SHOW_LOCKS();
	
Output:

.. code-block:: console

	statement id |statement string                  |username |server   |port |locked object  |lock mode |statement start time |lock start time    |is_statement_active |is_snapshot_active
	-------------+----------------------------------+---------+---------+-----+---------------+----------+---------------------+-------------------+--------------------+------------------
	2            |create or replace table t (x int);|sqream   |127.0.0.1|5000 |database$master|Inclusive |04-07-2024 15:07:02  |2024-07-04 15:07:02|1                   |1


Permissions
===========

This utility function requires a ``CONNECT`` permission on the database level.
