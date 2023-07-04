.. _performing_basic_blue_operations:

*************
SQL Workflows
*************

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:
   
**Jobs** is a workflow management tool that enables you to create complex SQL workflows. You can use **Jobs** to create and automate sequences of SQL scripts, enabling them to trigger one another and deliver insights or prepare your data for advanced tasks like data modeling and training. You may execute your jobs manually or schedule them for automatic execution. 

.. list-table:: SQL Workflow Elements
   :widths: auto
   :header-rows: 1

   * - Element
     - Description
   * - SQL Scripts
     - A list of saved and ready-to-use SQL scripts. When you choose a name for a SQL script, it is advisable to choose a name that accurately reflects the SQL action or purpose. Scripts are managed 
   * - Task
     - A step within a serial operation that forms a job. 
   * - Job
     - Composed of multiple tasks that are executed in a specific sequence.

Saving SQL Scripts to Be Used in Jobs
=====================================

Jobs are composed of multiple tasks. Each task is associated with a single SQL script. To create tasks, you need to have SQL scripts prepared and ready to be used. After having created and saved a SQL script, it will automatically appear on the **SQL Scripts** list that is used for creating jobs.

Keep in mind that SQL scripts that are saved and uploaded to the **SQL Scripts** list will be executed using your master database and public schema by default. To have your SQL scripts use any other database and/or schema, use the :ref:`use_database` and :ref:`use_schema` commands within your script. 

1. In the sidebar, go to **Editor** and create an SQL script.
2. On the right-hand side of the ribbon, select **Upload**.

   The **SQL Catalogue** window opens.
3. In the **Save As** box, type in a name for your SQL script and select **Save**.

.. tip:: When you choose a name for a SQL script, it is advisable to choose a name that accurately reflects the SQL action or purpose.

Creating a New Job
==================

Jobs are composed of multiple tasks that are executed in a specific sequence. Each individual **Task** represents a single SQL script. As jobs are sequential operations, it is important to order the tasks in a meaningful way. You have the flexibility to choose between executing jobs manually or scheduling them for automatic execution.

1. In the sidebar go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left-hand corner, type in the task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequel task, select the ``+`` button located under the last task in the **Preview** window.
6. After having added all required SQL scripts, it is essential that you save the job by selecting the **Save Job** button located in the upper right-hand corner.
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


Drafting Jobs
=============

If you are working on a job over a period of time or if you have started composing a job but haven't finished it, you have the option to save it as a draft. In case you didn't save the job and navigated to another page, the job will be automatically saved under **Jobs** > **Drafts**. It's important to note that you can only edit jobs saved in the **Drafts** section if you were the one who created them.

1. In the sidebar, go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left-hand corner, type in the task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequel task, select the ``+`` button located under the last task in the **Preview** window.
6. You may now close the webpage you are working on and the job will be automatically saved under **Jobs** > **Drafts**.
7. To edit a job that is saved to **Drafts**, hover over a job that you created, and from the three-dot menu on the right-hand side choose **Edit Job**.

Utilizing Existing Jobs
=======================

To optimize your time and effort, you have the option to create a new job based on existing jobs from other users. This feature proves helpful when there are elements within an existing job that you require for your own job but with some modifications or additional components.

1. In the sidebar, go to **Jobs** > **All Jobs**.
2. Hover over the job you wish to utilize and from the three-dot menu choose **Duplicate Job**.

   The duplication is automatically saved to the **Drafts** tab under the same name as the original job with a time-stamp addition ``yyyy-mm-dd hh:mm:ss``.

Monitoring Completed Jobs
=========================

You may monitor all completed jobs, verify query execution success, and investigate failed queries.

1. In the sidebar, go to **Jobs** > **History**.
2. Hover over and select the job you wish to investigate.

   A drop-down menu opens, reviling information about each task.

.. list-table:: Job and Task Status
   :widths: auto
   :header-rows: 1

   * - Option
     - Description
   * - 
     - 
   * - 
     - 

Deleting Jobs
=============

You may only delete jobs created by you.

1. In the sidebar, go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the job you wish to delete and from the three-dot menu choose **Delete**.

Session idleness may be set to 10—130,000 minutes.


