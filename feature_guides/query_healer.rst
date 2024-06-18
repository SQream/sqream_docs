.. _query_healer:

************
Query Healer
************
 

The **Query Healer** periodically examines the progress of running statements, creating a log entry for all statements exceeding a defined time period.   

Configuration
-------------

The following worker flags are required to configure the Query Healer:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Flag
     - Description
   * - ``is_healer_on``
     - The :ref:`is_healer_on` enables and disables the Query Healer.
   * - ``maxStatementInactivitySeconds``
     - The :ref:`max_statement_inactivity_seconds` worker level flag defines the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU. The default setting is five hours.
   * - ``healerDetectionFrequencySeconds``
     - The :ref:`healer_detection_frequency_seconds` worker level flag triggers the healer to examine the progress of running statements. The default setting is one hour. 

Query Log
---------

The following is an example of a log record for a query stuck in the query detection phase for more than five hours:

.. code-block:: console

   |INFO|0x00007f9a497fe700:Healer|192.168.4.65|5001|-1|master|sqream|-1|sqream|0|"[ERROR]|cpp/SqrmRT/healer.cpp:140 |"Stuck query found. Statement ID: 72, Last chunk producer updated: 1.

Once you identify the stuck worker, you can execute the ``shutdown_server`` utility function from this specific worker, as described in the next section.

Activating a Graceful Shutdown
------------------------------

You can activate a graceful shutdown if your log entry says ``Stuck query found``, as shown in the example above. You can do this by setting the **shutdown_server** utility function to ``select shutdown_server();``.

**To activte a graceful shutdown:**

1. Locate the IP and the Port of the stuck worker from the logs.

   .. note:: The log in the previous section identifies the IP **(192.168.4.65)** and port **(5001)** referring to the stuck query.

2. From the machine of the stuck query (IP: **192.168.4.65**, port: **5001**), connect to SQream SQL client:

   .. code-block:: console

      ./sqream sql --port=$STUCK_WORKER_IP --username=$SQREAM_USER --password=$SQREAM_PASSWORD databasename=$SQREAM_DATABASE

3. Execute ``shutdown_server``.

For more information, see the :ref:`shutdown_server_command` utility function. This page describes all of ``shutdown_server`` options.
