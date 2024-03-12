.. _retrieving_execution_plan_output_using_studio:

*******************************************************
Retrieving Execution Plan Output Using Workbench 
*******************************************************

You may use BLUE Workbench to create a query plan snapshot to be used for monitoring and troubleshooting slow running statements and for identifying long-running execution Workers that may cause performance issues. 

Keep in mind that CPU-based commands, such as all ``DESCRIBE`` commands, do not appear in the query plan snapshot. 

Retrieving Execution Plan Output
================================

You can retrieve the execution plan output either after the query execution has completed, in the case of a hanging query, or if you suspect no progress is being made.

1. In the **Result Panel**, select |icon-execution-details-view|.

   The **Execution Tree** window opens.

2. From the upper-right corner, select |icon-download| to download a CSV execution plan table.
   
3. Save the execution plan on your local machine.

You can analyze this information using :ref:`monitoring_query_performance` or with assistance from `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.



.. |icon-download| image:: /_static/images/studio_icon_download.png
   :align: middle
   
.. |icon-execution-details-view| image:: /_static/images/studio_icon_execution_details_view.png