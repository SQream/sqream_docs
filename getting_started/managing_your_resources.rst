.. _managing_your_resources:
  
*******************
Resource Management
*******************

You can optimize the utilization of your resources using the **Resource Pool** panel which enables you to manage your end-of-the-month cost by lowering runtime when your BLUE environment is idle and to enhance cluster utilization by allocating Workers according to the specific needs of different departments in your organization, whether it be high concurrency or performance.

All **Resource Pool** operations require a ``ClusterAdmin`` permission.

Cluster Management
------------------

Managing a BLUE cluster involves two core aspects: pools and Workers. Pools serve as organized resource compartments, enabling strategic allocation of Workers based on specific compute power needs. Workers, operating within these pools, execute tasks and process data. By adjusting the number of Workers in each pool, users can optimize resource usage, ensuring efficient compute power and task execution while effectively utilizing the cluster's capabilities.

Pools
^^^^^

Pools offer the ability to effectively manage available resources for various purposes within your BLUE cluster. By default, your cluster includes a single default pool that encompasses all the Workers in the cluster. You have the flexibility to create additional pools to further divide the resources based on your specific business needs, priorities, and concurrency preferences. This allocation of resources allows you to have better control over your business priorities and optimize parallelism, resulting in improved resource utilization and overall system efficiency.

Creating a New Pool
~~~~~~~~~~~~~~~~~~~

When creating new pools, Workers must be assigned to them. The number of Workers allocated to the new pool will be automatically deducted from your default pool.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. To create a new pool, select the **Create New Pool** button, provide a pool name, and assign Workers.
   Pool names are rendered as identifiers, which means they may not include whitespace characters. 
   
   See full list of :ref:`identifier rules<keywords_and_identifiers>`.

Readjusting Existing Pools
~~~~~~~~~~~~~~~~~~~~~~~~~~

To readjust an existing pool, the pool must be in either an idle or suspended state.

1. In the sidebar, go to **Settings** and select the **Resource Pool** tab.
2. Select a pool you wish to readjust.
   
   The pool you selected is now highlighted.

3. To add or reduce Workers, in the pool's settings panel, select the number to the right of the **Worker Count**, and use the ``+`` or ``-`` key.
   
   When adding workers to a pool, ensure that there are enough available workers in your default pool to be reduced from. 
   
4. To make this pool your default pool, go to the three-dot menu located in the top right corner of the pool panel, and choose **Make Default**.
5. To rename pool, you may either:

   * Go to the three-dot menu located in the top right corner of the pool panel and choose **Rename**
   * Select the pool name in the pool's settings panel and rename pool
6. To delete pool, go to the three-dot menu located in the top right corner of the pool panel and choose **Delete**.

Managing Pools within a Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can connect to a specific pool using third-party tools. Additionally, you have the ability to list all of your pools and shift between them within your current session as needed.

Syntax
""""""

The ``DESCRIBE [RESOURCE] POOLS`` is a CPU based SQL command that lists all of your pools. 

This command requires ``CONNECT`` permission.

.. code-block:: sql

	DESCRIBE [RESOURCE] POOLS
	DESC [RESOURCE] POOLS

The ``USE [RESOURCE] POOL`` command lets you shift between pools within a session. 

This command requires ``CONNECT`` permission.

.. code-block:: sql
	
	USE [RESOURCE] POOL <pool_name>
	
.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``pool_name``
     - Specifies the name of a specific pool you wish to shift to within the current session	
	
.. topic:: Using the Editor

	You may also shift between pools within a session using the **Editor**. 
	
	In the left-hand side of the ribbon, select a pool from the **Pool** drop-down menu. 
	
Examples
""""""""
	
Listing all existing pools:

.. code-block:: sql

	DESCRIBE RESOURCE POOLS;

Shifting between pools:

.. code-block:: sql

	USE POOL bi_pool;

Using Third-Party Tools
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``pool``
     - Specifies the name of a specific pool to connect to
	 
Examples
~~~~~~~~

Connecting to a specified pool:

.. code-block:: sql

	sudo java -jar jdbc-console-0.0.88-43.jar --host=myhost.isqream.com --access-token=######### --pool=bi_pool

Connecting to a default pool:

.. code-block:: sql

	sudo java -jar jdbc-console-0.0.88-43.jar --host=myhost.isqream.com --access-token=#########

Performance and Concurrency Preferences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each pool in the system is associated with a parallelism policy that determines whether it prioritizes performance or high concurrency. By configuring different pools with distinct parallelism modes, you can optimize resource usage based on the specific needs of various organizational departments or work groups.

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

------------------

Cost Management
---------------

Cost management involves optimizing expenses by efficiently adjusting resources, such as cluster size and worker numbers, based on varying workloads, and utilizing features like environment suspension to temporarily halt billing during periods of inactivity.

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

-----------------
	
Billing
-------

**BLUE GPU Uptime** (**BGU**) is a BLUE GPU instance measurement unit that is calculated into monthly fees. The BGU monitor provides precise understanding of credit consumption, cluster utilization, and historical cluster size changes. This knowledge empowers you to estimate expenses, optimize cluster sizing based on usage, and analyze monthly billing trends. 

Monitor Elements
^^^^^^^^^^^^^^^^

To view the BGU monitor, in the side bar go to **Settings** > **Billing**. 

.. list-table:: Billing Monitor Elements
   :widths: auto
   :header-rows: 1

   * - Element
     - Description
   * - BGU Per Hour Graph
     - Displays BGU unit usage per hour within a specific date range
   * - Calendar
     - Enables you to select the BGU usage date range to examine
   * - Grand Total Table
     - Sums up the total BGU usage and grand total to be paid in USD for a specific date range
   * - Filter Menu 
     - Enables you to export monitor view into a CSV, CSV (Excel), or Google Sheets file
   







