.. _update:

**********************
UPDATE
**********************
The **UPDATE** statement page describes the following:

.. |icon-new_2022.1.1| image:: /_static/images/new_2022.1.1.png
   :align: middle
   :width: 110

.. contents::
   :local:
   :depth: 1

Overview
==========
The ``UPDATE`` command is used to modify the value of certain columns in existing rows without creating a table.

It can be used to do the following:

* Performing localized changes in existing data, such as correcting mistakes discovered after ingesting data.

   ::

* Setting columns based on the values of others.

.. warning:: Using the ``UPDATE`` command on column clustered using a cluster key can undo your clustering.

Syntax
==========
The following is the correct syntax for the ``UPDATE`` command:

.. code-block:: postgres
 
   UPDATE target_table_name [[AS] alias1]
   SET column_name = expression [,...]
   [FROM additional_table_name [[AS] alias2][,...]]
   [WHERE condition]
  
The following is the correct syntax for triggering a clean-up:

.. code-block:: postgres

   SELECT cleanup_chunks('schema_name','table_name');
   SELECT cleanup_extents('schema_name','table_name');
   SELECT cleanup_discarded_chunks(‘public’,’t’);
   
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
     - Specifies the column containing the data to be updated.
   * - ``FROM`` |icon-new_2022.1.1|
     - For making complex joins, specifies additional tables to be used in the WHERE condition. ``FROM`` is similar to the ``FROM`` clause in a ``DELETE`` statement.
   * - ``condition``
     - Specifies the condition for updating the data.
	 
.. note:: A single table can appear **both** as a ``DELETE`` target *and* as a ``FROM`` table. This can be useful for deleting data based on self-join conditions. A ``SET`` clause can contain columns from tables specified in a ``FROM`` clause. For example, using the join ``WHERE`` condition updates rows in the target tables with the values of one of the matching rows.
	 
.. note:: Similar to a ``DELETE`` statement, an ``UPDATE`` statement may leave some uncleaned data behind, which requires a clean-up operation.

Examples
===========
The **Examples** section includes the following examples:

.. contents::
   :local:
   :depth: 1

Updating an Entire Table
-----------------
The Examples section shows how to modify the value of certain columns in existing rows without creating a table. The examples are based on the following tables:

.. image:: /_static/images/delete_optimization.png

The following methods for updating an entire table generate the same output, and result with the ``bands`` record set to ``NULL``:

.. code-block:: postgres

   UPDATE bands SET records_sold = 0;
   
.. code-block:: postgres

   UPDATE bands SET records_sold = 0 WHERE true;
   
.. code-block:: postgres

   UPDATE bands SET records_sold = 0 USING countries;

.. code-block:: postgres

   UPDATE bands SET records_sold = 0 USING countries WHERE 1=1;
   
Performing Simple Updates
-----------------
The following is an example of performing a simple update:

.. code-block:: postgres

   UPDATE bands SET records_sold = records_sold + 1 WHERE name LIKE 'The %';
   
Updating Tables that Contain Multi-Table Conditions
-----------------
The following shows an example of updating tables that contain multi-table conditions:

.. code-block:: postgres

   UPDATE bands
   SET records_sold = records_sold + 1
   WHERE EXISTS (
     SELECT 1 FROM countries
     WHERE countries.id=bands.country_id
     AND country.name = 'Sweden'
   );
   
Updating Tables that Contain Multi-Table Conditions using the FROM Clause
-----------------
The following shows an example of updating tables that contain multi-table conditions using the ``FROM`` clause:

.. code-block:: postgres

   UPDATE bands
   SET records_sold = records_sold +
     CASE
       WHEN c.name = 'Israel' THEN 2
       ELSE 1
     END
   FROM countries c

You can also write the statement above using the FROM clause:

.. code-block:: psql

   UPDATE bands
   SET records_sold = records_sold + 1
   FROM countries
   WHERE countries.id=bands.country_id AND country.name = 'Sweden';
   
Updating Tables that Contain Multi-Table Expressions
-----------------
The following shows an example of updating tables that contain multi-table expressions:

.. code-block:: postgres

   UPDATE bands
   SET records_sold = records_sold +
     CASE
       WHEN c.name = 'Israel' THEN 2
       ELSE 1
     END
   FROM countries c
   
Identifying and Cleaning Up Tables
---------------------------------------
The following section shows examples of each phase required for cleaning up tables:

* :ref:`Listing tables that require clean-up<listing_tables_that_require_cleanup>`
* :ref:`Identifying clean-up predicates<identifying_cleanup_predicates>`
* :ref:`Triggering a clean-up<triggering_a_cleanup>`

.. _listing_tables_that_require_cleanup:

Listing Tables that Require Clean-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following shows an example of listing tables that require clean-up:

.. code-block:: psql
   
   farm=> SELECT t.table_name FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      GROUP BY 1;
   cool_animals
   
   1 row

.. _identifying_cleanup_predicates:

Identifying Clean-Up Predicates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following shows an example of listing the clean-up predicates:

.. code-block:: psql

   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   weight > 1000
   
   1 row

.. _triggering_a_cleanup:

Triggering a Clean-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following section shows an example of triggering a clean-up:

.. code-block:: psql

   SELECT * FROM sqream_catalog.discarded_chunks;
   SELECT cleanup_discarded_chunks('public','t');   

The following is an example of the output generated from the above:

* **database_name** - _discarded_master
* **table_id** - 24
* **column_id** - 1
* **extent_ID** - 0

Security and Access Control
=============
Executing an ``UPDATE`` statement requires the following:

* Both ``UPDATE`` and ``SELECT`` permissions on the target table.

   ::
   
* The ``SELECT`` permission for each additional table referenced in the the statement (either in the ``FROM`` clause or in a ``WHERE`` subquery expression).

For more information, navigate to the **Access Control** page and see `Permissions <https://docs.sqream.com/en/v2022.1.1/operational_guides/access_control_permissions.html>`_.

file:///C:/Users/Yaniv/sqream_docs/_build/html/operational_guides/access_control_permissions.html

Locking and Concurrency
=============
Executing the ``UPDATE`` statement obtains an exclusive ``UPDATE`` lock on the target table.

Permissions
=============
Executing an ``UPDATE`` statement requires the following permissions:

* Both ``UPDATE`` and ``SELECT`` permissions on the target table.
* The ``SELECT`` permission for each additional table you reference in the statement (in ither the ``FROM`` clause or ``WHERE`` subquery section).