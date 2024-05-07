.. _blue_tour:

***************
BLUE Quick Tour
***************

Executing Statements
====================

The **Workbench**  provides a comprehensive environment for writing, managing, and optimizing statements. 

|workbench_quick_tour|

#. Database Navigator

#. Resource Pool Navigator

#. Execution Controls

#. Script Handlers:

   * Format SQL
   * Download Script from Cloud
   * Upload Script to Cloud
   * Load a Query from Local File
   * Save Query to Local File

#. Limit Rows

#. Schema Browser:

   * Database Tree
   * System Queries
	
#. Statement Editor

#. Result Pane:

   * Result Table
   * Result Statement
   * Execution Tree
   * Copy Execution Plan
   * Export Results

Administrating your Cluster
===========================

The **Settings** page is a cluster administration section accessible only to users with cluster admin privileges. This page provides important controls for managing your cluster's resources, configurations, and access tokens.

Cluster Scaling for Resource Optimization
-----------------------------------------

**Settings** »  **Worker Kit** » 

Navigate through different Worker kits to accommodate heavy loads or optimize resources during periods of low activity.

|worker_kit_quick_tour|

Cluster Downtime and Uptime
---------------------------

**Settings** »  **Resource Pool** » 

Configure your cluster to automatically enter a suspended state during idle periods and automatically resume when statements or jobs are executed. Customize performance and concurrency preferences to optimize cluster usage.

|resume_suspend_quick_tour|

#. Automatic suspension

#. Automatic resumption

#. Performance Vs. concurrency 

Define the conditions under which your cluster will shut down.

|suspension_policy_quick_tour|

#. Suspension policy for automatic suspension mode

#. Immediate suspension / resumption button

More about :ref:`resizing your cluster<cluster_management>`

Monitoring Cluster Activity
===========================

The **Dashboard** serves as a tool for you to monitor and promptly respond to any changes within your system. It enables you to track the health of your system and ensures that your workloads are operating as expected in near real-time.

Reading the Charts
------------------

The dashboard charts offer a comprehensive overview of Worker performance, detailing:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Chart
     - Description
     - Sampling Interval
     - Timeframe Options
   * - Worker Loads
     - This measures the average load on the system within a specified timeframe. It's calculated based on the execution time of statements and the number of workers engaged, relative to the processing capacity during that period.
     - 15 seconds
     - 24/48/ hrs, past week, past month
   * - Queued Statements
     - This indicates the number of statements awaiting execution in the queue over a specific timeframe. 
     - 15 seconds
     - 24/48/ hrs, past week, past month
   * - Jobs
     - This indicates the total number of executed Jobs within a specific timeframe. 
     - 1 hour
     - Week, past 2 weeks, past month
   * - Tasks
     - This indicates the total number of executed Tasks within a specific timeframe.
     - 1 hour
     - Week, past 2 weeks, past month

Evaluating the Current System Status
------------------------------------

The dashboard **Current Status** provides a real-time cluster overview of: 

* Running statements  
* Queued  statements
* Running Jobs


.. |workbench_quick_tour| image:: /_static/images/workbench_quick_tour.png
   :align: middle    
   
.. |jobs_quick_tour| image:: /_static/images/jobs_quick_tour.png
   :align: middle  
   
.. |worker_kit_quick_tour| image:: /_static/images/worker_kit_quick_tour.png
   :align: middle    
   
.. |resume_suspend_quick_tour| image:: /_static/images/resume_suspend_quick_tour.png
   :align: middle   
   
.. |suspension_policy_quick_tour| image:: /_static/images/suspension_policy_quick_tour.png
   :align: middle    
   
   