.. _blue_tour:

**********
Quick Tour
**********
 
Executing Statements
====================

The **Workbench**  provides a comprehensive environment for writing, managing, and optimizing statements. 

|workbench_quick_tour|

#. Database Navigator (which includes :ref:`sample data <sample_data>` ready for you to play around with)

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
   
Managing Workflows
==================

Jobs » All Jobs

The **Jobs** page is where you can create, execute, and manage your SQL and Python workflows. It displays a list of existing Jobs along with the following information for each Job:

* Job Name
* Creation Time
* Owner
* Last Runtime
* Next Runtime
* Frequency
* Status

More about :ref:`executing, monitoring, and managing Jobs<performing_basic_blue_operations>`

.. _monitoring_your_cluster:

Monitoring Your Cluster
=======================

The **Dashboard** serves as a tool for you to monitor and promptly respond to any changes within your cluster. It enables you to track the health of your cluster and ensures that your workloads are operating as expected in near real-time.

Reading the **Dashboard** Charts
--------------------------------

The **Dashboard** charts offer a comprehensive overview of Worker performance, detailing:

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

.. _evaluating_real_time_cluster_workloads:

Evaluating Real-Time Cluster Workloads
--------------------------------------

The **Dashboard** has a panel which provides real-time workload overview of your **Currently Running**: 
  
* Queued statements
* Statements
* Jobs

And a **Monthly Usage** panel with an overview of your monthly cluster:

* Uptime (in minutes)
* Data Read (in bytes)
* Rows Read

These panels also timestamp latest updates, enabling you to follow the evolution of changes with precision.

.. _monitoring_web_interface_activity:

Monitoring Web Interface Activity
---------------------------------

The **Activity** page provides a detailed overview of your actions initiated via the web interface. It displays a table with all executed statements along with the following details:

* Start time
* Session ID
* Query ID
* Type
* SQL Statements
* Duration (also shows failed statements)
* Execution Plan (read more :ref:`here<retrieving_execution_plan_output_using_studio>`)

You may also filter the information by **Session ID**, **Type**, **SQL Statements** (script), and **Duration**.

To view the full details of an executed statement, hover over the desired row and click on it. This action will open a side window displaying comprehensive execution details, as illustrated in the example below:


|activity_page_details|


Administrating Your Cluster
===========================

Scaling your Cluster
--------------------

Settings »  Worker Kit » 

Navigate through different Worker kits to accommodate heavy loads or optimize resources during periods of low activity.

|worker_kit_quick_tour|

More about :ref:`scaling your cluster<resizing_your_cluster>`

Suspending and Resuming Your Cluster
------------------------------------

Settings »  Resource Pool » 

Configure your cluster to automatically enter a suspended state during idle periods and automatically resume when statements or jobs are executed. Customize performance and concurrency preferences to optimize cluster usage.

|resume_suspend_quick_tour|

#. Automatic suspension

#. Automatic resumption

#. Performance Vs. concurrency 

Define the conditions under which your cluster will shut down.

|suspension_policy_quick_tour|

#. Suspension policy for automatic suspension mode

#. Immediate suspension / resumption button

More about :ref:`suspending and resuming your cluster<suspending_and_resuming_pools>`

Managing Statement Queue
------------------------



Viewing Information About a Role
--------------------------------

The **Permissions** page is where you can create and assign roles and manage user permissions. It displays a list of existing roles along with the following information:

* Role ID
* Role Name
* Superuser
* Connected Databases

Clicking a role in the roles table displays the following:

* Existing permissions for each database the role has Connect permissions for
* Whether it is a user or a group role (more about :ref:`user and group roles<access_control_managing_roles>`)
* Edit role option
* Delete role option

Creating a New Role
-------------------

On the **Permissions** page you can create new roles.

An admin creates a **user** by granting login permissions to a role. Each role is defined by a set of permissions. An admin can also group several roles together to form a **group** to manage them simultaneously. For example, permissions can be granted to or revoked on a group level.

Clicking **New Role** lets you do the following:

* Add and assign a role name (required)
* Enable or disable log-in permissions for the role
* Add or delete permissions
* Grant the selected user with superuser permissions
 
From the New Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field.

When adding a new role, you must select the **Grant login** checkbox.

Editing a Role
--------------

On the **Permissions** page you can edit existing roles.

Clicking a role in the roles table and choosing the edit button lets you do the following:

* Edit role name
* Enable or disable log-in permissions
* Assign or delete parent roles
* Add or delete permissions
* Grant the selected user with superuser permissions

From the **Edit Role** panel you can view all role granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions using the **Add permissions** box. From the **Edit Role** panel you can also search and scroll through the permissions.

Deleting a Role
---------------

On the **Permissions** page you can delete existing roles.

Clicking the **delete** icon displays a confirmation message with the amount of users and groups that will be impacted by deleting the role.


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
   :width: 600
   
.. |activity_page_details| image:: /_static/images/activity_page_details.png
   :align: middle 
