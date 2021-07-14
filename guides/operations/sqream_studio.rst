.. _sqream_studio:

****************************
SQream Acceleration Studio 5.3.1
****************************

The SQream Studio is a web-based client for use with SQream DB. The Studio provides users with all functionality available from the command line in an intuitive and easy-to-use format. This includes running statements, managing roles and permissions, and managing SQream DB clusters.


.. contents:: This page describes the following:
   :depth: 3

Getting Started
==================










.. _setting_up_and_starting_studio:


Setting Up and Starting Studio
----------------

Studio is included with all `dockerized installations of SQream DB <https://docs.sqream.com/en/latest/guides/operations/setup/local_docker.html#installing-sqream-db-docker>`_. When starting Studio, it listens on the local machine on port 8080.






You can start Studio using :ref:`sqream-console<start_editor>`.

Logging In to Studio
---------------
**To log in to SQream Studio:**

1. Open a browser to the host on **port 8080**.

   For example, if your machine IP address is ``192.168.0.100``, insert the IP address into the browser as shown below:

   .. code-block:: console

      $ http://192.168.0.100:8080

2. Fill in your SQream DB login credentials. These are the same credentials used for :ref:`sqream sql<sqream_sql_cli_reference>` or JDBC.

.. image:: /_static/images/studio_login_v5.3.0.png

When you sign in, the License Warning is displayed.

.. image:: /_static/images/license_warning_5.3.1.png

Using Studio
-------------
When you log in, you are automatically taken to the **Editor** screen.

The Studio's main functions are displayed in the **Navigation** pane on the left side of the screen.

.. image:: /_static/images/studio_main_functions_5.3.0.png

From here you can navigate between the main areas of the Studio:

.. list-table::
   :widths: 10 90
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Dashboard<studio_dashboard>`
     - Only users with **superuser** permissions have access to the Dashboard.
   * - :ref:`Editor<studio_editor>`
     - All users have access to the Editor and to databases that they have permissions for.   
   * - :ref:`Logs<logs>`
     - Only users with the **superuser** permissions have access to the logs.

By clicking the user icon |icon-user|, you can also use it for logging out and viewing the following:

* User information
* Connection type
* SQream version
* SQream Studio version
* Data size limitations
* Log out

.. image:: /_static/images/studio_user_info_5.3.1.png


.. _back_to_dashboard:

.. _studio_dashboard:

Dashboard
==============================

If you signed in with a ``SUPERUSER`` role, you can access the Dashboard.

The Dashboard includes the panes shown below:

.. image:: /_static/images/studio_dashboard_main_5.3.0.png

The following is a brief description of each pane:

.. list-table::
   :widths: 10 25 65
   :header-rows: 1  
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Data Storage panel<data_storage_panel>`
     - Used to monitor cluster storage.
   * - 2
     - :ref:`Services panel<services_panel>`
     - Used for viewing and monitoring the defined `service queues <https://docs.sqream.com/en/latest/guides/features/workload_manager.html#workload-manager>`_.
   * - 3
     - :ref:`Workers panel<workers_panel>`
     - Monitors system health and shows each Sqreamd worker running in the cluster.
   * - 4
     - :ref:`License information<license_information>`
     - Shows the remaining amount of days left on your license.
   

.. _data_storage_panel:

Data Storage Panel
-----------------------
The **Data Storage** area displays your system's total disk usage (percentage) and data storage (donut graph).

.. image:: /_static/images/studio_dashboard_data_storage_5.3.0.png

Your data storage is shows as the following four components:

* **Data** – Storage occupied by databases in SQream DB.
* **Free** – Free storage space.
* **Deleted** – Storage that is temporarily occupied, but has not been reclaimed. For more information, see `Deleting Data <https://docs.sqream.com/en/latest/guides/features/delete.html#delete-guide>`_. The **deleted** value is estimated and may not be accurate.
* **Other** – Storage used by other applications. On a dedicated SQream DB cluster this should be near zero.

.. _administration_storage_database:

Clicking the expand arrow on the Data Storage panel expands it to show more information.

.. image:: /_static/images/studio_dashboard_expand_data_storage_5.3.0.png

The expanded Data Storage panel can be used to drill down into each database's storage footprint, and displays a breakdown of how much storage each database in the cluster uses.

.. image:: /_static/images/studio_dashboard_expand_data_storage_2_5.3.0.png



The database information is displayed in a table and shows the following:

* **Database name** - the name of the database.
* **Raw Size** – the estimated size of (uncompressed) raw data in the database.
* **Storage Size** – the physical size of the compressed data.
* **Ratio** – the effective compression ratio
* **Deleted Data** – Storage that is temporarily occupied, but has not been reclaimed.

Below the table, an interactive line graph displays the database storage trends. By default, the line graph displays the total storage for all databases. You can show a particular database's graph by clicking it in the table.

You can also change the line graph's timespan by selecting one from the timespan dropdown menu.

.. image:: /_static/images/studio_dashboard_expand_data_storage_3_5.3.0.png

:ref:`Back to Dashboard<back_to_dashboard>`

.. _services_panel:

Services Panel
--------------------------
Services are used to categorize and associate (also known as **subscribing**) workers to particular services. The **Service** panel is used for viewing, monitoring, and adding defined `service queues <https://docs.sqream.com/en/latest/guides/features/workload_manager.html#workload-manager>`_.

.. image:: /_static/images/studio_dashboard_services_panel_5.3.0.png







The Dashboard includes the four panes shown below:



.. image:: /_static/images/studio_dashboard_service_queue_5.3.0.png

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
You can add a service by clicking **Add** and defining the service name.

.. image:: /_static/images/studio_dashboard_defining_new_service_5.3.0.png

.. note:: If you do not associate a worker with the new service, it will not be created.

You can manage workers from the **Workers** panel. For more information on managing workers, see :ref:`Workers<workers_panel>`.

:ref:`Back to Dashboard<back_to_dashboard>`

.. _workers_panel:

Workers
------------
The **Workers** panel section describes the following:

* :ref:`Using the Workers panel <overview>`
* :ref:`Adding a worker to a service<add_worker_to_service>`
* :ref:`Viewing a worker's active query information<view_worker_query_information>`
* :ref:`Viewing a worker's execution plan<view_worker_execution_plan>`

.. _overview:

Using the Worker's Panel
^^^^^^^^
The **Worker** panel shows each worker (``sqreamd``) running in the cluster. Each worker has a status bar that represents the status over time. The status bar is divided into 20 equal segments, showing the most dominant activity in that segment.

.. image:: /_static/images/studio_dashboard_worker_area_description_5.3.0.png
	 
You can set the time scale of the displayed information by selecting a timeframe in the time scale dropdown menu.

.. image:: /_static/images/studio_dashboard_worker_set_scale_5.3.0.png

You can hover over segments in the status bar to see the date and time corresponding to each activity type:

* **Idle** – the worker is idle and available for statements.
* **Compiling** – the worker is compiling a statement and is preparing for execution.
* **Executing** – the worker is executing a statement after compilation.
* **Stopped** – the worker was stopped (either deliberately or due to an error).
* **Waiting** – the worker was waiting on an object locked by another worker.

.. _add_worker_to_service:

Adding A Worker to A Service
^^^^^^^^^^^^^^^^^^^^^	 
You can add a worker to a service by clicking the **add** button. 

.. image:: /_static/images/studio_dashboard_add_worker_to_service_5.3.0.png

Clicking the **add** button shows the selected service's workers. You can add the selected worker to the service by clicking **Add Worker**. Adding a worker to a service does not break associations already made between that worker and other services.

.. image:: /_static/images/studio_dashboard_add_worker_to_service_2_5.3.0.png

.. _view_worker_query_information:

Viewing A Worker's Active Query Information
^^^^^^^^^^^^^^^^^^^^^	 
You can view a worker's active query information by clicking **Queries**, which displays them in the selected service.

.. image:: /_static/images/studio_dashboard_worker_status_5.3.0.png

Each statement shows the **query ID**, **status**, **service queue**, **elapsed time**, **execution time**, and **estimated completion status**. In addition, each statement can be stopped or expanded to show its execution plan and progress. For more information on viewing a statement's execution plan and progress, see :ref:`Viewing a Worker's Execution Plan <view_worker_execution_plan>` below.

Viewing A Worker's Host Utilization
^^^^^^^^^^^^^^^^^^^^^	 

While viewing a worker's query information, clicking the **down arrow** expands to show the host resource utilization.

.. image:: /_static/images/studio_dashboard_show_cpu_gpu_graph_5.3.0.png

The graphs show the resource utilization trends over time, and the CPU memory and utilization and the GPU utilization values on the right.

.. image:: /_static/images/studio_dashboard_show_cpu_gpu_graph_open_5.3.0.png

You can hover over the graph to see more information about the activity at any point on the graph.

Error notifications related to statements are displayed as shown in the figure below, and you can hover over them for more information about the error. 

.. image:: /_static/images/studio_dashboard_notification_error_5.3.0.png

.. _view_worker_execution_plan:

Viewing a Worker's Execution Plan
^^^^^^^^^^^^^^^^^^^^^
	 
Clicking the ellipsis in a service shows the following additional options:

.. image:: /_static/images/studio_dashboard_worker_additional_options_5.3.0.png

Clicking **Stop Query** stops the query. Clicking **Show Execution Plan** shows the execution plan in a table. The columns in the Show Execution Plan table can be sorted.

.. image:: /_static/images/studio_dashboard_show_execution_plan_5.3.0.png

For more information on the current query plan, see `SHOW_NODE_INFO <https://docs.sqream.com/en/latest/reference/sql/sql_statements/monitoring_commands/show_node_info.html#show-node-info>`_.

For more information on checking active sessions across the cluster, see `SHOW_SERVER_STATUS <https://docs.sqream.com/en/latest/reference/sql/sql_statements/monitoring_commands/show_server_status.html>`_.

.. include:: /reference/sql/sql_statements/monitoring_commands/show_server_status.rst
   :start-line: 67
   :end-line: 84

Managing Worker Status
^^^^^^^^^^^^^^^^^^^^^

In some cases you may want to stop or restart workers for maintenance purposes. Each Worker line has a :kbd:`⋮` menu used for stopping, starting, or restarting workers.

.. image:: /_static/images/stop_restart_worker.png

Starting or restarting workers terminates all queries related to that worker.

.. image:: /_static/images/stop_restart_worker_2.png

When you stop a worker, its background turns gray.

.. image:: /_static/images/worker_stopped.png



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
   
:ref:`Back to Dashboard<back_to_dashboard>`



.. _license_information:
   
License Information
----------------------
The license information is a counter showing the amount of time in days remaining on the license.

:ref:`Back to Dashboard<back_to_dashboard>`


.. _studio_editor:

.. _editor_top:

Editor
=================

The Editor's main screen includes the four panes shown below:

.. image:: /_static/images/studio_editor_main_screen_5.3.0.png


	 
The following is a brief description of each pane:

.. list-table::
   :widths: 10 34 56
   :header-rows: 1  
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Toolbar<studio_editor_toolbar>`
     - Used to select the active database you want to work on, limit the number of rows, save query, etc.
   * - 2
     - :ref:`Database Tree and System Queries panel<studio_editor_db_tree>`
     - Shows a heirarchy tree of databases, views, tables, and columns
   * - 3
     - :ref:`Statement panel<studio_editor_statement_area>`
     - Used for writing queries and statements
   * - 4
     - :ref:`Results panel<studio_editor_results>`
     - Shows query results and execution information.


.. _studio_editor_db_tree:

.. _top:

.. _studio_editor_toolbar:

Toolbar
-------------

The following figure shows the **Toolbar** pane:

.. image:: /_static/images/studio_editor_toolbar_5.3.0.png

You can access the following from the Toolbar pane:

* **Database dropdown list** - select a database that you want to run statements on.

* **Service dropdown list** - select a service that you want to run statements on. The options in the service dropdown menu depend on the database you select from the **Database** dropdown list.

* **Execute** - lets you set which statements to execute. The **Execute** button toggles between **Execute** and **Stop**, and can be used to stop an active statement before it completes:

  * **Statements** - executes the statement at the location of the cursor.
  * **Selected** - executes only the highlighted text. This mode should be used when executing subqueries or sections of large queries (as long as they are valid SQLs).
  * **All** - executes all statements in a selected tab.
   
For more information on stopping active statements, see the :ref:`STOP_STATEMENT<stop_statement>` command.

* **Format SQL** - Lets you reformat and reindent statements.

* **Download query** - Lets you download query text to your computer.

* **Open query** - Lets you upload query text from your computer.

* **Max Rows** - By default, the Editor fetches only the first 10,000 rows. You can modify this number by selecting an option from the **Max Rows** dropdown list. Note that setting a higher number may slow down your browser if the result is very large. This number is limited to 100,000 results. To see a higher number, you can save the results in a file or a table using the :ref:`create_table_as` command.

:ref:`Back to Editor<editor_top>`

Database Tree and System Queries Panel
---------------
The following figure shows the **Database Tree** and **System Queries** panel, with the Database Tree tab selected.

.. image:: /_static/images/studio_database_tree_system_queries_panel_5053.png

The database tree contains two tabs showing the following information:

* :ref:`Database Tree tab<database_tree_tab>` - shows the database object hierarchy (such as tables, views, functions, and columns), lets you perform statement-related operations, and shows metadata (such as a number indicating the amount of rows in the table).
* :ref:`System Queries tab<system_queries_tab>` - contains predefined catalog queries for execution.



.. _database_tree_tab:

Database Tree
^^^^^^^^^^^^^^^^^^^^^^^
The following figure shows the **TABLES** object data opened, and the database object functions in the **calcs** table object:

.. image:: /_static/images/studio_database_object_operations_5030.png



The database object functions are used to perform the following:


  * To generate a SELECT statement in the Statement panel |icon-select|.
  * To copy table names into the Statement panel |icon-copy|.  
  * To perform additional operations |icon-dots|.
  
  
Generating a SELECT Statement in Statement Panel
***************************

Clicking |icon-select| copies the selected table's **columns** into the Statement panel as ``SELECT`` parameters:
  
.. image:: /_static/images/studio_generate_select_statement_5030.png

Copying Tables into Statement Panel
****************************

Clicking |icon-copy| copies the selected table's **name** into the Statement panel:

.. image:: /_static/images/studio_public_calcs_5053.png



   

Using Additional Object Options
****************************

Clicking |icon-dots| displays the following additional options:

.. image:: /_static/images/studio_additional_options_5053.png

The following table describes the additional options:

.. list-table::
   :widths: 30 70
   :header-rows: 1   
   
   * - Function
     - Description
   * - Insert statement
     - Generates an `INSERT <https://docs.sqream.com/en/latest/reference/sql/sql_statements/dml_commands/insert.html#insert>`_ statement for the selected table in the editing area.
   * - Delete statement
     - Generates a `DELETE <https://docs.sqream.com/en/latest/reference/sql/sql_statements/dml_commands/delete.html#delete>`_ statement for the selected table in the editing area.
   * - Create Table As statement
     - Generates a `CREATE TABLE AS <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/create_table_as.html#create-table-as>`_ statement for the selected table in the editing area.	 
   * - Rename statement
     - Generates an `RENAME TABLE AS <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/rename_table.html#rename-table>`_ statement for renaming the selected table in the editing area.
   * - Adding column statement
     - Generates an `ADD COLUMN <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/add_column.html#add-column>`_ statement for adding columns to the selected table in the editing area.
   * - Truncate table statement
     - Generates a `TRUNCATE_IF_EXISTS <https://docs.sqream.com/en/latest/reference/sql/sql_statements/dml_commands/truncate_if_exists.html#truncate>`_ statement for the selected table in the editing area.
   * - Drop table statement
     - Generates a ``DROP`` statement for the selected object in the editing area.
   * - Table DDL
     - Generates a DDL statement for the selected object in the editing area. To get the entire database DDL, click the |icon-ddl-edit| icon next to the database name in the tree root. See also  `Seeing System Objects as DDL <https://docs.sqream.com/en/latest/guides/features/viewing_system_objects_as_ddl.html#seeing-system-objects-as-sql>`_.
   * - DDL Optimizer
     - The DDL Optimizer lets you analyze database tables and recommends possible optimizations. For more information, see the `Optimization and Best Practices <https://docs.sqream.com/en/latest/guides/operations/optimization_best_practices.html#sql-best-practices>`_ guide.
	 
	 
	 


Using the DDL Optimizer
************
As described in the previous table, you can access the DDL Optimizer by clicking the **additional options icon** and selecting **DDL Optimizer**.

The following image shows the DDL Optimizer screen:

.. image:: /_static/images/studio_editor_ddl_optimizer.5.3.0.png

The following table describes the DDL Optimizer screen:

.. list-table::
   :widths: 10 20 70
   :header-rows: 1  
   
   * - No.
     - Element
     - Description
   * - 1
     - Column area
     - Shows the column **names** and **column types** from the selected table. You can scroll down or to the right/left for long column lists.
   * - 2
     - Optimization area
     - Shows the following:
	   
	   * The number of rows to sample as the basis for running an optimization.
	   * The default setting when running an optimization (1,000,000). This is also the overhead threshold used when analyzing ``VARCHAR`` fields.
	   * The default percent buffer to add to ``VARCHAR`` lengths (10%). Attempts to determine field nullability.
   * - 3
     - Run Optimizer
     - Starts the optimization process.

Clicking **Run Optimizer** adds a tab to the Statement panel showing the optimized results of the selected object. The figure below shows the **calcs Optimized** tab for the optimized **calcs** table.

.. image:: /_static/images/studio_optimized_5.3.0.png




:ref:`Back to top<top>`

.. _system_queries_tab:


System Queries
^^^^^^^^^^^^^^^^^^^^^^^
The Editor includes the following system query types:

* **Catalog queries** - used for analyzing table compression rates, users and permissions, etc.
* **Admin queries** - Queries useful for SQream database management.

Clicking an item pastes the query into the Statement pane.

.. image:: /_static/images/studio_editor_catalog_query_databases_5.3.0.png

You can undo your previous operation by pressing **Ctrl + Z**.

:ref:`Back to Editor<editor_top>`

.. _studio_editor_statement_area:

Statement Pane
----------------

The multi-tabbed statement area is used for writing queries and statements, and is used in tandem with the toolbar.


.. image:: /_static/images/studio_editor_statement_5.3.0.png

When writing and executing statements, you must first select a database from the **Database** dropdown menu in the toolbar.

.. image:: /_static/images/select_database_from_toolbar_5.3.0.png

When you execute a statement, it passes through a series of statuses until completing. Knowing the status helps you with statement maintenance. The statuses are shown in the **Results panel**.

.. image:: /_static/images/statement_status.png

The following table shows the statement statuses:
	 
.. list-table::
   :widths: 45 160
   :header-rows: 1  
   
   * - Status
     - Description
   * - Pending
     - The statement is pending.
   * - In queue
     - The statement is waiting for execution.
   * - Initializing
     - The statement has entered execution checks.
   * - Executing
     - The statement is executing.
   * - Statement stopped
     - The statement has been stopped.
	 
You can add and name new tabs for each statement that you need to execute, and Studio preserves your created tabs when you switch between databases.

.. image:: /_static/images/switching_between_databases_5.3.0.png

You can add new tabs by clicking |icon-plus| , which creates a new tab to the right with a default name of SQL and an increasing number. This helps you keep track of your statements.

.. image:: /_static/images/statement_pane_adding_statement_5.3.0.png

You can also rename the default tab name by double-clicking it and typing a new name.

.. image:: /_static/images/statement_pane_renaming_statement_tab_5.3.0.png



You can write multiple statements in tandem in the same tab by separating them with semicolons (``;``):



If too many tabs to fit into the Statement Pane are open at the same time, the tab arrows are displayed. You can scroll through the tabs by clicking |icon-left| or |icon-right|, and close tabs by clicking |icon-close|. You can also close all tabs at once by clicking **Close all** located to the right of the tabs.

.. tip:: If this is your first time with SQream DB, see `First steps with SQream DB <https://docs.sqream.com/en/latest/first_steps.html#first-steps>`_.


.. Keyboard shortcuts
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. :kbd:`Ctrl` +: kbd:`Enter` - Execute all queries in the statement area, or just the highlighted part of the query.

.. :kbd:`Ctrl` + :kbd:`Space` - Auto-complete the current keyword

.. :kbd:`Ctrl` + :kbd:`↑` - Switch to next tab.

.. :kbd:`Ctrl` + :kbd:`↓` - Switch to previous tab

.. _studio_editor_results:

:ref:`Back to Editor<editor_top>`


Results Panel
------------------------------------
The results pane shows query results and execution information. By default, only the first 10,000 results are returned, although you can modify this from the :ref:`studio_editor_toolbar`, as described above.

.. image:: /_static/images/studio_editor_results_5053.png

By default, executing several statements together opens a separate results tab for each statement. Executing statements together executes them serially, and any failed statement cancels all subsequent executions.

The following figure shows the main functions available from the Results panel:

.. image:: /_static/images/studio_results_view_pane_5053.png

The following is a brief description of the elements on the Results panel views:

.. list-table::
   :widths: 10 34 56
   :header-rows: 1   
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Results view<results_view>`
     - Lets you view search query results. For more information on running parallel statements, see :ref:`Running Parallel Statements<running_parallel_statements>`
   * - 2
     - :ref:`Execution Details view<execution_details_view>`
     - Lets you view execution details, such as statement ID, number of rows, and averge number of rows in chunk. 
   * - 3
     - :ref:`SQL view<sql_view>`
     - Lets you see the SQL view.
   * - 4
     - :ref:`Save results to clipboard<save_results_to_clipboard>`
     - Lets you save your search results to the clipboard to paste into another text editor.
   * - 5
     - :ref:`Save results to local file<save_results_to_local_file>`
     - Lets you save your search query results to a local file.


	 

.. _results_view:


	 
Results View
^^^^^^^^^^^^
The following figure shows the Results view:

.. image:: /_static/images/studio_results_pane_5053.png

The following is a brief description of the Results view:

.. list-table::
   :widths: 10 90
   :header-rows: 1   
   
   * - No.
     - Element
   * - 1
     - Lets you switch between tabs. 
   * - 2
     - Lets you close all tabs.  You can also close tabs by clicking |icon-close|.
   * - 3
     - Lets you scroll between tabs if too many result tabs are open to fit in the panel. Click |icon-left| or |icon-right| to scroll through the tab listings. 
   * - 4
     - Lets you keep each new statement that you execute in a separate tab. When **Keep tabs** is disabled, each new statement you execute clears all existing results.
   * - 5
     - Lets you sort column results.
   * - 6
     - Lets you view the amount of time (in seconds) taken for a query to finish executing.
	 

.. _running_parallel_statements:

Running Parallel Statements
^^^^^^^^^^^^
While Studio's default functionality is to open a new tab for each executed statement, Studio supports running parallel statements in one statement tab. Running parallel statements requires using macros and is useful for advanced users.

The following shows the syntax for running parallel statements:

.. code-block:: console
     
   $ @@ parallel
   $ $$
   $ select 1;
   $ select 2;
   $ select 3;
   $ $$
   
The following figure shows the parallel statement syntax in the Editor:

.. image:: /_static/images/running_parallel_statements.png

.. _execution_details_view:

Execution Details View
^^^^^^^^^^^^
The **Execution Details** view lets you view a query’s execution plan for monitoring purposes. Most importantly, the Execution Details view highlights rows based on how long they ran relative to the entire query. This can be seen in the **timeSum** column as follows:

* **Rows highlighted red** - longest runtime
* **Rows highlighted orange** - medium runtime
* **Rows highlighted yellow** - shortest runtime

.. image:: /_static/images/execution_details_view_3.png



.. _sql_view:

SQL View
^^^^^^^^^^^^
The SQL View panel allows you to more easily view certain queries, such as a long string that appears on one line. The SQL View makes it easier to see by wrapping it so that you can see the entire string at once. It also reformats and organizes query syntax entered in the Statement panel for more easily locating particular segments of your queries. The SQL View is identical to the **Format SQL** feature in the Toolbar, allowing you to retain your originally constructed query while viewing a more intuititively structured snapshot of it.

The following figure shows the SQL view:

.. image:: /_static/images/sql_view_5.0.3.png

.. _save_results_to_clipboard:

Saving Results to the Clipboard
^^^^^^^^^^^^
The **Save results to clipboard** function lets you save your results to the clipboard to paste into another text editor or into Excel for further analysis.

.. image:: /_static/images/studio_editor_save_result_to_clipboard_5.3.0.png

.. _save_results_to_local_file:

Saving Results to a Local File
^^^^^^^^^^^^
The **Save results to local file** functions lets you save your search query results to a local file.

Clicking **Save results to local file** downloads the contents of the Results panel to an Excel sheet. You can then use copy and paste this content into other editors as needed.

.. image:: /_static/images/studio_editor_save_results_to_local_file_5.3.0.png

The following figure shows the contents of the Results panel downloaded to an Excel sheet:

.. image:: /_static/images/studio_editor_save_result_to_clipboard_excel_5.3.0.png



Analyzing the Results
----------------------------

When results are produced, a :kbd:`Generate CREATE statement` button will appear.
Clicking the button creates a new tab with an optimized :ref:`create_table` statement, and an :ref:`insert` statement to copy the data to the new table.

.. _logs:

.. _logs_top:

:ref:`Back to Editor<editor_top>`

Logs
============
The following figure shows the **Logs** screen.

.. image:: /_static/images/studio_logs_main_screen_5.3.0.png

The following is a brief description of the elements on the Results panel views:

.. list-table::
   :widths: 10 15 75
   :header-rows: 1   
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Filter<filter>`
     - Lets you filter the data shown in the table. 
   * - 2
     - :ref:`Queries<queries>`
     - Shows basic query information, such as query number and the time the query was run. 
   * - 3
     - :ref:`Sessions<sessions>`
     - Shows basic session information, such as session ID and user name.
   * - 4
     - :ref:`System<system>`
     - Shows all system logs.
   * - 5
     -  :ref:`Log lines<log_lines>`
     - Shows the total amount of log lines.


.. _filter:

Filter Area
-------------

From the Logs tab, from the **FILTERS** area you can also apply the **TIMESPAN**, **ONLY ERRORS**, and additional filters (**Add**). The **Timespan** filter lets you select a timespan. The **Only Errors** toggle button lets you show all queries, or only queries that generated errors. The **Add** button lets you add additional filters to the data shown in the table. The **Filter** button applies the selected filter(s).
	 
.. image:: /_static/images/logs_queries_filters_5.3.0.png

Some filters require you to type text to define the filter.

.. image:: /_static/images/logs_filters_5.3.0.png

Other filters require you to select an item from a dropdown menu.

.. image:: /_static/images/logs_filters_2_5.3.0.png

You can also export a record of all of your currently filtered logs in Excel format by clicking **Download**.

.. image:: /_static/images/logs_download_5.3.0.png

.. _queries:

:ref:`Back to Logs<logs_top>`


Queries
----------
Clicking **Queries** displays the query data table and is used for viewing and keeping track of queries that you have run. The number at the top indicates the amount of queries that have been run.

.. image:: /_static/images/logs_queries_5.3.0.png

From here you can see and sort by the following:

* Query ID
* Start time
* Query
* Compilation duration
* Execution duration
* Total duration
* Details (execution details, error details, successful query details)

In the Query table, you can click on the **Statement ID** and **Query** items to set them as your filters.

The following figure shows the **Details** options:

.. image:: /_static/images/logs_queries_details_5.3.0.png

Clicking one of the details options shows a more detailed explanation of the query, such as the error example below:

.. image:: /_static/images/logs_queries_error_explanation_5.3.0.png

:ref:`Back to Logs<logs_top>`

.. _sessions:

Sessions
----------

Clicking **Sessions** displays the sessions table and is used for viewing activity that has occurred during your sessions. The number at the top indicates the amount of sessions that have occurred.

.. image:: /_static/images/logs_sessions_5.3.0.png

From here you can see and sort by the following:

* Timestamp
* Connection ID
* Username
* Client IP
* Login (Success or Failed)
* Duration (of session)
* Configuration Changes

In the Sessions table, you can click on the **Timestamp**, **Connection ID**, and **Username** items to set them as your filters.

:ref:`Back to Logs<logs_top>`


.. _system:

System
----------
Clicking **System** displays the system table and is used for viewing all system logs. The number at the top indicates the amount of sessions that have occurred. Because system logs occur less frequently than queries and sessions, you may need to increase the filter timespan for the table to display any system logs.

.. image:: /_static/images/logs_system_5.3.0.png

From here you can see and sort by the following:

* Timestamp
* Log type
* Message

In the **SYSTEMS** table, you can click on the **Timestamp** and **Log type** items to set them as your filters. You can also click on an item in the **Message** column to show more information about the message.

.. image:: /_static/images/logs_system_error_message_5.3.0.png

:ref:`Back to Logs<logs_top>`


.. _log_lines:

Log Lines
----------
Clicking **LOG LINES** used for viewing the total amount of log lines in a table. From here users can view a more granular breakdown of log information collected by Studio. The other tabs (QUERIES, SESSIONS, and SYSTEM) show a filtered form of the raw log lines. For example, the QUERIES tab shows an aggregation of several log lines.

.. image:: /_static/images/logs_log_lines_5.3.0.png

From here you can see and sort by the following:

* Timestamp
* Message level
* Worker hostname
* Worker port
* Connection ID
* Database name
* User name
* Statement ID

In the **LOG LINES** table, you can click on any of the items to set them as your filters.

:ref:`Back to Logs<logs_top>`

:ref:`Back to Editor<editor_top>`
