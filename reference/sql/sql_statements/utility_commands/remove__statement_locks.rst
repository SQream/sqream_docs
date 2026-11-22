:orphan:

.. _remove_statement_locks:

**********************
REMOVE STATEMENT LOCKS
**********************

The ``REMOVE STATEMENT LOCKS`` utility function clears all locks held by the given statement ID. It refuses while that statement is active, unless ``ignore_stmt_exists`` is ``true``.

To remove specific locks, see :ref:`remove_lock`

Read more about locks in :ref:`concurrency_and_locks`.

Syntax
======

.. code-block:: postgres

	SELECT REMOVE_STATEMENT_LOCKS(<stmt_id> [, <ignore_stmt_exists> ])

Example
=======

.. code-block:: postgres

	SELECT REMOVE_STATEMENT_LOCKS (0);

Permissions
===========

This utility function requires the cluster-level ``SUPERUSER`` permission.
