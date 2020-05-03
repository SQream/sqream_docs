.. _delete_guide:

***********************
Deleting data
***********************

SQream DB supports deleting data, but it's important to understand how this works and how to maintain deleted data.

How does deleting in SQream DB work?
========================================

In SQream DB, when you run a delete statement, any rows that match the delete predicate will no longer be returned when running subsequent queries.
Deleted rows are tracked in a separate location, in *delete predicates*.

After the delete statement, a separate process can be used to reclaim the space occupied by these rows, and to remove the small overhead that queries will have until this is done. 

Some benefits to this design are:

#. Delete transactions complete quickly

#. The total disk footprint overhead at any time for a delete transaction or cleanup process is small and bounded (while the system still supports low overhead commit, rollback and recovery for delete transactions).


Phase 1: Delete
---------------------------

.. TODO: isn't the delete cleanup able to complete a certain amount of work transactionally, so that you can do a massive cleanup in stages?

.. TODO: our current best practices is to use a cron job with sqream sql to run the delete cleanup. we should document how to do this, we have customers with very different delete schedules so we can give a few extreme examples and when/why you'd use them
   
When a :ref:`delete` statement is run, SQream DB records the delete predicates used. These predicates will be used to filter future statements on this table until all this delete predicate's matching rows have been physically cleaned up.

This filtering process takes full advantage of SQream's zone map feature.

Phase 2: Clean-up
--------------------

The cleanup process is not automatic. This gives control to the user or DBA, and gives flexibility on when to run the clean up.

Files marked for deletion during the logical deletion stage are removed from disk. This is achieved by calling both utility function commands: ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS`` sequentially.

.. note::
   * :ref:`alter_table` and other DDL operations are blocked on tables that require clean-up. See more in the :ref:`concurrency_and_locks` guide.
   * If the estimated time for a cleanup processs is beyond a threshold, you will get an error message about it. The message will explain how to override this limitation and run the process anywhere.

Notes on data deletion
=========================================

Deleting data does not free up space
-----------------------------------------

With the exception of a full table delete (:ref:`TRUNCATE<truncate>`), deleting data does not free up disk space. To free up disk space, trigger the cleanup process.

``SELECT`` performance on deleted rows
----------------------------------------

Queries on tables that have deleted rows may have to scan data that hasn't been cleaned up.
In some cases, this can cause queries to take longer than expected. To solve this issue, trigger the cleanup process.

Use ``TRUNCATE`` instead of ``DELETE``
---------------------------------------
For tables that are frequently emptied entirely, consider using :ref:`truncate` rather than :ref:`delete`. TRUNCATE removes the entire content of the table immediately, without requiring a subsequent cleanup to free up disk space.

Cleanup is I/O intensive
-------------------------------

The cleanup process actively compacts tables by writing a complete new version of column chunks with no dead space. This minimizes the size of the table, but can take a long time. It also requires extra disk space for the new copy of the table, until the operation completes.

Cleanup operations can create significant I/O load on the database. Consider this when planning the best time for the cleanup process.

If this is an issue with your environment, consider using ``CREATE TABLE AS`` to create a new table and then rename and drop the old table.


Example
=============

Deleting values from a table
------------------------------

.. code-block:: psql

   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
   farm=> DELETE FROM cool_animals WHERE weight > 1000;
   executed
   
   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   6,\N,\N
   
   4 rows

Deleting values based on more complex predicates
---------------------------------------------------

.. code-block:: psql

   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
   farm=> DELETE FROM cool_animals WHERE weight > 1000;
   executed
   
   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   6,\N,\N
   
   4 rows

Identifying and cleaning up tables
---------------------------------------

List tables that haven't been cleaned up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql
   
   farm=> SELECT t.table_name FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      GROUP BY 1;
   cool_animals
   
   1 row

Identify predicates for clean-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   weight > 1000
   
   1 row

Triggering a cleanup
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   -- Chunk reorganization (aka SWEEP)
   farm=> SELECT CLEANUP_CHUNKS('public','cool_animals');
   executed

   -- Delete leftover files (aka VACUUM)
   farm=> SELECT CLEANUP_EXTENTS('public','cool_animals');
   executed
   
   
   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   
   0 rows



Best practices for data deletion
=====================================

* Run ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS`` after large ``DELETE`` operations.

* When deleting large proportions of data from very large tables, consider running a ``CREATE TABLE AS`` operation instead, then rename and drop the original table.

* Never kill VACUUM on catalog tables.

* SQream DB is optimised for time-based data. When data is naturally ordered by a date or timestamp, deleting based on those columns will perform best. For more information, see our :ref:`time based data management guide<time_based_data_management>`.

.. soft update concept

.. delete cleanup and it's properties. automatic/manual, in transaction or background

.. automatic background gives fast delete, minimal transaction overhead,
.. small cost to queries until background reorganised

.. when does delete use the metadata effectively

.. more examples

