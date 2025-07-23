.. _query_healer:

************
Query Healer
************
 

The **Query Healer** periodically examines the progress of running statements and connections, creating a log entry for all statements exceeding a defined time period and connections with no data transfer over a specified time.
It can also take action based on its findings, for two issues - a stuck query or a hung connection.
The query healer runs on a separate thread on each worker, this is able to take action if the worker it is coupled with has a problem.

Configuration
-------------

The following worker flags are required to configure the Query Healer. These are all worker level flags:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Flag
     - Description
   * - ``isHealerOn``
     - The :ref:`is_healer_on` enables and disables the Query Healer.
   * - ``healerDetectionFrequencySeconds``
     - The :ref:`healer_detection_frequency_seconds` triggers the healer to examine the progress of running statements. The default setting is one hour.
   * - ``maxStatementInactivitySeconds``
     - The :ref:`max_statement_inactivity_seconds` defines the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU. If a statement did not make any progress during this time, it is considerd stuck. The default setting is five hours.
   * - ``healerRunActionAutomatically``
     - The healerRunActionAutomatically triggers the healer to take action once it detects a problem. In order for the healer to take an automatic correction action, this flag needs to be true, AND the flag that relates to the detected problem. The default setting is true. 
   * - ``healerActionGracefulShutdown``
     - The healerActionGracefulShutdown triggers the healer to restart a stuck worker automatically (both this flag AND healerRunActionAutomatically need to be true). The default setting is false. 
   * - ``healerActionCleanupConnection``
     - The healerActionCleanupConnection triggers the healer to close a hung connection automatically (both this flag AND healerRunActionAutomatically need to be true). The default setting is true. 


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
