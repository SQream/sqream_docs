.. _performing_basic_blue_operations:

**********************
Workflow Orchestration
**********************

.. toctree::
   :maxdepth: 1
   :glob:
   :titlesonly:
   :hidden:
   
You can orchestrate complicated operations based on SQL scripts using **Jobs**, the BLUE workflow management tool. Use **Jobs** to create linear, step-by-step operations to generate insights. 

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

Drafting Jobs
=============


	 
