.. _cost_management:
  
***********************
Managing Your Resources
***********************

Resource Pool enables you to optimize resource usage by managing and customizing your BLUE clusters and your BLUE environment runtime. This is highly effective for organizations that may wish to allocate budget resources according to different departments, use more than one concurrency mode for different purposes, and control their environment's runtime and downtime for better end-of-the-month costs. 

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

Press the three-dot menu that is located in the top right corner of the pool you wish to edit and select:

* **Rename**
* **Make Default**
* **Delete Pool**

Managing Cost
=============

When you suspend an environment, its resources are temporarily released, which allows billing to be paused for a set duration during which the environment is not expected to be used. If your BLUE environment is suspended, it means that your Workers are not operational, and statements cannot be executed. However, after you resume operation, the resource count will return to its pre-suspension value. It's important to note that your cluster remains accessible, and you can still perform administrative actions like resize and flow management.

Suspending Your BLUE Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To control the automatic suspension of your environment through the BLUE web interface, navigate to the **Settings** tab. 
Within the **Worker Management** section, you can manage worker activity.

To automatically suspend idle workers after a defined number of minutes, activate the **Automatically Suspend Workers** feature.

At the bottom of the page you will find the **Suspension By** feature. This feature provides three suspension method options that you can choose from. 
Use this feature to define your preferred suspension method.

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

Resuming Your BLUE Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To control the automatic resumption of your environment through the BLUE web interface, navigate to the **Settings** tab. 
Within the **Worker Management** section, you can manage worker activity to control Real Time Communication (RTC).

Activate the **Automatically Resume Workers** feature to enable the resumption of your environment by executing statements.

**Subscription Management**
To manage you BLUE subscription, follow this link.
