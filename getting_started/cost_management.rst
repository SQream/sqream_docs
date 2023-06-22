.. _cost_management:
  
***********************
Managing Your Resources
***********************

Resource Pool enables you to optimize resource usage by managing and customizing your BLUE clusters and your BLUE environment runtime. This is highly effective for organizations that may wish to allocate budget resources according to different departments, use multiple concurrency modes for various purposes, and control their environment's runtime and downtime for better end-of-the-month costs. 

Managing Clusters
=================

You can define the number of resource pools you wish to create and the number of workers you wish to designate for each pool to optimize the allocation and usage of your resources. 

Creating a New Pool
^^^^^^^^^^^^^^^^^^^

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
   All of your workers are assigned to the default **SQream** pool.
2. To create a new pool, press **Create New Pool**, provide a pool name and assign workers.
   The number of workers assigned to the new pool will automatically be reduced from your default pool.

Editing Existing Pools
^^^^^^^^^^^^^^^^^^^^^^

Press the three-dot menu that is located in the top right corner of the pool you wish to edit and select one of the following:

* **Rename**
* **Make Default**
* **Delete Pool**

Setting Worker Parallelism Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can manage worker activity to control Real-Time Communication (RTC) and concurrency.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select the pool of which you wish to set automatic resumption and make sure it is now highlighted.
3. Under **Parallelism Policy**, select one of the policies:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Policy
     - Description
   * - No parallelism
     - 
   * - Partial parallelism (50% of workers)
     - 
   * - Maximum parallelism
     - 

Managing Cost
=============

When you suspend an environment, its resources are temporarily released, which allows billing to be paused for a set duration during which the environment is not expected to be used. If your BLUE environment is suspended, it means that your Workers are not operational, and statements cannot be executed. However, after you resume operation, the resource count will return to its pre-suspension value. It's important to note that your cluster remains accessible, and you can still perform administrative actions like resize and flow management.

You can set each of your pools with a unique suspension policy.

Setting Automatic Worker Suspension and Resumption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To enable the automatic suspension of idle workers, activate the **Automatically Suspend Workers** feature.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select the pool of which you wish to set automatic suspension and make sure it is now highlighted.
3. Toggle **Automatically suspend workers** on/off.
4. If toggled on, make sure to define the **Idle suspension period**.
5. If toggled on, go to **Suspension policy** and select one of the suspension methods:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Suspension Method
     - Description
   * - Brute force
     - All workers are immediately suspended and all running statements are aborted
   * - Graceful shutdown
     - Suspension of all workers will occur only after completion of all running statements
   * - Graceful shutdown and pending requests
     - Suspension of workers will occur only after completion of all running statements and execution of all queued statements

To enable the automatic resumption of your environment, activate the **Automatically Resume Workers** feature.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select the pool of which you wish to set automatic resumption and make sure it is now highlighted.
3. Toggle **Automatically resume workers** on/off.

.. topic:: Subscription

  To manage your BLUE subscription, follow this link.
