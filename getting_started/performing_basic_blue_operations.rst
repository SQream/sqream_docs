.. _performing_basic_blue_operations:

*************
Workflows
*************
   
Workflows play a pivotal role in data preparation, modeling, and training. Managing intricate workflows requires the orchestration of sequences in which SQL and Python script dependencies trigger one another. The **Jobs** workflow management tool caters to this need, enabling both manual and scheduled automatic runs of workflows.

What are Jobs
===================

A Job is an automated set of SQL and Python scripts that form a workflow. Think of a Job as your main strategy and the scripts as the individual steps needed to carry it out. Each individual script is represented by a single **Task**.

New Job
========

Authentication
---------------

The Jobs feature requires its own access-token protected connection, which is a simple setup. If you haven't configured a secure connection yet, check out the :ref:`connecting_to_blue` guide for step-by-step instructions.

.. _creating_a_job:

Creating a Job
---------------

1. In the sidebar go to **Jobs**.
2. Select the **Create New Job** button, enter Job name, and select **Save**.

   The Job **Preview** opens.
   
3. In the upper left corner, type in the task name and description.
4. Drag a SQL or Python script from the **Scripts** menu to the **Drag Script** box of the task.

   Ensure that scripts are saved under your bucket's parent directory; otherwise, it will not appear in the menu.

5. To create a new task, select |add_task| located under the last task in the **Preview** window.
6. After having created all tasks, select the **Save Job** button located in the upper right corner and choose one of the following options:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Option
     - Description
   * - Save to Jobs
     - Your Job is saved under **Jobs** > **All Jobs**. You are able to manually execute the Job by hovering over it and selecting |play_job|.  
   * - Schedule Job
     - You may set the date and time of day for the Job to be executed for the first time by setting **Date** and **Time**. Additionally, you may set the Job to be executed repeatedly by setting it to **Repeat Every** certain number of days. Your Job is saved under **Jobs** > **All Jobs**. The |scheduled_job| indicates Scheduled Jobs.


Working with SQL and Python Scripts
-----------------------------------

Jobs are composed of multiple tasks. Each task is associated with a single SQL or Python script. To create tasks, you need to have scripts prepared and ready to be used. For SQL scripts, after having created and saved a script, it will automatically appear on the **Scripts** list that is used for creating Jobs. You cannot create Python scripts using the Workbench. Python scripts may only be uploaded from your bucket. 

Keep in mind that scripts that are saved and uploaded to the **Scripts** list will be executed using your master database and public schema by default. To have your scripts use other database and/or schema and/or resource pool, you may use the :ref:`use_database`, :ref:`use_schema`, and :ref:`use_pool` commands within your script. 

1. In the sidebar, go to **Workbench** and create a SQL script.
2. On the right side of the ribbon, select **Upload**.

   The **SQL Catalogue** window opens.

3. In the **Save As** box, type in a name for your SQL script and select **Save**.

   SQL script names may not contain special characters.

.. tip:: When choosing a script name, it is advisable to accurately reflect its action or purpose.

Drafting Jobs
==============

Whether you're actively working on a Job for an extended duration or have initiated the composition without completion, you can choose to save it as a draft. If you navigate away without saving the Job manually, it will be automatically preserved in the **Jobs** > **Drafts** section. Only the creator of a draft can edit it.

1. In the sidebar, go to **Jobs**.
2. Select the **Create New Job** button, enter Job name, and select **Save**.

   The newly created Job page opens.
   
3. In the upper left corner, type in the task name and description.
4. Drag a script from the **Scripts** menu to the **Drag Script** box of the task.

    Ensure that your script is saved under your bucket parent directory or it will not show in the menu.

5. To create a task, select the |add_task| located under the last task in the **Preview** window.
6. You may now close the webpage you are working on and the Job will be automatically saved under **Jobs** > **Drafts**.
7. To edit a Job that is saved to **Drafts**, hover over a Job that you created, and from the |three_dot_job| menu choose **Edit Job**.

Managing Existing Jobs
=======================

Whether it's for maintenance or general enhancements, you can manage and edit Jobs and Tasks, provided that the Job is not currently running.

Editing a Job
---------------

1. In the sidebar, go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the Job you wish to edit and from the |three_dot_job| menu choose **Edit Job**.

   The Job **Preview** opens.
   
3. You may now:

* Delete a task by hovering over it and choosing |delete_task| 
* Change the task script by hovering over it, choosing |delete_script|, and dragging a new SQL or Python script
* Rename Job
* Rename tasks
* Add or edit task description

Editing SQL Tasks Using the Workbench
--------------------------------------

1. In the sidebar, go to **Workbench**.
2. On the right side of the ribbon, select **Download**.

   The SQL **Catalogue** window opens.
   
3. Select the script you wish to edit by either typing in the script name in the **File Name** box or select the script from the script menu.
4. Select **Open**.

   The SQL script is displayed in the **Workbench**.

5. Edit the script.
6. On the right side of the ribbon, select **Upload**.

   The **SQL Catalogue** window opens. 
   
7. Name the script you wish to save by either typing in the script name in the **Save As** box or select the script from the script menu.

Utilizing Existing Jobs
----------------------------

You have the option to utilize other users' Jobs to optimize your time and effort. This is done by duplicating existing Jobs and using the duplication as the grounds to build upon your own Job. 

1. In the sidebar, go to **Jobs** > **All Jobs**.
2. Hover over the Job you wish to utilize and from the |three_dot_job| menu choose **Duplicate Job**.

   The duplication is automatically saved to the **Drafts** tab under the same name as the original Job with an addition of a time-stamp.

.. _sharing_jobs:

Sharing Jobs 
----------------

1. In the sidebar, go to **Jobs** > **All Jobs**.

2. To share a Job with specific users:

   a. Hover over the Job you wish to share and from the |three_dot_job| menu choose **Share Job**.

      The **Share Job** window opens.
   
   b. In the search box, type the name or email of the user you want to share your Job with and select **Share**.

      The user you shared your Job with is now able to delete, duplicate, and share this Job.
   
3. To share a Job with all users:

   a. Make your Job public by hovering over it and select |locked_lock|.

      The lock icon changes to |open_lock|, indicating your Job is now public.
	  
   b. To make your Job private again, select |open_lock|.

.. _importing_and_exporting_jobs:

Importing and Exporting Jobs
-----------------------------

The seamless import and export capability for existing jobs between clusters or environments empowers you to transfer them without the need for recreation. Jobs are exported and imported in JSON format.

**Importing**

1. In the sidebar, go to **Jobs**.

2. Select **Import Job**.

   Your local directory and file dialog opens.
   
3. Select the Job you wish to import into your cluster.

   The Job has been successfully imported and appears under **Jobs** > **Drafts**.
   
**Exporting**

1. In the sidebar, go to **Jobs** > **All Jobs**.

2. Hover over the Job you wish to export and from the |three_dot_job| menu choose **Export Job**.

   Your local folder and file dialog opens.
   
3. Select a directory where you want to save the job.

   The Job has been successfully exported to a local directory.
   
Changing Job Ownership
-----------------------

1. In the sidebar, go to **Jobs** > **All Jobs**.

2. Hover over the Job which ownership you wish to change and from the |three_dot_job| menu choose **Change Job Owner**.

   The **Change job owner** window opens.
   
3. In the search box, type the name or email of the user you want to grant ownership to and select **Change**.

   The new owner is granted Job ownership privileges while you are remained with shared Job privileges.

.. _terminating_a_running_job:

Terminating a Running Job
--------------------------

Please be aware that once successfully executed before you stopped the Job, DML statements have already made the changes to the tables and database.

1. In the sidebar, go to **Jobs** > **All Jobs**.
2. Hover over the Job you wish to stop and select |stop_job|. 

   The Job is stopped and assigned a **Failed** status.

Deleting Jobs
--------------

You may only delete Jobs owned by you.

1. In the sidebar, go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the Job you wish to delete and from the |three_dot_job| menu choose **Delete**.

Monitoring Jobs
================

The **History** tab is your go-to for checking the last execution time, the next scheduled execution, and the current status of your Job.

Job status may be one of four options:

.. list-table:: Job Status
   :widths: auto
   :header-rows: 1

   * - Status
     - Description
   * - Completed Successfully
     - Your job was successfully completed
   * - Failed
     - Your job has failed and is not completed
   * - Running
     - Your job is currently running
   * - Pending
     - Your job will be executed as soon as a Worker becomes available

Failed Jobs
------------ 

1. To investigate failed Jobs, in the sidebar, go to **Jobs** and select the **History** tab.
2. Select the Job you wish to investigate.

   A drop-down table opens, revealing one of four options for each task: 

.. list-table:: Task Status
   :widths: auto
   :header-rows: 1

   * - Status
     - Description
   * - Done
     - Task was successfully completed
   * - Failed
     - Task has failed and is not completed
   * - Running
     - Task is currently running
   * - Pending
     - Task will be executed as soon as a Worker becomes available

3. To retrieve a failed task log, click on the **Failed** button.  

   A pop-up error log opens, depicting error details.                                         



.. |scheduled_job| image:: /_static/images/jobs/scheduled_job.png
   :align: middle

.. |delete_script| image:: /_static/images/jobs/delete_script.png
   :align: middle
   
.. |add_task| image:: /_static/images/jobs/add_task.png
   :align: middle
   
.. |scheduled_task| image:: /_static/images/jobs/scheduled_task.png
   :align: middle
   
.. |delete_task| image:: /_static/images/jobs/delete_task.png
   :align: middle

.. |three_dot_job| image:: /_static/images/jobs/three_dot_job.png
   :align: middle

.. |locked_lock| image:: /_static/images/jobs/locked_lock.png
   :align: middle

.. |open_lock| image:: /_static/images/jobs/open_lock.png
   :align: middle

.. |play_job| image:: /_static/images/jobs/play_job.png
   :align: middle   
   
.. |stop_job| image:: /_static/images/jobs/stop_job.png
   :align: middle      
