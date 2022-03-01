.. _microstrategy:

*************************
Connect to SQream Using MicroStrategy
*************************

Overview 
==========
MicroStrategy is a Business Intelligence software offering a wide variety of data analytics capabilities. SQream uses the MicroStrategy connector for reading and loading data into SQream. The **Connect to SQream Using MicroStrategy** page describes how to install MicroStrategy and connect a datasource to the MicroStrategy dasbhoard for analysis, and describes the following:

.. contents:: 
   :local:
   :depth: 1

For more information about Microstrategy, see `MicroStrategy <https://www.microstrategy.com/>`_.

Prerequisites
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Installing MicroStrategy
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Configuring MicroStrategy
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Launching MicroStrategy
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Operating MicroStrategy
-------------------
The **Operating MicroStrategy** section describes how to connect a data source.

**To connect a data source:**

1. Activate the **MicroStrategy Desktop** app. The app displays the Dossiers panel to the right.

    ::
	
2. Download the most current version of the `SQream JDBC driver <https://docs.sqream.com/en/latest/guides/client_drivers/index.html#client-drivers>`_.

    ::

3. Click **Dossiers** and **New Dossier**. The **Untitled Dossier** panel is displayed.

    ::
	
4. Click **New Data**.

    ::
	
5. From the **Data Sources** panel, select **Databases** to access data from tables. The **Select Import Options** panel is displayed.

    ::
	
6. Select one of the following:

   * Build a Query
   * Type a Query
   * Select Tables
   
    ::
	
7. Click **Next**.

    ::
	
8. In the Data Source panel, do the following:

   1. From the **Database** dropdown menu, select **Generic**. The **Host Name**, **Port Number**, and **Database Name** fields are removed from the panel.

    ::
	
   2. In the **Version** dropdown menu, verify that **Generic DBMS** is selected.

    ::
	   
   3. Click **Show Connection String**.

    ::
	
   4. Select the **Edit connection string** checkbox.

    ::
	
   5. From the **Driver** dropdown menu, select a driver for one of the following connectors:

      * **JDBC** - The SQream driver is not integrated with MicroStrategy and does not appear in the dropdown menu. However, to proceed, you must select an item, and in the next step you must specify the path to the SQream driver that you installed on your machine.
	  
	    ::
		
      * **ODBC** - SQreamDB ODBC

       ::

   6. In the **Connection String** text box, type the relevant connection string and path to the JDBC jar file using the following syntax:

      .. code-block:: console

         $ jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>sqream;[<optional parameters>; ...]

      The following example shows the correct syntax for the JDBC connector:
 
      .. code-block:: console

         jdbc;MSTR_JDBC_JAR_FOLDER=C:\path\to\jdbc\folder;DRIVER=<driver>;URL={jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>;[<optional parameters>; ...];}
   
      The following example shows the correct syntax for the ODBC connector:
  
      .. code-block:: console

         odbc:Driver={SqreamODBCDriver};DSN={SQreamDB ODBC};Server=<Host>;Port=<Port>;Database=<database name>;User=<username>;Password=<password>;Cluster=<boolean>;

      For more information about the available **connection parameters** and other examples, see `Connection Parameters <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html#connection-parameters>`_.

   7. In the **User** and **Password** fields, fill out your user name and password.

    ::
	   
   8. In the **Data Source Name** field, type **SQreamDB**.

    ::
	    
   9. Click **Save**. The SQreamDB that you picked in the Data Source panel is displayed.
   

9. In the **Namespace** menu, select a namespace. The tables files are displayed.

    ::

10. Drag and drop the tables into the panel on the right in your required order.

     ::

11. **Recommended** - Click **Prepare Data** to customize your data for analysis.

     ::

12. Click **Finish**.

     ::

13. From the **Data Access Mode** dialog box, select one of the following:

   * Connect Live
   * Import as an In-memory Dataset
	
Your populated dashboard is displayed and is ready for data discovery and analytics.

Supported SQream Drivers
-------------------
**Comment**- Do we need this section? If so, it belongs in **Overview**.

The following list shows the supported SQream drivers and versions:

* **JDBC** - Version 4.3.3 and higher.
* **ODBC** - Version 4.0.0.

Troubleshooting MicroStrategy
-------------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.