.. _monitoring_workers_and_services_from_the_dashboard:

.. _back_to_dashboard_5.4.3:

****************************
Monitoring Workers and Services from the Dashboard
****************************
The **Dashboard** is used for the following:

* Monitoring system health.
* Viewing, monitoring, and adding defined service queues.
* Viewing and managing worker status and add workers.

The following is an image of the Dashboard:

.. image:: /_static/images/dashboard.png

You can only access the Dashboard if you signed in with a ``SUPERUSER`` role.

The following is a brief description of the Dashboard panels:

.. list-table::
   :widths: 10 25 65
   :header-rows: 1  
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Services panel<services_panel_5.4.3>`
     - Used for viewing and monitoring the defined service queues.
   * - 2
     - :ref:`Workers panel<workers_panel_5.4.3>`
     - Monitors system health and shows each Sqreamd worker running in the cluster.
   * - 3
     - :ref:`License information<license_information_5.4.3>`
     - Shows the remaining amount of days left on your license.
   

.. _data_storage_panel_5.4.3:



:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.3>`

.. _services_panel_5.4.3:

Subscribing to Workers from the Services Panel
--------------------------
Services are used to categorize and associate (also known as **subscribing**) workers to particular services. The **Service** panel is used for viewing, monitoring, and adding defined `service queues <https://docs.sqream.com/en/latest/guides/features/workload_manager.html#workload-manager>`_.



The following is a brief description of each pane:
	 
.. list-table::
   :widths: 10 90
   :header-rows: 1  
   
   * - No.
     - Description
   * - 1
     - Adds a worker to the selected service.
   * - 2
     - Shows the service name.
   * - 3
     - Shows a trend graph of queued statements loaded over time.
   * - 4
     - Adds a service.
   * - 5
     - Shows the currently processed queries belonging to the service/total queries for that service in the system (including queued queries).	 

Adding A Service
^^^^^^^^^^^^^^^^^^^^^	 
You can add a service by clicking **+ Add** and defining the service name.

.. note:: If you do not associate a worker with the new service, it will not be created.

You can manage workers from the **Workers** panel. For more information about managing workers, see the following:

* :ref:`Managing Workers from the Workers Panel<workers_panel_5.4.3>`
* `Workers <https://docs.sqream.com/en/latest/reference/cli/sqream_console.html?highlight=workers#workers>`_

:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.3>`

.. _workers_panel_5.4.3:

Managing Workers from the Workers Panel
------------
From the **Workers** panel you can do the following:

* :ref:`View workers <view_workers_5.4.3>`
* :ref:`Add a worker to a service<add_worker_to_service_5.4.3>`
* :ref:`View a worker's active query information<view_worker_query_information_5.4.3>`
* :ref:`View a worker's execution plan<view_worker_execution_plan_5.4.3>`

.. _view_workers_5.4.3:

Viewing Workers
^^^^^^^^
The **Worker** panel shows each worker (``sqreamd``) running in the cluster. Each worker has a status bar that represents the status over time. The status bar is divided into 20 equal segments, showing the most dominant activity in that segment.
	 
From the **Scale** dropdown menu you can set the time scale of the displayed information
You can hover over segments in the status bar to see the date and time corresponding to each activity type:

* **Idle** – the worker is idle and available for statements.
* **Compiling** – the worker is compiling a statement and is preparing for execution.
* **Executing** – the worker is executing a statement after compilation.
* **Stopped** – the worker was stopped (either deliberately or due to an error).
* **Waiting** – the worker was waiting on an object locked by another worker.

.. _add_worker_to_service_5.4.3:

Adding A Worker to A Service
^^^^^^^^^^^^^^^^^^^^^	 
You can add a worker to a service by clicking the **add** button. 



Clicking the **add** button shows the selected service's workers. You can add the selected worker to the service by clicking **Add Worker**. Adding a worker to a service does not break associations already made between that worker and other services.


.. _view_worker_query_information_5.4.3:

Viewing A Worker's Active Query Information
^^^^^^^^^^^^^^^^^^^^^	 
You can view a worker's active query information by clicking **Queries**, which displays them in the selected service.


Each statement shows the **query ID**, **status**, **service queue**, **elapsed time**, **execution time**, and **estimated completion status**. In addition, each statement can be stopped or expanded to show its execution plan and progress. For more information on viewing a statement's execution plan and progress, see :ref:`Viewing a Worker's Execution Plan <view_worker_execution_plan_5.4.3>` below.

Viewing A Worker's Host Utilization
^^^^^^^^^^^^^^^^^^^^^	 

While viewing a worker's query information, clicking the **down arrow** expands to show the host resource utilization.



The graphs show the resource utilization trends over time, and the **CPU memory** and **utilization** and the **GPU utilization** values on the right. You can hover over the graph to see more information about the activity at any point on the graph.

Error notifications related to statements are displayed, and you can hover over them for more information about the error. 


.. _view_worker_execution_plan_5.4.3:

Viewing a Worker's Execution Plan
^^^^^^^^^^^^^^^^^^^^^
	 
Clicking the ellipsis in a service shows the following additional options:

* **Stop Query** - stops the query.
* **Show Execution Plan** - shows the execution plan as a table. The columns in the **Show Execution Plan** table can be sorted.

For more information on the current query plan, see `SHOW_NODE_INFO <https://docs.sqream.com/en/v2020-1/reference/sql/sql_statements/monitoring_commands/show_node_info.html#show-node-info>`_. For more information on checking active sessions across the cluster, see `SHOW_SERVER_STATUS <https://docs.sqream.com/en/v2020-1/reference/sql/sql_statements/monitoring_commands/show_server_status.html>`_.

.. include:: /reference/sql/sql_statements/monitoring_commands/show_server_status.rst
   :start-line: 67
   :end-line: 84

Managing Worker Status
^^^^^^^^^^^^^^^^^^^^^

In some cases you may want to stop or restart workers for maintenance purposes. Each Worker line has a :kbd:`⋮` menu used for stopping, starting, or restarting workers.


Starting or restarting workers terminates all queries related to that worker. When you stop a worker, its background turns gray.




.. |icon-user| image:: /_static/images/studio_icon_user.png
   :align: middle
   
.. |icon-dots| image:: /_static/images/studio_icon_dots.png
   :align: middle   
   
.. |icon-editor| image:: /_static/images/studio_icon_editor.png
   :align: middle

.. |icon-copy| image:: /_static/images/studio_icon_copy.png
   :align: middle

.. |icon-select| image:: /_static/images/studio_icon_select.png
   :align: middle

.. |icon-dots| image:: /_static/images/studio_icon_dots.png
   :align: middle

.. |icon-filter| image:: /_static/images/studio_icon_filter.png
   :align: middle

.. |icon-ddl-edit| image:: /_static/images/studio_icon_ddl_edit.png
   :align: middle

.. |icon-run-optimizer| image:: /_static/images/studio_icon_run_optimizer.png
   :align: middle

.. |icon-generate-create-statement| image:: /_static/images/studio_icon_generate_create_statement.png
   :align: middle

.. |icon-plus| image:: /_static/images/studio_icon_plus.png
   :align: middle

.. |icon-close| image:: /_static/images/studio_icon_close.png
   :align: middle

.. |icon-left| image:: /_static/images/studio_icon_left.png
   :align: middle

.. |icon-right| image:: /_static/images/studio_icon_right.png
   :align: middle

.. |icon-format-sql| image:: /_static/images/studio_icon_format.png
   :align: middle

.. |icon-download-query| image:: /_static/images/studio_icon_download_query.png
   :align: middle

.. |icon-open-query| image:: /_static/images/studio_icon_open_query.png
   :align: middle

.. |icon-execute| image:: /_static/images/studio_icon_execute.png
   :align: middle

.. |icon-stop| image:: /_static/images/studio_icon_stop.png
   :align: middle

.. |icon-dashboard| image:: /_static/images/studio_icon_dashboard.png
   :align: middle

.. |icon-expand| image:: /_static/images/studio_icon_expand.png
   :align: middle

.. |icon-scale| image:: /_static/images/studio_icon_scale.png
   :align: middle

.. |icon-expand-down| image:: /_static/images/studio_icon_expand_down.png
   :align: middle

.. |icon-add| image:: /_static/images/studio_icon_add.png
   :align: middle

.. |icon-add-worker| image:: /_static/images/studio_icon_add_worker.png
   :align: middle

.. |keep-tabs| image:: /_static/images/studio_keep_tabs.png
   :align: middle
   
:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.3>`



.. _license_information_5.4.3:
   
License Information
----------------------
The license information section shows the following:

 * The amount of time in days remaining on the license.
 * The license storage capacity.
 
.. image:: /_static/images/license_storage_capacity.png

 
:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.3>`
