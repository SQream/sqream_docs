.. _viewing_logs:

.. _logs_top_5.4.6:

****************************
Viewing Logs
****************************
The **Logs** screen is used for viewing logs and includes the following elements:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Filter area<filter_5.4.6>`
     - Lets you filter the data shown in the table. 
   * - :ref:`Query tab<queries_5.4.6>`
     - Shows basic query information logs, such as query number and the time the query was run. 
   * - :ref:`Session tab<sessions_5.4.6>`
     - Shows basic session information logs, such as session ID and user name.
   * - :ref:`System tab<system_5.4.6>`
     - Shows all system logs.
   * - :ref:`Log lines tab<log_lines_5.4.6>`
     - Shows the total amount of log lines.


.. _filter_5.4.6:

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

.. _queries_5.4.6:

:ref:`Back to Viewing Logs<logs_top_5.4.6>`


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

:ref:`Back to Viewing Logs<logs_top_5.4.6>`

.. _sessions_5.4.6:

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

:ref:`Back to Viewing Logs<logs_top_5.4.6>`

.. _system_5.4.6:

Viewing System Logs
----------
The **SYSTEM** tab shows the system log table and is used for viewing all system logs. The number at the top indicates the amount of sessions that have occurred. Because system logs occur less frequently than queries and sessions, you may need to increase the filter timespan for the table to display any system logs.

From here you can see and sort by the following:

* Timestamp
* Log type
* Message

In the Systems table, you can click on the **Timestamp** and **Log type** items to set them as your filters. In the **Message** column, you can also click on an item to show more information about the message.

:ref:`Back to Viewing Logs<logs_top_5.4.6>`

.. _log_lines_5.4.6:

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

:ref:`Back to Viewing Logs<logs_top_5.4.6>`