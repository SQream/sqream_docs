.. _monitoring_jobs:

***************
Monitoring Jobs
***************

The **History** tab is your go-to for checking the current job status, the last execution time, and the next scheduled execution.

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

.. topic:: ``clusteradmin``

   A ``clusteradmin`` can enable **View cluster jobs** to view all the Jobs of all users. This is helpful for managing your cluster and keeping it clean.

Failed Jobs
=========== 

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
