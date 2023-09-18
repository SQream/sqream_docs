.. _retrieving_execution_plan_output_using_studio:

*******************************************************
Retrieving Execution Plan Output Using SQreamDB Studio 
*******************************************************

You may use SQreamDB Studio to create a query plan snapshot to be used for monitoring and troubleshooting slow running statements and for identifying long-running execution Workers (components that process data), that may cause performance issues.

Retrieving Execution Plan Output
================================

You can retrieve the execution plan output either after the query execution has completed, in the case of a hanging query, or if you suspect no progress is being made.

1. In the **Result Panel**, select **Execution Details View** |icon-execution-details-view|.

	The **Execution Tree** window opens.

.. |icon-execution-details-view| image:: /_static/images/studio_icon_execution_details_view.png

2. From the upper-right corner, select the |icon-download| to download a CSV execution plan table.

.. |icon-download| image:: /_static/images/studio_icon_download.png
   :align: middle
   
3. Save the execution plan on your local machine.

The information may be analyzed by :ref:`monitoring_query_performance` or with help from `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.