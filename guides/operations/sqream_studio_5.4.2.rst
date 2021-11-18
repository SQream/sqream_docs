.. _acceleration_studio_version_5.4.2:

****************************
SQream Acceleration Studio 5.4.2
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







Logging In to Studio
---------------
**To log in to SQream Studio:**

1. Open a browser to the host on **port 8080**.

   For example, if your machine IP address is ``192.168.0.100``, insert the IP address into the browser as shown below:

   .. code-block:: console

      $ http://192.168.0.100:8080

2. Fill in your SQream DB login credentials. These are the same credentials used for :ref:`sqream sql<sqream_sql_cli_reference>` or JDBC.

   When you sign in, the License Warning is displayed.

   
.. _top1_5.4.2:
   
   
   
   
   

Navigating Studio's Main Features
-------------
When you log in, you are automatically taken to the **Editor** screen. The Studio's main functions are displayed in the **Navigation** pane on the left side of the screen.


From here you can navigate between the main areas of the Studio:

.. list-table::
   :widths: 10 90
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Dashboard<studio_dashboard_5.4.2>`
     - Lets you monitor system health and manage queues and workers.
   * - :ref:`Editor<studio_editor_5.4.2>`
     - Lets you select databases, perform statement operations, and write and execute queries.   
   * - :ref:`Logs<logs_5.4.2>`
     - Lets you view usage logs.
   * - :ref:`Roles<roles_5.4.2>`
     - Lets you create users and manage user permissions.
   * - :ref:`Configuration<configuration_1_5.4.2>`
     - Lets you configure your instance of SQream.

By clicking the user icon, you can also use it for logging out and viewing the following:

* User information
* Connection type
* SQream version
* SQream Studio version
* License expiration date
* License storage capacity
* Log out



.. _back_to_dashboard_5.4.2:

.. _studio_dashboard_5.4.2:

Monitoring Workers and Services from the Dashboard
==============================
The **Dashboard** is used for the following:

* Monitoring system health.
* Viewing, monitoring, and adding defined service queues.
* Viewing and managing worker status and add workers.


You can only access the Dashboard if you signed in with a ``SUPERUSER`` role.

The following is a brief description of the Dashboard panels:

.. list-table::
   :widths: 10 25 65
   :header-rows: 1  
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Services panel<services_panel_5.4.2>`
     - Used for viewing and monitoring the defined service queues.
   * - 2
     - :ref:`Workers panel<workers_panel_5.4.2>`
     - Monitors system health and shows each Sqreamd worker running in the cluster.
   * - 3
     - :ref:`License information<license_information_5.4.2>`
     - Shows the remaining amount of days left on your license.
   

.. _data_storage_panel_5.4.2:



:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.2>`

.. _services_panel_5.4.2:

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

You can manage workers from the **Workers** panel. For more information about managing workers, see :ref:`Workers<workers_panel>`.

:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.2>`

.. _workers_panel_5.4.2:

Managing Workers from the Workers Panel
------------
From the **Workers** panel you can do the following:

* :ref:`View workers <view_workers_5.4.2>`
* :ref:`Add a worker to a service<add_worker_to_service_5.4.2>`
* :ref:`View a worker's active query information<view_worker_query_information_5.4.2>`
* :ref:`View a worker's execution plan<view_worker_execution_plan_5.4.2>`

.. _view_workers_5.4.2:

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

.. _add_worker_to_service_5.4.2:

Adding A Worker to A Service
^^^^^^^^^^^^^^^^^^^^^	 
You can add a worker to a service by clicking the **add** button. 



Clicking the **add** button shows the selected service's workers. You can add the selected worker to the service by clicking **Add Worker**. Adding a worker to a service does not break associations already made between that worker and other services.


.. _view_worker_query_information_5.4.2:

Viewing A Worker's Active Query Information
^^^^^^^^^^^^^^^^^^^^^	 
You can view a worker's active query information by clicking **Queries**, which displays them in the selected service.


Each statement shows the **query ID**, **status**, **service queue**, **elapsed time**, **execution time**, and **estimated completion status**. In addition, each statement can be stopped or expanded to show its execution plan and progress. For more information on viewing a statement's execution plan and progress, see :ref:`Viewing a Worker's Execution Plan <view_worker_execution_plan_5.4.2>` below.

Viewing A Worker's Host Utilization
^^^^^^^^^^^^^^^^^^^^^	 

While viewing a worker's query information, clicking the **down arrow** expands to show the host resource utilization.



The graphs show the resource utilization trends over time, and the **CPU memory** and **utilization** and the **GPU utilization** values on the right. You can hover over the graph to see more information about the activity at any point on the graph.

Error notifications related to statements are displayed as shown in the figure below, and you can hover over them for more information about the error. 


.. _view_worker_execution_plan_5.4.2:

Viewing a Worker's Execution Plan
^^^^^^^^^^^^^^^^^^^^^
	 
Clicking the ellipsis in a service shows the following additional options:

* **Stop Query** - stops the query.
* **Show Execution Plan** - shows the execution plan as a table. The columns in the **Show Execution Plan** table can be sorted.

For more information on the current query plan, see `SHOW_NODE_INFO <https://docs.sqream.com/en/latest/reference/sql/sql_statements/monitoring_commands/show_node_info.html#show-node-info>`_. For more information on checking active sessions across the cluster, see `SHOW_SERVER_STATUS <https://docs.sqream.com/en/latest/reference/sql/sql_statements/monitoring_commands/show_server_status.html>`_.

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
   
:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.2>`



.. _license_information_5.4.2:
   
License Information
----------------------
The license information section shows the following:

 * The amount of time in days remaining on the license.
 * The license storage capacity.
 
.. image:: /_static/images/license_storage_capacity.png

:ref:`Back to Monitoring Workers and Services from the Dashboard<back_to_dashboard_5.4.2>`

:ref:`Back to Navigating Studio’s Main Features<top1_5.4.2>`

.. _studio_editor_5.4.2:

.. _editor_top_5.4.2:

Executing Statements and Running Queries from the Editor
=================
The **Editor** is used for the following:

* Selecting an active database and executing queries.
* Performing statement-related operations and showing metadata.
* Executing pre-defined queries.
* Writing queries and statements and viewing query results.
	 
The following is a brief description of the Editor panels:


.. list-table::
   :widths: 10 34 56
   :header-rows: 1  
   
   * - No.
     - Element
     - Description
   * - 1
     - :ref:`Toolbar<studio_5.4.2_editor_toolbar>`
     - Used to select the active database you want to work on, limit the number of rows, save query, etc.
   * - 2
     - :ref:`Database Tree and System Queries panel<studio_5.4.2_editor_db_tree>`
     - Shows a heirarchy tree of databases, views, tables, and columns
   * - 3
     - :ref:`Statement panel<studio_5.4.2_editor_statement_area>`
     - Used for writing queries and statements
   * - 4
     - :ref:`Results panel<studio_5.4.2_editor_results>`
     - Shows query results and execution information.



.. _top_5.4.2:

.. _studio_5.4.2_editor_toolbar:

Executing Statements from the Toolbar
-------------
You can access the following from the Toolbar pane:

* **Database dropdown list** - select a database that you want to run statements on.

    ::

* **Service dropdown list** - select a service that you want to run statements on. The options in the service dropdown menu depend on the database you select from the **Database** dropdown list.

    ::

* **Execute** - lets you set which statements to execute. The **Execute** button toggles between **Execute** and **Stop**, and can be used to stop an active statement before it completes:

  * **Statements** - executes the statement at the location of the cursor.
  * **Selected** - executes only the highlighted text. This mode should be used when executing subqueries or sections of large queries (as long as they are valid SQLs).
  * **All** - executes all statements in a selected tab.
   
* **Format SQL** - Lets you reformat and reindent statements.

    ::

* **Download query** - Lets you download query text to your computer.

    ::

* **Open query** - Lets you upload query text from your computer.

    ::

* **Max Rows** - By default, the Editor fetches only the first 10,000 rows. You can modify this number by selecting an option from the **Max Rows** dropdown list. Note that setting a higher number may slow down your browser if the result is very large. This number is limited to 100,000 results. To see a higher number, you can save the results in a file or a table using the :ref:`create_table_as` command.


For more information on stopping active statements, see the :ref:`STOP_STATEMENT<stop_statement>` command.

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.2>`


.. _studio_5.4.2_editor_db_tree:

Performing Statement-Related Operations from the Database Tree
---------------
From the Database Tree you can perform statement-related operations and show metadata (such as a number indicating the amount of rows in the table).





The database object functions are used to perform the following:

* The **SELECT** statement - copies the selected table's **columns** into the Statement panel as ``SELECT`` parameters.  

   ::

* The **copy** feature |icon-copy| - copies the selected table's **name** into the Statement panel. 

   ::

* The **additional operations** |icon-dots| - displays the following additional options:
  




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
     - Generates a DDL statement for the selected object in the editing area. To get the entire database DDL, click the |icon-ddl-edit| icon next to the database name in the tree root. See `Seeing System Objects as DDL <https://docs.sqream.com/en/latest/guides/features/viewing_system_objects_as_ddl.html#seeing-system-objects-as-sql>`_.
   * - DDL Optimizer
     - The `DDL Optimizer <https://docs.sqream.com/en/latest/guides/operations/sqream_studio.html#using-the-ddl-optimizer DDL>`_  lets you analyze database tables and recommends possible optimizations.
	 
	 
	 


Optimizing Database Tables Using the DDL Optimizer
^^^^^^^^^^^^^^^^^^^^^
The **DDL Optimizer** tab analyzes database tables and recommends possible optimizations according to SQream's best practices.

As described in the previous table, you can access the DDL Optimizer by clicking the **additional options icon** and selecting **DDL Optimizer**.

The following table describes the DDL Optimizer screen:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Element
     - Description
   * - Column area
     - Shows the column **names** and **column types** from the selected table. You can scroll down or to the right/left for long column lists.
   * - Optimization area
     - Shows the number of rows to sample as the basis for running an optimization, the default setting (1,000,000) when running an optimization (this is also the overhead threshold used when analyzing ``VARCHAR`` fields),  and the default percent buffer to add to ``VARCHAR`` lengths (10%). Attempts to determine field nullability.
   * - Run Optimizer
     - Starts the optimization process.

Clicking **Run Optimizer** adds a tab to the Statement panel showing the optimized results of the selected object. The figure below shows the **calcs Optimized** tab for the optimized **calcs** table.

For more information, see `Optimization and Best Practices <https://docs.sqream.com/en/latest/guides/operations/optimization_best_practices.html>`_.




Executing Pre-Defined Queries from the System Queries Panel
---------------
The **System Queries** panel lets you execute pre-defined queries and includes the following system query types:

* **Catalog queries** - used for analyzing table compression rates, users and permissions, etc.
    
	::
	
* **Admin queries** - queries related to available  (describe the functionality in a general way). Queries useful for SQream database management:





Clicking an item pastes the query into the Statement pane, and you can undo a previous operation by pressing **Ctrl + Z**.


.. _studio_5.4.2_editor_statement_area:

Writing Statements and Queries from the Statement Panel
----------------
The multi-tabbed statement area is used for writing queries and statements, and is used in tandem with the toolbar. When writing and executing statements, you must first select a database from the **Database** dropdown menu in the toolbar. When you execute a statement, it passes through a series of statuses until completing. Knowing the status helps you with statement maintenance, and the statuses are shown in the **Results panel**.

The auto-complete feature assists you when writing statements by suggesting statement options.

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
	 
You can add and name new tabs for each statement that you need to execute, and Studio preserves your created tabs when you switch between databases. You can add new tabs by clicking |icon-plus| , which creates a new tab to the right with a default name of SQL and an increasing number. This helps you keep track of your statements.



You can also rename the default tab name by double-clicking it and typing a new name and write multiple statements in tandem in the same tab by separating them with semicolons (``;``).If too many tabs to fit into the Statement Pane are open at the same time, the tab arrows are displayed. You can scroll through the tabs by clicking |icon-left| or |icon-right|, and close tabs by clicking |icon-close|. You can also close all tabs at once by clicking **Close all** located to the right of the tabs.

.. tip:: If this is your first time using SQream, see `Getting Started <https://docs.sqream.com/en/latest/first_steps.html#first-steps>`_.


.. Keyboard shortcuts
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. :kbd:`Ctrl` +: kbd:`Enter` - Execute all queries in the statement area, or just the highlighted part of the query.

.. :kbd:`Ctrl` + :kbd:`Space` - Auto-complete the current keyword

.. :kbd:`Ctrl` + :kbd:`↑` - Switch to next tab.

.. :kbd:`Ctrl` + :kbd:`↓` - Switch to previous tab

.. _studio_editor_results_5.4.2:

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.2>`

.. _studio_5.4.2_editor_results:

Viewing Statement and Query Results from the Results Panel
------------------------------------
The results panel shows statment and query results. By default, only the first 10,000 results are returned, although you can modify this from the :ref:`studio_editor_toolbar`, as described above. By default, executing several statements together opens a separate results tab for each statement. Executing statements together executes them serially, and any failed statement cancels all subsequent executions.


The following is a brief description of the Results panel views:

.. list-table::
   :widths: 45 160
   :header-rows: 1  
   
   * - Element
     - Description
   * - :ref:`Results view<results_view_5.4.2>`
     - Lets you view search query results.
   * - :ref:`Execution Details view<execution_details_view_5.4.2>`
     - Lets you view execution details, such as statement ID, number of rows, and averge number of rows in chunk.
   * - :ref:`SQL view<sql_view_5.4.2>`
     - Lets you see the SQL view.
   * - :ref:`Save results to clipboard<save_results_to_clipboard_5.4.2>`
     - Lets you save your search results to the clipboard to paste into another text editor.
   * - :ref:`Save results to local file<save_results_to_local_file_5.4.2>`
     - Lets you save your search query results to a local file.

.. _results_view_5.4.2:

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.2>`

	 
Searching Query Results in the Results View
^^^^^^^^^^^^
The **Results view** lets you view search query results.

From this view you can also do the following:

* View the amount of time (in seconds) taken for a query to finish executing.
* Switch and scroll between tabs.
* Close all tabs at once.
* Enable keeping tabs by selecting **Keep tabs**.
* Sort column results.

In the Results view you can also run parallel statements, as described in **Running Parallel Statements** below.

.. _running_parallel_statements_5.4.2:

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
   


.. _execution_details_view_5.4.2:

Execution Details View
^^^^^^^^^^^^
The **Execution Details** view lets you view a query’s execution plan for monitoring purposes. The Execution Details view highlights rows based on how long they ran relative to the entire query.

This can be seen in the **timeSum** column as follows:

* **Rows highlighted red** - longest runtime
* **Rows highlighted orange** - medium runtime
* **Rows highlighted yellow** - shortest runtime

You can download the execution plan table in .csv format by clicking the download arrow in the upper-right corner.

.. _sql_view_5.4.2:

Viewing Wrapped Strings in the SQL View
^^^^^^^^^^^^
The SQL View panel allows you to more easily view certain queries, such as a long string that appears on one line. The SQL View makes it easier to see by wrapping it so that you can see the entire string at once. It also reformats and organizes query syntax entered in the Statement panel for more easily locating particular segments of your queries. The SQL View is identical to the **Format SQL** feature in the Toolbar, allowing you to retain your originally constructed query while viewing a more intuititively structured snapshot of it.



.. _save_results_to_clipboard_5.4.2:

Saving Results to the Clipboard
^^^^^^^^^^^^
The **Save results to clipboard** function lets you save your results to the clipboard to paste into another text editor or into Excel for further analysis.


.. _save_results_to_local_file_5.4.2:

Saving Results to a Local File
^^^^^^^^^^^^
The **Save results to local file** functions lets you save your search query results to a local file. Clicking **Save results to local file** downloads the contents of the Results panel to an Excel sheet. You can then use copy and paste this content into other editors as needed.

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.2>`


Analyzing Results
----------------------------

When results are produced, a **Generate CREATE statement** button is displayed. Clicking this button creates a new tab with an optimized :ref:`create_table` statement, and an :ref:`insert` statement to copy the data to the new table.

.. _logs_5.4.2:

.. _logs_top_5.4.2:

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.2>`

:ref:`Back to Navigating Studio’s Main Features<top1_5.4.2>`

Viewing Logs
============
The **Logs** screen is used for viewing logs and includes the following elements:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Filter area<filter_5.4.2>`
     - Lets you filter the data shown in the table. 
   * - :ref:`Query tab<queries_5.4.2>`
     - Shows basic query information logs, such as query number and the time the query was run. 
   * - :ref:`Session tab<sessions_5.4.2>`
     - Shows basic session information logs, such as session ID and user name.
   * - :ref:`System tab<system_5.4.2>`
     - Shows all system logs.
   * - :ref:`Log lines tab<log_lines_5.4.2>`
     - Shows the total amount of log lines.


.. _filter_5.4.2:

Filtering Table Data
-------------
From the Logs tab, from the **FILTERS** area you can also apply the **TIMESPAN**, **ONLY ERRORS**, and additional filters (**Add**). The **Timespan** filter lets you select a timespan. The **Only Errors** toggle button lets you show all queries, or only queries that generated errors. The **Add** button lets you add additional filters to the data shown in the table. The **Filter** button applies the selected filter(s).
	 



Other filters require you to select an item from a dropdown menu:

* INFO
* WARNING
* ERROR
* FATAL
* SYSTEM

You can also export a record of all of your currently filtered logs in Excel format by clicking **Download** located above the Filter area.

.. _queries_5.4.2:

:ref:`Back to Viewing Logs<logs_top_5.4.2>`


Viewing Query Logs
----------
The **QUERIES** log area shows basic query information, such as query number and the time the query was run. The number next to the title indicates the amount of queries that have been run.

From the Queries area you can see and sort by the following:

* Query ID
* Start time
* Query
* Compilation duration
* Execution duration
* Total duration
* Details (execution details, error details, successful query details)

In the Queries table, you can click on the **Statement ID** and **Query** items to set them as your filters. In the **Details** column you can also access additional details by clicking one of the **Details** options for a more detailed explanation of the query.

:ref:`Back to Viewing Logs<logs_top_5.4.2>`

.. _sessions_5.4.2:

Viewing Session Logs
----------
The **SESSIONS** tab shows the sessions log table and is used for viewing activity that has occurred during your sessions. The number at the top indicates the amount of sessions that have occurred.

From here you can see and sort by the following:

* Timestamp
* Connection ID
* Username
* Client IP
* Login (Success or Failed)
* Duration (of session)
* Configuration Changes

In the Sessions table, you can click on the **Timestamp**, **Connection ID**, and **Username** items to set them as your filters.

:ref:`Back to Viewing Logs<logs_top_5.4.2>`

.. _system_5.4.2:

Viewing System Logs
----------
The **SYSTEM** tab shows the system log table and is used for viewing all system logs. The number at the top indicates the amount of sessions that have occurred. Because system logs occur less frequently than queries and sessions, you may need to increase the filter timespan for the table to display any system logs.

From here you can see and sort by the following:

* Timestamp
* Log type
* Message

In the Systems table, you can click on the **Timestamp** and **Log type** items to set them as your filters. In the **Message** column, you can also click on an item to show more information about the message.

:ref:`Back to Viewing Logs<logs_top_5.4.2>`

.. _log_lines_5.4.2:

Viewing All Log Lines
----------
The **LOG LINES** tab is used for viewing the total amount of log lines in a table. From here users can view a more granular breakdown of log information collected by Studio. The other tabs (QUERIES, SESSIONS, and SYSTEM) show a filtered form of the raw log lines. For example, the QUERIES tab shows an aggregation of several log lines.

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

:ref:`Back to Viewing Logs<logs_top_5.4.2>`

:ref:`Back to Navigating Studio’s Main Features<top1_5.4.2>`

.. _roles_5.4.2:


Creating, Assigning, and Managing Roles and Permissions
============
Overview
---------------
In the **Roles** area you can create and assign roles and manage user permissions. 

The **Type** column displays one of the following assigned role types:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Role Type
     - Description
   * - Groups
     - Roles with no users.
   * - Enabled users
     - Users with log-in permissions and a password.
   * - Disabled users
     - Users with log-in permissions and with a disabled password. An admin may disable a user's password permissions to temporary disable access to the system.

.. note:: If you disable a password, when you enable it you have to create a new one.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.2>`


Viewing Information About a Role
--------------------
Clicking a role in the roles table displays the following information:

 * **Parent Roles** - displays the parent roles of the selected role. Roles inherit all roles assigned to the parent.
 
    ::
   
 * **Members** - displays all members that the role has been assigned to. The arrow indicates the roles that the role has inherited. Hovering over a member displays the roles that the role is inherited from.

    ::
   
 * **Permissions** - displays the role's permissions. The arrow indicates the permissions that the role has inherited. Hovering over a permission displays the roles that the permission is inherited from.
 
:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.2>`


Creating a New Role
--------------------
You can create a new role by clicking **New Role**.


   
An admin creates a **user** by granting login permissions and a password to a role. Each role is defined by a set of permissions. An admin can also group several roles together to form a **group** to manage them simultaneously. For example, permissions can be granted to or revoked on a group level.

Clicking **New Role** lets you do the following:

 * Add and assign a role name (required)
 * Enable or disable log-in permissions for the role.
 * Set a password.
 * Assign or delete parent roles.
 * Add or delete permissions.
 * Grant the selected user with superuser permissions.
 
From the New Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field. From the New Role panel you can also search and scroll through the permissions. In the **Search** field you can use the **and** operator to search for strings that fulfill multiple criteria.

When adding a new role, you must select the **Enable login for this role** and **Has password** check boxes.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.2>`


Editing a Role
--------------------
Once you've created a role, clicking the **Edit Role** button lets you do the following:

 * Edit the role name.
 * Enable or disable log-in permissions.
 * Set a password.
 * Assign or delete parent roles.
 * Assign a role **administrator** permissions.
 * Add or delete permissions.
 * Grant the selected user with superuser permissions.

From the Edit Role panel you view directly and indirectly (or inherited) granted permissions. Disabled permissions have no connect permissions for the referenced database and are displayed in gray text. You can add or remove permissions from the **Add permissions** field. From the Edit Role panel you can also search and scroll through the permissions. In the **Search** field you can use the **and** operator to search for strings that fulfill multiple criteria.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.2>`


Deleting a Role
-----------------
Clicking the **delete** icon displays a confirmation message with the amount of users and groups that will be impacted by deleting the role.

:ref:`Back to Creating, Assigning, and Managing Roles and Permissions<roles_5.4.2>`

:ref:`Back to Navigating Studio’s Main Features<top1_5.4.2>`


.. _configuration_5.4.2:

.. _configuration_1_5.4.2:





Configuring Your Instance of SQream
==============================
The **Configuration** section lets you edit parameters from one centralized location. While you can edit these parameters from the **worker configuration file (config.json)** or from your CLI, you can also modify them in Studio in an easy-to-use format.

Configuring your instance of SQream in Studio is session-based, which enables you to edit parameters per session on your own device. 
Because session-based configurations are not persistent and are deleted when your session ends, you can edit your required parameters while avoiding conflicts between parameters edited on different devices at different points in time.



Editing Your Parameters
-------------------------------
When configuring your instance of SQream in Studio you can edit parameters for the **Generic** and **Admin** parameters only.

Studio includes two types of parameters: toggle switches, such as **flipJoinOrder**, and text fields, such as **logSysLevel**. After editing a parameter, you can reset each one to its previous value or to its default value individually, or revert all parameters to their default setting simultaneously. Note that you must click **Save** to save your configurations.

You can hover over the **information** icon located on each parameter to read a short description of its behavior.

:ref:`Back to Configuring Your Instance of SQream<configuration_1_5.4.2>`

.. _configuration_5.4.2:





Exporting and Importing Configuration Files
-------------------------
You can also export and import your configuration settings into a .json file. This allows you to easily edit your parameters and to share this file with other users if required.

For more information about configuring your instance of SQream, see `Configuration <https://docs.sqream.com/en/latest/guides/operations/configuration.html>`_.


:ref:`Back to Configuring Your Instance of SQream<configuration_1_5.4.2>`

:ref:`Back to Navigating Studio’s Main Features<top1_5.4.2>`
