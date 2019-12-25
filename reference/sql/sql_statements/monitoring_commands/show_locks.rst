.. _show_locks:

********************
SHOW_LOCKS
********************

``SHOW_LOCKS`` returns a list of locks from across the cluster.

Permissions
=============

The role must have the ``SUPERUSER`` privileges.

Syntax
==========

.. code-block:: postgres

   show_locks_statement ::=
       SELECT SHOW_LOCKS()
       ;

Parameters
============

None

Returns
=========

This function returns a list of active locks. If no locks are active in the cluster, the result set will be empty.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1
   
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
     - The locking mode (``inclusive`` or ``exclusive``).
   * - ``statement_start_time``
     - Timestamp the statement started
   * - ``lock_start_time``
     - Timestamp the lock was obtained

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


Examples
===========

Using ``SHOW_LOCKS`` to see active locks
---------------------------------------------------

In this example, we create a table based on results (:ref:`create_table_as`), but we are also effectively dropping the previous table (by using ``OR REPLACE``). Thus, SQream DB applies locks during the table creation process to prevent the table from being altered during it's creation.


.. code-block:: psql

   t=> SELECT SHOW_LOCKS();
   statement_id | statement_string                                                                                | username | server       | port | locked_object                   | lockmode  | statement_start_time | lock_start_time    
   -------------+-------------------------------------------------------------------------------------------------+----------+--------------+------+---------------------------------+-----------+----------------------+--------------------
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | database$t                 | Inclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | globalpermission$               | Exclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | schema$t$public            | Inclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | table$t$public$nba2$Insert | Exclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30
   287          | CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1; | sqream   | 192.168.1.91 | 5000 | table$t$public$nba2$Update | Exclusive | 2019-12-26 00:03:30  | 2019-12-26 00:03:30


