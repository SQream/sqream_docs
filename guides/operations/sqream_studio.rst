.. _sqream_studio:

****************************
SQream Acceleration Studio
****************************

The studio is a web-based client for use with SQream DB. 

It can be used to run statements, manage roles and permissions, and manage a SQream DB cluster.

.. contents:: In this topic:
   :local:


Setting up and starting the studio
====================================================

The studio is included with all :ref:`dockerized installations of SQream DB<installing_sqream_db_docker>`.

.. todo: How to start it?
.. You can start the studio using :ref:`sqream-console<start_editor>`:
.. .. code-block:: console
.. 
..    $ ./sqream-console
..   sqream-console> sqream editor --start
..    access sqream statement editor through Chrome http://192.168.0.100:3000

When starting the studio, it listens on the local machine, on port 8080.

Logging in
===================

Open a browser to the host, on port 8080. (e.g. If the machine is ``196.168.0.100``, navigate to http://192.168.0.100:8080) .

Fill in your login details for SQream DB. These are the same credentials you might use when using :ref:`sqream sql<sqream_sql_cli_reference>` or JDBC.

.. image:: /_static/images/studio_login.png

Your user level in SQream DB changes what you see.

* ``SUPERUSER`` levels have full access to the studio, including the :ref:`Dashboard<studio_dashboard>`.

* All users have access to the :ref:`Editor<studio_editor>`, and can only see databases they have permissions for.

.. _studio_editor:

Statement editor
=================

Familiarizing yourself with the editor
-----------------------------------------

The editor is built up of main panes.

.. image:: /_static/images/studio_editor_familiarize.png

* :ref:`Toolbar<studio_editor_toolbar>` - used to select the active database you want to work on, limit the number of rows, save query, etc.

* :ref:`Statement area<studio_editor_statement_area>` - The statement area is a multi-tab text editor where you write SQL statements. Each tab can connect to a different database.

* :ref:`Results<studio_editor_results>` - Results from a query will populate here. This is where you can copy or save query results, or show query execution details.

* :ref:`Database tree<studio_editor_db_tree>` - contains a heirarchy tree of databases, views, tables, and columns. Can be used to navigate and perform some table operations.

See more about each pane below:

Navigation and user information
=======
The following is a brief description of each pane:

.. list-table::
   :widths: 1 23 76
   :header-rows: 1
   
   * - No.
     - Element
     - Function
   * - 1
     - :ref:`Navigation pane<navigation>`
     - Lets you access the Dashboard, Editor, Logs, and shows user information.
   * - 2
     - :ref:`Toolbar pane<studio_editor_toolbar>`
     - Lets you select the active database and service to manage queries.
   * - 3
     - :ref:`Statement pane<studio_editor_statement_area>`
     - Lets you write SQL statements.
   * - 4
     - :ref:`Results pane<studio_editor_results>`
     - Lets you see the results generated from queries.
   * - 5
     - :ref:`Database tree pane<studio_editor_db_tree>`
     - Lets you see a heirarchical tree of databases, views, tables, and columns, and can be used to navigate and perform table operations.

.. _navigation:



Navigation Pane
-------------------------------------

The user information menu is located on the bottom left portion of the screen |icon-user|.

.. image:: /_static/images/studio_user_info.png


The menu contains information about the currently signed-in user, as well as version information.

* User information
* Connection type
* SQream version
* SQream Studio version
* Logging out

.. image:: /_static/images/studio_user_info_5053.png

You can sign out of the current user at any point, by selecting :kbd:`Logout` in the user menu.


.. _studio_editor_toolbar:

Toolbar Pane
-------------

In the toolbar, you can perform the folllowing operations (from left to right):

.. image:: /_static/images/studio_editor_toolbar.png

* Database dropdown - Select the database you want to the statements to run on.

* Queue - specify which service queue the statement should run in

* :kbd:`⯈ Execute` / :kbd:`STOP` - Use the :kbd:`⯈ EXECUTE` button to execute the statement in the Editor pane. When a statement is running, the button changes to :kbd:`STOP`, and can be used to :ref:`stop the active statement<stop_statement>`.

* :kbd:`Format SQL` - Reformats and reindents the statement

* :kbd:`Download query` - save query text to your computer
=======
* **Execute**:

  * **Statements** - executes the statement at the location of the cursor.
  * **Selected** - executes only the highlighted text. This mode should be used when executing subqueries or sections of large queries (as long as they are valid SQLs).
  * **All** - executes all statements in a selected tab.

  The **Execute** button toggles between **Execute** and **Stop**, and can be used to stop an active statement before it completes.   

* :kbd:`Open query` - load query text from your computer

* Max. Rows - By default, the editor will only fetch the first 1000 rows. Click the number to edit. Click outside the number area to save. Setting a higher limit can slow down your browser if the result set is very large. This number is limited to 100000 results (To see more results, consider saving the results to a file or a table with :ref:`create_table_as`).
=======
* **Download query** - Lets you download query text to your computer into a new editor tab.

* **Open query** - Lets you upload query text from your computer.

* **Max Rows** - By default, the Editor fetches only the first 1,000 rows. You can modify this number by selecting an option from the **Max Rows** dropdown list. Note that setting a higher number may slow down your browser if the result is very large. This number is limited to 100,000 results.



Keyboard Shortcuts for Executing Queries
~~~~~~~~~~~~~~~~~~
You can use the following keyboard shortcuts when executing queries:

:kbd:`Ctrl` + :kbd:`Enter` - Executes all queries in the statement pane, or only the highlighted part of a query.

:kbd:`Ctrl` + :kbd:`Space` - Auto-completes the keyword that you are typing.

:kbd:`Ctrl` + :kbd:`↑` - Switches to next tab.

:kbd:`Ctrl` + :kbd:`↓` - Switches to previous tab.
   
Related Information
~~~~~~~~~~~~~~~~~~~~
The following table shows commands related to running statements:

.. list-table::
   :widths: 50 50
   :header-rows: 1
   
   * - Command
     - Function
   * - Stop active statements
     - :ref:`STOP_STATEMENT<stop_statement>`
   * - Save row results in a file or table
     - :ref:`create_table_as`


.. _studio_editor_statement_area:

Statement area
----------------

The multi-tabbed statement pane is used for writing queries and statements. You can write multiple statements in tandem in the same tab by separating them with semicolons (``;``):




You can add tabs for separate statements to different databases by clicking |icon-plus|. This opens a new tab to the right with the default name **SQL <increasing number>**.

.. image:: /_static/images/statement_area_5.0.0.png



You can rename tabs to help you keep track of your statements by double-clicking their default name and typing a new one:

.. image:: /_static/images/studio_editor_statement_rename_5053.png


If too many tabs to fit into the Statement Pane are open at the same time, the tab arrows are displayed. You can scroll through the tabs by clicking |icon-left| or |icon-right|, and close tabs by clicking |icon-close|. You can also close all tabs at once by clicking **Close all** located to the right of the tabs.


.. tip:: If this is your first time with SQream DB, see our :ref:`first steps guide<first_steps>`.



.. _studio_editor_results:



.. _top:

Results Pane
-------------

This section describes the following:

* :ref:`Using the Results pane<using_results_pane>`
* :ref:`The Results view<results_view>`
* :ref:`The Scripts Log view<scripts_log_view>`
* :ref:`The SQL view<sql_view>`
* :ref:`Saving results to a file or clipboard<saving_results_to_file>`

.. _using_results_pane:

Using the Results Pane
~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Results Pane** shows query results and execution information. By default, only the first 10,000 results are returned, which you can modify from the :ref:`studio_editor_toolbar`.

.. image:: /_static/images/studio_editor_results.png

By default, executing several statements in tandem opens a separate results tab for each statement.



Statements are executed serially, and if a statement fails, all subsequent statements are cancelled.

The |keep-tabs| switch lets you do the following when executing new statements:

* **When enabled** - creates a new tab for each statement.
* **When disabled** - clears existing results.

You can rename tabs to help you keep track of your results by double-clicking their default name and typing a new one. The default name for each result is the statement value and the time that the result was generated:

.. image:: /_static/images/studio_editor_results_rename_5053.png


   
An incorrectly built statement generates a results error:  
  
.. image:: /_static/images/studio_editor_results_error_5053.png

If too many tabs to fit into the Results Pane are open at the same time, the tab arrows are displayed. You can scroll through the tabs by clicking |icon-left| or |icon-right|, and close tabs by clicking |icon-close|. You can also close all results tabs at once by clicking **Close all** located to the right of the tabs.

Clicking **Close all** displays the following message:

.. image:: /_static/images/studio_editor_results_close_all_5053.png

:ref:`Back to top<top>`

.. contents:: In this topic:
   :local:

.. _results_view:

The Results View
-------------------------

After the results have appeared, sort them by clicking the column name.

:ref:`Back to top<top>`


.. _scripts_log_view:

The Scripts Log View
-----------------------------------

While a query is being execute, the elapsed time is tracked in seconds.

The :kbd:`Show Execution Details` button opens the query's :ref:`execution plan<show_node_info>`, for monitoring purposes.

:ref:`Back to top<top>`



   


.. _sql_view:
   
The SQL View
--------------------------------


:ref:`Back to top<top>`

   
.. _saving_results_to_file:

Saving Results to a File or the Clipboard
--------------------------------

Query results can be saved to a clipboard (for pasting into another text editor) or a local file.



.. _studio_editor_db_tree:

:ref:`Back to top<top>`

The Database Tree
---------------

The database tree shows the database objects (e.g. tables, columns, views), as well as some metadata like row counts.

It also contains a few predefined catalog queries for execution.

.. image:: /_static/images/studio_editor_db_tree.png

Each level contains a context menu relevant to that object, accessible via a right-click.

.. contents:: In this topic:
   :local:

System Queries
^^^^^^^^^^^^^^^^^^^^^^^

The studio editor comes with several predefined catalog queries that are useful for analysis of table compression rates, users and permissions, etc.

Clicking on the :kbd:`System queries` tab in the Tree section will show a list of pre-defined system queries.

Clicking on an item will paste the query into the editing area.


Filtering (searching) for objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the |icon-filter| filter icon by columns or tables opens an editable field that can be used for searching.

To remove the filter, click the icon again or select ❌.

Copying object names
^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the |icon-copy| icon will copy the object name

Generating SELECT statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the |icon-select| icon will generate a :ref:`select` query for the selected table in the editing area.

Generating an INSERT statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Insert statement` option under the :kbd:`⋮` menu generates an :ref:`insert` statement for the selected table in the editing area.

Generating a DELETE statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Delete statement` option under the :kbd:`⋮` menu generates a :ref:`delete` statement for the selected table in the editing area.

Generating a CREATE TABLE AS statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Create table as` option under the :kbd:`⋮` menu generates a :ref:`create_table_as` statement for the selected table in the editing area.

Renaming a table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Rename table` option under the :kbd:`⋮` menu generates an :ref:`alter_table` statement for renaming the selected table in the editing area.


Adding columns to table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Add column` option under the :kbd:`⋮` menu generates an :ref:`alter_table` statement for adding columns to the selected table in the editing area.

Truncate a table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Truncate table` option under the :kbd:`⋮` menu generates a :ref:`truncate` statement for the selected table in the 
editing area.


Dropping an object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Drop table`, :kbd:`Drop view`, or :kbd:`Drop function` option under the :kbd:`⋮` menu generates a ``DROP`` statement for the selected object in the editing area.


Generating DDL statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking the :kbd:`Table DDL`, :kbd:`View DDL`, or :kbd:`Function function` option under the :kbd:`⋮` menu generates a DDL  statement for the selected object in the editing area.

To get the entire database DDL, click the |icon-ddl-edit| icon next to the database name in the tree root.
See also :ref:`seeing_system_objects_as_sql`.

The DDL optimizer
^^^^^^^^^^^^^^^^^^^^^^^^^

The DDL optimizer tab analyzes database tables and recommends possible optimizations, per the :ref:`sql_best_practices` guide.

Using the DDL optimizer
---------------------------

Navigate to the DDL optimizer module by selecting :kbd:`DDL Optimizer` from the :kbd:`⋮` ("More") menu.

.. image:: /_static/images/studio_ddl_optimizer.png

* ``Rows`` - number of rows to scan for analysis. Defaults to 1,000,000

* ``Buffer Size`` - overhead threshold to use when analyzing ``VARCHAR`` fields. Defaults to 10%.

* ``Optimize NULLs`` - attempt to figure out field nullability.

Click :kbd:`Run Optimizer` to start the optimization process.

Analyzing the results
----------------------------

When results are produced, a :kbd:`Generate CREATE statement` button will appear.
Clicking the button creates a new tab with an optimized :ref:`create_table` statement, and an :ref:`insert` statement to copy the data to the new table.


.. _studio_dashboard:

Administration Dashboard
==============================

If you signed in with a ``SUPERUSER`` role, you can enter the administration dashboard.

Enter the administration dashboard by clicking the |icon-dashboard| icon in the navigation bar.



Familiarizing yourself with the dashboard
---------------------------------------------

.. image:: /_static/images/studio_dashboard_familiarize.png

The main dashboard screen contains two main panes:

* 
   :ref:`Data storage pane<administration_storage_pane>` - monitor the SQream DB cluster's storage

   - can be expanded to :ref:`drill down into database storage<administration_storage_database>`

* 
   :ref:`Worker pane<administration_worker_pane>` - monitor system health
   
   - the worker pane used to monitor workers and :ref:`service queues<workload_manager>` in the cluster.

.. _administration_storage_pane:

Data storage pane
-----------------------

The left section of the Admin Dashboard shows you the status of your system's storage as a donut.

.. image:: /_static/images/studio_dashboard_storage.png

Storage is displayed broken up into four components:

* Data – Storage occupied by databases in SQream DB

* Free – Free storage space

* 
   Deleted – Storage that is temporarily occupied but hasn't been reclaimed (see our :ref:`delete guide<delete_guide>` to understand how data deletion works). 
   
   (This value is estimated and may not be accurate)
   
* Other – Storage used by other applications. On a dedicated SQream DB cluster, this should be close to zero.

.. _administration_storage_database:

Database storage
^^^^^^^^^^^^^^^^^^^^^^^^

Expanding the storage pane (|icon-expand|) will show a breakdown of how much storage is used by each database in the cluster.

.. image:: /_static/images/studio_dashboard_storage_breakdown.png

This can be used to drill down into each database's storage footprint.

Databases are displayed in a table, containing the following information:
* Database name
* Raw storage size – the estimated size of raw data (uncompressed) in the database
* Storage size – the physical size of the compressed data
* Ratio – effective compression ratio
* Deleted data – storage that is temporarily occupied but hasn't been reclaimed (see our :ref:`delete guide<delete_guide>` to understand how data deletion works). (This value is estimated and may not be accurate)

Below the table, a graph shows the database storage trends.

By default, the graph shows the total storage for all databases. Clicking a database in the table will filter to show just that database.

The scale of the presented information can be controlled by changing the timeframe in the scale dropdown (|icon-scale|).

.. _administration_worker_pane:

Service and workers pane
--------------------------

This pane shows the cluster status in workers and their :ref:`service queues<workload_manager>`.

.. _administration_services:

Services
^^^^^^^^^^^

The services bar shows the defined :ref:`service queues<workload_manager>`.

Services are used to divide workers and associate (subscribe) workers to services.

Each service queue contains the following details:
* Service name
* A graph of load over time (statements in that queue)
* Currently processed queries of the Service / total queries for that service in the system (including queued queries)

Creating new service queues
********************************

Click the |icon-add| button above the service list. Type the service queue name and associate new workers to the service queue.

.. note:: if you choose not to associate a worker with the new service, it will not be created.

Associating a worker with an existing service
**********************************************

Clicking on the |icon-add-worker| icon on a service name is used to attach workers to a service.

Clicking on a service queue in the services bar will display the list of workers in the main pane.

.. image:: /_static/images/studio_dashboard_services.png

In this mode, the :kbd:`⋮` icon (more menu) can be used to detach a worker from a service.

You can select a Worker from the list that is available to process queries of the relevant Service and by clicking on the  button of that Worker that Worker will be associated with the Service. After that the page will go back to its normal layout and you will be able to click the Service and see the Worker associated with the Service.
Other Services associated with that Worker will remain associated to it.


.. _administration_workers:

Workers
^^^^^^^^^^^^^

The worker pane shows each worker (``sqreamd``) running in the cluster. 

Each worker has a status bar that represents the status over time. The scale of the presented information can be controlled by changing the timeframe in the scale dropdown (|icon-scale|).

The status bar is divided into 20 equal sections, showing the most dominant activity in that slice. Hover over the status bar sections to see the activity:

* Idle – worker is idle and available for statements
* Compiling – Compiling a statement, in preparation for execution
* Executing – executing a statement after compilation
* Stopped – worker was stopped (either deliberately or due to a fault)
* Waiting – worker was waiting on an object locked by another worker

Show host resources
*****************************

Clicking the |icon-expand-down| button below each host will expand to show the host resource utilization.

.. image:: /_static/images/studio_worker_activity.png

The host resource utilization includes information about:

* CPU utilization
* Memory utilization
* GPU utilization

Graphs show resource utilization over time. Current values are shown on the right.

Hover over the graph line to see the activity at a given time.


Active queries
******************

Clicking the |icon-expand-down| button on a worker will expand to show the active statements running.

Each statement has a statement ID, status, service queue, elapsed time, execution time, and estimated completion status.

Each statement can be stopped or expanded to show its execution plan and progress (:ref:`show_node_info`).

.. include:: /reference/sql/sql_statements/monitoring_commands/show_server_status.rst
   :start-line: 67
   :end-line: 84

Control worker status (start, stop, restart)
****************************************************

In some cases, it may be useful to stop or restart workers for maintenance.

Each Worker line has a :kbd:`⋮` menu (more menu). This menu allows stopping, starting, or restarting workers.

When a worker is stopped, it has a gray background and its status is "Stopped". 




.. |icon-user| image:: /_static/images/studio_icon_user.png
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

You can start the studio using :ref:`sqream-console<start_editor>`:
