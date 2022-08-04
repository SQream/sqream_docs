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
The **Query Healer** periodically examines the progress of running statements, creating a log entry for all statements exceeding the ``healerMaxInactivityHours`` flag setting. The default setting of the ``healerMaxInactivityHours`` is five hours.

The following is an example of a log record for a query stuck in the query detection phase for more than five hours:

.. code-block:: console

   #SQ#|1659621825880088264|2022-05-19 20:01:25.880|INFO|0x00007f9a497fe700:Healer|192.168.4.65|5001|-1|master|sqream|-1|sqream|0|"[ERROR]|cpp/SqrmRT/healer.cpp:140 |"Stuck query found. Statement ID: 72, Last chunk producer updated: 1 WriteTable, Started on: Thu May 19 14:01:25 2022, Last updated: Thu May 19 15:01:25 2022, Stuck time: 5 hours, Max allowed stuck query time: 5 hours"|#EOM#

The ``healerMaxInactivityHours`` log frequency is calculated as 5% of the flag setting. When set to to five hours (the default setting), the Query Healer triggers an examination every 15 minutes.

.. note:: The logs are located in your cluster.

Configuring the Healer
------------------
The following **Administration Worker** flags are required to configure the Query Healer:

 * :ref:`is_healer_on` - Enables the Query Healer.

    ::

 * :ref:`healer_max_inactivity_hours` - Defines the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.

The ``healerMaxInactivityHours`` log frequency is calculated as 5% of the flag setting. For example, setting ``healerMaxInactivityHours`` to five hours (the default setting) triggers an examination every 15 minutes.