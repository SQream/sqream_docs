.. _new_job:

*******
New Job
*******

The Jobs feature requires its own access-token protected connection, which is a simple setup. If you haven't configured a secure connection yet, check out the :ref:`connecting_to_blue` guide for step-by-step instructions.

.. _creating_a_job:

Creating a Job
==============

**Before You Begin**

* Python scripts must be Python 3.9.17 compatible. 
* If you are missing Python libraries, please contact BLUE support at `blue_support@sqreamtech.com <blue_support@sqreamtech.com>`_ for assistance.
* Once you've set up a new job, it may take a few minutes for the job to become available for you to run.

1. In the sidebar go to **Jobs**.
2. Select the **Create New Job** button, enter Job name, and select **Save**.

   The Job **Preview** opens.
   
3. In the upper left corner, type in the task name and description.
4. Drag a SQL or Python script from the **Scripts** menu to the **Drag Script** box of the task.

   Ensure that scripts are saved under your bucket's parent directory; otherwise, they will not appear in the menu.

5. To create a new task, select |add_task| located under the last task in the **Preview** window.
6. After having created all tasks, select the **Save Job** button located in the upper right corner and choose one of the following options:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Option
     - Description
   * - Save to Jobs
     - Your Job is saved under **Jobs** > **All Jobs**. You can manually execute the Job by hovering over it and selecting |play_job|.  
   * - Schedule Job
     - You may set the date and time of day for the Job to be executed for the first time by setting **Date** and **Time**. Additionally, you may set the Job to be executed repeatedly by setting it to **Repeat Every** certain number of days. Your Job is saved under **Jobs** > **All Jobs**. The |scheduled_job| indicates Scheduled Jobs.


Working with SQL and Python Scripts
===================================

Jobs are composed of multiple tasks. Each task is associated with a single SQL or Python script. To create tasks, you must have scripts prepared and ready to use. Keep in mind that scripts that are saved and uploaded to the **Scripts** list will be executed using your master database and public schema by default. To have your scripts use other databases and/or schema and/or resource pool, you may use the :ref:`use_database`, :ref:`use_schema`, and :ref:`use_pool` commands within your script. 

**For Python Scripts**

You cannot create Python scripts using the Workbench and they may only be uploaded from your bucket. Scripts must be Python 3.9.17 compatible. 

**For SQL Scripts** 

After having created and saved a script, it will automatically appear on the **Scripts** list that is used for creating Jobs.

1. In the sidebar, go to **Workbench** and create a SQL script.
2. On the right side of the ribbon, select **Upload**.

   The **SQL Catalogue** window opens.

3. In the **Save As** box, type in a name for your SQL script and select **Save**.

   SQL script names may not contain special characters.

.. tip:: When choosing a script name, it is advisable to accurately reflect its action or purpose.


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