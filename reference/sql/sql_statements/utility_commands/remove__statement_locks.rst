:orphan:

.. _remove_statement_locks:

**********************
REMOVE STATEMENT LOCKS
**********************

The ``REMOVE STATEMENT LOCKS`` utility function clears all orphaned locks that block file cleanup and prevent operations on locked objects within the system.

To remove specific locks, see :ref:`remove_lock`

Read more about locks in :ref:`concurrency_and_locks`.

Syntax
======

.. code-block:: postgres

	SELECT REMOVE_STATEMENT_LOCK(<stmt_id> [, <ignore_stmt_exists> ])

Example
=======

.. code-block:: postgres

	SELECT REMOVE_STATEMENT_LOCKS (0);

Permissions
===========

This utility function requires a ``SUPERUSER`` permission on the database level.
