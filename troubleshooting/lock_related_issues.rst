.. _lock_related_issues:

***********************
Lock Related Issues
***********************

Sometimes, a rare situation can occur where a lock is never freed. 

The workflow for troubleshooting locks is:

#. Identify which statement has obtained locks.
#. Understand if the statement is itself stuck, or waiting for another statement.
#. Try to :ref:`ABORT<abort>` the offending statement, as in the following example:

.. code-block:: sql

	ABORT('ed59dc5e-2fdd-4ba5-b912-c152a4562134', '3')