.. _query_healer:

***********************
Query Healer
***********************
The **Query Healer** page describes the following:

.. contents:: 
   :local:
   :depth: 1      
   
Overview
----------
The **Query Healer** periodically examines the progress of running statements, creating a log entry for all statements exceeding the ``healerMaxInactivityHours`` flag setting. The default setting of the ``healerMaxInactivityHours`` is five hours. The ``healerMaxInactivityHours`` log frequency is calculated as 5% of the flag setting. When set to five hours (the default setting), the Query Healer triggers an examination every 15 minutes.  

The following is an example of a log record for a query stuck in the query detection phase for more than five hours:

.. code-block:: console

   |INFO|0x00007f9a497fe700:Healer|192.168.4.65|5001|-1|master|sqream|-1|sqream|0|"[ERROR]|cpp/SqrmRT/healer.cpp:140 |"Stuck query found. Statement ID: 72, Last chunk producer updated: 1.

Once you identify the stuck worker, you can execute the ``shutdown_server`` utility function from this specific worker, as described in the next section.

Activating a Graceful Shutdown
------------------
You can activate a graceful shutdown if your log entry says ``Stuck query found``, as shown in the example above. You can do this by setting the **shutdown_server** utility function to ``select shutdown_server();``.

**To activte a graceful shutdown:**

1. Locate the IP and the Port of the stuck worker from the logs.

   .. note:: The log in the previous section identifies the IP **(192.168.4.65)** and port **(5001)** referring to the stuck query.

2. From the machine of the stuck query (IP: **192.168.4.65**, port: **5001**), connect to SQream SQL client:

   .. code-block:: console

      ./sqream sql --port=$STUCK_WORKER_IP --username=$SQREAM_USER --password=$SQREAM_PASSWORD databasename=$SQREAM_DATABASE

3. Execute ``shutdown_server``.

For more information, see the following:

* Activating the :ref:`shutdown_server_command` utility function. This page describes all of ``shutdown_server`` options.

   ::

* Configuring the :ref:`shutdown_server` flag.

Configuring the Healer
------------------
The following **Administration Worker** flags are required to configure the Query Healer:

 * :ref:`is_healer_on` - Enables the Query Healer.

    ::

 * :ref:`healer_max_inactivity_hours` - Defines the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.