.. _talend:

*************************
Connecting to SQream Using Talend
*************************

Overview
================= 
This page describes how to use Talend to interact with a SQream cluster. The Talend connector is used for reading data from a SQream cluster and loading data into SQream. In addition, this page provides a viability report on Talend's comptability with SQream for stakeholders.

The **Connecting to SQream Using Talend** describes the following:

.. contents::
   :local:
   :depth: 1

Creating a New Metadata JDBC DB Connection
----------------
**To create a new metadata JDBC DB connection:**

1. In the **Repository** panel, nagivate to **Metadata** and right-click **Db connections**.

    ::
	
2. Select **Create connection**.

    ::
	
3. In the **Name** field, type a name.

    ::

   Note that the name cannot contain spaces.

4. In the **Purpose** field, type a purpose and click **Next**.

   Note that you cannot continue to the next step until you define both a Name and a Purpose.

    ::

5. In the **DB Type** field, select **JDBC**.

    ::

6. In the **JDBC URL** field, type the relevant connection string.

   For connection string examples, see `Connection Strings <https://docs.sqream.com/en/v2021.1/connecting_to_sqream/client_drivers/jdbc/index.html#connection-string-examples>`_.
   
7. In the **Drivers** field, click the **Add** button.

   The **"newLine"** entry is added.

8. One the **"newLine'** entry, click the ellipsis.

   The **Module** window is displayed.

9. From the Module window, select **Artifact repository(local m2/nexus)** and select **Install a new module**.

    ::

10. Click the ellipsis.

    Your hard drive is displayed.	

11. Navigate to a **JDBC jar file** (such as **sqream-jdbc-4.5.3.jar**)and click **Open**.

     ::

12. Click **Detect the module install status**.

     ::

13. Click **OK**.

    The JDBC that you selected is displayed in the **Driver** field.

14. Click **Select class name**.

     ::

15. Click **Test connection**.

    If a driver class is not found (for example, you didn't select a JDBC jar file), the following error message is displayed:

    After creating a new metadata JDBC DB connection, you can do the following:

    * Use your new metadata connection.
	
	   ::
	   
    * Drag it to the **job** screen.
	
	   ::
	   
    * Build Talend components.
 
    For more information on loading data from JSON files to the Talend Open Studio, see `How to Load Data from JSON Files in Talend <https://www.youtube.com/watch?v=qNt9CYZFFqQ&list=PLOr008ImHvfan_fuDr5RVyexpeYJAp9FX&index=6>`_.

Supported SQream Drivers
----------------
The following list shows the supported SQream drivers and versions:

* **JDBC** - Version 4.3.3 and higher.

   ::
   
* **ODBC** - Version 4.0.0. This version requires a Bridge to connect. For more information on the required Bridge, see `Connecting Talend on Windows to an ODBC Database <https://www.easysoft.com/blog/talend.html>`_.

Supported Data Sources
----------------
Talend Cloud connectors let you create reusable connections with a wide variety of systems and environments, such as those shown below. This lets you access and read records of a range of diverse data.

* **Connections:** Connections are environments or systems for storing datasets, including databases, file systems, distributed systems and platforms. Because these systems are reusable, you only need to establish connectivity with them once.

   ::

* **Datasets:** Datasets include database tables, file names, topics (Kafka), queues (JMS) and file paths (HDFS). For more information on the complete list of connectors and datasets that Talend supports, see `Introducing Talend Connectors <https://help.talend.com/r/vqIZei8ynfi_BaDCg3d~_g/M0qzU1kTnL0bPou7OuxJfw>`_.

Known Issues
----------------
As of 6/1/2021 schemas were not displayed for tables with identical names.

If you experience issues using Talend, see the `SQream support portal <https://support.sqream.com>`_.