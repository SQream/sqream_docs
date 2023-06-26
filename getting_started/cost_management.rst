.. _cost_management:
  
***********************
Managing Your Resources
***********************

You can optimize the utilization of your resources using the **Resource Pool** panel which enables you to manage your end-of-the-month cost by lowering runtime when your BLUE environment is idle and to enhance cluster utilization by allocating Real-Time Communication (RTC) Workers according to specific needs of different departments in your organization, whether it be high concurrency or high performance.

All **Resource Pool** operations require a ``ClusterAdmin`` permission.

Managing Cluster
================

By default, your cluster has a single default pool that is assigned all the Real-Time Communication (RTC) workers in the cluster.

Creating a New Pool
^^^^^^^^^^^^^^^^^^^

When creating a pool, it is crucial to remember that Worker assignment is only possible during the initial setup. It is recommended to carefully consider the number of Workers you intend to assign to new pools before their creation.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. To create a new pool, press **Create New Pool**, provide a pool name, and assign Workers.

   The number of Workers assigned to the new pool will automatically be reduced from your default pool.

Editing Existing Pools
^^^^^^^^^^^^^^^^^^^^^^

To edit an existing pool, it must be in either an idle or suspended state.

1. Press the three-dot menu that is located in the top right corner of the pool you wish to edit and select one of the following:

   * Rename
   * Make Default
   * Delete Pool

Setting Worker Parallelism Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each pool in the system is associated with a parallelism policy that determines whether it prioritizes high performance or high concurrency. By configuring different pools with distinct parallelism modes, you can optimize resource usage based on the specific needs of various organizational departments or work groups.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
3. Under **Parallelism Policy**, select one of the policies:

   * No parallelism
   * Partial parallelism (50% of workers)
   * Maximum parallelism

.. list-table:: Parallelism Policies
   :widths: auto
   :header-rows: 1

   * - Policy
     - Description
   * - No parallelism
     - A single query can be executed using only one Worker. It means that the query will run sequentially on a single worker, which may result in slower execution time compared to parallel execution.
   * - Partial parallelism (50% of workers)
     - Utilizes 50% of the available Workers to execute a query. The query is divided among the selected Workers, enabling faster execution compared to the no parallelism policy, but not utilizing the full capacity of the worker pool.
   * - Maximum parallelism
     - Enables the execution of a single query using multiple Workers. This allows the query to be divided among all available Workers, significantly reducing the execution time. It fully utilizes the Worker pool and provides the highest level of performance.

Managing Cost
=============

When you suspend an environment, its resources are temporarily released, which allows billing to be paused for a set duration during which the environment is not expected to be used. If your BLUE environment is suspended, it means that your Workers are not operational, and statements cannot be executed. However, after you resume operation, the resource count will return to its pre-suspension value. It's important to note that your cluster remains accessible, and you can still perform administrative actions like resize and flow management.

You have the flexibility to manually or automatically suspend and resume each of your pools based on your specific requirements. 

Setting Automatic Pool Suspension and Resumption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To enable the automatic suspension of idle workers, activate the **Automatically Suspend Workers** feature.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
3. Under **Suspension Policy**, select one of the policies:
4. Select one of the suspension policies:

   * Brute force
   * Graceful shutdown
   * Graceful shutdown and pending requests

.. list-table:: Suspension Policies
   :widths: auto
   :header-rows: 1

   * - Suspension Policy
     - Description
   * - Brute force
     - All workers are immediately suspended and all running statements are aborted
   * - Graceful shutdown
     - Suspension of all workers will occur only after completion of all running statements
   * - Graceful shutdown and pending requests
     - Suspension of workers will occur only after completion of all running statements and execution of all queued statements

Manually Suspending and Resuming Pools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
3. To suspend pool ,under **Suspension Policy**, select **Suspend Now**
4. To resume pool ,under **Suspension Policy**, select **Activate Now**

.. topic:: Subscription

  To manage your BLUE subscription, follow this link.
