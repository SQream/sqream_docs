.. _delete_guide:

***********************
Deleting Data
***********************

When working with a table in a database, deleting data typically involves removing rows, although it can also involve removing columns. The process for deleting data involves first deleting the desired content, followed by a cleanup operation that reclaims the space previously occupied by the deleted data. This process is further explained below.

The ``DELETE`` statement is used to remove rows that match a specified predicate, thereby preventing them from being included in subsequent queries. For example, the following statement deletes all rows in the ``cool_animals`` table where the weight of the animal is greater than 1000 weight units:

.. code-block:: psql

	DELETE FROM cool_animals WHERE weight > 1000;

By using the WHERE clause in the DELETE statement, you can specify a condition or predicate that determines which rows should be deleted from the table. In this example, the predicate "weight > 1000" specifies that only rows with an animal weight greater than 1000 should be deleted.

.. contents::
   :local:
   :depth: 1

The Deletion Process
==========

When you delete rows from a SQL database, the actual deletion process occurs in two steps:

* **Marking for Deletion**: When you issue a ``DELETE`` statement to remove one or more rows from a table, the database marks these rows for deletion. These rows are not actually removed from the database immediately, but are instead temporarily ignored when you run any query. 

   ::
   
* **Clean-up**: Once the rows have been marked for deletion, you need to trigger a clean-up operation to permanently remove them from the database. During the clean-up process, the database frees up the disk space previously occupied by the deleted rows. To remove all files associated with the deleted rows, you can use the utility function commands ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS``. These commands should be run sequentially to ensure that these files removed from disk.

If you want to delete all rows from a table, you can use the :ref:`TRUNCATE<truncate>` command, which deletes all rows in a table and frees up the associated disk space.


Usage Notes
=====================
   
General Notes
-------------

* The :ref:`alter_table` command and other DDL operations are locked on tables that require clean-up. If the estimated clean-up time exceeds the permitted threshold, an error message is displayed describing how to override the threshold limitation. For more information, see :ref:`concurrency_and_locks`.

   ::

* If the number of deleted records exceeds the threshold defined by the ``mixedColumnChunksThreshold`` parameter, the delete operation is aborted. This alerts users that the large number of deleted records may result in a large number of mixed chunks. To circumvent this alert, use the following syntax (replacing ``XXX`` with the desired number of records) before running the delete operation:

  .. code-block:: postgres

     set mixedColumnChunksThreshold=XXX;
   

Clean-Up Operations Are I/O Intensive
-------------------------------------
The clean-up process reduces table size by removing all unused space from column chunks. While this reduces query time, it is a time-costly operation occupying disk space for the new copy of the table until the operation is complete.

.. tip::  Because clean-up operations can create significant I/O load on your database, consider using them sparingly during ideal times.

If this is an issue with your environment, consider using ``CREATE TABLE AS`` to create a new table and then rename and drop the old table.

Examples
========

To follow the examples section, create the following table:

   .. code-block:: psql
   
	   CREATE OR REPLACE TABLE cool_animals (
		animal_id INT,
		animal_name TEXT,
		animal_weight FLOAT
	   );

Insert the following content:

   .. code-block:: psql
   
		INSERT INTO cool_animals (animal_id, animal_name, animal_weight)
		VALUES
		(1, 'Dog', 7),
		(2, 'Possum', 3),
		(3, 'Cat', 5),
		(4, 'Elephant', 6500),
		(5, 'Rhinoceros', 2100),
		(6, NULL, NULL);

View table content:

.. code-block:: psql
   
	farm=> SELECT * FROM cool_animals;
		
	Return:
		
	   animal_id   | animal_name      | animal_weight
	   ------------+------------------+--------------------
	   1           | Dog              | 7 
	   2           | Possum           | 3  
	   3           | Cat              | 5      
	   4           | Elephant         | 6500
	   5           | Rhinoceros       | 2100
	   6           | NULL             | NULL 

Now you may use the following examples for:

.. contents::
   :local:
   :depth: 1
   
Deleting Rows from a Table
--------------------------

1. Delete rows from the table:

.. code-block:: psql

    farm=> DELETE FROM cool_animals WHERE animal_weight > 1000;
	  
2. Display the table:

.. code-block:: psql

	farm=> SELECT * FROM cool_animals;
   
	Return

	animal_id   | animal_name      | animal_weight
	------------+------------------+--------------------
	1           | Dog              | 7 
	2           | Possum           | 3  
	3           | Cat              | 5      
	6           | NULL             | NULL 
   
   
Deleting Values Based on Complex Predicates
---------------------------------------------------
   
1. Delete rows from the table:

.. code-block:: psql

    farm=>  DELETE FROM cool_animals
	   WHERE animal_weight < 100 AND animal_name LIKE '%o%';
	  
2. Display the table:

.. code-block:: psql

	farm=> SELECT * FROM cool_animals;

	Return

	animal_id   | animal_name      | animal_weight
	------------+------------------+--------------------
	3           | Cat              | 5      
	4           | Elephant         | 6500
	6           | NULL             | NULL 
   
Identifying and Cleaning Up Tables
---------------------------------------
   
Listing Tables that Have Not Been Cleaned Up

.. code-block:: psql
   
   farm=> SELECT t.table_name FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      GROUP BY 1;
   cool_animals
   
   1 row

Identifying Predicates for Clean-Up

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

When running the clean-up operation, you need to specify two parameters: ``schema_name`` and ``table_name``. However, it's important to note that the second parameter is case-sensitive for both ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS``.

Running a ``CLEANUP_CHUNKS`` command (also known as ``SWEEP``) to reorganize the chunks:

   .. code-block:: psql

      farm=> SELECT CLEANUP_CHUNKS('<schema_name>','<table_name>');

Running a ``CLEANUP_EXTENTS`` command (also known as ``VACUUM``) to delete the leftover files:

   .. code-block:: psql
   
      farm=> SELECT CLEANUP_EXTENTS('<schema_name>','<table_name>');

	  
If you should want to run a clean-up operation without worrying about uppercase and lowercase letters, you can use the ``false`` flag to enable lowercase letters for both lowercase and uppercase table and schema names, such as in the following examples:

	.. code-block:: psql

	  farm=> SELECT CLEANUP_CHUNKS('<schema_name>','<table_name>', false);
			  
	.. code-block:: psql
		   
	  farm=> SELECT CLEANUP_EXTENTS('<schema_name>','<table_name>', false);
	  
   
To display the table:

   .. code-block:: psql
   
      farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
         JOIN sqream_catalog.tables t
         ON dp.table_id = t.table_id
         WHERE t.table_name = 'cool_animals';
		 
Best Practice
=============


* After running large ``DELETE`` operations, run ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS`` to improve performance and free up space. These commands remove empty chunks and extents, respectively, and can help prevent fragmentation of the table.

   ::

* If you need to delete large segments of data from very large tables, consider using a ``CREATE TABLE AS`` operation instead. This involves creating a new table with the desired data and then renaming and dropping the original table. This approach can be faster and more efficient than running a large ``DELETE`` operation, especially if you don't need to preserve any data in the original table.

   ::

* Avoid interrupting or killing ``CLEANUP_EXTENTS`` operations that are in progress. These operations can take a while to complete, especially if the table is very large or has a lot of fragmentation, but interrupting them can cause data inconsistencies or other issues.

   ::

* SQream is optimized for time-based data, which means that data that is naturally ordered according to date or timestamp fields will generally perform better. If you need to delete rows from such tables, consider using the time-based columns in your ``DELETE`` predicates to improve performance.
