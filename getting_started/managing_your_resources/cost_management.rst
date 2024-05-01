.. _cost_management:

***************
Cost Management
***************

Cost management involves optimizing expenses by efficiently adjusting resources, such as cluster size and worker numbers, based on varying workloads, and utilizing features like environment suspension to temporarily halt billing during periods of inactivity.

Monitoring Worker Usage
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /_static/images/worker_counter.jpg
   :align: right

The BLUE web interface offers continuous monitoring of the number of active Workers being utilized at any given time. Positioned in the upper ribbon across all pages, a Worker counter displays the current count of active Workers out of the total available within your cluster. 


If you frequently find that one or more Workers are idle, it may be beneficial to review the :ref:`performance_and_concurrency_preferences` guide and consider reallocating the Workers in your cluster.


.. _resizing_your_cluster:

Resizing Your Cluster
^^^^^^^^^^^^^^^^^^^^^

Resizing your cluster provides adaptable and cost-effective resource management by enabling the adjustment of worker numbers in response to changing workloads. This flexibility allows you to optimize costs by reducing the cluster size during periods of lower demand, while also enabling dynamic scaling to meet performance needs during peak times. 

Resize may take 10—30 minutes, during which executed queries continue to run. 

#. To resize your cluster, go to **Settings** > **Cluster Resize**.

#. You may choose between one of the following plans:

.. list-table:: Cluster Sizes
   :widths: auto
   :header-rows: 1

   * - Cluster Size
     - Worker Count
     - Capability
   * - Small
     - 1
     - Experiment with the BLUE interface 	 	
   * - Medium
     - 4
     - Gain parallelism capabilities such as concurrency and shorter processing duration	
   * - Large
     - 10
     - Take advantage of parallelism capabilities such as concurrency, shorter query times and the ability to adjust resource pool sizes to suit various business needs	
 	 

.. _suspending_and_resuming_pools:

Suspending and Resuming Pools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you suspend an environment, its resources are temporarily released, which allows billing to be paused for a set duration during which the environment is not expected to be used. If your BLUE environment is suspended, it means that your Workers are not operational, and statements cannot be executed. However, after you resume operation, the resource count will return to its pre-suspension value. It's important to note that your cluster remains accessible, and you can still perform administrative actions.

You have the flexibility to manually or automatically suspend and resume each of your pools based on your specific requirements. 

Automatically Suspending and Resuming Pools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Suspending**

Once the automatic suspension is activated, Workers will automatically be suspended after a specific idle session period that has been defined.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
3. Toggle **Automatically suspend workers** on.
4. Under **Idle suspension period**, define the number of minutes for an idle period after which the pool will be suspended.
5. To turn off automatic suspension, toggle **Automatically suspend workers** off.

**Resuming**

Once the automatic resumption is activated, Workers will automatically be resumed when a query is executed.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
3. Toggle **Automatically resume workers** on.
4. To turn off automatic resumption, toggle **Automatically resume workers** off.

Manually Suspending and Resuming Pools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Suspending**

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
3. Under **Suspension Policy**, select one of the following policies:

   * Brute force
   * Graceful shutdown
   * Graceful shutdown and pending requests

.. list-table:: Suspension Policies
   :widths: auto
   :header-rows: 1

   * - Suspension Policy
     - Description
   * - Brute force
     - Workers are immediately suspended and all running statements are aborted
   * - Graceful shutdown
     - Workers are suspended only after completion of all running statements
   * - Graceful shutdown and pending requests
     - Workers are suspended only after completion of all running and queued statements

4. select **Suspend Now**.

**Resuming**

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to set.
   
   The pool you selected is now highlighted.
4. Under **Suspension Policy**, select **Activate Now**.