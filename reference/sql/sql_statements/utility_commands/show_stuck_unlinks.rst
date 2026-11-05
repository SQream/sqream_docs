:orphan:

.. _show_stuck_unlinks:

**********************
SHOW STUCK UNLINKS
**********************

``SHOW_STUCK_UNLINKS`` lists groups of deleted files that SQreamDB has tried to remove from disk and failed at least
once.

When you drop a table, or clean up after a ``DELETE``, the files that held the data are not removed at once. They are
queued, and a background process removes them from disk. If removing a group of files fails, for example because of a
storage error, the group is queued again and retried. Use ``SHOW_STUCK_UNLINKS`` when disk space is not freed after a
``DROP TABLE`` or a clean-up, to see whether any files are waiting on a failed removal and where they are.

See also :ref:`delete_guide`, :ref:`delete`.

Syntax
======

.. code-block:: postgres

   show_stuck_unlinks_statement ::=
       SELECT SHOW_STUCK_UNLINKS()
       ;

The function takes no arguments.

Returns
=======

A result set with one row for each group of files whose removal has failed at least once. Files that are queued for
removal but have not yet been tried are not listed. When no removal has failed, the result set is empty.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1

   * - Column name
     - Description
   * - ``path``
     - The folder that holds the files
   * - ``files``
     - The number of files in the group
   * - ``attempts``
     - The number of times removing the group has failed
   * - ``key``
     - The metadata key under which the group is queued

Permissions
===========

The role must have ``SUPERUSER`` permissions.

Notes
=====

* A large set of files from one folder is queued in several groups, so the same ``path`` can appear in more than one
  row.
* The ``attempts`` count is stored in the metadata, so it is kept across a restart.
* The result is capped at 100,000 rows. If more groups are stuck, the rest are not shown and a warning is written to
  the log.
* The function reads the queue across all databases in the cluster.

Examples
========

Listing files whose removal has failed
---------------------------------------

.. code-block:: postgres

   SELECT SHOW_STUCK_UNLINKS();
