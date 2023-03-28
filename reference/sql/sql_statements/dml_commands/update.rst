.. _update:

**********************
UPDATE
**********************
The **UPDATE** statement page describes the following:

.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   :width: 110

.. contents::
   :local:
   :depth: 1

Overview
==========
The ``UPDATE`` statement is used to modify the value of certain columns in existing rows without creating a table.

It can be used to do the following:

* Performing localized changes in existing data, such as correcting mistakes discovered after ingesting data.

   ::

* Setting columns based on the values of others.

.. warning:: Using the ``UPDATE`` command on column clustered using a cluster key can undo your clustering.

The ``UPDATE`` statement cannot be used to reference other tables in the ``WHERE`` or ``SET`` clauses.

Syntax
==========
The following is the correct syntax for the ``UPDATE`` command:

.. code-block:: postgres
 
	UPDATE target_table_name [[AS] alias1]
	SET column_name = expression [,...]
	[FROM additional_table_name [[AS] alias2][,...]]
	[WHERE condition]
  

   
Parameters
============
The following table describes the ``UPDATE`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``target_table_name``
     - Specifies the table containing the data to be updated.
   * - ``column_name``
     - Specifies the column containing the data to be updated.
   * - ``additional_table_name``
     - Additional tables used in the WHERE condition for performing complex joins.
   * - ``condition``
     - Specifies the condition for updating the data.

Examples
===========

The examples section shows how to modify the value of certain columns in existing rows without creating a table.

To be able to follow the examples, create these two tables:

**countries**

+----+--------+--------------+	
| id | name   | records_sold |
+====+========+==============+
| 1  | Israel | null         |
+----+--------+--------------+
| 2  | UK     | null         |
+----+--------+--------------+
| 3  | USA    | null         |
+----+--------+--------------+
| 4  | Sweden | null         |
+----+--------+--------------+

**bands**

+----+-------------+------------+
| id | name        | country_id |
+====+=============+============+
| 1  | The Beatles | 2          |
+----+-------------+------------+
| 2  | The Ramones | 3          |
+----+-------------+------------+
| 3  | ABBA        | 4          |
+----+-------------+------------+
| 4  | Ace of Base | 4          |
+----+-------------+------------+

.. code-block:: postgres

	create or replace table countries ( id int, name text, records_sold int); 
	insert into countries values (1, 'Israel', null); 
	insert into countries values (2, 'UK', null); 
	insert into countries values (3, 'USA', null); 
	insert into countries values (4, 'Sweden', null); 
   
	create or replace table bands ( id int, name text, country_id int); 
	insert into bands values (1, 'The Beatles', 2); 
	insert into bands values (2, 'The Ramones', 3); 
	insert into bands values (3, 'ABBA', 4); 
	insert into bands values (4, 'Ace of Base', 4); 
	
	

.. contents::
   :local:
   :depth: 1

Updating an Entire Table
-----------------

Two different ``UPDATE`` methods for updating an entire table.

.. code-block:: postgres

   UPDATE countries SET records_sold = 0;
   
.. code-block:: postgres

   UPDATE countries SET records_sold = 0 WHERE true;


Performing Simple Updates
-----------------
The following is an example of performing a simple update:

.. code-block:: postgres

    UPDATE countries SET records_sold = records_sold + 1 WHERE name = 'Israel';

Updating Tables that Contain Multi-Table Conditions
-----------------
The following shows an example of updating tables that contain multi-table conditions:

.. code-block:: postgres

	UPDATE countries
	SET records_sold = records_sold + 1
	WHERE EXISTS (
	  SELECT 1 FROM bands
	  WHERE bands.country_id = countries.id
	  AND bands.name = 'ABBA'
	);


Updating Tables that Contain Multi-Table Expressions
----------------------------------------------------
The following shows an example of updating tables that contain multi-table expressions:

.. code-block:: postgres

	UPDATE countries
	SET records_sold = records_sold +
	  CASE
		WHEN name = 'Israel' THEN 2
		ELSE 1
	  END
	FROM countries c  
	;
 
Triggering a Cleanup
---------------------

When an ``UPDATE`` statement is executed, it creates a new table that contains the updated data, while the original table remains intact. As a result, residual data may be left behind, and a cleanup operation is necessary to ensure the database remains in a consistent state.

 
The following is the syntax for triggering a cleanup:

.. code-block:: postgres

   SELECT cleanup_chunks('schema_name','table_name');
   SELECT cleanup_extents('schema_name','table_name'); 

   
Permissions
===========
Executing an ``UPDATE`` statement requires the following permissions:

* Both ``UPDATE`` and ``SELECT`` permissions on the target table.
* The ``SELECT`` permission for each additional table you reference in the statement (in ither the ``FROM`` clause or ``WHERE`` subquery section).

Locking and Concurrency
=======================
Executing the ``UPDATE`` statement obtains an exclusive UPDATE lock on the target table, but does not lock the destination tables.