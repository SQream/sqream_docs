.. _lock_related_issues:

***********************
Lock Related Issues
***********************

Sometimes, a rare situation can occur where a lock is never freed. 

The workflow for troubleshooting locks is:

#. Identify which statement has obtained locks.
#. Understand if the statement is itself stuck, or waiting for another statement.
#. Try to :ref:`stop<stop_statement>` the offending statement, as in the following example:

.. code-block:: sql

	SELECT STOP_STATEMENT(2484923);