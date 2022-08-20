.. _tableau_related_issues:

***********************
Tableau Related Issues
***********************
This section describes the following best practices and troubleshooting procedures when connecting to Tableau:

.. contents::
   :local:

Inserting Only Required Data
~~~~~~~~~~~~~~~~~~
When using Tableau, SQream recommends using only data that you need, as described below:

* Insert only the data sources you need into Tableau, excluding tables that don't require analysis.

   ::

* To increase query performance, add filters before analyzing. Every modification you make while analyzing data queries the SQream database, sometimes several times. Adding filters to the datasource before exploring limits the amount of data analyze and increases query performance.

Using Tableau's Table Query Syntax
~~~~~~~~~~~~~~~~~~~
Dragging your desired tables into the main area in Tableau builds queries based on its own syntax. This helps ensure increased performance, while using views or custom SQL may degrade performance. In addition, SQream recommends using the :ref:`create_view` to create pre-optimized views, which your datasources point to. 

Creating a Separate Service for Tableau
~~~~~~~~~~~~~~~~~~~
SQream recommends creating a separate service for Tableau with the DWLM. This reduces the impact that Tableau has on other applications and processes, such as ETL. In addition, this works in conjunction with the load balancer to ensure good performance.

Error Saving Large Quantities of Data as Files
~~~~~~~~~~~~~~~~~~~
An **FAB9A2C5** error can when saving large quantities of data as files. If you receive this error when writing a connection string, add the ``fetchSize`` parameter to ``1``, as shown below:

.. code-block:: text

   jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>sqream;[<optional parameters>; fetchSize=1...]
   
For more information on troubleshooting error **FAB9A2C5**, see the `Tableau Knowledge Base <https://community.tableau.com/s/global-search/%40uri#q=FAB9A2C5&t=All&f:content-type-facet=[Knowledge%20Base]>`_.

Troubleshooting Workbook Performance Before Deploying to the Tableau Server
~~~~~~~~~~~~~~~~~~~
Tableau has a built-in `performance recorder <https://help.tableau.com/current/pro/desktop/en-us/perf_record_create_desktop.htm>`_ that shows how time is being spent. If you're seeing slow performance, this could be the result of a misconfiguration such as setting concurrency too low.

Use the Tableau Performance Recorder for viewing the performance of queries run by Tableau. You can use this information to identify queries that can be optimized by using views.

Troubleshooting Error Codes
~~~~~~~~~~~~~~~~~~~
Tableau may be unable to locate the SQream JDBC driver. The following message is displayed when Tableau cannot locate the driver:

.. code-block:: console
     
   Error Code: 37CE01A3, No suitable driver installed or the URL is incorrect
   
**To troubleshoot error codes:**

If Tableau cannot locate the SQream JDBC driver, do the following:

 1. Verify that the JDBC driver is located in the correct directory:
 
   * **Tableau Desktop on Windows:** *C:\Program Files\Tableau\Drivers*
   * **Tableau Desktop on MacOS:** *~/Library/Tableau/Drivers*
   * **Tableau on Linux**: */opt/tableau/tableau_driver/jdbc*
   
 2. Find the file path for the JDBC driver and add it to the Java classpath:
   
   * **For Linux** - ``export CLASSPATH=<absolute path of SQream DB JDBC driver>;$CLASSPATH``

        ::
		
   * **For Windows** - add an environment variable for the classpath:
 
	

If you experience issues after restarting Tableau, see the `SQream support portal <https://support.sqream.com>`_.
