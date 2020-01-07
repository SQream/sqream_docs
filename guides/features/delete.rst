.. _delete_guide:

***********************
Deleting data
***********************

SQream DB allows users to delete data. However, the process is actually two-step.

Read this guide to understand how SQream DB deletes data.

How does deleting in SQream DB work?
========================================

In SQream DB, deleting data is a two-step process. :ref:`delete` of rows does not immediately remove the underlying data.

This approach is necessary to gain the benefits of :ref:`time_based_data_management`. Eventually, when the new insert is completed, the deleted row version is no longer of interest to any transaction. The space it occupies can then be freed up. This is performed in the physical delete operation that follows.


Phase 1: Logical Delete
---------------------------

When a :ref:`delete` statement is run, SQream DB marks rows as deleted, but they remain on-disk until a cleanup process is initiated.

The result set for :ref:`select` queries will not contain the deleted data. Data is marked for deletion, but not physically deleted from disk.

Phase 2: Clean-up
--------------------

The cleanup process is not automatic, as it can take some time for very large tables which some administrators prefer to perform during off-peak hours.

Files marked for deletion during the logical deletion stage are removed from disk. This is achieved by calling both utility function commands: ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS`` sequentially.

.. note::
   * :ref:`alter_table` and other DDL operations are blocked on tables that require clean-up. See more in the :ref:`concurrency_and_locks` guide.
   * SQream DB may prevent a very long delete process. If the estimated time is beyond the threshold, the error message will explain how to override this limitation and continue the process.

Notes on data deletion
=========================================

Deleting data does not free up space
-----------------------------------------

With the exception of a full table delete (:ref:`TRUNCATE<truncate>`), deleting data does not free up disk space. To free up disk space, trigger the cleanup process.

Select performance on deleted rows
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

   -- Chunk reorganization (SWEEP)
   farm=> SELECT CLEANUP_CHUNKS('public','cool_animals');
   executed

   -- Delete leftover files (VACUUM)
   farm=> SELECT CLEANUP_EXTENTS('public','cool_animals');
   executed
   
   
   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   
   0 rows


.. soft update concept

.. delete cleanup and it's properties. automatic/manual, in transaction or background

.. automatic background gives fast delete, minimal transaction overhead,
.. small cost to queries until background reorganised

.. pointer to the time based management idea - delete is optimised for this

.. when does delete use the metadata effectively

.. more examples

