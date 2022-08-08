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
  
Performing Simple Updates
-----------------
The following is an example of performing a simple update:

.. code-block:: postgres

   UPDATE bands SET records_sold = records_sold + 1 WHERE name LIKE 'The %';
   
Triggering a Clean-Up
-----------------
The following section shows an example of triggering a clean-up:

.. code-block:: psql

   SELECT * FROM sqream_catalog.discarded_chunks;
   SELECT cleanup_discarded_chunks('public','t');   

The following is an example of the output generated from the above:

* **database_name** - _discarded_master
* **table_id** - 24
* **column_id** - 1
* **extent_ID** - 0

Locking and Concurrency
=============
Executing the ``UPDATE`` statement obtains an exclusive ``UPDATE`` lock on the target table.

Permissions
=============
Executing an ``UPDATE`` statement requires the following permissions:

* Both ``UPDATE`` and ``SELECT`` permissions on the target table.
* The ``SELECT`` permission for each additional table you reference in the statement (in ither the ``FROM`` clause or ``WHERE`` subquery section).