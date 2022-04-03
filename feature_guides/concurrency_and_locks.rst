.. _concurrency_and_locks:

***********************
Concurrency and Locks
***********************

Locks are used in SQream DB to provide consistency when there are multiple concurrent transactions updating the database. 

Read only transactions are never blocked, and never block anything. Even if you drop a database while concurrently running a query on it, both will succeed correctly (as long as the query starts running before the drop database commits).

.. _locking_modes:

Locking modes
================

SQream DB has two kinds of locks:

* 
   ``exclusive`` - this lock mode prevents the resource from being modified by other statements
   
   This lock tells other statements that they'll have to wait in order to change an object.
   
   DDL operations are always exclusive. They block other DDL operations, and update DML operations (insert and delete).

* 
   ``inclusive`` - For insert operations, an inclusive lock is obtained on a specific object. This prevents other statements from obtaining an exclusive lock on the object.
   
   This lock allows other statements to insert or delete data from a table, but they'll have to wait in order to run DDL.

When are locks obtained?
============================

.. list-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   * - Operation
     - :ref:`select`
     - :ref:`insert`
     - :ref:`delete`, :ref:`truncate`
     - DDL
   * - :ref:`select`
     - Concurrent
     - Concurrent
     - Concurrent
     - Concurrent
   * - :ref:`insert`
     - Concurrent
     - Concurrent
     - Concurrent
     - Wait
   * - :ref:`delete`, :ref:`truncate`
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

Global locks
----------------

Some operations require exclusive global locks at the cluster level. These usually short-lived locks will be obtained for the following operations:

   * :ref:`create_database`
   * :ref:`create_role`
   * :ref:`create_table`
   * :ref:`alter_role`
   * :ref:`alter_table`
   * :ref:`drop_database`
   * :ref:`drop_role`
   * :ref:`drop_table`
   * :ref:`grant`
   * :ref:`revoke`

Monitoring locks
===================

Monitoring locks across the cluster can be useful when transaction contention takes place, and statements appear "stuck" while waiting for a previous statement to release locks.

The utility :ref:`show_locks` can be used to see the active locks.

In this example, we create a table based on results (:ref:`create_table_as`), but we are also effectively dropping the previous table (by using ``OR REPLACE`` which also :ref:`drops the table<drop_table>`). Thus, SQream DB applies locks during the table creation process to prevent the table from being altered during it's creation.


.. code-block:: psql

   t=> SELECT SHOW_LOCKS();
   statement_id | statement_string                                                                                | username | server       | port | locked_object                   | lockmode  | statement_start_time | lock_start_time    
   -------------+-------------------------------------------------------------------------------------------------+----------+--------------+------+---------------------------------+-----------+----------------------+--------------------
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | database$t                      | Inclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | globalpermission$               | Exclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | schema$t$public                 | Inclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | table$t$public$nba2$Insert      | Exclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | table$t$public$nba2$Update      | Exclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30