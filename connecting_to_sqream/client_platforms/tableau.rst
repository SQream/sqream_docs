.. _tableau:

*************************
Connecting to SQream Using Tableau
*************************

Overview
=====================
SQream's Tableau connector plugin, based on standard JDBC, enables storing and fast querying large volumes of data.

The **Connecting to SQream Using Tableau** page is a Quick Start Guide that describes how install Tableau and the JDBC driver and connect to SQream for data analysis. It also describes using best practices and troubleshoot issues that may occur while installing Tableau. SQream supports both Tableau Desktop and Tableau Server on Windows, MacOS, and Linux distributions.

For more information on SQream's integration with Tableau, see `Tableau's Extension Gallery <https://extensiongallery.tableau.com/connectors?version=2019.4>`_.

The Connecting to SQream Using Tableau page describes the following:

.. contents::
   :local:
   :depth: 1

Installing the JDBC Driver and Tableau Connector Plugin
-------------------
This section describes how to install the JDBC driver using the fully-integrated Tableau connector plugin (Tableau Connector, or **.taco** file). SQream has been tested with Tableau versions 9.2 and newer.

You can connect to SQream using Tableau by doing one of the following:

   * **For MacOS or Linux** - See :ref:`Installing the JDBC Driver <tableau_jdbc_installer>`.

.. _tableau_jdbc_installer:
   
Installing the JDBC Driver
-------------------
If you are using MacOS, Linux, or the Tableau server, after installing the Tableau Desktop application you can install the JDBC driver manually. When the driver is installed, you can connect to SQream.

**To install the JDBC driver:**

1. Download the JDBC installer and SQream Tableau connector (.taco) file from the :ref:`from the client drivers page<client_drivers>`.

    ::

2. Based on your operating system, your Tableau driver directory is located in one of the following places:

   * **Tableau Desktop on MacOS:** *~/Library/Tableau/Drivers*
   
      ::
	  
   * **Tableau Desktop on Windows:** *C:\\Program Files\\Tableau\\Drivers*
      
      ::
   
   * **Tableau on Linux**: */opt/tableau/tableau_driver/jdbc*
	  
   Note the following when installing the JDBC driver:

   * You must have read permissions on the .jar file.
   
      ::
	  
   * Tableau requires a JDBC 4.0 or later driver.
   
      ::
	  
   * Tableau requires a Type 4 JDBC driver.
   
      ::
	  
   * The latest 64-bit version of Java 8 is installed.

3. Install the **SQreamDB.taco** file by moving the SQreamDB.taco file into the Tableau connectors directory.
   
   Based on the installation method that you used, your Tableau driver directory is located in one of the following places:

   * **Tableau Desktop on Windows:** *C:\\Users\\<your user>\\My Tableau Repository\\Connectors*
   
      ::
	  
   * **Tableau Desktop on MacOS:** *~/My Tableau Repository/Connectors*

You can now restart Tableau Desktop or Server to begin using the SQream driver by connecting to SQream as described in the section below.

Connecting to SQream
---------------------
After installing the JDBC driver you can connect to SQream.

**To connect to SQream:**

#. Start Tableau Desktop.

    ::
	
#. In the **Connect** menu, in the **To a Server** sub-menu, click **More...**.

   More connection options are displayed.

    ::
	
#. Select **SQream DB by SQream Technologies**.

   The **New Connection** dialog box is displayed.

    ::
	
#. In the New Connection dialog box, fill in the fields and click **Sign In**.

  The following table describes the fields:
   
  .. list-table:: 
     :widths: 15 38 38
     :header-rows: 1
   
     * - Item
       - Description
       - Example
     * - Server
       - Defines the server of the SQream worker.
       - ``127.0.0.1`` or ``sqream.mynetwork.co``
     * - Port
       - Defines the TCP port of the SQream worker.
       - ``3108`` when using a load balancer, or ``5100`` when connecting directly to a worker with SSL.
     * - Database
       - Defines the database to establish a connection with.
       - ``master``
     * - Cluster
       - Enables (``true``) or disables (``false``) the load balancer. After enabling or disabling the load balance, verify the connection.
       - 
     * - Username
       - Specifies the username of a role to use when connecting.
       - ``rhendricks``	 
     * - Password
       - Specifies the password of the selected role.
       - ``Tr0ub4dor&3``
     * - Require SSL (recommended)
       - Sets SSL as a requirement for establishing this connection.
       - 

The connection is established and the data source page is displayed.
  
.. _set_up_sqream_tables_as_data_sources:

Setting Up SQream Tables as Data Sources
----------------
After connecting to SQream you must set up the SQream tables as data sources.

**To set up SQream tables as data sources:**
	
1. From the **Table** menu, select the desired database and schema.

   SQream's default schema is **public**.
   
    ::
	
#. Drag the desired tables into the main area (labeled **Drag tables here**).

   This area is also used for specifying joins and data source filters.
   
    ::
	
#. Open a new sheet to analyze data. 

Tableau Best Practices and Troubleshooting
---------------
This section describes the following best practices and troubleshooting procedures when connecting to SQream using Tableau:

.. contents::
   :local:

Using Tableau's Table Query Syntax
~~~~~~~~~~~~~~~~~~~
Dragging your desired tables into the main area in Tableau builds queries based on its own syntax. This helps ensure increased performance, while using views or custom SQL may degrade performance. In addition, SQream recommends using the :ref:`create_view` to create pre-optimized views, which your datasources point to. 

Creating a Separate Service for Tableau
~~~~~~~~~~~~~~~~~~~
SQream recommends creating a separate service for Tableau with the DWLM. This reduces the impact that Tableau has on other applications and processes, such as ETL. In addition, this works in conjunction with the load balancer to ensure good performance.

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
   
      ::
	  
   * **Tableau Desktop on MacOS:** *~/Library/Tableau/Drivers*
   
      ::
	  
   * **Tableau on Linux**: */opt/tableau/tableau_driver/jdbc*
   
 2. Find the file path for the JDBC driver and add it to the Java classpath:
   
   * **For Linux** - ``export CLASSPATH=<absolute path of SQream DB JDBC driver>;$CLASSPATH``

        ::
		
   * **For Windows** - add an environment variable for the classpath:  

	.. image:: /_static/images/Third_Party_Connectors/tableau/envrionment_variable_for_classpath.png

If you experience issues after restarting Tableau, see the `SQream support portal <https://support.sqream.com>`_.