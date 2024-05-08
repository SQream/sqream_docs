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

Roles and Permissions
=====================

In the **Roles** area you can create and assign roles and manage user permissions. 

The **Type** column displays one of the following assigned role types:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Role Type
     - Description
   * - Groups
     - Roles with no users.
   * - Enabled users
     - Users with log-in permissions and a password.
   * - Disabled users
     - Users with log-in permissions and with a disabled password. An admin may disable a user's password permissions to temporary disable access to the system.


Viewing Information About a Role
--------------------------------

Clicking a role in the roles table displays the following information:

* **Parent Roles** - displays the parent roles of the selected role. Roles inherit all roles assigned to the parent.
   
* **Members** - displays all members that the role has been assigned to. The arrow indicates the roles that the role has inherited. Hovering over a member displays the roles that the role is inherited from.
   
* **Permissions** - displays the role's permissions. The arrow indicates the permissions that the role has inherited. Hovering over a permission displays the roles that the permission is inherited from.


Creating a New Role
-------------------

You can create a new role by clicking **New Role**.

An admin creates a **user** by granting login permissions to a role. Each role is defined by a set of permissions. An admin can also group several roles together to form a **group** to manage them simultaneously. For example, permissions can be granted to or revoked on a group level.

Clicking **New Role** lets you do the following:

* Add and assign a role name (required)
* Enable or disable log-in permissions for the role
* Add or delete permissions
* Grant the selected user with clusteradmin permissions
 
From the New Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field. From the New Role panel you can also search and scroll through the permissions. In the **Search** field you can use the **and** operator to search for strings that fulfill multiple criteria.

When adding a new role, you must select the **Enable login for this role** check boxe.

Editing a Role
--------------

Once you've created a role, clicking the **Edit Role** button lets you do the following:

* Edit role name
* Enable or disable log-in permissions
* Assign or delete parent roles
* Assign a role **administrator** permissions
* Add or delete permissions
* Grant the selected user with superuser permissions

From the Edit Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field. From the Edit Role panel you can also search and scroll through the permissions. In the **Search** field you can use the **and** operator to search for strings that fulfill multiple criteria.

Deleting a Role
---------------

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
   
