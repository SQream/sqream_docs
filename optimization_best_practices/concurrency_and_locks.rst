.. _concurrency_and_locks:

*********************
Concurrency and Locks
*********************

Locks are used in BLUE to provide consistency when there are multiple concurrent transactions updating the database. 

Read only transactions are never blocked, and never block anything. Even if you drop a database while concurrently running a query on it, both will succeed correctly (as long as the query starts running before the drop database commits).

.. _locking_modes:

Locking Modes
=============

BLUE has two kinds of locks:

* 
   ``exclusive`` - this lock mode prevents the resource from being modified by other statements.
   
   This lock tells other statements that they'll have to wait in order to change an object.
   
   DDL operations are always exclusive. They block other DDL operations, and update DML operations such as ``INSERT``.

* 
   ``inclusive`` - For ``INSERT`` operations, an inclusive lock is obtained on a specific object. This prevents other statements from obtaining an exclusive lock on the object.
   
   This lock allows other statements to insert or delete data from a table, but they'll have to wait in order to run DDL.

When are Locks Obtained?
========================

.. list-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   * - Operation
     - :ref:`describe_locks`
     - :ref:`INSERT`
     - :ref:`DELETE`, :ref:`TRUNCATE`
     - DDL
   * - :ref:`describe_locks`
     - Concurrent
     - Concurrent
     - Concurrent
     - Concurrent
   * - :ref:`DELETE`
     - Concurrent
     - Concurrent
     - Wait
     - Wait
   * - DDL
     - Concurrent
     - Wait
     - Wait
     - Wait


Statements that wait will exit with an error if they hit the lock timeout. The default timeout is 3 seconds, see ``statementLockTimeout``.

Monitoring Locks
================

Monitoring locks across the cluster can be useful when transaction contention takes place, and statements appear "stuck" while waiting for a previous statement to release locks.

The utility :ref:`describe_locks` can be used to see the active locks.


.. code-block:: postgres

  DESCRIBE_LOCKS();
   
Output:

.. code-block:: console

  statement_id|username|server      |port|locked_object|lock_mode|statement_start_time|lock_start_time     |statement_string                                                                               |
  ------------+--------+------------+----+-------------+---------+--------------------+--------------------+-----------------------------------------------------------------------------------------------+
  287         |sqream  |192.168.1.91|5000|database$t   |Inclusive| 2019-12-26 00:03:30| 2019-12-26 00:03:30|CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1;|

For more information on troubleshooting lock related issues, see :ref:`lock_related_issues`.