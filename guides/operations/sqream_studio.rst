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
-------------------------------------

The user information menu is located on the bottom left portion of the screen |icon-user|.

.. image:: /_static/images/studio_user_info.png


The menu contains information about the currently signed-in user, as well as version information.

You can sign out of the current user at any point, by selecting :kbd:`Logout` in the user menu.


.. _studio_editor_toolbar:

Toolbar
-------------

In the toolbar, you can perform the folllowing operations (from left to right):

.. image:: /_static/images/studio_editor_toolbar.png

* Database dropdown - Select the database you want to the statements to run on.

* Queue - specify which service queue the statement should run in

* :kbd:`⯈ Execute` / :kbd:`STOP` - Use the :kbd:`⯈ EXECUTE` button to execute the statement in the Editor pane. When a statement is running, the button changes to :kbd:`STOP`, and can be used to :ref:`stop the active statement<stop_statement>`.

* :kbd:`Format SQL` - Reformats and reindents the statement

* :kbd:`Download query` - save query text to your computer

* :kbd:`Open query` - load query text from your computer

* Max. Rows - By default, the editor will only fetch the first 1000 rows. Click the number to edit. Click outside the number area to save. Setting a higher limit can slow down your browser if the result set is very large. This number is limited to 100000 results (To see more results, consider saving the results to a file or a table with :ref:`create_table_as`).

.. _studio_editor_statement_area:

Statement area
----------------

The multi-tabbed statement area is where you write queries and statements.

.. image:: /_static/images/studio_editor_statement.png


Select the database you wish to use in the toolbar, and then write and execute statements.

A new tab can be opened for each statement. Tabs can be used to separate statements to different databases. Clicking the |icon-plus| will open a new tab with a default name of SQL + a running number.

Multiple statements can be written in the same tab, separated by semicolons (``;``).

If too many tabs are open, pagination controls will appear. Click |icon-left| or |icon-right| to scroll through the tab listings.
Rename a tab by double clicking it's name.

Close a tab by clicking |icon-close|

To close all tabs, click :kbd:`Close all`, to the right of the tabs.


.. tip:: If this is your first time with SQream DB, see our :ref:`first steps guide<first_steps>`.

.. Keyboard shortcuts
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. :kbd:`Ctrl` +: kbd:`Enter` - Execute all queries in the statement area, or just the highlighted part of the query.

.. :kbd:`Ctrl` + :kbd:`Space` - Auto-complete the current keyword

.. :kbd:`Ctrl` + :kbd:`↑` - Switch to next tab.

.. :kbd:`Ctrl` + :kbd:`↓` - Switch to previous tab

.. _studio_editor_results:


Formatting your SQL
^^^^^^^^^^^^^^^^^^^^^^^^^^

The |icon-format-sql| button can be used to automatically indent and reformat your SQL statements.

Saving statements
^^^^^^^^^^^^^^^^^^^^^

The |icon-download-query| saves the tab contents to your computer.

Loading SQL to a tab
^^^^^^^^^^^^^^^^^^^^^^^

The |icon-open-query| button loads a local file from your computer into a new editor tab.

Executing SQL statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clicking |icon-execute| will execute statements from the active tab.

The button has three modes, which can be selected with the dropdown arrow :kbd:`ᐯ`

* Execute statements – executes the statements where the cursor is located.
* Execute selected – executes the exact highlighted text. This mode is good for executing a subquery or other part of a large query (as long as it is a valid SQL).
* Execute all – executes all statements in the active tab, regardless of any selection

When a statement is running, the button changes to :kbd:`STOP`, and can be used to :ref:`stop the active statement<stop_statement>`.

Results
-------------

The results pane shows query results and execution information. By default, only the first 10000 results are returned (modify via the :ref:`studio_editor_toolbar`).

.. image:: /_static/images/studio_editor_results.png

By default, executing several statements together will open a separate results tab for each statement.

Statements will be executed serially. Any failed statement will cancel subsequent statements.

If the |keep-tabs| switch is on, new statements will create new tabs. When off, existing result will be cleared.

If too many result tabs are open, pagination controls will appear. Click |icon-left| or |icon-right| to scroll through the tab listings.

Close a tab by clicking |icon-close|

To close all tabs, click :kbd:`Close all`, to the right of the tabs.

.. contents:: In this topic:
   :local:


Sorting results
^^^^^^^^^^^^^^^^^^^^^^

After the results have appeared, sort them by clicking the column name.

Viewing execution information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During query execution the time elapsed is tracked in seconds.

The :kbd:`Show Execution Details` button opens the query's :ref:`execution plan<show_node_info>`, for monitoring purposes.

Saving results to a file or clipboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Query results can be saved to a clipboard (for pasting into another text editor) or a local file.

.. _studio_editor_db_tree:

Database tree
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

.. image:: /_static/images/studio_dashboard_main.png

The main dashboard screen contains two panes:

* :ref:`Data storage pane<administration_storage_pane>` - used to monitor the cluster's storage, and drill down into different databases.

* :ref:`Worker pane<administation_worker_pane>` - used to monitor workers and :ref:`service queues<workload_manager>` in the cluster.

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

Expanding the storage pane (|icon-expand|) will show a breakdown of how much storage is used by each database in the cluster.

.. image:: /_static/images/studio_dashboard_storage_breakdown.png


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

.. |icon-format-sql| image:: /_static/images/studio_icon_format_sql.png
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