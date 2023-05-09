.. _lock_related_issues:

***********************
Lock Related Issues
***********************
Sometimes, a rare situation can occur where a lock is never freed. 

The workflow for troubleshooting locks is:

#. Identify which statement has obtained locks
#. Understand if the statement is itself stuck, or waiting for another statement
#. Try to abort the offending statement
#. Force the stale locks to be removed

For example, we will assume that the statement from the previous example is stuck (statement #\ ``287``). We can attempt to abort it using :ref:`stop_statement`:

.. code-block:: psql

   t=> SELECT STOP_STATEMENT(287);
   executed

If the locks still appear in the :ref:`show_locks` utility, we can force remove the stale locks:

.. code-block:: psql

   t=> SELECT RELEASE_DEFUNCT_LOCKS();
   executed

.. warning:: This operation can cause some statements to fail on the specific worker on which they are queued. This is intended as a "last resort" to solve stale locks.