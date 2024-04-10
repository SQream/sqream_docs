.. _delete:

******
DELETE
******

The ``DELETE`` statement removes specific rows from a table. 

BLUE's deletion process follows these steps:

#. Marked rows remain on disk until a user-initiated clean-up process.

#. Clean-up process permanently deletes designated rows.

For more information about delete methodology, see the :ref:`delete_guide` guide.

For complete deletion:

* Use :ref:`TRUNCATE<truncate>` to delete all rows.

* Use :ref:`DROP COLUMN<drop_column>` for deleting columns.

Syntax
======

.. code-block:: postgres

	DELETE FROM [ "<schema_name>". ]"<table_name>" 
	     [ WHERE <condition> ]
   
	-- Clean-up syntax:
	SELECT
	  CLEANUP_CHUNKS ("<schema_name>"."<table_name>")

	SELECT 
	  CLEANUP_EXTENTS ( "<schema_name>"."<table_name>" )

For systems with delete parallelism capabilities, use the following syntax to enhance deletion performance and shorten runtime:

.. code-block:: postgres

	SELECT set_parallel_delete_threads(x);

.. note:: You may configure up to 10 threads.

Parameters
==========

The following table describes the parameters used for executing the ``DELETE`` statement:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema for the table.
   * - ``table_name``
     - The name of the table to delete rows from.
   * - ``condition``
     - An condition that returns Boolean values using columns, such as ``<column> = <value>``. Rows that match the expression will be deleted.

Usage Notes
===========

.. glossary::

	``ALTER TABLE``

		:ref:`alter_table` and other DDL operations are blocked during clean-up.

	``WHERE <condition>``
	
		A condition for deletion can't be from sub-queries or joins.

	**Long Deletions**

		BLUE may abort delete processes surpassing a time threshold, offering an override option.

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

.. _deleting_values_from_a_table:

Deleting Values from a Table
----------------------------

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
   
Deleting Values that Contain Multi-Table Conditions
---------------------------------------------------

The following shows an example of deleting values that contain multi-table conditions. The example is based on the following tables:

.. code-block:: none

	-- countries
	id | name      | country_id 
	---+-----------+-----------
	1  | Israel    |null
	2  | UK        |null
	3  | USA       |null
	4  | Sweden    |null

	-- bands
	id |name        |country_id 
	---+------------+-----------
	1  |The Beatles |2
	2  |The Ramones |3
	3  |ABBA        |4
	4  |Ace of Base |4

The statement below uses the ``EXISTS`` subquery to delete all bands based in Sweden:

.. code-block:: psql

	DELETE FROM 
	  bands
	WHERE EXISTS 
	 (
	  SELECT 
	   1 
	  FROM 
	   countries
	  WHERE 
	   countries.country_id=bands.id
	  AND 
	   country.name = 'Sweden'
	 );

.. _identifying_and_cleaning_up_tables:

.. _listing_tables_that_require_cleanup:

Listing Tables that Require Clean-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql
   
	SELECT 
	  t.table_name 
	FROM 
	  sqream_catalog.delete_predicates dp
	JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	GROUP BY 1;
	
	table_name
	------------
	cool_animals
   
.. _identifying_cleanup_predicates:

Identify Clean-Up Predicates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

	SELECT 
	  delete_predicate 
	FROM 
	  sqream_catalog.delete_predicates dp
	JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	WHERE t.table_name = 'cool_animals';
	
	delete_predicate
	----------------
	weight > 1000


.. _triggering_a_cleanup:

Triggering a Clean-Up
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: postgres

	-- Chunk reorganization (SWEEP)
	SELECT 
	  CLEANUP_CHUNKS('public','cool_animals');
   
	-- Delete leftover files (VACUUM)
	SELECT 
	  CLEANUP_EXTENTS('public','cool_animals');
      
	SELECT 
	  delete_predicate 
	FROM 
	  sqream_catalog.delete_predicates dp
	JOIN sqream_catalog.tables t ON dp.table_id = t.table_id
	WHERE 
	  t.table_name = 'cool_animals';
   
   
Permissions
=============

To execute the ``DELETE`` statement, the ``DELETE`` and ``SELECT`` permissions must be assigned to the role at the table level.