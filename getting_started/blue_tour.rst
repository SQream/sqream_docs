.. _blue_tour:

***************
BLUE Quick Tour
***************
 
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

Evaluating Real-Time Cluster Workloads
--------------------------------------

The **Dashboard** has a **Current** (Cluster) **Status** panel which provides real-time workload overview with: 

* Running statements  
* Queued  statements
* Running Jobs

This panel also timestamps its latest updates, enabling you to follow the evolution of changes with precision.

Monitoring the BLUE Web Interface Activity
------------------------------------------

The **Activity** page provides a detailed overview of your BLUE web interface activity. It displays all executed statements along with the following details:

* Start time
* Session ID
* Query ID
* Type
* SQL Statements
* Duration (also shows failed statements)
* Execution Plan

You may also filter the information by **Session ID**, **Type**, **SQL Statements** (script), and **Duration**.

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
   :width: 800
