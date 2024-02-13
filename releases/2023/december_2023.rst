.. _december_2023:

******************
December 2023
******************

Job Execution Termination
^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, you have the option to use the UI to terminate any executed Job. This functionality proves valuable in scenarios where a Job is stuck or exceeds expected duration, leading to significant consumption of system resources. Additionally, it is beneficial when an executed Job is awaiting a resource, like a table, held by another Job or different cluster users. Jobs may encounter errors or unforeseen issues during execution, and granting users the ability to stop a job allows timely intervention to prevent further complications.

See :ref:`Job termination<terminating_a_running_job>` using the UI.

Importing and Exporting Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users often encounter the need to transfer existing Jobs seamlessly between BLUE clusters or BLUE environments without the necessity of recreating them. This is particularly crucial for data teams aiming to capitalize on successful Jobs across various environments, enabling them to expedite data movement tasks efficiently. Jobs are exported and imported in JSON format.

See how to :ref:`import and export<importing_and_exporting_jobs>` Jobs.

Using Python Scripts for Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may now use Python scripts when creating Jobs. The integration of Python scripts into database operations enhances automation as users harness Python's efficiency to schedule and execute routine database tasks, thereby reducing manual effort and mitigating the risk of errors. Python's scripting flexibility enables agile development and quick iterations. Users can rapidly prototype, test, and refine scripts, fostering an iterative and responsive approach to database Job creation.

See how you can :ref:`use Python scripts<creating_a_job>` when creating Jobs.
