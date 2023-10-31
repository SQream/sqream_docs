.. _performing_basic_blue_operations:

*************
SQL Workflows
*************
   
SQL workflows play a pivotal role in data preparation, modeling, and training. Managing intricate SQL workflows requires the orchestration of sequences in which SQL script dependencies trigger one another. The **Jobs** workflow management tool caters to this need, enabling both manual and scheduled automatic runs of SQL workflows.

What are Jobs
===================

A Job is an automated set of SQL scripts that form a workflow. Think of a Job as your main strategy and the SQL scripts as the individual steps needed to carry it out. Each individual SQL script is represented by a single **Task**.

.. list-table:: Workflow Concepts
   :widths: auto
   :header-rows: 1

   * - Element
     - Description
   * - SQL Script
     - A list of saved and ready-to-use SQL scripts. When you choose a name for a SQL script, it is advisable to choose a name that accurately reflects the SQL action or purpose. Saved SQL scripts may be managed using the `Workbench <https://docs.sqream.com/en/blue/getting_started/performing_basic_blue_operations.html#editing-saved-sql-scripts>`_.
   * - Task
     - A step within a serial operation that forms a job. 
   * - Job
     - Composed of multiple tasks that are executed in a specific sequence.

New Job
========

Authentication
---------------

The Jobs feature requires its own access-token protected connection, which is a simple setup. If you haven't configured a secure connection yet, check out the :ref:`connecting_to_blue` guide for step-by-step instructions.


Creating a Job
---------------

1. In the sidebar go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left corner, type in the task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequel task, select the ``+`` button located under the last task in the **Preview** window.
6. After having added all required SQL scripts, select the **Save Job** button located in the upper right corner.
7. You may choose one of the following options:

* **Save to Jobs**
* **Schedule Job**

.. list-table:: Save Job Options
   :widths: auto
   :header-rows: 1

   * - Option
     - Description
   * - Save to Jobs
     - Your job will be saved under **Jobs** > **All Jobs**. You will be able to manually execute the job by hovering over the job list and selecting the ``►`` button. After having selected ``►``, the job **Status** will show **Running**.  
   * - Schedule Job
     - You may set the date and time of day for the job to be executed for the first time by setting **Date** and **Time**. Additionally, you may set the job to be executed repeatedly by setting it to **Repeat Every** certain number of days. Your job will be saved under **Jobs** > **All Jobs**. The job **Status** will show **Pending**.


Saving SQL Scripts as Tasks
----------------------------

Jobs are composed of multiple tasks. Each task is associated with a single SQL script. To create tasks, you need to have SQL scripts prepared and ready to be used. After having created and saved a SQL script, it will automatically appear on the **SQL Scripts** list that is used for creating jobs.

Keep in mind that SQL scripts that are saved and uploaded to the **SQL Scripts** list will be executed using your master database and public schema by default. To have your SQL scripts use other database and/or schema and/or resource pool, you may use the :ref:`use_database`, :ref:`use_schema`, and :ref:`use_pool` commands within your script. 

1. In the sidebar, go to **Workbench** and create a SQL script.
2. On the right side of the ribbon, select **Upload**.

   The **SQL Catalogue** window opens.

3. In the **Save As** box, type in a name for your SQL script and select **Save**.

.. tip:: When choosing a SQL script name, it is advisable to accurately reflect the SQL action or purpose.


Job Edit
================

Whether it's for maintenance or general enhancements, you can edit existing Jobs and Tasks, provided that the Job is not currently running.

Editing Tasks
---------------------------

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

You have the option to utilize other users' jobs to optimizes your time and effort. This is done by duplicating existing Jobs and using the duplication as the grounds to build upon your own Job. 

1. In the sidebar, go to **Jobs** > **All Jobs**.
2. Hover over the job you wish to utilize and from the three-dot menu choose **Duplicate Job**.

   The duplication is automatically saved to the **Drafts** tab under the same name as the original job with an addition of a time-stamp.

Drafting Jobs
---------------

Whether you're actively working on a job for an extended duration or have initiated the composition without completion, you can choose to save it as a draft. If you navigate away without saving the job manually, it will be automatically preserved in the **Jobs** > **Drafts** section. Only the creator of a draft can edit jobs saved in the **Drafts** section.

1. In the sidebar, go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left corner, type in the task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequel task, select the ``+`` button located under the last task in the **Preview** window.
6. You may now close the webpage you are working on and the job will be automatically saved under **Jobs** > **Drafts**.
7. To edit a job that is saved to **Drafts**, hover over a job that you created, and from the three-dot menu choose **Edit Job**.

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
     - You job will be executed as soon as a Worker becomes available

Failed Jobs
------------ 

1. To investigate failed Jobs, in the sidebar, go to **Jobs** and select the **History** tab.
2. Select the job you wish to investigate.

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

Deleting Jobs
=============

You may only delete jobs owned by you.

1. In the sidebar, go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the job you wish to delete and from the three-dot menu choose **Delete**.





