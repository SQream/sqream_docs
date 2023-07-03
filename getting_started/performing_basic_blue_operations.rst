.. _performing_basic_blue_operations:

**********************
Workflow Orchestration
**********************

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:
   
You can use **Jobs**, the BLUE workflow management tool, to orchestrate complex, sequential operations based on SQL scripts.

.. list-table:: Job Elements
   :widths: auto
   :header-rows: 1

   * - Element
     - Description
   * - SQL Scripts
     - A list of SQL scripts that are saved in the system. It is recommended to name each script according to the action the script does when executed. 
   * - Task
     - A task is one element within a linear, step-by-step operation. Tasks are meant to be arranged one after the other in a way that will form a workflow.
   * - Job
     - A job constructed out of several tasks. The aim of executing a job is to automatically execute all the tasks, one by one, in a way that will form a workflow and generate insight.

Creating a New Job
==================

Jobs are constructed out of one or more SQL scripts that are represented by tasks. A **Task** has a name and a SQL script. Since jobs are sequential operations, the order of the tasks within a job has to make sense. You can set jobs to be executed either manually or schedule them to be executed automatically.

1. In the sidebar and go to **Jobs**.
2. Select the **Create New Job** button, enter job name, and select **Save**.

   The newly created job page opens.
   
3. In the upper left-hand corner, type in task name and description.
4. Drag a script from the **SQL Scripts** menu to the **Drag SQL** box of the task.

   Tasks are always shown in the **Preview** window.

5. To create a sequential task, select the ``+`` button located under the last task in the *Preview** window.
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


	 
