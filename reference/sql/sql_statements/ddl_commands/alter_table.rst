.. _alter_table:

**********************
ALTER TABLE
**********************

``ALTER TABLE`` can be used to make schema changes to a table. It works in conjunction with several subcommands.

Locks
=======

Schema changes take an exclusive lock on tables. While these operations are usually short, other statements may have to wait until the schema changes are completed.

Subcommands
==============

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Usage
   * - :ref:`ADD COLUMN<add_column>`
     - Add a new column to a table
   * - :ref:`DROP COLUMN<drop_column>`
     - Drop a column from a table
   * - :ref:`RENAME COLUMN<rename_column>`
     - Rename a column
   * - :ref:`RENAME TABLE<rename_table>`
     - Rename a table
   * - :ref:`CLUSTER BY<cluster_by>`
     - Modify (add or reorder) the clustering keys in a table
   * - :ref:`DROP CLUSTERING KEY<drop_clustering_key>`
     - Drop all clustering keys