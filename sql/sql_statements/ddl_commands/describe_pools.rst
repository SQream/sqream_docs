.. _describe_pools:

**************
DESCRIBE POOLS
**************

The ``DESCRIBE POOLS`` lists all of your pools.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

	DESC[RIBE] [RESOURCE] POOLS
	 
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``resource_pool_name``
     - ``TEXT``
     - Name of the resource pool	 
   * - ``number_of_workers``
     - ``INT``
     - Number of Workers dedicated to the resource pool	 
   * - ``parallelism_policy``
     - ``TEXT``
     - Performance and concurrency preferences of the resource pool	 
   * - ``auto_suspend``
     - ``BOOLEAN``
     - Policy for suspending the resource pool	 
   * - ``auto_suspend_inactivity_period``
     - ``INT``
     - Idle session suspension period for the resource pool	 
   * - ``auto_resume``
     - ``BOOLEAN``
     - Policy for automatically resuming resource pool Workers 	 
   * - ``is_default``
     - ``BOOLEAN``
     - Indicates whether the resource pool is the default one 
   * - ``pool_id``
     - ``TEXT``
     - ID of the resource pool	 
	 
Examples
========

.. code-block:: sql

	DESCRIBE RESOURCE POOLS;

	resource_pool_name   | number_of_workers   | parallelism_policy   | auto_suspend   | auto_suspend_inactivity_period   | auto_resume   | is_default   | pool_id
	---------------------+---------------------+----------------------+----------------+----------------------------------+---------------+--------------+------------------------------------
	SQream               |3                    |ParallelizeAll        |false           |120                               |false          |true          |27e2b27f-115e-4e03-8206-56f930257fc3
	bi                   |1                    |ParallelizeAll        |true            |15                                |true           |false         |1f2f2fe4-37d0-41ac-a48c-4af0706dd3b4

Permissions
===========

The ``DESCRIBE POOLS`` command requires ``CONNECT`` permission.