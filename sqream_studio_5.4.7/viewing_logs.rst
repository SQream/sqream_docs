.. _viewing_logs:

.. _logs_top_5.4.7:

****************************
Viewing Logs
****************************
The **Logs** screen is used for viewing logs and includes the following elements:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Filter area<filter_5.4.7>`
     - Lets you filter the data shown in the table. 
   * - :ref:`Query tab<queries_5.4.7>`
     - Shows basic query information logs, such as query number and the time the query was run. 
   * - :ref:`Session tab<sessions_5.4.7>`
     - Shows basic session information logs, such as session ID and user name.
   * - :ref:`System tab<system_5.4.7>`
     - Shows all system logs.

.. note:: Because the logs are stored in the **system** database, you cannot search the logs without first creating a **system** database. When you access the **Logs** tab, SQream can automatically create a **system** database for you.

.. _filter_5.4.7:

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

.. _queries_5.4.7:

:ref:`Back to Viewing Logs<logs_top_5.4.7>`


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

:ref:`Back to Viewing Logs<logs_top_5.4.7>`

.. _sessions_5.4.7:

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

:ref:`Back to Viewing Logs<logs_top_5.4.7>`

.. _system_5.4.7: