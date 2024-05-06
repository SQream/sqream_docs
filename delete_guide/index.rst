.. _delete_guide:

*************
Deleting Data
*************

When managing a database table, deleting data typically involves removing rows, though it can also entail removing columns. The deletion process begins with eliminating the desired content, followed by a cleanup operation to reclaim the space previously occupied by the deleted data. Below is a breakdown of this process.

The ``DELETE`` statement is used to remove rows that meet a specified condition, thereby excluding them from subsequent queries. 

The Deletion Process
====================

When you delete rows from a SQL database, the actual deletion process occurs in two steps:

.. glossary::

	**Marking for Deletion** 
		Upon issuing a ``DELETE`` statement to remove one or more rows from a table, the database marks these rows for deletion. They are not immediately removed from the database but are instead temporarily disregarded when executing any query.

	**Clean-up** 
		Once the rows have been marked for deletion, a clean-up operation needs to be triggered to permanently remove them from the database. During this process, the database frees up the disk space previously occupied by the deleted rows. To remove all files associated with the deleted rows, you can use utility function commands such as ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS``. These commands should be executed sequentially to ensure the removal of these files from disk.

To delete all rows from a table, use the :ref:`TRUNCATE<truncate>` command, which deletes all rows in a table and frees up the associated disk space.

Usage Notes
===========

``ALTER TABLE``
    The :ref:`alter_table` command and other DDL operations are locked on tables that require clean-up. If the estimated clean-up time exceeds the permitted threshold, an error message is displayed describing how to override the threshold limitation. For more information, see :ref:`concurrency_and_locks`.

**Deletion Size Threshold**
    If the number of deleted records exceeds the threshold defined by the ``mixedColumnChunksThreshold`` parameter, the delete operation is aborted. This alerts users that the large number of deleted records may result in a large number of mixed chunks. To circumvent this alert, use the following syntax before running the delete operation:

    .. code-block:: postgres

		SET mixedColumnChunksThreshold = <record_number>;
   

Optimizing Clean-Up Operations for Database Performance
=======================================================

Clean-up processes are crucial for reducing table size by eliminating unused space from column chunks. Although this enhances query efficiency, it's important to note that this operation can be time-intensive and occupies disk space for the new table copy until completion.

Due to the significant I/O load clean-up operations can impose on your database, it's advisable to use them sparingly, preferably during optimal times.

If this presents challenges in your environment, consider using ``CREATE TABLE AS`` to generate a new table, followed by renaming and dropping the old table.

Examples
========

Consider the following table:

.. code-block:: none

	id |name       | weight 
	---+-----------+-------
	1  |Dog        |7
	2  |Possum     |3
	3  |Cat        |5
	4  |Elephant   |6500
	5  |Rhinoceros |2100
	6  |\N         |\N
   
Deleting Rows from a Table
--------------------------

.. code-block:: psql

	DELETE FROM 
	  cool_animals 
	WHERE 
	  weight > 1000;

.. code-block:: psql

	SELECT 
	  * 
	FROM 
	  cool_animals;
	  
	id |name       | weight 
	---+-----------+-------
	1  |Dog        |7
	2  |Possum     |3
	3  |Cat        |5
	6  |\N         |\N
   
   
Deleting Values Based on Complex Predicates
-------------------------------------------

.. code-block:: psql

	DELETE FROM
	  cool_animals
	WHERE
	  animal_weight < 100
	  AND animal_name LIKE '%o%';

.. code-block:: psql

	SELECT
	  *
	FROM
	  cool_animals;

	id |name       | weight 
	---+-----------+-------
	3  |Cat        |5
	4  |Elephant   |6500
	6  |\N         |\N
   
Identifying and Cleaning Up Tables
---------------------------------------
   
Listing tables that have not been cleaned up:

.. code-block:: psql
   
	SELECT
	  t.table_name
	FROM
	  sqream_catalog.delete_predicates dp
	  JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	GROUP BY
	  1;
	
	table_name
	------------
	cool_animals;
   
Identifying predicates for Clean-Up:

.. code-block:: psql

	SELECT
	  delete_predicate
	FROM
	  sqream_catalog.delete_predicates dp
	  JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	WHERE
	  t.table_name = 'cool_animals';
	  
	delete_predicate
	----------------
	weight > 1000
   
Triggering a Clean-Up
^^^^^^^^^^^^^^^^^^^^^

When running the clean-up operation, you need to specify two parameters: ``schema_name`` and ``table_name``.

.. code-block:: postgres

	-- Chunk reorganization (SWEEP)
	SELECT 
	  CLEANUP_CHUNKS("public","cool_animals");
   
	-- Delete leftover files (VACUUM)
	SELECT 
	  CLEANUP_EXTENTS("public","cool_animals");
      
	SELECT 
	  delete_predicate 
	FROM 
	  sqream_catalog.delete_predicates dp
	JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	WHERE 
	  t.table_name = 'cool_animals';
  
If you should want to run a clean-up operation without worrying about uppercase and lowercase letters, you can use the ``false`` flag to enable lowercase letters for both lowercase and uppercase table and schema names, such as in the following examples:

.. code-block:: psql

	SELECT 
	  CLEANUP_CHUNKS("public","cool_animals", true);
   
	SELECT 
	  CLEANUP_EXTENTS("public","cool_animals", true);
	   
To display the table:

.. code-block:: psql
   
	SELECT
	  delete_predicate
	FROM
	  sqream_catalog.delete_predicates dp
	  JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	WHERE
	  t.table_name = "cool_animals";
		 
Best Practice
=============

.. glossary::

	**Avoid Interrupting or Killing CLEANUP_EXTENTS Operations** 
		It's best to refrain from interrupting or terminating ``CLEANUP_EXTENTS`` operations that are in progress. These operations may take some time to complete, especially for large tables or those with significant fragmentation. However, interrupting them can lead to data inconsistencies or other issues.

	**Optimize Time-Based Data with BLUE** 
		BLUE is designed to optimize time-based data, meaning that data naturally ordered by date or timestamp fields will generally perform better. When deleting rows from such tables, consider leveraging the time-based columns in your DELETE predicates to enhance performance.