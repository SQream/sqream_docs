.. _performing_basic_blue_operations:

*************
SQL Workflows
*************

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:
   
**Jobs** is a workflow management tool that enables you to create complex SQL workflows. You can use **Jobs** to create and automate sequences of SQL scripts, enabling them to trigger one another and deliver insights or prepare your data for advanced tasks like data modeling and training. Each job is constructed out of the following elements:

.. list-table:: Job Elements
   :widths: auto
   :header-rows: 1

   * - Element
     - Description
   * - SQL Scripts
     - A list of saved SQL scripts. It is recommended that scripts be named according to the action performed when the script is executed. 
   * - Task
     - A step within a linear operation that forms a workflow.
   * - Job
     - Consists of multiple tasks, executed in sequence to generate insights.

Creating a New Job
==================

Jobs are constructed from one or more SQL scripts represented by tasks. A **Task** has a name and a SQL script. Since jobs are sequential operations, the order of the tasks within a job has to make sense. You can set jobs to be executed either manually or schedule them to be executed automatically.

1. In the sidebar go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left-hand corner, type in task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequel task, select the ``+`` button located under the last task in the **Preview** window.
6. After having added all required SQL scripts, it is essential that you save the job by selecting the **Save Job** button located in the upper right-hand corner.
7. You may choose on of the following options:
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

You can decide that for some jobs it is best to work on over time or else, you might have started constructing a job but for any reason did not get to finish the work. If you did not save the job and had moved on to another page, the job will automatically be saved under **Jobs** > **Drafts**. You may edit jobs saved to **Drafts** only if they were created by you. 

1. In the sidebar go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left-hand corner, type in task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequel task, select the ``+`` button located under the last task in the **Preview** window.
6. You may now close the webpage you are working on and the job will be automatically be saved under **Jobs** > **Drafts**.
7. To edit a job that is saved to **Drafts**, hover over a job that you created and from the three-dot menu on the right-hand side choose **Edit Job**.

Utilizing Other Users' Jobs
===========================

To save time, you may create a job based on other users' jobs. This may be helpful when an existing job has elements in it that are required for a job you plan to create, but require some modifications or additions.

1. In the sidebar go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the job you wish to utilize and choose **Duplicate Job** from the three-dot menu.
3. 

Monitoring Completed Jobs
=========================

You may monitor all completed jobs, verify query execution success, and investigate failed queries.

1. In the sidebar go to **Jobs** > **History**.
2. Hover over and select the job you wish to investigate.

   A drop-down menu opens, reviling information about each job task. 

Deleting Jobs
=============

You may only delete jobs created by you.

1. In the sidebar go to **Jobs** and then either **All Jobs** or **Drafts**.
2. Hover over the job you wish to delete and choose **Delete** from the three-dot menu.


