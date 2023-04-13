.. system_suspension:
  
*****************
Cost Management
*****************

This page explains how to suspend and resume your BLUE environment automatically, which can be a useful strategy for managing costs. While it is possible to suspend and resume manually, setting up automatic suspension can result in a smoother experience.

When you suspend an environment, its resources are temporarily released, which allows billing to be paused for a set duration during which the environment is not expected to be used. If your BLUE environment is suspended, it means that your `Workers <glossary>_` are not operational, and statements cannot be executed. However, after you resume operation, the resource count will return to its pre-suspension value. It's important to note that your cluster remains accessible, and you can still perform administrative actions like resize and flow management.

Suspending Your BLUE Environment
================================

To control the automatic suspension of your environment through the BLUE web interface, navigate to the **Settings** tab. 
Within the **Worker Management** section, you can manage worker activity.

Activate the **Automatically Suspend Workers** feature to define the number of minutes afterwhich all workers will automatically be suspended.

At the bottom of the page you will find the **Suspension By** feature. This feature provides three suspension method options that you can choose from. 
Use this feature to define your preferred suspension method.

+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Suspension Method**                  | **Description**                                                                                                          |
+========================================+==========================================================================================================================+
| Brute force                            | All workers are immediately suspended and all running statements are aborted.                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Graceful shutdown                      | Suspension of all workers will occur only after completion of all running statements.                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Graceful shutdown and pending requests | Suspension of workers will occur only after completion of all running statements and execution of all queued statements. |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+



Resuming Your BLUE Environment
==============================

To control the automatic resumption of your environment through the BLUE web interface, navigate to the **Settings** tab. 
Within the **Worker Management** section, you can manage worker activity to control Real Time Communication (RTC).

Activate the **Automatically Resume Workers** feature to enable the resumption of your environment by executing statements.
