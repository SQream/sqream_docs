:orphan:

.. _alter_table:

***********
ALTER TABLE
***********

You can use the ``ALTER TABLE`` command to:

* Add, drop, and rename table columns
* Rename tables
* Add and reorder table clustering keys
* Drop table clustering keys

Usage Note
==========

Making changes to a schema makes an :ref:`exclusive lock<concurrency_and_locks>` on tables. While these operations do not typically take much time, other statements may have to wait until the schema changes are completed.

Sub-Commands
============

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`ADD COLUMN<add_column>`
     - Adds a new column to a table.
   * - :ref:`DROP COLUMN<drop_column>`
     - Drops a column from a table.
   * - :ref:`RENAME COLUMN<rename_column>`
     - Renames a column.
   * - :ref:`RENAME TABLE<rename_table>`
     - Renames a table.
   * - :ref:`CLUSTER BY<cluster_by>`
     - Modifies (adds or reorders) the clustering keys in a table.
   * - :ref:`DROP CLUSTERING KEY<drop_clustering_key>`
     - Drops all clustering keys.
