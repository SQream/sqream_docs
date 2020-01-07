.. _concurrency_and_locks:

***********************
Concurrency and locks
***********************

Statements in SQream DB can lock resources that are written or modified. 

The locking system is the method of concurrency control within SQream DB. It stops transactions from overwriting each other and creating inconsistencies.

When a pending change from one statement conflicts with another, the later statement must wait for the earlier transaction to complete.

.. _locking_modes:

Locking modes
================

SQream DB has two locking modes:

* 
   ``exclusive`` - this lock mode prevents the resource from being read or modified by other statements (it excludes the object). It is usually obtained to modify the data or structure. 
   
   This lock tells other statements that they'll have to wait in order to read or write to the object.
   
   DDL operations are always exclusive.
   

* 
   ``inclusive`` - For some read operations, an inclusive lock is obtained on a specific object. This prevents other statements from obtaining an exclusive lock on the object.
   
   This lock allows other statements to read data from the object, but they'll have to wait in order to modify it.

When are locks obtained?
============================

.. list-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   * - Operation
     - :ref:`select`
     - DML (:ref:`insert`)
     - DML (:ref:`delete`, :ref:`truncate`)
     - DDL
   * - :ref:`select`
     - Concurrent
     - Concurrent
     - Concurrent
     - Concurrent
   * - DML (:ref:`insert`)
     - Concurrent
     - Concurrent
     - Concurrent
     - Block
   * - DML (:ref:`delete`, :ref:`truncate`)
     - Concurrent
     - Concurrent
     - Wait
     - Block
   * - DDL
     - Concurrent
     - Block
     - Block
     - Block

.. note::
   
   * A DDL operation will block all other statements from requesting a lock, and the statement will fail with an error.
   
   * DML operations will cause other statements to wait, rather than block. Because most locks are short-lived, SQream DB will wait for a period of 3 seconds before giving up and returning an error. This parameter is called ``statementLockTimeout`` and is modifiable.

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


Troubleshooting locks
==========================

Sometimes, a rare situation can occur where a lock is never freed. 

The workflow for troubleshooting locks is:

#. Identify which statement has obtained locks
#. Understand if the statement is itself stuck, or waiting for another statement
#. Try to abort the offending statement
#. Force the stale locks to be removed

Example
-----------

We will assume that the statement from the previous example is stuck (statement #\ ``287``). We can attempt to abort it using :ref:`stop_statement`:

.. code-block:: psql

   t=> SELECT STOP_STATEMENT(287);
   executed

If the locks still appear in the :ref:`show_locks` utility, we can force remove the stale locks:

.. code-block:: psql

   t=> SELECT RELEASE_DEFUNCT_LOCKS();
   executed

.. warning:: This operation can cause some statements to fail on the specific worker on which they are queued. This is intended as a "last resort" to solve stale locks.