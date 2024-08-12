.. _performing_basic_blue_operations:

*********
Workflows
*********
   
Workflows play a pivotal role in data preparation, modeling, and training. Managing intricate workflows requires the orchestration of sequences in which SQL and Python script dependencies trigger one another. The **Jobs** workflow management tool caters to this need, enabling both manual and scheduled automatic runs of workflows.

Before You Begin
================

It is essential that you create a BLUE client and associate it with an :ref:`access token<access_tokens>`.

.. topic:: ``clusteradmin``

   Only a ``clusteradmin`` can create access tokens.

What are Jobs
=============

A Job is an automated set of SQL and Python scripts that form a workflow. Think of a Job as your main strategy and the scripts as the individual steps needed to carry it out. Each script is represented by a single **Task**.

Job Permissions
---------------

A Job can have one owner. When granting ownership of a Job to another user, the current Job owner forfeits owner permissions and receives the permissions of a user with whom the Job is shared.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Permission
     - Job Owner
     - User Job is Shared With
     - User Job is not Shared With
   * - Edit
     - |:white_check_mark:|
     - |:no_entry:|
     - |:no_entry:|
   * - Delete
     - |:white_check_mark:|
     - |:no_entry:|	 
     - |:no_entry:|
   * - Duplicate
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
   * - Share
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:no_entry:|
   * - Change Ownership
     - |:white_check_mark:|
     - |:no_entry:|
     - |:no_entry:|
   * - Export
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
   * - View Private Job
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:no_entry:|
   * - View Public Job
     - |:white_check_mark:|
     - |:white_check_mark:|
     - |:white_check_mark:|
   * - Make Job Private / Public
     - |:white_check_mark:|
     - |:no_entry:|
     - |:no_entry:|	 
	 

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:
   
   performing_basic_blue_operations/creating_a_job
   performing_basic_blue_operations/drafting_jobs
   performing_basic_blue_operations/managing_existing_jobs
   performing_basic_blue_operations/monitoring_jobs


