.. _monitoring_dashboard:

*********
Dashboard
*********

The **Dashboard** serves as a tool for you to monitor and promptly respond to any changes within your system. It enables you to track the health of your system and ensures that your workloads are operating as expected in near real-time.

Reading the Charts
==================

The dashboard charts offer a comprehensive overview of Worker performance, detailing:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Chart
     - Description
     - Sampling Interval
     - Timeframe Options
   * - Worker Loads
     - This measures the average load on the system within a specified timeframe. It's calculated based on the execution time of statements and the number of workers engaged, relative to the processing capacity during that period.
     - 15 seconds
     - 24/48/ hrs, past week, past month
   * - Queued Statements
     - This indicates the number of statements awaiting execution in the queue over a specific timeframe. 
     - 15 seconds
     - 24/48/ hrs, past week, past month
   * - Jobs
     - This indicates the total number of executed Jobs within a specific timeframe. 
     - 1 hour
     - Week, past 2 weeks, past month
   * - Tasks
     - This indicates the total number of executed Tasks within a specific timeframe.
     - 1 hour
     - Week, past 2 weeks, past month

Evaluating the Current System Status
====================================

The dashboard **Current Status** provides a real-time cluster overview of: 

* Running statements  
* Queued  statements
* Running Jobs