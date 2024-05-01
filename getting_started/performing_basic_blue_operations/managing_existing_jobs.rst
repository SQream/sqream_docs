.. _managing_existing_jobs:

**********************
Managing Existing Jobs
**********************

Whether it's for maintenance or general enhancements, you can manage and edit Jobs and Tasks, provided that the Job is not currently running.

Editing a Job
=============

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
=====================================

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
=======================

You have the option to utilize other users' Jobs to optimize your time and effort. This is done by duplicating existing Jobs and using the duplication as the grounds to build upon your own Job. 

1. In the sidebar, go to **Jobs** > **All Jobs**.
2. Hover over the Job you wish to utilize and from the |three_dot_job| menu choose **Duplicate Job**.

   The duplication is automatically saved to the **Drafts** tab under the same name as the original Job with an addition of a time-stamp.

.. _sharing_jobs:

Sharing Jobs 
============

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
============================

The import and export capability for existing Jobs between BLUE clusters or BLUE environments empowers you to transfer them without the need for recreating the Job's execution tree. Please be aware that in addition to importing and exporting a Job, you need to verify that the required Task scripts and DDLs exist in the target BLUE cluster or Environment. 

Jobs are exported and imported in JSON format.

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
======================

1. In the sidebar, go to **Jobs** > **All Jobs**.

2. Hover over the Job which ownership you wish to change and from the |three_dot_job| menu choose **Change Job Owner**.

   The **Change job owner** window opens.
   
3. In the search box, type the name or email of the user you want to grant ownership to and select **Change**.

   The new owner is granted Job ownership privileges while you are remained with shared Job privileges.

.. _terminating_a_running_job:

Terminating a Running Job
=========================

Please be aware that once successfully executed before you stopped the Job, DML statements have already made the changes to the tables and database.

1. In the sidebar, go to **Jobs** > **All Jobs**.
2. Hover over the Job you wish to stop and select |stop_job|. 

   The Job is stopped and assigned a **Failed** status.

Deleting Jobs
=============

You may only delete Jobs owned by you.

1. In the sidebar, go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the Job you wish to delete and from the |three_dot_job| menu choose **Delete**.


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