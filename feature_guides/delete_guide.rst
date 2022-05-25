.. _delete_guide:

***********************
Deleting Data
***********************
The **Deleting Data** page describes how the **Delete** statement works and how to maintain data that you delete:

.. contents::
   :local:
   :depth: 1

Overview
========================================
Deleting data typically refers to deleting rows, but can refer to deleting other table content as well. The general workflow for deleting data is to delete data followed by triggering a cleanup operation. The cleanup operation reclaims the space occupied by the deleted rows, eliminating the small overhead for running queries on occupied space, discussed further below.

The **DELETE** statement deletes rows defined by a predicate you specify, and prevents them from appearing in subsequent queries.

For example, the predicate below deletes rows containing animals heavier than 1000 weight units:

.. code-block:: psql

   farm=> DELETE FROM cool_animals WHERE weight > 1000;
   executed
	  
Rows that you delete are tracked in a separate location called *delete predicates*.

**Comment** - *We should maybe tell the user a bit more about this location, such as where this location is, i.e., is it a folder, etc...?*

**Comment** - *While true, it may not be relevant to include this information in a feature description.*

Some benefits to this design are:

#. Delete transactions complete quickly

#. The total disk footprint overhead at any time for a delete transaction or cleanup process is small and bounded (while the system still supports low overhead commit, rollback and recovery for delete transactions).

The Deletion Process
==========
Deleting rows occurs in the following two phases:

* **Phase 1 - Deletion** - SQream records the predicates you specify and uses them to filter queries run on the same table. This filtering operation takes full advantage of SQream's zone map feature.

  **Comment** - *We should say something else about the zone map feature, or remove it.*

   ::
   
* **Phase 2 - Cleanup** - The cleanup phase is not automated, letting users or DBAs control when to activate it. Files marked for deletion during Phase 1 are removed from disk, achieved by sequentially running the utility function commands ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS``.

.. TODO: isn't the delete cleanup able to complete a certain amount of work transactionally, so that you can do a massive cleanup in stages?

.. TODO: our current best practices is to use a cron job with sqream sql to run the delete cleanup. we should document how to do this, we have customers with very different delete schedules so we can give a few extreme examples and when/why you'd use them.

Usage Notes
=====================
The **Usage Notes** section includes important information about the DELETE statement:

.. contents::
   :local:
   :depth: 1
   
General Notes
----------------

* :ref:`alter_table` and other DDL operations are blocked on tables that require clean-up. For more information, see :ref:`concurrency_and_locks`. If the estimated cleanup time exceeds the permitted threshold, an error message is displayed describing how to override the threshold limitation.

   ::

* If the number of deleted records exceeds the threshold defined by the ``mixedColumnChunksThreshold`` parameter, the delete operation is aborted. This alerts users that the large number of deleted records may result in a large number of mixed chunks. To circumvent this alert, use the following syntax (replacing ``XXX`` with the desired number of records) before running the delete operation:

  .. code-block:: postgres

     set mixedColumnChunksThreshold=XXX;
   
**Comment** - *I didn't see the above parameter in the Configuration Flags sheet. Has it been updated or replaced with a different parameter?*

Deleting Data does not Reclaim Unused Space
-----------------------------------------
With the exception of running a full table delete, deleting data does not free up disk space. To free up disk space, trigger the cleanup process.

For more information on running a full table delete, see (:ref:`TRUNCATE<truncate>`).

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


Examples
=============
The **Examples** section includes the following examples:

.. contents::
   :local:
   :depth: 1
   
Deleting Rows from a Table
------------------------------
The following example shows how to delete rows from a table.

1. Display the table:

   .. code-block:: psql

      farm=> SELECT * FROM cool_animals;
   
   The following table is displayed:

   .. code-block:: psql

      1,Dog                 ,7
      2,Possum              ,3
      3,Cat                 ,5
      4,Elephant            ,6500
      5,Rhinoceros          ,2100
      6,\N,\N
   
2. Delete rows from the table:

   .. code-block:: psql

      farm=> DELETE FROM cool_animals WHERE weight > 1000;
      executed
   
   The following table is displayed:
  
   .. code-block:: psql
    
      farm=> SELECT * FROM cool_animals;
      1,Dog                 ,7
      2,Possum              ,3
      3,Cat                 ,5
      6,\N,\N
   
Deleting Values Based on More Complex Predicates
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

* Avoid killing ``CLEANUP_EXTENTS`` operations after they've started.

* SQream DB is optimised for time-based data. When data is naturally ordered by a date or timestamp, deleting based on those columns will perform best. For more information, see our :ref:`time based data management guide<time_based_data_management>`.



.. soft update concept

.. delete cleanup and it's properties. automatic/manual, in transaction or background

.. automatic background gives fast delete, minimal transaction overhead,
.. small cost to queries until background reorganised

.. when does delete use the metadata effectively

.. more examples

