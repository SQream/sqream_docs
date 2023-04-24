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
Deleting data typically refers to deleting rows, but can refer to deleting other table content as well. The general workflow for deleting data is to delete data followed by triggering a cleanup operation. The cleanup operation reclaims the space occupied by the deleted rows, discussed further below.

The **DELETE** statement deletes rows defined by a predicate that you have specified, preventing them from appearing in subsequent queries.

For example, the predicate below defines and deletes rows containing animals heavier than 1000 weight units:

.. code-block:: psql

   farm=> DELETE FROM cool_animals WHERE weight > 1000;

The major benefit of the DELETE statement is that it deletes transactions simply and quickly.

The Deletion Process
==========
Deleting rows occurs in the following two phases:

* **Phase 1 - Deletion** - All rows you mark for deletion are ignored when you run any query. These rows are not deleted until the clean-up phase. 

   ::
   
* **Phase 2 - Clean-up** - The rows you marked for deletion in Phase 1 are physically deleted. The clean-up phase is not automated, letting users or DBAs control when to activate it. The files you marked for deletion during Phase 1 are removed from disk, which you do by sequentially running the utility function commands ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS``.

.. TODO: isn't the delete cleanup able to complete a certain amount of work transactionally, so that you can do a massive cleanup in stages?

.. TODO: our current best practices is to use a cron job with sqream sql to run the delete cleanup. we should document how to do this, we have customers with very different delete schedules so we can give a few extreme examples and when/why you'd use them.

Usage Notes
=====================

.. contents::
   :local:
   :depth: 1
   
General Notes
----------------

* The :ref:`alter_table` command and other DDL operations are locked on tables that require clean-up. If the estimated clean-up time exceeds the permitted threshold, an error message is displayed describing how to override the threshold limitation. For more information, see :ref:`concurrency_and_locks`.

   ::

* If the number of deleted records exceeds the threshold defined by the ``mixedColumnChunksThreshold`` parameter, the delete operation is aborted. This alerts users that the large number of deleted records may result in a large number of mixed chunks. To circumvent this alert, use the following syntax (replacing ``XXX`` with the desired number of records) before running the delete operation:

  .. code-block:: postgres

     set mixedColumnChunksThreshold=XXX;
   
Deleting Data does not Free Space
-----------------------------------------
With the exception of running a full table delete, deleting data does not free unused disk space. To free unused disk space you must trigger the clean-up process.

For more information on running a full table delete, see :ref:`TRUNCATE<truncate>`.

  ::
  
For more information on freeing disk space, see :ref:`Triggering a Clean-Up<trigger_cleanup>`.

Clean-Up Operations Are I/O Intensive
-------------------------------
The clean-up process reduces table size by removing all unused space from column chunks. While this reduces query time, it is a time-costly operation occupying disk space for the new copy of the table until the operation is complete.

.. tip::  Because clean-up operations can create significant I/O load on your database, consider using them sparingly during ideal times.

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
   
	   animal_id   | animal_name      | animal_weight
	   ------------+------------------+--------------------
	   1           | Dog              | 7 
	   2           | Possum           | 3  
	   3           | Cat              | 5      
	   4           | Elephant         | 6500
	   5           | Rhinoceros       | 2100
	   6           | NULL             | NULL 


2. Delete rows from the table:

   .. code-block:: psql

      farm=> DELETE FROM cool_animals WHERE animal_weight > 1000;
	  
3. Display the table:

   .. code-block:: psql

      farm=> SELECT * FROM cool_animals;
   
   The following table is displayed:
  
   .. code-block:: psql    

	   animal_id   | animal_name      | animal_weight
	   ------------+------------------+--------------------
	   1           | Dog              | 7 
	   2           | Possum           | 3  
	   3           | Cat              | 5      
	   6           | NULL             | NULL 
   
Deleting Values Based on Complex Predicates
---------------------------------------------------
The following example shows how to delete values based on complex predicates.

1. Display the table:

   .. code-block:: psql

      farm=> SELECT * FROM cool_animals;
   
   The following table is displayed:

   .. code-block:: psql

	   animal_id   | animal_name      | animal_weight
	   ------------+------------------+--------------------
	   1           | Dog              | 7 
	   2           | Possum           | 3  
	   3           | Cat              | 5      
	   4           | Elephant         | 6500
	   5           | Rhinoceros       | 2100
	   6           | NULL             | NULL 
   
2. Delete rows from the table:

   .. code-block:: psql

      farm=>  DELETE FROM cool_animals
	     WHERE animal_weight < 100 AND animal_name LIKE '%o%';
	  
3. Display the table:

   .. code-block:: psql

      farm=> SELECT * FROM cool_animals;
   
   The following table is displayed:
  
   .. code-block:: psql    

	   animal_id   | animal_name      | animal_weight
	   ------------+------------------+--------------------
	   3           | Cat              | 5      
	   4           | Elephant         | 6500
	   6           | NULL             | NULL 
   
Identifying and Cleaning Up Tables
---------------------------------------

.. contents::
   :local:
   :depth: 1
   
Listing Tables that Have Not Been Cleaned Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql
   
   farm=> SELECT t.table_name FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      GROUP BY 1;
   cool_animals
   
   1 row

Identifying Predicates for Clean-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   weight > 1000
   
   1 row
   
.. _trigger_cleanup:

Triggering a Clean-Up
^^^^^^^^^^^^^^^^^^^^^^

1. Run the ``CLEANUP_CHUNKS`` command (also known as ``SWEEP``) to reorganize the chunks:

   .. code-block:: psql

      farm=> SELECT CLEANUP_CHUNKS('public','cool_animals');

2. Run the ``CLEANUP_EXTENTS`` command (also known as ``VACUUM``) to delete the leftover files:

   .. code-block:: psql
   
      farm=> SELECT CLEANUP_EXTENTS('public','cool_animals');
   
3. Display the table:

   .. code-block:: psql
   
      farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
         JOIN sqream_catalog.tables t
         ON dp.table_id = t.table_id
         WHERE t.table_name = 'cool_animals';
		 
Best Practices
==============


* After running large ``DELETE`` operations, run ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS`` to improve performance and free up space. These commands remove empty chunks and extents, respectively, and can help prevent fragmentation of the table.

   ::

* If you need to delete large segments of data from very large tables, consider using a ``CREATE TABLE AS`` operation instead. This involves creating a new table with the desired data and then renaming and dropping the original table. This approach can be faster and more efficient than running a large ``DELETE`` operation, especially if you don't need to preserve any data in the original table.

   ::

* Avoid interrupting or killing ``CLEANUP_EXTENTS`` operations that are in progress. These operations can take a while to complete, especially if the table is very large or has a lot of fragmentation, but interrupting them can cause data inconsistencies or other issues.

   ::

* SQream is optimized for time-based data, which means that data that is naturally ordered according to date or timestamp fields will generally perform better. If you need to delete rows from such tables, consider using the time-based columns in your ``DELETE`` predicates to improve performance.
