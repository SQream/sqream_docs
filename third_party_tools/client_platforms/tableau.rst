.. _connect_to_tableau:

*************************
Connect to SQream Using Tableau
*************************

Overview
=====================
SQream's Tableau connector plugin, based on standard JDBC, enables storing and fast querying large volumes of data. The **Connecting to SQream Using Tableau** page describes how install Tableau and the JDBC and ODBC drivers and connect to SQream using the JDBC and ODBC drivers for data analysis. SQream supports both Tableau Desktop and Tableau Server on Windows, MacOS, and Linux distributions.

The Connecting to SQream Using Tableau page describes the following:

.. contents:: 
   :local:
   :depth: 1
   
For more information on SQream's integration with Tableau, see `Tableau's Extension Gallery <https://extensiongallery.tableau.com/connectors?version=2019.4>`_.
   
Prerequisites
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Installing Tableau
-------------------
The **Installing Tableau** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Installing the JDBC Driver and Tableau Connector Plugin
~~~~~~~~~~~~~~~~~~
This section describes how to install the JDBC driver using the fully-integrated Tableau connector plugin (Tableau Connector, or **.taco** file). SQream has been tested with Tableau versions 9.2 and newer.

**To connect to SQream using Tableau:**
   
#. Install the Tableau Desktop application.

   For more information about installing the Tableau Desktop application, see the `Tableau products page <https://www.tableau.com/products/trial>`_ and click **Download Free Trial**. Note that Tableau offers a 14-day trial version.
   
   ::

#. Do one of the following:

   * **For Windows** - See :ref:`Installing Tableau Using the Windows Installer <tableau_windows_installer>`.
   
      ::
	 
   * **For MacOS or Linux** - See :ref:`Installing the JDBC Driver Manually <tableau_jdbc_installer>`.

.. note:: For Tableau **2019.4 versions and later**, SQream recommends installing the JDBC driver instead of the previously recommended ODBC driver.

.. _tableau_windows_installer:

Installing the JDBC Driver Using the Windows Installer
~~~~~~~~~~~~~~~~~~
If you are using Windows, after installing the Tableau Desktop application you can install the JDBC driver using the Windows installer. The Windows installer is an installation wizard that guides you through the JDBC driver installation steps. When the driver is installed, you can connect to SQream.

**To install Tableau using the Windows installer**:

#. Close Tableau Desktop.

    ::

#. Download the most current version of the `SQream JDBC driver <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

    ::
	
#. Do the following:

   #. Start the installer.
   
       ::
	   
   #. Verify that the **Tableau Desktop connector** item is selected.

       ::

   #. Follow the installation steps.

    ::

You can now restart Tableau Desktop or Server to begin using the SQream driver by :ref:`connecting to SQream <tableau_connect_to_sqream>`.

.. _tableau_jdbc_installer:

Installing the JDBC Driver Manually
~~~~~~~~~~~~~
If you are using MacOS, Linux, or the Tableau server, after installing the Tableau Desktop application you can install the JDBC driver manually. When the driver is installed, you can connect to SQream.

**To install the JDBC driver manually:**

1. Download the JDBC installer and SQream Tableau connector (.taco) file from the :ref:`from the client drivers page<client_drivers>`.

    ::

#. Install the JDBC driver by unzipping the JDBC driver into a Tableau driver directory.
   
   Based on the installation method that you used, your Tableau driver directory is located in one of the following places:

   * **Tableau Desktop on Windows:** *C:/Program Files/Tableau/Drivers*
   
       ::
	   
   * **Tableau Desktop on MacOS:** *~/Library/Tableau/Drivers*
   
       ::
	   
   * **Tableau on Linux**: */opt/tableau/tableau_driver/jdbc*
	  
.. note:: If the driver includes only a single .jar file, copy it to *C:\\Program Files\\Tableau/Drivers*. If the driver includes multiple files, create a subfolder *A* in *C:\\Program Files\\Tableau/Drivers* and copy all files to folder *A*.

   ::

Note the following when installing the JDBC driver:

  * You must have read permissions on the .jar file.
  * Tableau requires a JDBC 4.0 or later driver.
  * Tableau requires a Type 4 JDBC driver.
  * The latest 64-bit version of Java 8 is installed.

3. Install the **SQreamDB.taco** file by moving the SQreamDB.taco file into the Tableau connectors directory.
   
   Based on the installation method that you used, your Tableau driver directory is located in one of the following places:

   * **Tableau Desktop on Windows:** *C:\\Users\\<your user>\\My Tableau Repository\\Connectors*
   
       ::
	   
   * **Tableau Desktop on Windows:** *~/My Tableau Repository/Connectors*
   
      ::
	  
4. *Optional* - If you are using the Tableau Server, do the following:
   
   1. Create a directory for Tableau connectors and give it a descriptive name, such as *C:\\tableau_connectors*.
      
      This directory needs to exist on all Tableau servers.
      
       ::
   
   2. Copy the SQreamDB.taco file into the new directory.
   
       ::
   
   3. Set the **native_api.connect_plugins_path** option to ``tsm`` as shown in the following example:

      .. code-block:: console
   
         $ tsm configuration set -k native_api.connect_plugins_path -v C:/tableau_connectors
      
      If a configuration error is displayed, add ``--force-keys`` to the end of the command as shown in the following example:

      .. code-block:: console
   
         $ tsm configuration set -k native_api.connect_plugins_path -v C:/tableau_connectors--force-keys
		 
   4. To apply the pending configuration changes, run the following command:

      .. code-block:: console
    
         $ tsm pending-changes apply
      
      .. warning:: This restarts the server.

You can now restart Tableau Desktop or Server to begin using the SQream driver by :ref:`connecting to SQream <tableau_connect_to_sqream>` as described in the section below.

.. _tableau_connect_to_sqream:	

Configuring Tableau
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Launching Tableau
-------------------
The **Launching Tableau** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Connecting Tableau to SQream
~~~~~~~~~~~~
**To connect Tableau to SQream:**

1. Start Tableau Desktop.

    ::
	
#. In the **Connect** menu, in the **To a server** sub-menu, click **More Servers** and select **Other Databases (ODBC)**.

   The **Other Databases (ODBC)** window is displayed.
   
    ::
	
#. In the Other Databases (ODBC) window, select the DSN that you created in :ref:`Setting Up SQream Tables as Data Sources <set_up_sqream_tables_as_data_sources>`.

   Tableau may display the **Sqream ODBC Driver Connection Dialog** window and prompt you to provide your username and password.

#. Provide your username and password and click **OK**.   
  
.. _tableau_connect_to_sqream_db:

Connecting to SQream
~~~~~~~~~~~~
After installing and configuring the JDBC driver you can connect to SQream.

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

.. tip:: 
   Tableau automatically assigns your connection a default name based on the DSN and table. SQream recommends giving the connection a more descriptive name.
   
.. _set_up_sqream_tables_as_data_sources:

Operating Tableau
-------------------
After connecting to SQream you must set up the SQream tables as data sources, described below.

**To set up SQream tables as data sources:**
	
1. From the **Table** menu, select the desired database and schema.

   SQream's default schema is **public**.
   
    ::
	
#. Drag the desired tables into the main area (labeled **Drag tables here**).

   This area is also used for specifying joins and data source filters.
   
    ::
	
#. Open a new sheet to analyze data. 

.. tip:: 
   For more information about configuring data sources, joining, filtering, see Tableau's `Set Up Data Sources <https://help.tableau.com/current/pro/desktop/en-us/datasource_prepare.htm>`_ tutorials.
   
Troubleshooting Tableau
-------------------
This section describes the following best practices and troubleshooting procedures when connecting to SQream using Tableau:

.. contents:: 
   :local:
   :depth: 1

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
 
    .. image:: /_static/images/third_party_connectors/tableau/envrionment_variable_for_classpath.png
        :align: center
	
If you experience issues after restarting Tableau, see the `SQream support portal <https://support.sqream.com>`_.