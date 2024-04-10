.. _update:

******
UPDATE
******

The ``UPDATE`` statement modifies existing row values in a table, allowing localized data corrections and setting column values based on others. Caution is advised when updating clustered columns, as it may disrupt clustering. Additionally, it doesn't support referencing other tables in the ``WHERE`` or ``SET`` clauses.

Syntax
======

.. code-block:: postgres
 
	UPDATE "<table_name>" [ [ AS ] alias1 ]
	SET <column_name> = <expression> [,... ]
	[ FROM "<additional_table_name>" [ [ AS ] alias2 ] [,... ] ]
	[ WHERE <condition> ]
  
Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``table_name``
     - Specifies the table containing the data to be updated.
   * - ``column_name``
     - Specifies the column containing the data to be updated.
   * - ``additional_table_name``
     - Additional tables used in the WHERE condition for performing complex joins.
   * - ``condition``
     - Specifies the condition for updating the data.

Usage Notes
===========

.. glossary::

	**Triggering a Cleanup**

		After executing an ``UPDATE`` statement, a new table containing the updated data is generated, leaving the original table unchanged. This process may result in residual data, requiring a cleanup operation to maintain database consistency.

		.. code-block:: postgres

			SELECT
			  cleanup_chunks("schema_name", "table_name");

			SELECT 
			  cleanup_extents("schema_name","table_name"); 

	**Locking and Concurrency**

		Executing the ``UPDATE`` statement obtains an exclusive ``UPDATE`` lock on the target table, but does not lock the destination tables.

Examples
========

The examples section follows these two tables: 

.. code-block:: postgres

	-- countries table:
	CREATE OR REPLACE TABLE
	  countries (id INT, name TEXT, records_sold INT);

	INSERT INTO
	  countries
	VALUES
	  (1, 'Israel', null),
	  (2, 'UK', null),
	  (3, 'USA', null),
	  (4, 'Sweden', null); 
	   
.. code-block:: postgres
	   
	  -- bands table:
	CREATE OR REPLACE TABLE
	  bands (id INT, name TEXT, country_id INT); 

	INSERT INTO
	  bands
	VALUES
	  (1, 'The Beatles', 2),
	  (2, 'The Ramones', 3),
	  (3, 'ABBA', 4),
	  (4, 'Ace of Base', 4); 

Updating an Entire Table
------------------------

There are two different methods for updating an entire table.

.. code-block:: postgres

	UPDATE
	  countries
	SET
	  records_sold = 0;
   
.. code-block:: postgres

	UPDATE
	  countries
	SET
	  records_sold = 0
	WHERE
	  true;

Performing Simple Updates
-------------------------

.. code-block:: postgres

	UPDATE
	  countries
	SET
	  records_sold = records_sold + 1
	WHERE
	  name = 'Israel';

Updating Tables that Contain Multi-Table Conditions
---------------------------------------------------

.. code-block:: postgres

	UPDATE
	  countries
	SET
	  records_sold = records_sold + 1
	WHERE
	  EXISTS (
	    SELECT
	      1
	    FROM
	      bands
	    WHERE
	      bands.country_id = countries.id
	      AND bands.name = 'ABBA'
	  );


Updating Tables that Contain Multi-Table Expressions
----------------------------------------------------

.. code-block:: postgres

	UPDATE
	  countries
	SET
	  records_sold = records_sold + CASE
	    WHEN name = 'Israel' THEN 2
	    ELSE 1
	  END
	FROM
	  countries c;


Permissions
===========

Executing an ``UPDATE`` statement requires the following permissions:

* Both ``UPDATE`` and ``SELECT`` permissions on the target table.
* The ``SELECT`` permission for each additional table you reference in the statement (in either the ``FROM`` clause or ``WHERE`` subquery section).



