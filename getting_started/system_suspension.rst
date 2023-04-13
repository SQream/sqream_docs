.. system_suspension:
  
*****************
System Suspension
*****************

When an environment is suspended, its resources are temporarily released, allowing for billing to be paused for a set duration in which the environment is not expected to be used. 
It's important to note that the environment will not execute any statements while it is suspended. 
However, once you resume operation, the resource count will return to its pre-suspension value. 
While manual suspension and resumption is possible, you may also use automatic suspension for a smoother experience.

Suspending Your BLUE Environment
================================

To control the automatic suspension of your environment through the BLUE web interface, navigate to the **Settings** tab. 
Within the **Worker Management** section, you can manage worker activity.

Activate the **Automatically Suspend Workers** feature and define the number of minutes afterwhich all workers will automatically be suspended.

At the bottom of the page you will find the **Suspension By** feature. This feature provides three suspension method options that you can choose from. 
Use this feature to define your preferred suspension method.

+----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Suspension Method**                  | **Description**                                                                                                    |
+========================================+====================================================================================================================+
| Brute force                            | All workers and all running queries are immediately suspended.                                                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Graceful shutdown                      | Suspension of all workers will occur only after completion of all running queries.                                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Graceful shutdown and pending requests | Suspension of workers will occur only after completion of all running queries and execution of all queued queries. |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------+


Resuming Your BLUE Environment
==============================

To control the automatic resumption of your environment through the BLUE web interface, navigate to the **Settings** tab. 
Within the **Worker Management** section, you can manage worker activity to control Real Time Communication (RTC).

Activate the **Automatically Resume Workers** feature to enable the resumption of your environment by executing statements.
