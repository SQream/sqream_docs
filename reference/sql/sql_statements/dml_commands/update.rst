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

Performing Simple Updates
-----------------
The following is an example of performing a simple update:

.. code-block:: postgres

   UPDATE bands SET records_sold = records_sold + 1 WHERE name LIKE 'The %';

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
Executing an ``UPDATE`` statement requires both ``UPDATE`` and ``SELECT`` permissions on the target table.

Locking and Concurrency
=============
Executing the ``UPDATE`` statement obtains an exclusive UPDATE lock on the target table.