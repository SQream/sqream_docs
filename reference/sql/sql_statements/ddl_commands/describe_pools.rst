.. _describe_pools:

**************
DESCRIBE POOLS
**************

The ``DESCRIBE [RESOURCE] POOLS`` lists all of your pools.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE POOLS`` command:

.. code-block:: sql

	DESCRIBE [RESOURCE] POOLS
	DESC [RESOURCE] POOLS
	 
Examples
========

.. code-block:: sql

	DESCRIBE RESOURCE POOLS;
   
Output
======

.. code-block:: none

	resource_pool_name   | number_of_workers   | parallelism_policy   | auto_suspend   | auto_suspend_inactivity_period   | auto_resume   | is_default   | pool_id
	---------------------+---------------------+----------------------+----------------+----------------------------------+---------------+--------------+-------------------------------------
	SQream               | 3                   | ParallelizeAll       | false          | 120                              | false         | true         | 27e2b27f-115e-4e03-8206-56f930257fc3

Permissions
===========

The ``DESCRIBE POOLS`` command requires ``CONNECT`` permission.