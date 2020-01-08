.. _statement_editor:

****************************
Using the statement editor
****************************

The statement editor is a web-based client for use with SQream DB.

Use the statement editor to run ad-hoc statements, queries, and to manage roles and permissions.

.. note:: We recommend using Google Chrome or Chrome-based browsers to access the statement editor.

.. contents:: In this topic:
   :local:

Setting up and starting the statement editor
====================================================

The statement editor is included with all :ref:`dockerized installations of SQream DB<installing_sqream_db_docker>`.

You can start the editor using :ref:`sqream-console<start_editor>`:


.. code-block:: console

   $ ./sqream-console
   sqream-console> sqream editor --start
   access sqream statement editor through Chrome http://192.168.0.100:3000

When starting the editor, it listens on the local machine, on port 3000.

Logging in
===================

Open a browser to the host, on port 3000. If the machine is ``196.168.0.100``, navigate to http://192.168.0.100:3000 .

Fill in your login details for SQream DB. These are the same credentials you might use when using :ref:`sqream sql<sqream_sql_cli_reference>` or JDBC.

.. image:: /_static/images/statement_editor_login.png

.. tip:: 
   * If using a :ref:`load balancer<server_picker_cli_reference>`, select the ``Server picker`` box and make sure to use the correct port (usually ``3108``). If connecting directly to a worker, make sure to untick the box and use the correct port, usually ``5000`` and up.
   * If this is your first time using SQream DB, use database name ``master``.
   * When using SQream DB on AWS, the initial password is the EC2 instance ID.

Familiarizing yourself with the editor
==============================================

The editor is built up of main panes.

.. image:: /_static/images/statement_editor_main.png

* :ref:`Toolbar<editor_toolbar>` - used to select the active database you want to work on, limit the number of rows, save query results, control tab behavior, and more.

* :ref:`Statement area<editor_statement_area>` - The statement area is a multi-tab text editor where you write SQL statements. Each tab can connect to a different database.

* :ref:`Results<editor_results>` - Results from a query will populate here. 

* :ref:`Database tree<editor_db_tree>` - contains a heirarchy tree of databases, views, tables, and columns. Can be used to navigate and perform some table operations.

See more about each pane below:

.. _editor_toolbar:

Toolbar
-------------

.. image:: /_static/images/statement_editor_toolbar.png

In the toolbar, you can perform the folllowing operations (from left to right):

* Toggle Database Tree - Click •••​ to show or hide the Database Tree pane.

* Database dropdown - Select the database you want to the statements to run on.

* :kbd:`⯈ RUN` / :kbd:`◼ STOP` - Use the :kbd:`⯈ RUN` button to execute the statement in the Editor pane. When a statement is running, the button changes to :kbd:`◼ STOP`, and can be used to :ref:`stop the active statement<stop_statement>`.

* :kbd:`SQL` - Reformats and reindents the statement

* Max. Rows - By default, the editor will only fetch the first 1000 rows. Click the number to edit. Click outside the number area to save. Setting a higher limit can slow down your browser if the result set is very large.

* 💾 (Save) - Save the query text to a file.

* 📃 (Load) - Load query text from a file.

* ⋮ (more) - 
   
   * Append new results - When checked, every statement executed will open a new Results tab. If unchecked, the Results tab is reused and overwritten with every new statement.

.. _editor_statement_area:

Statement area
----------------

.. image:: /_static/images/statement_editor_editor.png

The multi-tabbed statement area is where you write queries and statements.

Select the database you wish to use in the toolbar, and then write and execute statements.

* A new tab can be opened for each statement. Tabs can be used to separate statements to different databases.

* Multiple statements can be written in the same tab, separated by semicolons. 

* When multiple statements exist in the tab, clicking :kbd:`Run` executes all statements in the tab, or only the selected statements.

.. tip:: If this is your first time with SQream DB, see our :ref:`first steps guide<first_steps>`.

Keyboard shortcuts
^^^^^^^^^^^^^^^^^^^^^^^^^

:kbd:`Ctrl` +: kbd:`Enter` - Execute all queries in the statement area, or just the highlighted part of the query.

:kbd:`Ctrl` + :kbd:`Space` - Auto-complete the current keyword

:kbd:`Ctrl` + :kbd:`↑` - Switch to next tab.

:kbd:`Ctrl` + :kbd:`↓` - Switch to previous tab

.. _editor_results:

Results
-------------

The results pane shows query results and execution information. By default, only the first 1000 results are returned (modify via the :ref:`editor_toolbar`).

A context menu, accessible via a right click on the results tab, enables:

* Renaming the tab name
* Show the SQL query text
* Reload results
* Close the current tab
* Close all result tabs

Sorting results
^^^^^^^^^^^^^^^^^^^^^^

After the results have appeared, sort them by clicking the column name.

Viewing execution information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During query execution the time elapsed is tracked in seconds.

.. image:: /_static/images/statement_editor_statistics.png

The :kbd:`SHOW STATISTICS` button opens the query's :ref:`execution plan<show_node_info>`, for monitoring purposes.

Saving results to a file or clipboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/statement_editor_save.png

Query results can be saved to a clipboard (for pasting into another text editor) or a local file.

.. _editor_db_tree:

Database tree
---------------

The database tree shows the database objects (e.g. tables, columns, views), as well as some metadata like row counts.

It also contains a few predefined catalog queries for execution.

.. image:: /_static/images/statement_editor_db_tree.png

Each level contains a context menu relevant to that object, accessible via a right-click.

Database
^^^^^^^^^^^^^

* :ref:`Copy the database DDL<dump_database_ddl>` to the clipboard

Schema
^^^^^^^^^^

* Drop the schema (copies statement to the clipboard)

Table
^^^^^^^^^^

* Show row count in the database tree

* :ref:`Copy the create table script<get_ddl>` to the clipboard

* Copy :ref:`select` to clipboard

* Copy :ref:`insert` to clipboard

* Copy :ref:`delete` to clipboard

* Rename table - Copy :ref:`rename_table` to clipboard

* Create table LIKE - Copy :ref:`create_table_as` to clipboard

* Add column - Copy :ref:`add_column` to clipboard

* Truncate table - Copy :ref:`truncate` to clipboard

* Drop table - Copy :ref:`drop_table` to pclipboard

* Create a table - Add a new table by running a statement, or alternatively use the **Add new** link near the **TABLES** group. 

Create a table
^^^^^^^^^^^^^^^^^^^^

Creating a new table is also possible using the wizard which can guide you with creating a table.

Refer to the :ref:`create_table` reference for information about creating a table (e.g. able parameters like default values, identity, etc.).

.. image:: /_static/images/statement_editor_add_table.png

Fill in the table name, and add a new row for each table column.

If a table by the same name exists, check **Create or Replace table** to overwrite it.

Click :kbd:`EXEC` to create the table.

Catalog views
^^^^^^^^^^^^^^^^^^^

To see :ref:`catalog views<catalog_reference>`, click the catalog view name in the tree. The editor will run a query on that view.

.. image:: /_static/images/statement_editor_view_catalog.png

Predefined queries
^^^^^^^^^^^^^^^^^^^^^^^

The editor comes with several predefined catalog queries that are useful for analysis of table compression rates, users and permissions, etc.

.. image:: /_static/images/statement_editor_predefined_queries.png

Notifications
===================

Desktop notificaitons lets you receive a notification when a statement is completed. 

You can minimize the browser or switch to other tabs, and still recieve a notification when the query is done.

.. image:: /_static/images/statement_editor_notifications.png

Enable the desktop notification through the **Allow Desktop Notification** from the menu options.

DDL optimizer
==================

The DDL optimizer tab analyzes database tables and recommends possible optimizations, per the :ref:`sql_best_practices` guide.

Using the DDL optimizer
---------------------------

Navigate to the DDL optimizer module by selecting it from the :kdb:`⋮` ("More") menu.

.. image:: /_static/images/statement_editor_ddl_optimizer.png

* ``Database`` and ``Table`` - select the database and desired table to optimize
* ``Rows`` is the number to scan for analysis. Defaults to 1,000,000

* ``Buffer Size`` - overhead threshold to use when analyzing ``VARCHAR`` fields. Defaults to 10%.

* ``Optimize NULLs`` - attempt to figure out field nullability.

Click ``EXECUTE`` to start the optimization process.

Analyzing the results
----------------------------

The analysis process shows results for each row.

.. image:: /_static/images/statement_editor_ddl_optimizer_results.png

The results are displayed in two tabs:

* **OPTIMIZED COLUMNS** - review the system recommendation to:

   #. decrease the length of ``VARCHAR`` fields

   #. remove the ``NULL`` option

* **OPTIMIZED DDL** - The recommended :ref:`create_table` statement

Analyzing the DDL culminates in four possible actions:

* :kbd:`COPY DDL TO CLIPBOARD` - Copies the optimized :ref:`create_table` to the clipboard

* :kbd:`CREATE A NEW TABLE` - Creates the new table structure with ``_new`` appended to the table name. No data is populated

* :kbd:`CREATE AND INSERT INTO EXISTING DATA` - Create a new table in same database and schema as the original table and populates the data

* **Back** - go back to the statement editor and abandon any recommendations