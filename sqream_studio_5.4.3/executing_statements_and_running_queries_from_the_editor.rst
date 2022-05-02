.. _executing_statements_and_running_queries_from_the_editor:

.. _editor_top_5.4.3:

****************************
Executing Statements and Running Queries from the Editor
****************************
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
     - :ref:`Toolbar<studio_5.4.3_editor_toolbar>`
     - Used to select the active database you want to work on, limit the number of rows, save query, etc.
   * - 2
     - :ref:`Database Tree and System Queries panel<studio_5.4.3_editor_db_tree>`
     - Shows a hierarchy tree of databases, views, tables, and columns
   * - 3
     - :ref:`Statement panel<studio_5.4.3_editor_statement_area>`
     - Used for writing queries and statements
   * - 4
     - :ref:`Results panel<studio_5.4.3_editor_results>`
     - Shows query results and execution information.



.. _top_5.4.3:

.. _studio_5.4.3_editor_toolbar:

Executing Statements from the Toolbar
================
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

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.3>`


.. _studio_5.4.3_editor_db_tree:

Performing Statement-Related Operations from the Database Tree
================
From the Database Tree you can perform statement-related operations and show metadata (such as a number indicating the amount of rows in the table).





The database object functions are used to perform the following:

* The **SELECT** statement - copies the selected table's **columns** into the Statement panel as ``SELECT`` parameters.  

   ::

* The **copy** feature |icon-copy| - copies the selected table's **name** into the Statement panel. 

   ::

* The **additional operations** |icon-dots| - displays the following additional options:
  

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


.. list-table::
   :widths: 30 70
   :header-rows: 1   
   
   * - Function
     - Description
   * - Insert statement
     - Generates an `INSERT <https://docs.sqream.com/en/v2022.1/reference/sql/sql_statements/dml_commands/insert.html#insert>`_ statement for the selected table in the editing area.
   * - Delete statement
     - Generates a `DELETE <https://docs.sqream.com/en/v2022.1/reference/sql/sql_statements/dml_commands/delete.html#delete>`_ statement for the selected table in the editing area.
   * - Create Table As statement
     - Generates a `CREATE TABLE AS <https://docs.sqream.com/en/v2022.1/reference/sql/sql_statements/ddl_commands/create_table_as.html#create-table-as>`_ statement for the selected table in the editing area.	 
   * - Rename statement
     - Generates an `RENAME TABLE AS <https://docs.sqream.com/en/v2022.1/reference/sql/sql_statements/ddl_commands/rename_table.html#rename-table>`_ statement for renaming the selected table in the editing area.
   * - Adding column statement
     - Generates an `ADD COLUMN <https://docs.sqream.com/en/v2022.1/reference/sql/sql_statements/ddl_commands/add_column.html#add-column>`_ statement for adding columns to the selected table in the editing area.
   * - Truncate table statement
     - Generates a `TRUNCATE_IF_EXISTS <https://docs.sqream.com/en/v2022.1/reference/sql/sql_statements/dml_commands/truncate_if_exists.html#truncate>`_ statement for the selected table in the editing area.
   * - Drop table statement
     - Generates a ``DROP`` statement for the selected object in the editing area.
   * - Table DDL
     - Generates a DDL statement for the selected object in the editing area. To get the entire database DDL, click the |icon-ddl-edit| icon next to the database name in the tree root. See `Seeing System Objects as DDL <https://docs.sqream.com/en/v2022.1/operational_guides/seeing_system_objects_as_ddl.html>`_.
   * - DDL Optimizer
     - The `DDL Optimizer <https://docs.sqream.com/en/v2022.1/sqream_studio_5.4.3/executing_statements_and_running_queries_from_the_editor.html#optimizing-database-tables-using-the-ddl-optimizer>`_  lets you analyze database tables and recommends possible optimizations.

Optimizing Database Tables Using the DDL Optimizer
-----------------------
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

Clicking **Run Optimizer** adds a tab to the Statement panel showing the optimized results of the selected object.

For more information, see `Optimization and Best Practices <https://docs.sqream.com/en/v2022.1/operational_guides/optimization_best_practices.html>`_.

Executing Pre-Defined Queries from the System Queries Panel
---------------
The **System Queries** panel lets you execute predefined queries and includes the following system query types:

* **Catalog queries** - Used for analyzing table compression rates, users and permissions, etc.
    
	::
	
* **Admin queries** - Queries useful for SQream database management.

Clicking an item pastes the query into the Statement pane, and you can undo a previous operation by pressing **Ctrl + Z**.

.. _studio_5.4.3_editor_statement_area:

Writing Statements and Queries from the Statement Panel
==============
The multi-tabbed statement area is used for writing queries and statements, and is used in tandem with the toolbar. When writing and executing statements, you must first select a database from the **Database** dropdown menu in the toolbar. When you execute a statement, it passes through a series of statuses until completed. Knowing the status helps you with statement maintenance, and the statuses are shown in the **Results panel**.

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

.. tip:: If this is your first time using SQream, see `Getting Started <https://docs.sqream.com/en/v2022.1/first_steps.html#first-steps>`_.


.. Keyboard shortcuts
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. :kbd:`Ctrl` +: kbd:`Enter` - Execute all queries in the statement area, or just the highlighted part of the query.

.. :kbd:`Ctrl` + :kbd:`Space` - Auto-complete the current keyword

.. :kbd:`Ctrl` + :kbd:`↑` - Switch to next tab.

.. :kbd:`Ctrl` + :kbd:`↓` - Switch to previous tab

.. _studio_editor_results_5.4.3:

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.3>`

.. _studio_5.4.3_editor_results:

.. _results_panel_5.4.3:

Viewing Statement and Query Results from the Results Panel
==============
The results panel shows statement and query results. By default, only the first 10,000 results are returned, although you can modify this from the :ref:`studio_editor_toolbar`, as described above. By default, executing several statements together opens a separate results tab for each statement. Executing statements together executes them serially, and any failed statement cancels all subsequent executions.

.. image:: /_static/images/results_panel.png

The following is a brief description of the Results panel views highlighted in the figure above:

.. list-table::
   :widths: 45 160
   :header-rows: 1  
   
   * - Element
     - Description
   * - :ref:`Results view<results_view_5.4.3>`
     - Lets you view search query results.
   * - :ref:`Execution Details view<execution_details_view_5.4.3>`
     - Lets you analyze your query for troubleshooting and optimization purposes.
   * - :ref:`SQL view<sql_view_5.4.3>`
     - Lets you see the SQL view.


.. _results_view_5.4.3:

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.3>`
	 
Searching Query Results in the Results View
----------------
The **Results view** lets you view search query results.

From this view you can also do the following:

* View the amount of time (in seconds) taken for a query to finish executing.
* Switch and scroll between tabs.
* Close all tabs at once.
* Enable keeping tabs by selecting **Keep tabs**.
* Sort column results.

Saving Results to the Clipboard
^^^^^^^^^^^^
The **Save results to clipboard** function lets you save your results to the clipboard to paste into another text editor or into Excel for further analysis.

.. _save_results_to_local_file_5.4.3:

Saving Results to a Local File
^^^^^^^^^^^^
The **Save results to local file** functions lets you save your search query results to a local file. Clicking **Save results to local file** downloads the contents of the Results panel to an Excel sheet. You can then use copy and paste this content into other editors as needed.

In the Results view you can also run parallel statements, as described in **Running Parallel Statements** below.

.. _running_parallel_statements_5.4.3:

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


:ref:`Back to Viewing Statement and Query Results from the Results Panel<results_panel_5.4.3>`

.. _execution_details_view_5.4.3:

.. _execution_tree_5.4.3:

Execution Details View
--------------
The **Execution Details View** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Overview
^^^^^^^^^^^^
Clicking **Execution Details View** displays the **Execution Tree**, which is a chronological tree of processes that occurred to execute your queries. The purpose of the Execution Tree is to analyze all aspects of your query for troubleshooting and optimization purposes, such as resolving queries with an exceptionally long runtime.

.. note::  The **Execution Details View** button is enabled only when a query takes longer than five seconds. 

From this screen you can scroll in, out, and around the execution tree with the mouse to analyze all aspects of your query. You can navigate around the execution tree by dragging or by using the mini-map in the bottom right corner.

.. image:: /_static/images/execution_tree_1.png

You can also search for query data by pressing **Ctrl+F** or clicking the search icon |icon-search| in the search field in the top right corner and typing text.

.. image:: /_static/images/search_field.png

Pressing **Enter** takes you directly to the next result matching your search criteria, and pressing **Shift + Enter** takes you directly to the previous result. You can also search next and previous results using the up and down arrows.

.. |icon-search| image:: /_static/images/studio_icon_search.png
   :align: middle

The nodes are color-coded based on the following:

* **Slow nodes** - red
* **In progress nodes** - yellow
* **Completed nodes** - green
* **Pending nodes** - white
* **Currently selected node** - blue
* **Search result node** - purple (in the mini-map)

The execution tree displays the same information as shown in the plain view in tree format.

The Execution Tree tracks each phase of your query in real time as a vertical tree of nodes. Each node refers to an operation that occurred on the GPU or CPU. When a phase is completed, the next branch begins to its right until the entire query is complete. Joins are displayed as two parallel branches merged together in a node called **Join**, as shown in the figure above. The nodes are connected by a line indicating the number of rows passed from one node to the next. The width of the line indicates the amount of rows on a logarithmic scale.

Each node displays a number displaying its **node ID**, its **type**, **table name** (if relevant), **status**, and **runtime**. The nodes are color-coded for easy identification. Green nodes indicate **completed nodes**, yellow indicates **nodes in progress**, and red indicates **slowest nodes**, typically joins, as shown below:

.. image:: /_static/images/nodes.png

Viewing Query Statistics
^^^^^^^^^^^^
The following statistical information is displayed in the top left corner, as shown in the figure above:

* **Query Statistics**:

    * **Elapsed** - the total time taken for the query to complete.
    * **Result rows** - the amount of rows fetched.
    * **Running nodes completion**
    * **Total query completion** - the amount of the total execution tree that was executed (nodes marked green).
	
* **Slowest Nodes** information is displayed in the top right corner in red text. Clicking the slowest node centers automatically on that node in the execution tree.

You can also view the following **Node Statistics** in the top right corner for each individual node by clicking a node:

.. list-table::
   :widths: 45 160
   :header-rows: 1  
   
   * - Element
     - Description
   * - Node type
     - Shows the node type.
   * - Status
     - Shows the execution status.
   * - Time
     - The total time taken to execute.
   * - Rows
     - Shows the number of produced rows passed to the next node.
   * - Chunks
     - Shows number of produced chunks.
   * - Average rows per chunk
     - Shows the number of average rows per chunk.
   * - Table (for **ReadTable** and joins only)
     - Shows the table name.
   * - Write (for joins only)
     - Shows the total date size written to the disk.
   * - Read (for **ReadTable** and joins only)
     - Shows the total data size read from the disk.

Note that you can scroll the Node Statistics table. You can also download the execution plan table in .csv format by clicking the download arrow |icon-download| in the upper-right corner.

.. |icon-download| image:: /_static/images/studio_icon_download.png
   :align: middle

Using the Plain View
^^^^^^^^^^^^
You can use the **Plain View** instead of viewing the execution tree by clicking **Plain View** |icon-plain| in the top right corner. The plain view displays the same information as shown in the execution tree in table format.

.. |icon-plain| image:: /_static/images/studio_icon_plain.png
   :align: middle
   



The plain view lets you view a query’s execution plan for monitoring purposes and highlights rows based on how long they ran relative to the entire query.

This can be seen in the **timeSum** column as follows:

* **Rows highlighted red** - longest runtime
* **Rows highlighted orange** - medium runtime
* **Rows highlighted yellow** - shortest runtime

:ref:`Back to Viewing Statement and Query Results from the Results Panel<results_panel_5.4.3>`

.. _sql_view_5.4.3:

Viewing Wrapped Strings in the SQL View
------------------
The SQL View panel allows you to more easily view certain queries, such as a long string that appears on one line. The SQL View makes it easier to see by wrapping it so that you can see the entire string at once. It also reformats and organizes query syntax entered in the Statement panel for more easily locating particular segments of your queries. The SQL View is identical to the **Format SQL** feature in the Toolbar, allowing you to retain your originally constructed query while viewing a more intuitively structured snapshot of it.

.. _save_results_to_clipboard_5.4.3:

:ref:`Back to Viewing Statement and Query Results from the Results Panel<results_panel_5.4.3>`

:ref:`Back to Executing Statements and Running Queries from the Editor<editor_top_5.4.3>`
