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

Configuring the Healer
------------------
The following flags are required to configure the Query Healer:

 * **isHealerOn** - Enables the Query Healer.

    ::

 * **healerMaxInactivityHours** - Defines the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.

The ``healerMaxInactivityHours`` log frequency is calculated as 5% of the flag setting. For example, setting ``healerMaxInactivityHours`` to five hours (the default setting) triggers an examination every 15 minutes.

For more information, see the following Administration Worker flags:

 * :ref:`is_healer_on`

    ::

 * :ref:`healerMaxInactivityHours`