.. _update:

**********************
UPDATE
**********************

The **UPDATE** statement page  |icon-new_2022.1| describes the following:

.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   :width: 110

.. contents::
   :local:
   :depth: 1

Overview
==========
The ``UPDATE`` command is used to modify the value of certain columns in existing rows without creating a table.

It can be used to do the following:

* Perform localized changes in existing data, such as correcting mistakes discovered after ingesting data.

* Setting columns based on the values of others.

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
   
**Comment** - *The cleanup example above is different than the one used on the DELETED page. Is this correct?*

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
	 
.. note:: Similar to a DELETE statement, an UPDATE statement may leave some uncleaned data behind, which requires a cleanup operation.

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
   
Configuring Update Behavior
-----------------
The ``failOnNondeterministicUpdate`` flag is used to configure ``UPDATE`` behavior when updating tables containing multi-table expressions. This flag is needed when you use the ``FROM`` clause along with a set expression containing columns from additional tables. Doing this can cause a match to occur between a row from the target table with multiple rows from the additional tables.

**Note to self** - *Check if the Studio documentation must be updated for this flag.*

For instance, the example in the previous section sets the records sold to ``2`` when the country name is Israel. If you were to insert a new entry into this table with Israel spelled in Hebrew (using the same country ID), you would have two rows with identical country ID's. 

When this happens, both rows 5 and 6 in the ``bands`` table match both Israel entries. Because no algorithm exists for determining which entry to use, updating this table may either increase ``records_sold`` by 2 (for Israel in English) or 1 (for Israel in Hebrew).

You must set the ``failOnNondeterministicUpdate`` flag to ``FALSE`` to prevent an error from occuring.

**Comment** - *Does the system actually choose one, or does it generate an error?*

Note that a similar ambiguity can occur when the Hebrew spelling is used in the following example:

.. code-block:: postgres

   UPDATE bands
   SET record_count = record_count + 1
   FROM countries c
   WHERE c.name = 'Israel'
   
However, the ``WHERE`` clause above prevents a match with any entry other than the defined one. Because the target table row must match with the ``WHERE`` condition at least once to be included in the UPDATE statment, this scenario does not require configuring the ``failOnNondeterministicUpdate`` flag.

**Comment** - *Please review the paragraph above. I'm pretty sure I described this correctly.*

For more information, see `SQream Acceleration Studio <https://docs.sqream.com/en/latest/guides/operations/sqream_studio_5.4.2.html#configuring-your-instance-of-sqream>`_.

Identifying and Cleaning Up Tables
---------------------------------------
**Comment** - *I copied and pasted this entire section from "DELETE". Does anything have to adjusted here for "UPDATE"?*

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
^^^^^^^^^^^^^^^^^^^^^^
The following shows an example of triggering a clean-up:

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

Permissions
=============
Executing an ``UPDATE`` statement requires the following permissions:

* Both ``UPDATE`` and ``SELECT`` permissions on the target table.
* The ``SELECT`` permission for each additional table you reference in the statement (in ither the ``FROM`` clause or ``WHERE`` subquery section).

Locking and Concurrency
=============
Executing the ``UPDATE`` statement obtains an exclusive UPDATE lock on the target table, but does not lock the destination tables.